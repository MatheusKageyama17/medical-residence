import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_line = ".no-print,.btn-row,#liveTotalBar,#pctWarning,#summaryBar,#resultSection,#cardCorretor{display:none !important;}"
new_line = ".no-print,.btn-row,#liveTotalBar,#pctWarning,#summaryBar,#resultSection,#cardCorretor,.simulator-selector{display:none !important;}"

if old_line in html:
    html = html.replace(old_line, new_line)
    print("Replaced successfully.")
else:
    print("Line not found.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
