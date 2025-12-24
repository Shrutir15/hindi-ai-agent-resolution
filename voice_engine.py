import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import time

# 1. THE EARS: Listen to Hindi Speech
def listen_hindi():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n[LISTENING...] बोलिए, मैं सुन रहा हूँ...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='hi-IN')
        print(f"[YOU SAID]: {text}")
        return text
    except Exception as e:
        print("[ERROR]: आवाज समझ नहीं आई।")
        return None

# 2. THE VOICE: Speak in Hindi
def speak_hindi(text):
    print(f"[AGENT SPEAKING]: {text}")
    tts = gTTS(text=text, lang='hi')
    filename = "temp_voice.mp3"
    tts.save(filename)
    
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    pygame.mixer.quit()
    os.remove(filename)

# TEST THE VOICE
if __name__ == "__main__":
    speak_hindi("नमस्ते, मैं आपकी कैसे मदद कर सकता हूँ?")