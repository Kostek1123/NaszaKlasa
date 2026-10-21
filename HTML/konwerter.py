import os
from docx import Document

def czytaj_txt(sciezka):
    html = ""
    with open(sciezka, encoding-"utf-8") as f:
        for linia in f:
            linia = linia.strip()
            if linia:
                html += f"<p>{linia}</p>\n"
    return html

def czytaj_docx(sciiezka):
    html = ""
    doc = Document(sciezka)
    for akapit in doc.paragraphs:
        if akapit.style.name == "Heading 1":
            html += f"<h2>{akapit.ext}</p>\n"
        else:
            html += f"<p>{akapit.text}</p>\n"
    return html

for nazwa in os.listdir("notatki"):
    sciezka = os.path.join("notatki", nazwa)

    if nazwa.endswith(".txt"):
        tresc = czytaj_txt(sciezka)
    elif nazwa.endswith(".docx"):
        tresc = czytaj_docx(sciezka)
    else:
        continue

szablon = open("szablon.html", encoding="utf-8").read()
strona = szablo.replace("{{tytul}}", "test123").replace("{{tresc}}", html)