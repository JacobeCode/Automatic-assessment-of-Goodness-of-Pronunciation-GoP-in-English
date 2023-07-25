import soundfile as sf
import librosa as lb
import numpy as np

class processors:
    def __init__(self, speech_wav):
        self.speech_wav = speech_wav

    def pre_emphasis(self, audio_to_process):
        if audio_to_process is not None:
            self.speech_wav = audio_to_process
        processed_audio = lb.effects.preemphasis(self.speech_wav, coef=0.97)

        sf.write("Recordings/mic_emp.wav", processed_audio, 44100, subtype="PCM_24")

        return processed_audio

    def silence_removal(self, audio_to_process):
        if audio_to_process is None:
            audio_to_process = lb.load("Recordings/mic_emp.wav")[0]
        audio_split = lb.effects.split(audio_to_process, top_db=30)
        audio_removed_silence = []
        for chunk in audio_split:
            audio_removed_silence.append(audio_to_process[chunk[0]:chunk[1]])
        audio_without_silence = np.concatenate(audio_removed_silence, axis=0)

        sf.write("Recordings/mic_emp_wout_silence.wav", audio_without_silence, 44100, subtype="PCM_24")

        return audio_without_silence

    def RMS_normalization(self, audio_to_process):
        if audio_to_process is None:
            audio_to_process = lb.load("Recordings/mic_emp_wout_silence.wav")[0]
        signal_rms = np.sqrt(np.mean(audio_to_process**2))

        normalized_r = 10**(signal_rms / 10.0)

        normalized_parameter = np.sqrt((len(audio_to_process)*normalized_r**2)/np.sum(audio_to_process**2))

        normalized_audio = audio_to_process*normalized_parameter

        sf.write("Recordings/mic_emp_wout_silence.wav", normalized_audio, 44100, subtype="PCM_24")

        return normalized_audio

    def full_pre_process(self):
        pre_emphasised_audio = self.pre_emphasis(None)
        without_silence = self.silence_removal(pre_emphasised_audio)
        normalized = self.RMS_normalization(without_silence)

        return normalized