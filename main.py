from wav_operator import wav_operator
from recorder import recorder
from player import player
from graph_helper import graph_helper

# if __name__ == '__main__':
#     rec = recorder("Recordings/mic.wav")
#     play = player("Recordings/mic.wav")
#     wav_operator = wav_operator(rec, play)
#     print("Hold Ctrl to record, press p to playback, press q to quit.")
#     wav_operator.start()
#     wav_operator.join()
#
# wav_operator.pre_emphasis("mic")

gp = graph_helper()
gp.plot_spectrogram()
