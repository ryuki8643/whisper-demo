import sounddevice as sd
import numpy as np
import os
import whisper
import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings
from aiortc.contrib.media import MediaRecorder


wav_file_path = "record.wav"

def sound_to_text(file_path):
    if os.path.exists(file_path):
        model = whisper.load_model("small") # this is model size of whisper base or small or medium or large
        result = model.transcribe(file_path)
        st.text(result["text"])


def recorder_factory():
    return MediaRecorder(wav_file_path)

st.title('Record to Text By Whisper ')


webrtc_streamer(
        key="sendonly-audio",
        mode=WebRtcMode.SENDRECV,
        in_recorder_factory=recorder_factory,
        client_settings=ClientSettings(
            media_stream_constraints={
                "audio": True,
                "video": False,
            },
        ),
    )

if st.button('Whisper text recognition'):
        st.text('Start to recognize')
        sound_to_text(wav_file_path)
        st.text('Finish to recognize')
