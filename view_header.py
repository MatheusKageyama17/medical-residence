import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find header content
header_match = re.search(r'<header>(.*?)</header>', html, re.DOTALL)
if header_match:
    header_content = header_match.group(1)
    print("Header length:", len(header_content))
    print("Header snippet end:")
    print(header_content[-500:])
else:
    print("No header found")
