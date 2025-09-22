import speech_recognition as sr

def transcribe_from_file(audio_path):
    recognizer=sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        print("Listening from file....")
        audio_data = recognizer.record(source) #read the entire file
    
    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcribed Text : ",text)
        with open("Transcript.txt","w") as f:
            f.write(text)
    except sr.UnknownValueError:
        print("Could not understand the audio.")

    except sr.RequestError as e:
        print("API error ; {0}".format(e))

def transcribe_from_microphone():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source :
        print("Adjusting fro ambient noise ... Please wait....")
        recognizer.adjust_for_ambient_noise(source)
        print("Speak something : ")
        audio_data = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio_data,language="hi-IN")
        
        print("You said : \n",text)
        with open("Transcript.txt","w") as f:
            f.write(text)

    except sr.UnknownValueError:
        print("Could not understand your speach.")
    except sr.RequestError as e:
        print("API ERROR; {0}".format(e))

if __name__=="__main__":
    #transcribe_from_file("speech.wav")
    transcribe_from_microphone()