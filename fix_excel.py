import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace hardcoded TIMELESS with dynamic title
html = html.replace("['SIMULAÇÃO DE COMPRA – TIMELESS RESIDENCE'],[],", "['SIMULAÇÃO DE COMPRA – ' + (currentSimulator === 'TResidence' ? 'TIMELESS RESIDENCE' : 'MEDICAL CBMC')],[],")

html = html.replace("XLSX.writeFile(wb,`Simulacao_TIMELESS_${u.unidade}_${nome}.xlsx`);", "XLSX.writeFile(wb,`Simulacao_${currentSimulator === 'TResidence' ? 'TIMELESS' : 'CBMC'}_${u.unidade}_${nome}.xlsx`);")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Export Excel successfully updated.")
