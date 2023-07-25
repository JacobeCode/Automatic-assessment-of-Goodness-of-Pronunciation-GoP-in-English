from threading import Thread, Lock
from pynput import keyboard
import pyaudio
import wave


class player:
    def __init__(self, wavfile):
        self.wavfile = wavfile
        self.playing = 0  # flag so we don't try to record while the wav file is in use
        self.lock = Lock()  # muutex so incrementing and decrementing self.playing is safe

    # contents of the run function are processed in another thread so we use the blocking
    # version of pyaudio play file example: http://people.csail.mit.edu/hubert/pyaudio/#play-wave-example
    def run(self):
        with self.lock:
            self.playing += 1
        with wave.open(self.wavfile, 'rb') as wf:
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            data = wf.readframes(8192)
            while data != b'':
                stream.write(data)
                data = wf.readframes(8192)

            stream.stop_stream()
            stream.close()
            p.terminate()
            wf.close()
        with self.lock:
            self.playing -= 1