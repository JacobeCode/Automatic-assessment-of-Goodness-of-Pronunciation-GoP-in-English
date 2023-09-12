# Auto_assessment_of_GoP_Eng

## Introduction
This repository contains files and information about project created as Engineering Thesis. 

Main goal of the program is automatic assessment with Goodnees of Pronuanciaction algorithm in English. In this approach, the newer and other tools will be used in comparison to older implementations and works. Final product should be a functional program - user-friendly and ready-to-use.

Program is created as Engineering Thesis by [JacobeCode](https://github.com/JacobeCode).

## Installation/Requirements

- Python 3.x
- packages assembled in [GoP_Ebg.yml](GoP_Eng.yml)
- PyTorch (torch, torchvision, torchaudio) as shown at starting page [PyTorch](https://pytorch.org/get-started/locally/)

## Instances and functions to use:

- [main.py](main.py) - main executive file of the program.
- [extractors.py](extractors.py) - contains all functions and functionalities that are responsible for extracting information and data from audio recordings of speech.
- [phonemizer.py](phonemizer.py) - contains functionalities responsible for diving audio recordings and transcriptions into smaller chunks ex. phonemes and words.
- [processors.py](processors.py) - instance for pre- / post-processing of data including: pre-processing, pre-emphasis and post-processing.
- [graph_helper.py](graph_helper.py) - class contains auxiliary function for plotting graph with audio waves and spectrogram for analysis to choose the best parameters.
- [wav_operator.py](wav_operator.py) - instance that controls recording / playback of user speech - this one is using two subclasses:
  - [recorder.py](recorder.py) - subclass that is responsible for recording of user speech with use of pyaudio and wave.
  - [player.py](player.py) - subclass that is responsible for playback of user recording.

## Content

### Issues to fix

- scaling graphs and spectrogram's