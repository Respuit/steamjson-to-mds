import json
import os

# Cargar el JSON
with open("games.json", "r", encoding="utf-8") as file:
    games = json.load(file)

# Crear el directorio para los archivos Markdown si no existe
output_dir = "markdown_files"
os.makedirs(output_dir, exist_ok=True)

# Procesar cada juego y crear un archivo Markdown
for game_id, game_data in games.items():
    # Escapar comillas en el título
    title = game_data.get("name", "Unknown").replace('"', '\\"')

    # Construir el contenido del archivo Markdown
    markdown_content = f"""---
id: {game_id}
title: "{title}"
windows: "{str(game_data.get('windows', False)).lower()}"
mac: "{str(game_data.get('mac', False)).lower()}"
linux: {str(game_data.get('linux', False)).lower()}
positive: {game_data.get('positive', 0)}
negative: {game_data.get('negative', 0)}
estimated_owners: "{game_data.get('estimated_owners', '0 - 0')}"
peak_ccu: {game_data.get('peak_ccu', 0)}

image: {game_data.get('header_image', 'N/A')}
opinions:
---
"""

    # Escribir el archivo Markdown
    file_path = os.path.join(output_dir, f"{game_id}.md")
    with open(file_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

print(f"Archivos Markdown generados en el directorio: {output_dir}")
