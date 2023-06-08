import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import os

def record(filename):
    # sampling rate
    fs = 44100
    # record 5 seconds  
    t = 5

    # 録音を実行
    rec = sd.rec(int(t * fs), samplerate=fs, channels=2, dtype='float32')
    sd.wait()

    # 録音したデータをWAVファイルとして保存
    write(filename, fs, rec)

def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")

if __name__ == '__main__':
    filename = 'output.wav'
    record(filename=filename)

    remove_file(filename=filename)