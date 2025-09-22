**Install the Required Library**

Open a terminal or command prompt and run:

```bash
pip install SpeechRecognition
```

(Optional) If you want to record from a microphone:

```bash
pip install pyaudio
```

On Windows, if `pyaudio` fails, install it from [PyAudio wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

Project Folder Structure

```
speech_to_text/
│
├─ speech.wav      # (Optional) a test audio file
└─ speech_to_text.py     # main Python script
```


1. Place an audio file like `speech.wav` in the project folder.
2. Run:

   ```bash
   python speech_to_text.py
   ```
3. To use the microphone, **comment out** the file function and **uncomment** the microphone function.

---

How It Works

* `speech_recognition.Recognizer()` creates a recognizer instance.
* `recognizer.record()` captures audio from the file.
* `recognizer.recognize_google()` sends the audio to Google’s free speech-to-text API and returns the transcribed text.



This project is small enough to run in a single Python file and works with any clear `.wav` or `.flac` audio.
