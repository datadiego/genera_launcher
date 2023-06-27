import ffmpeg
import colorama
import os
local_path = os.getcwd()

colorama.init()

def to_gif():
    print("🐔 ", end="")
    print(colorama.Back.GREEN, colorama.Fore.BLACK, "¿Como se llama tu archivo?", colorama.Style.RESET_ALL, end="")
    input_file = input("Archivo de entrada: ")
    # move where actual terminal is
    os.chdir(local_path)
    input_file = local_path + "\\" + input_file
    output_file = local_path + "\\" + "output.gif"
    ffmpeg.input(input_file).output(output_file, acodec='mp3').run()
    print("👌🏻🐔 ", end="")
    print(colorama.Back.GREEN, colorama.Fore.BLACK, "Archivo "+output_file+" creado", colorama.Style.RESET_ALL)

def to_mp4():
    print("🐔 ", end="")
    print(colorama.Back.GREEN, colorama.Fore.BLACK, "¿Como se llama tu archivo?", colorama.Style.RESET_ALL, end="")
    input_file = input("Archivo de entrada: ")
    # move where actual terminal is
    os.chdir(local_path)
    input_file = local_path + "\\" + input_file
    output_file = local_path + "\\" + "output.mp4"
    ffmpeg.input(input_file).output(output_file, acodec='mp3').run()
    print("👌🏻🐔 ", end="")
    print(colorama.Back.GREEN, colorama.Fore.BLACK, "Archivo "+output_file+" creado", colorama.Style.RESET_ALL)


def to_webm():
    print("🐔 ", end="")
    print(colorama.Back.GREEN, colorama.Fore.BLACK, "¿Como se llama tu archivo?", colorama.Style.RESET_ALL, end="")
    input_file = input("Archivo de entrada: ")
    # move where actual terminal is
    os.chdir(local_path)
    input_file = local_path + "\\" + input_file
    output_file = local_path + "\\" + "output.webm"
    ffmpeg.input(input_file).output(output_file, acodec='mp3').run()
    print("👌🏻🐔 ", end="")
    print(colorama.Back.GREEN, colorama.Fore.BLACK, "Listo! Archivo "+output_file+" creado", colorama.Style.RESET_ALL)


def to_mp3():
    print("🐔 ", end="")
    print(colorama.Back.GREEN, colorama.Fore.BLACK, "¿Como se llama tu archivo?", colorama.Style.RESET_ALL, end="")
    input_file = input("Archivo de entrada: ")
    # move where actual terminal is
    os.chdir(local_path)
    input_file = local_path + "\\" + input_file
    output_file = local_path + "\\" + "output.mp3"
    ffmpeg.input(input_file).output(output_file, acodec='mp3').run()
    print("👌🏻🐔 ", end="")

    print(colorama.Back.GREEN, colorama.Fore.BLACK, "Listo! Archivo "+output_file+" creado", colorama.Style.RESET_ALL)


def to_wav():
    print("🐔 ", end="")
    print(colorama.Back.GREEN, colorama.Fore.BLACK, "¿Como se llama tu archivo?", colorama.Style.RESET_ALL, end="")
    input_file = input("Archivo de entrada: ")
    # move where actual terminal is
    os.chdir(local_path)
    input_file = local_path + "\\" + input_file
    output_file = local_path + "\\" + "output.wav"
    ffmpeg.input(input_file).output(output_file, acodec='mp3').run()
    print("👌🏻🐔 ", end="")

    print(colorama.Back.GREEN, colorama.Fore.BLACK, "Listo! Archivo "+output_file+" creado", colorama.Style.RESET_ALL)


