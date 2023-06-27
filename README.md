# Genera Launcher
## Lanzador de aplicaciones de codigo creativo
Este launcher reune algunas de las herramientas que más he usado, junto a scripts y utilidades que uso a diario, orientado a facilitar la creación de proyectos de código creativo.

## Caracteristicas:
### Proyectos web
- Creación de proyectos web:
  - HTML+CSS+JS
  - p5.js
  - p5.js + p5.capture + Utilidades
  - Blog con 11ty
- Creacion de proyectos con Python
  - Entorno virtual básico
  - Entorno virtual con FastAPI
- Editar videos con ffmpeg
  - Convertir a GIF
  - Convertir a MP4
  - Extraer mp3/wav
- Descargar media online con yt-dlp
- Transcribir con Whisper
  - Transcribir audio/video
  - Grabar y transcribir nota de audio
## Requisitos
- Python 3.8+

## Instalación
Clona el repositorio:
```
git clone https://github.com/datadiego/genera_launcher.git
cd genera_launcher
python -m venv env
```
Activa el entorno virtual:
```
source env/bin/activate
```
Instala las dependencias:
```
pip install -r requirements.txt
```
## Uso
Con tu entorno virtual activado, ejecuta el script:
```
python gen_launcher.py
```
Idealmente querrás crear un alias o añadir el script a tu path para ejecutarlo desde cualquier lugar.

## Librerias 
Este proyecto usa las siguientes tecnologias:
- [p5.js](https://p5js.org/)
- [ffmpeg](https://ffmpeg.org/)
- [p5.capture](https://github.com/tapioca24/p5.capture)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Whisper](https://openai.com/research/whisper)