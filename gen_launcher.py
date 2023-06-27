import os
import io
import shutil
import subprocess
import pyaudio
import wave
import keyboard
import importlib
from colorama import init, Fore, Back, Style

from record_audio import grabar_audio
from ffmpeg_scripts import to_gif, to_mp4, to_mp3, to_wav

init(autoreset=True)
pet = "🐔"
root_folder = os.path.dirname(os.path.abspath(__file__))
local_path = os.getcwd()

def prompt_user(question, options, colors, choice_question="Introduce tu eleccion: "):
    #esta funcion recibe una pregunta y un diccionario de opciones
    #y devuelve la opcion elegida por el usuario
    print(question)
    for key, value in options.items():
        #print using colorama
        print("  "+colors[key] + str(key) + "." + value)
    choice = int(input(pet+"💬 "+choice_question))
    return choice
def abrir_vscode():
    print(pet+"💬 ¿Quieres abrir el proyecto?")
    choice = input(pet+"💬 Introduce tu eleccion (s/n): ")
    if choice.lower() == "s":
        os.system("code " + local_path)
def salida():
    print(pet+"💬 Adios!")
    exit()
def crea_htmlcssjs():
    # copy the template folder to the current folder
    nombre_proyecto = input(pet+"💬 ¿Como se llama tu proyecto? ")
    if nombre_proyecto == "":
        salida()
    print("🪛"+pet+" Creando proyecto "+nombre_proyecto)
    shutil.copytree(root_folder+"/templates/html", local_path+"/"+nombre_proyecto)
    print("🔥"+pet+" Estamos ready papi!")
    abrir_vscode()
def crea_p5js():
    # copy the template folder to the current folder
    nombre_proyecto = input(pet+"💬 ¿Como se llama tu proyecto? ")
    if nombre_proyecto == "":
        salida()
    print("🪛"+pet+"Creando proyecto "+nombre_proyecto)
    shutil.copytree(root_folder+"/templates/p5js_basico", local_path+"/"+nombre_proyecto)
    print("🔥"+pet+" Estamos ready papi!")
    abrir_vscode()
def crea_p5js_extras():
    # copy the template folder to the current folder
    nombre_proyecto = input(pet+"💬 ¿Como se llama tu proyecto? ")
    if nombre_proyecto == "":
        salida()
    print("🪛"+pet+"Creando proyecto "+nombre_proyecto)
    shutil.copytree(root_folder+"/templates/p5js_extras", local_path+"/"+nombre_proyecto)
    print("🔥"+pet+" Estamos ready papi!")
    abrir_vscode()
def crea_python():
    nombre_proyecto = input(pet+"💬 ¿Como se llama tu proyecto? ")
    if nombre_proyecto == "":
        salida()
    print("🪛"+pet+"Creando proyecto "+nombre_proyecto)
    os.mkdir(nombre_proyecto)
    os.chdir(nombre_proyecto)
    subprocess.run(["python", "-m", "venv", "env"])
    print("🔥"+pet+" Estamos ready papi!")
    abrir_vscode()    
def crea_fastapi():
    nombre_proyecto = input(pet+"💬 ¿Como se llama tu proyecto? ")
    if nombre_proyecto == "":
        salida()
    print("🪛"+pet+"Creando proyecto "+nombre_proyecto)
    shutil.copytree(root_folder+"/templates/python_fastapi", local_path+"/"+nombre_proyecto)
    os.chdir(nombre_proyecto)
    print("🪛"+pet+"Creando entorno virtual")
    subprocess.run(["python", "-m", "venv", "env"])
    subprocess.run(["env/Scripts/python", "-m", "pip", "install", "fastapi"])
    subprocess.run(["env/Scripts/python", "-m", "pip", "install", "uvicorn"])
    # now copy the template
    print("🔥"+pet+" Estamos ready papi!")
    abrir_vscode()
def crea_eleventy():
    #copy the template folder to the current folder
    nombre_proyecto = input(pet+"💬 ¿Como se llama tu proyecto? ")
    if nombre_proyecto == "":
        salida()
    print("🪛"+pet+"Creando proyecto "+nombre_proyecto)
    shutil.copytree(root_folder+"/templates/eleventy", local_path+"/"+nombre_proyecto)
    print("🔥"+pet+" Estamos ready papi!")
    abrir_vscode()
def ejecuta_ffmpeg():
    opciones = {
        1: "🎞️  Convertir a GIF",
        2: "🎞️  Convertir a MP4",
        3: "🎞️  Extraer MP3",
        4: "🎞️  Extraer WAV",
    }
    acciones = {
        1: to_gif,
        2: to_mp4,
        3: to_mp3,
        4: to_wav
    }

    print(pet+"💬 ¿Que quieres hacer?")
    for key, value in opciones.items():
        print("  "+Fore.GREEN + str(key) + "." + value)
    choice = int(input(pet+"💬 Introduce tu eleccion: "))
    acciones[choice]()
    print("🔥"+pet+" Estamos ready papi!")
def crea_media_download():
    print(pet+"💬 Pásame el link de tu vídeo")
    url = input(pet+"💬 ")
    subprocess.run(["yt-dlp", url], check=True)
def whisper_transcribe():
    print(pet+"💬 ¿Cómo se llama el archivo a transcribir?")
    file_name = input(pet+"💬 ")
    subprocess.run(["whisper", file_name, "--language", "es"])
def whisper_translate():
    print(pet+"💬 ¿Cómo se llama el archivo a traducir?")
    file_name = input(pet+"💬 ")
    subprocess.run(["whisper", file_name, "--task", "translate", "--language", "es"])
def whisper_record():
    grabar_audio()
    file_name = "grabacion.wav"
    subprocess.run(["whisper", file_name, "--language", "es"])
def crea_whisper():
    print(pet + "Que quieres que hagamos?")
    opciones = {
        1: "🎞️  Transcribir",
        2: "🎞️  Traducir",
        3: "🎞️  Grabar y transcribir"
    }
    acciones = {
        1: whisper_transcribe,
        2: whisper_translate,
        3: whisper_record
    }
    
    for key, value in opciones.items():
        print("  "+Fore.GREEN + str(key) + "." + value)
    choice = int(input(pet+"💬 Introduce tu eleccion: "))
    acciones[choice]()
    print("🔥"+pet+" Estamos ready papi!")

print(Back.RED + Fore.WHITE + " APP LAUNCHER ")
options_dict = {
    1: "🏺 HTML+CSS+JS ", 
    2: "🔮 p5js", 
    3: "🔮 p5js + p5.Capture + Utils",
    4: "🐍 Python Environment",
    5: "🐍 FastAPI",
    6: "📝 Eleventy",
    7: "📹 ffmpeg",
    8: "📀 Media Download",
    9: "👻 Whisper",
    0: "💀 Salir",
    }
colors_options = {
    1: Fore.BLUE,
    2: Fore.MAGENTA,
    3: Fore.MAGENTA,
    4: Fore.GREEN,
    5: Fore.GREEN,
    6: Fore.YELLOW,
    7: Fore.CYAN,
    8: Fore.YELLOW,
    9: Fore.RED,
    0: Fore.WHITE,

}
results_dict = {
    1: crea_htmlcssjs,
    2: crea_p5js,
    3: crea_p5js_extras,
    4: crea_python,
    5: crea_fastapi,
    6: crea_eleventy,
    7: ejecuta_ffmpeg,
    8: crea_media_download,
    9: crea_whisper,
    0: salida, 
    }

choice = prompt_user(pet+"Que vamos a hacer?", options_dict, colors_options)
results_dict[choice]()