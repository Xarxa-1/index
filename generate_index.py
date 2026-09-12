import os

def generate_html_index():
    """Genera un índex HTML de totes les pàgines HTML de la carpeta actual."""
    html_files = []
    
    # Escaneja tots els fitxers de la carpeta
    for root, dirs, files in os.walk('.'):
        # Ignora carpetes ocultes i sistemes de versió
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in sorted(files):
            # Busca fitxers HTML excepto indexpagines.html
            if file.endswith('.html') and file.lower() != 'indexpagines.html':
                rel_path = os.path.relpath(os.path.join(root, file), '.')
                # Normalitza la ruta per a web
                web_path = rel_path.replace('\\', '/')
                html_files.append(web_path)
    
    html_files.sort()
    
    print(f"Fitxers HTML detectats: {len(html_files)}")
    
    # Crea el contingut HTML
    html_content = """<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Índex de Pàgines HTML</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 20px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 1.1em;
            opacity: 0.9;
        }
        
        .content {
            padding: 40px 20px;
        }
        
        .stats {
            display: flex;
            justify-content: space-around;
            gap: 20px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        
        .stat-box {
            background: #f5f5f5;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            flex: 1;
            min-width: 150px;
        }
        
        .stat-box .number {
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }
        
        .stat-box .label {
            color: #666;
            margin-top: 5px;
        }
        
        .search-box {
            margin-bottom: 30px;
        }
        
        .search-box input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1em;
            transition: all 0.3s;
        }
        
        .search-box input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 10px rgba(102, 126, 234, 0.3);
        }
        
        .file-list {
            display: grid;
            gap: 10px;
        }
        
        .file-item {
            display: flex;
            align-items: center;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            transition: all 0.3s;
            text-decoration: none;
            color: inherit;
        }
        
        .file-item:hover {
            background: #f0f0f0;
            transform: translateX(5px);
            border-left-color: #764ba2;
        }
        
        .file-icon {
            width: 30px;
            height: 30px;
            background: #667eea;
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 15px;
            font-weight: bold;
        }
        
        .file-info {
            flex: 1;
        }
        
        .file-name {
            font-weight: 600;
            color: #333;
            margin-bottom: 3px;
        }
        
        .file-path {
            font-size: 0.9em;
            color: #999;
            font-family: 'Courier New', monospace;
        }
        
        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: #999;
        }
        
        .empty-state svg {
            width: 80px;
            height: 80px;
            margin-bottom: 20px;
            opacity: 0.5;
        }
        
        .footer {
            background: #f5f5f5;
            padding: 20px;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }
        
        @media (max-width: 600px) {
            .header h1 {
                font-size: 1.8em;
            }
            
            .stats {
                flex-direction: column;
            }
            
            .file-item {
                flex-direction: column;
                align-items: flex-start;
            }
            
            .file-icon {
                margin-right: 0;
                margin-bottom: 10px;
            }
        }
    </style>
    <script>
        function filterFiles() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const fileItems = document.querySelectorAll('.file-item');
            let visibleCount = 0;
            
            fileItems.forEach(item => {
                const fileName = item.textContent.toLowerCase();
                if (fileName.includes(searchTerm)) {
                    item.style.display = 'flex';
                    visibleCount++;
                } else {
                    item.style.display = 'none';
                }
            });
            
            const emptyState = document.getElementById('emptyState');
            if (visibleCount === 0 && searchTerm) {
                if (!emptyState) {
                    const empty = document.createElement('div');
                    empty.id = 'emptyState';
                    empty.className = 'empty-state';
                    empty.textContent = 'Cap fitxer coincideix amb la recerca.';
                    document.querySelector('.file-list').appendChild(empty);
                }
            } else if (emptyState) {
                emptyState.remove();
            }
        }
    </script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📑 Índex de Pàgines HTML</h1>
            <p>Navegació per a totes les pàgines disponibles</p>
        </div>
        
        <div class="content">
            <div class="stats">
                <div class="stat-box">
                    <div class="number">""" + str(len(html_files)) + """</div>
                    <div class="label">Pàgines HTML</div>
                </div>
            </div>
            
            <div class="search-box">
                <input type="text" id="searchInput" placeholder="🔍 Cerca una pàgina..." onkeyup="filterFiles()">
            </div>
            
            <div class="file-list">
"""
    
    if html_files:
        for i, file_path in enumerate(html_files, 1):
            file_name = os.path.basename(file_path)
            html_content += f"""                <a href="{file_path}" class="file-item" target="_blank">
                    <div class="file-icon">{i % 10}</div>
                    <div class="file-info">
                        <div class="file-name">{file_name}</div>
                        <div class="file-path">{file_path}</div>
                    </div>
                </a>
"""
    else:
        html_content += """                <div class="empty-state">
                    <div style="font-size: 3em; margin-bottom: 20px;">📭</div>
                    <p>No s'han trobat fitxers HTML en aquest repositori.</p>
                </div>
"""
    
    html_content += """            </div>
        </div>
        
        <div class="footer">
            <p>Generat automàticament • Última actualització: """ + str(__import__('datetime').datetime.now().strftime('%d/%m/%Y %H:%M')) + """</p>
        </div>
    </div>
</body>
</html>"""
    
    # Guarda el fitxer
    with open('indexpagines.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ indexpagines.html generat correctament amb {len(html_files)} pàgines.")

if __name__ == '__main__':
    generate_html_index()
