#!/usr/bin/env python3
from odf.opendocument import load
from odf.table import Table, TableRow, TableCell
from odf.text import P

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

doc = load('base-uneiaparjour.ods')
sheets = doc.spreadsheet.getElementsByType(Table)
print(f"Onglets : {[s.getAttribute('name') for s in sheets]}")

base_sheet = next(s for s in sheets if s.getAttribute('name') == 'Base')
rows = base_sheet.getElementsByType(TableRow)
print(f"Nombre de lignes : {len(rows)}")

# Ligne 2 (index 1)
row = rows[1]
cells = row.getElementsByType(TableCell)
print(f"\nLigne 2 — {len(cells)} cellules brutes :")
for i, cell in enumerate(cells):
    repeat = cell.getAttribute('numbercolumnsrepeated') or '1'
    text = get_cell_text(cell)
    print(f"  cellule {i} (repeat={repeat}) : '{text}'")

# Expansion avec numbercolumnsrepeated
print("\nLigne 2 — colonnes expandées :")
col = 0
for cell in cells:
    repeat = int(cell.getAttribute('numbercolumnsrepeated') or 1)
    text = get_cell_text(cell)
    for _ in range(repeat):
        print(f"  col {col} : '{text}'")
        col += 1
        if col > 12:
            break
    if col > 12:
        break
