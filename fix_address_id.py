import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find the p tag in the header after h1
# We know it looks something like <p>Endereo: Rua Tanzania, Jardim Aclimatao  CBMC Incorporadora</p>
# Let's just find the exact line and replace it
html = re.sub(r'<p>Endere.o: Rua Tanzania, Jardim Aclimata.o [–\-] CBMC Incorporadora</p>', r'<p id="mainAddress">Endereço: Rua Tanzania, Jardim Aclimatação – CBMC Incorporadora</p>', html)

# Just to be safe, if the above didn't work because of another character:
if 'id="mainAddress"' not in html.split('</header>')[0]:
    # fallback: find </h1> and the next <p>
    html = re.sub(r'(<h1 id="mainTitle">.*?</h1>\s*)<p>(.*?)</p>', r'\1<p id="mainAddress">\2</p>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("mainAddress ID successfully added to HTML.")
