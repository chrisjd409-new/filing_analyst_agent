from bs4 import BeautifulSoup

with open("data/apple_first_10k.html", encoding='utf-8') as f:
    html = f.read()


# Parse and pull out the text
soup = BeautifulSoup(html, "html.parser")

# Found unreadable html at top. Remove hidden xbrl data block at top
# Remove hidden XBRL data (two ways SEC filings hide it)
removed = 0
for tag in soup.find_all("ix:header"):
    tag.decompose()
    removed += 1
for tag in soup.find_all(style=lambda s: s and "display:none" in s.replace(" ", "")):
    tag.decompose()
    removed += 1
print("removed", removed, "hidden blocks")


text = soup.get_text(separator="\n")


# Clean up -> remove extra spaces and empty lines
lines = [line.strip() for line in text.splitlines()]
text = '\n'.join(line for line in lines if line)


# save clean text
# "w" is write mode -> creates apple_first_10k.txt in my data folder (writing this for self study)
with open("data/apple_first_10k.txt", 'w', encoding='utf-8') as f:
    f.write(text)


# check result
print(len(text), 'characters')
print(text[:1000])