import pyaudio
import pynput
import wave
import pynput

from pynput import keyboard

from recorder import recorder
from player import player

import librosa as lb

class wav_operator(keyboard.Listener):
    def __init__(self, recorder, player):
        super().__init__(on_press=self.on_press, on_release=self.on_release)
        self.recorder = recorder
        self.player = player

    def pre_emphasis(self, filename):
        analysed_audio = lb.load(filename + ".wav", sr=44100)
        emphasis_audio = lb.effects.preemphasis(analysed_audio[0])

        writefile = wave.open(filename + "_emp.wav", 'w')
        writefile.setnchannels(2)
        writefile.setsampwidth(2)
        writefile.setframerate(44100)
        writefile.writeframes(emphasis_audio)
        writefile.close()

    def on_press(self, key):
        if key is None:
            pass
        elif isinstance(key, keyboard.Key):
            if key.ctrl and self.player.playing == 0:
                self.recorder.start()
        elif isinstance(key, keyboard.KeyCode):
            if key.char == 'q':
                if self.recorder.recording:
                    self.recorder.stop()
                return False
            if key.char == 'p' and not self.recorder.recording:
                self.player.run()

    def on_release(self, key):
        if key is None:
            pass
        elif isinstance(key, keyboard.Key):
            self.recorder.stop()
        elif isinstance(key, keyboard.KeyCode):
            pass