# Automatic assessment of Goodness of Pronunciation in English

## This repository contains files, models and results connected to the project entitled "Automatic Assessment of Goodness of Pronunciation in English". The main goal of this project done as an engineering thesis was to train ASR models compatible with the Goodness of Pronunciation (GoP) algorithm and test (or improve if it is possible) the classic formulation of Goodness of Pronunciation with the use of [Kaldi](https://github.com/kaldi-asr/kaldi) toolkit. Also, project involved a full literature study about related topics.

## Introduction
This repository contains files and informations about project created as Engineering Thesis. 

Main goal of this project and research is Automatic Assessment with Goodnees of Pronuanciaction algorithm in English language. This project was based on Kaldi toolit and as in solution used there, the solution proposed in (1) was used as reference in implementation and training.

In course of this project with use of Kaldi toolit a few ASR models was trained and tested with GoP algorithm.

Results and models can be found in respecive directories.

Thesis and report (currently only in Polish) can be found in `reports_and_thesis`.

## Content

This version of repository contains final files and reports connected to this project (exceptions are the files with `[draft version]` tag - these files might be a little outdated or not very well organized).

In consecutive directories can be found:
- `GoP_Best_Results_Backup_Example` - files of the final and best GoP run with tdnn_sp_1c_smallset_cmvn model.
- `GoP_logs` - log files from consecutive algorithm runs with description of actions and results.
- `asr_models` - files and models connected to all trained ASR models in course of this project.
- `best_model_plots` - plots connected to training [Accuracy and Loss] for best models (also used in report).
- `data [wer_gop_trainstats]` - data in xlsx format - can be used for plotting or analysis. Mainly GoP and WER results and also Loss and Accuracy stats.
- `librispeech_train_logs` - log files from consecutive ASR training runs with description of actions and results.
- `models_plot_data` - separate data for each model about training process (can be used for plotting results).
- `other_models_and_data` - mainly data and files connected to smaller models trained and used in whole process (like mono models).
- `reports_and_thesis` - thesis, reports and presentation (in Polish language).

Program is created as Engineering Thesis by [JacobeCode](https://github.com/JacobeCode).

## Citing

> (1) Hu, W., Qian, Y., Soong, F.K., & Wang, Y. (2015). Improved mispronunciation detection with deep neural network trained
> acoustic models and transfer learning based logistic regression classifiers. Speech Commun., 67, 154-166.
