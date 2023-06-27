import pyaudio
import wave
import keyboard

def grabar_audio():
    chunk = 1024
    formato = pyaudio.paInt16
    canales = 1
    frecuencia_muestreo = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=formato,
                    channels=canales,
                    rate=frecuencia_muestreo,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []
    grabando = False

    print("Presiona Enter para comenzar a grabar. Presiona Enter nuevamente para detener la grabación.")

    def on_key_press(event):
        nonlocal grabando

        if event.name == 'enter':
            if grabando:
                grabando = False
                return False  # Detiene el listener de keyboard

            grabando = True
            print("Grabando audio...")

    keyboard.on_press(on_key_press)

    while True:
        if grabando:
            data = stream.read(chunk)
            frames.append(data)
        else:
            if frames:
                print("¡Grabación finalizada!")
                break

    stream.stop_stream()
    stream.close()

    p.terminate()

    nombre_archivo = "grabacion.wav"
    wf = wave.open(nombre_archivo, 'wb')
    wf.setnchannels(canales)
    wf.setsampwidth(p.get_sample_size(formato))
    wf.setframerate(frecuencia_muestreo)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Grabación guardada en el archivo:", nombre_archivo)


# Ejecutar la función si se ejecuta el script directamente
if __name__ == '__main__':
    grabar_audio()
