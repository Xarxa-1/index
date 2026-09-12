import os

def generate_html_index():
    html_files = []
    for root, dirs, files in os.walk('.'):
        # Ignorar carpetes ocultes i sistemes de versió
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            # Cerca qualsevol fitxer .html que no sigui indexpagines.html
            if file.endswith('.html') and file.lower() != 'indexpagines.html':
                rel_path = os.path.relpath(os.path.join(root, file), '.')
                # Normalitzar la ruta per a URL web (substituir \ per /)
                web_path = rel_path.replace('\\', '/')
                html_files.append(web_path)

    html_files.sort()

    print(f"Fitxers HTML trobats: {len(html_files)}")
    for f in html_files:
        print(f" - {f}")

    content = """<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Índex de Pàgines</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }
        h1 { color: #2563eb; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; padding: 8px; border-bottom: 1px solid #f3f4f6; }
        a { color: #1d4ed8; text-decoration: none; font-size: 1.1rem; font-weight: 500; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Índex de Pàgines</h1>
    <ul>
"""

    if not html_files:
        content += "        <li><em>No s'han trobat fitxers HTML en aquest repositori.</em></li>\n"
    else:
        for file_path in html_files:
            content += f'        <li><a href="{file_path}" target="_blank">{file_path}</a></li>\n'

    content += """    </ul>
</body>
</html>"""

    with open('indexpagines.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    generate_html_index()
