import os

# Extensions de fitxers que vols incloure a la llista
ALLOWED_EXTENSIONS = ('.html', '.pdf', '.md')
EXCLUDE_FILES = {'index.html'}

def generate_index():
    files_list = []
    
    for root, dirs, files in os.walk('.'):
        # Ignora carpetes ocultes com .git o .github
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file in EXCLUDE_FILES:
                continue
            if file.endswith(ALLOWED_EXTENSIONS):
                rel_path = os.path.relpath(os.path.join(root, file), '.')
                # Utilitza barres enllà per a les URLs
                url_path = rel_path.replace("\\", "/")
                files_list.append(url_path)

    files_list.sort()

    html_content = """<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Índex de Documents</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 2rem; background: #f6f8fa; color: #24292f; }
        h1 { border-bottom: 2px solid #d0d7de; padding-bottom: 0.5rem; }
        ul { list-style-type: none; padding: 0; }
        li { background: white; margin: 0.5rem 0; padding: 0.75rem 1rem; border-radius: 6px; border: 1px solid #d0d7de; }
        a { color: #0969da; text-decoration: none; font-weight: 600; word-break: break-all; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Índex de Recursos</h1>
    <ul>
"""
    
    for file_path in files_list:
        html_content += f'        <li><a href="{file_path}" target="_blank">{file_path}</a></li>\n'
        
    html_content += """    </ul>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_index()
