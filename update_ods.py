#!/usr/bin/env python3
"""
update_ods.py — Mise à jour incrémentale de base-uneiaparjour.ods
depuis le flux RSS de uneiaparjour.fr

Logique :
1. Lit la date de la ligne 2 de l'ODS (article le plus récent)
2. Récupère les articles du RSS publiés après cette date
3. Filtre les Focus (catégorie = 'Focus')
4. Insère les nouveaux articles en haut de l'ODS (après en-tête)
5. Sauvegarde l'ODS si des articles ont été ajoutés
"""

import re
import sys
import time
from datetime import datetime, timezone
from html import unescape
from urllib.parse import urlparse, parse_qs, urlencode

import feedparser
from odf.opendocument import load
from odf.table import Table, TableRow, TableCell
from odf.text import P

ODS_PATH = "base-uneiaparjour.ods"
FEED_URL = "https://www.uneiaparjour.fr/feed/"
MAX_CATEGORIES = 6
DELAY = 1.0


def get_cell_text(cell):
    ps = cell.getElementsByType(P)
    if not ps:
        return ''
    p = ps[0]
    text = ''
    for node in p.childNodes:
        if hasattr(node, 'data'):
            text += node.data
        elif hasattr(node, 'childNodes'):
            for child in node.childNodes:
                if hasattr(child, 'data'):
                    text += child.data
    return text


def strip_html(html_text):
    text = re.sub(r"<[^>]+>", "", html_text)
    text = unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_first_paragraph(entry):
    content = ""
    if hasattr(entry, "content") and entry.content:
        content = entry.content[0].get("value", "")
    if not content:
        content = entry.get("description", "") or entry.get("summary", "")
    matches = re.findall(r"<p[^>]*>(.*?)</p>", content, re.DOTALL | re.IGNORECASE)
    for match in matches:
        text = strip_html(match)
        if text:
            return text
    return strip_html(content)


def parse_ods_date(date_str):
    try:
        return datetime.strptime(date_str, "%d/%m/%Y").replace(tzinfo=timezone.utc)
    except (ValueError, TypeError):
        return None


def parse_rss_date(date_str):
    try:
        return datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
    except (ValueError, TypeError):
        return None


def format_date(date_str):
    try:
        dt = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
        return dt.strftime("%d/%m/%Y")
    except (ValueError, TypeError):
        return ""


def build_paged_url(base_url, page):
    parsed = urlparse(base_url)
    params = parse_qs(parsed.query)
    params["paged"] = [str(page)]
    new_query = urlencode(params, doseq=True)
    return parsed._replace(query=new_query).geturl()


def get_last_date_from_ods(ods_path):
    doc = load(ods_path)
    sheets = doc.spreadsheet.getElementsByType(Table)
    base_sheet = next(s for s in sheets if s.getAttribute('name') == 'Base')
    rows = base_sheet.getElementsByType(TableRow)
    if len(rows) < 2:
        return None
    cells = rows[1].getElementsByType(TableCell)
    for i, cell in enumerate(cells):
        if i == 9:
            return parse_ods_date(get_cell_text(cell))
    return None


def fetch_new_entries(last_date):
    new_entries = []
    seen_links = set()
    page = 1

    while True:
        url = build_paged_url(FEED_URL, page) if page > 1 else FEED_URL
        print(f"📡 Page {page} : {url}")
        feed = feedparser.parse(url)

        if not feed.entries:
            print(f"   → Fin (page vide)")
            break

        found_older = False
        new_on_page = 0
        for entry in feed.entries:
            link = entry.get("link", "")
            if link in seen_links:
                continue
            seen_links.add(link)

            pub_date = parse_rss_date(entry.get("published", ""))
            if pub_date and last_date and pub_date <= last_date:
                found_older = True
                continue

            new_entries.append(entry)
            new_on_page += 1

        print(f"   → {new_on_page} nouveaux (total : {len(new_entries)})")

        if found_older:
            break

        page += 1
        time.sleep(DELAY)

    return new_entries


def make_row(entry):
    categories = [tag.term for tag in getattr(entry, "tags", [])]

    if any(c.strip() == 'Focus' for c in categories):
        return None

    cats = (categories + [""] * MAX_CATEGORIES)[:MAX_CATEGORIES]

    values = [
        entry.get("title", ""),
        extract_first_paragraph(entry),
        entry.get("link", ""),
    ] + cats + [format_date(entry.get("published", ""))]

    row = TableRow()
    for val in values:
        cell = TableCell()
        cell.addElement(P(text=val))
        row.addElement(cell)
    return row


def insert_rows_into_ods(ods_path, new_entries):
    doc = load(ods_path)
    sheets = doc.spreadsheet.getElementsByType(Table)
    base_sheet = next(s for s in sheets if s.getAttribute('name') == 'Base')
    rows = base_sheet.getElementsByType(TableRow)
    second_row = rows[1]

    rows_to_insert = []
    skipped_focus = 0
    for entry in new_entries:
        row = make_row(entry)
        if row is not None:
            rows_to_insert.append(row)
        else:
            skipped_focus += 1

    for row in reversed(rows_to_insert):
        base_sheet.insertBefore(row, second_row)

    inserted = len(rows_to_insert)

    if skipped_focus:
        print(f"   → {skipped_focus} Focus ignorés")

    if inserted > 0:
        doc.save(ods_path)
        print(f"✅ {inserted} article(s) ajouté(s) — ODS sauvegardé")
    else:
        print("ℹ️  Aucun nouvel article à ajouter (hors Focus)")

    return inserted


def main():
    print("🔄 Mise à jour incrémentale de l'ODS...")

    last_date = get_last_date_from_ods(ODS_PATH)
    if last_date:
        print(f"📅 Dernier article en base : {last_date.strftime('%d/%m/%Y')}")
    else:
        print("⚠️  Impossible de lire la date du dernier article", file=sys.stderr)
        sys.exit(1)

    new_entries = fetch_new_entries(last_date)

    if not new_entries:
        print("✓ Base à jour, aucun nouvel article")
        sys.exit(0)

    insert_rows_into_ods(ODS_PATH, new_entries)
    sys.exit(0)


if __name__ == "__main__":
    main()
