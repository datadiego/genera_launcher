import whisper

model = whisper.load_model("base")
result = model.transcribe("output.mp3")
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(result['text'])
