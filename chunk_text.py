from bs4 import BeautifulSoup

with open("data/apple_first_10k.html", encoding='utf-8') as f:
    html = f.read()


# Parse and pull out the text
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text(separator="\n")


# Clean up -> remove extra spaces and empty lines
lines = [line.strip() for line in text.splitlines()]
text = '\n'.join(line for line in lines if line)
