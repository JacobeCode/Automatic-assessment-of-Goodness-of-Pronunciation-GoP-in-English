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
        audio = lb.load("Recordings/mic.wav", sr=self.fs)
        audio_emp = lb.effects.preemphasis(audio[0])
        s_orig = lb.amplitude_to_db(np.abs(lb.stft(audio[0])), ref=np.max, top_db=None)
        s_emphasised = lb.amplitude_to_db(np.abs(lb.stft(audio_emp)), ref=np.max, top_db=None)
        fig, ax = plt.subplots(nrows=2, sharex=True, sharey=True)
        lb.display.specshow(s_orig, y_axis='log', x_axis='time', ax=ax[0])
        ax[0].set(title='Original signal')
        ax[0].label_outer()
        img = lb.display.specshow(s_emphasised, y_axis='log', x_axis='time', ax=ax[1])
        ax[1].set(title='Pre-emphasized signal')
        fig.colorbar(img, ax=ax, format="%+2.f dB")

        sf.write("Recordings/mic_emp.wav", audio_emp, 44100, subtype="PCM_24")

        plt.figure(figsize=(20, 5))
        lb.display.waveshow(audio_emp, sr=44100)
        plt.title('Audio Signal')
        plt.ylabel('Amplitude')
        plt.xlabel('Time (Sec)')

        audio_rem_silence = []
        audio_split = lb.effects.split(audio_emp, top_db=30)
        for sample in audio_split:
            audio_rem_silence.append(audio_emp[sample[0]:sample[1]])
        audio_wout_silence = np.concatenate(audio_rem_silence, axis=0)

        time = np.linspace(0, len(audio_wout_silence)/44100, num=len(audio_wout_silence))

        plt.figure(figsize=(20, 5))
        plt.plot(time, audio_wout_silence)
        plt.title('Emphasized Signal without Silence (Librosa)')
        plt.ylabel('Amplitude')
        plt.xlabel('Time (Sec)')
        plt.show()

        sf.write("Recordings/mic_emp_wout_silence.wav", audio_wout_silence, 44100, subtype="PCM_24")

        signal_RMS = np.sqrt(np.mean(audio_wout_silence**2))

        r_normalized = 10**(signal_RMS / 10.0)
        norm_param = np.sqrt((len(audio_wout_silence)*r_normalized**2)/np.sum(audio_wout_silence**2))

        audio_normalized = audio_wout_silence*norm_param

        sf.write("Recordings/mic_normalized.wav", audio_normalized, 44100, subtype="PCM_24")

        plt.figure(figsize=(20, 5))
        s_normalized = lb.amplitude_to_db(np.abs(lb.stft(audio_normalized)), ref=np.max, top_db=None)
        lb.display.specshow(s_normalized, y_axis='log', x_axis='time')
        plt.title('Emphasized Signal without Silence (Librosa)')
        plt.ylabel('Amplitude')
        plt.xlabel('Time (Sec)')

        plt.show()
