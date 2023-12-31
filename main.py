import speech_recognition as sr
from os import path
from pydub import AudioSegment
import ffprobe

import sys
sys.path.append("ffmpeg-6.0")
# convert mp3 file to wav
sound = AudioSegment.from_mp3("BEP395-Strategic-Decisions-1.mp3")
sound.export("transcript.wav", format="wav")


# transcribe audio file
AUDIO_FILE = "transcript.wav"

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

        print("Transcription: " + r.recognize_google(audio))