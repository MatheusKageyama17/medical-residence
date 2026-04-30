import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the h1 and p tags in the header
html = re.sub(r'<h1>Simulador de Compra [–-] TIMELESS RESIDENCE</h1>', r'<h1 id="mainTitle">Simulador de Compra – TIMELESS RESIDENCE</h1>', html)
html = re.sub(r'<p>Endereço: Rua Tanzania, Jardim Aclimatação [–-] CBMC Incorporadora</p>', r'<p id="mainAddress">Endereço: Rua Tanzania, Jardim Aclimatação – CBMC Incorporadora</p>', html)

# Now, we need to update the switchSimulator function to update mainTitle and mainAddress
# Instead of replacing the whole function, let's just find the function body and replace the inner if statement.
old_if = """  if (sim === 'TResidence') {
    UNITS = UNITS_TRESIDENCE;
    document.getElementById('mainSubtitle').textContent = 'TIMELESS RESIDENCE';
  } else if (sim === 'CBMC') {
    UNITS = UNITS_CBMC;
    document.getElementById('mainSubtitle').textContent = 'MEDICAL CBMC';
  }"""

new_if = """  if (sim === 'TResidence') {
    UNITS = UNITS_TRESIDENCE;
    document.getElementById('mainTitle').textContent = 'Simulador de Compra – TIMELESS RESIDENCE';
    document.getElementById('mainAddress').textContent = 'Endereço: Rua Tanzania, Jardim Aclimatação – CBMC Incorporadora';
  } else if (sim === 'CBMC') {
    UNITS = UNITS_CBMC;
    document.getElementById('mainTitle').textContent = 'Simulador de Compra – MEDICAL CBMC';
    document.getElementById('mainAddress').textContent = 'Endereço: Venda Medical CBMC';
  }"""

html = html.replace(old_if, new_if)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML successfully fixed.")
