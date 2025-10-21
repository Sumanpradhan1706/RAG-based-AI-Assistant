import whisper

model = whisper.load_model("small")
result = model.transcribe(audio ="audios/1_Introduction to Python.mp3", language ="hi",
task="translate")

print(result["text"])