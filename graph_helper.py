import matplotlib.pyplot as plt
import librosa as lb
import numpy as np
import soundfile as sf

import time
import wave
import math

class graph_helper:
    def __init__(self):
        self.fs = 44100

    def plot_spectrogram(self):
        audio = lb.load("Recordings/mic.wav")
        audio_emphasised = lb.load("Recordings/mic_emp.wav")
        audio_without_silence = lb.load("Recordings/mic_emp_wout_silence.wav")
        audio_normalized = lb.load("Recordings/mic_normalized.wav")

        s_orig = lb.amplitude_to_db(np.abs(lb.stft(audio[0])), ref=np.max, top_db=None)
        s_emphasised = lb.amplitude_to_db(np.abs(lb.stft(audio_emphasised[0])), ref=np.max, top_db=None)
        s_without_silence = lb.amplitude_to_db(np.abs(lb.stft(audio_without_silence[0])), ref=np.max, top_db=None)
        s_normalized = lb.amplitude_to_db(np.abs(lb.stft(audio_normalized[0])), ref=np.max, top_db=None)

        fig, ax = plt.subplots(nrows=4, sharex=True, sharey=True)
        lb.display.specshow(s_orig, y_axis='log', x_axis='time', ax=ax[0])
        ax[0].set(title='Original signal')
        img = lb.display.specshow(s_emphasised, y_axis='log', x_axis='time', ax=ax[1])
        ax[1].set(title='Pre-emphasized signal')
        fig.colorbar(img, ax=ax, format="%+2.f dB")
        img = lb.display.specshow(s_without_silence, y_axis='log', x_axis='time', ax=ax[2])
        ax[2].set(title='Cleaned signal from silence')
        img = lb.display.specshow(s_normalized, y_axis='log', x_axis='time', ax=ax[3])
        ax[3].set(title='Normalized audio')

        fig, ax = plt.subplots(nrows=4, sharex=True, sharey=True)
        lb.display.waveshow(audio[0], axis='time', ax=ax[0])
        ax[0].set(title='Original signal')
        img = lb.display.waveshow(audio_emphasised[0], axis='time', ax=ax[1])
        ax[1].set(title='Pre-emphasized signal')
        img = lb.display.waveshow(audio_without_silence[0], axis='time', ax=ax[2])
        ax[2].set(title='Cleaned signal from silence')
        img = lb.display.waveshow(audio_normalized[0], axis='time', ax=ax[3])
        ax[3].set(title='Normalized audio')

        plt.show()