import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import os
import whisper

def record(filename):

    fs = 44100
    t = 5
    rec = sd.rec(int(t * fs), samplerate=fs, channels=2, dtype='float32')
    sd.wait()

    write(filename, fs, rec)

def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")

def sound_to_text(filename):

    model = whisper.load_model("base")
    result = model.transcribe(filename)
    print(result["text"])

if __name__ == '__main__':
    filename = 'output.wav'

    record(filename=filename)
    sound_to_text(filename=filename)
    remove_file(filename=filename)