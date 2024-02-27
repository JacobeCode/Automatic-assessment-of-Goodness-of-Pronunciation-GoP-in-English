# Automatic assessment of Goodness of Pronunciation in English

## This repository contains files, models and results connected to the project entitled "Automatic Assessment of Goodness of Pronunciation in English". The main goal of this project done as an engineering thesis was to train ASR models compatible with the Goodness of Pronunciation (GoP) algorithm and test (or improve if it is possible) the classic formulation of Goodness of Pronunciation with the use of [Kaldi](https://github.com/kaldi-asr/kaldi) toolkit. Also, project involved a full literature study about related topics.

## Introduction
This repository contains files and information about the project created as an Engineering Thesis. 

The main goal of this project and research is Automatic Assessment with the Goodness of Pronunciation algorithm in the English language. This project was based on the Kaldi toolkit and as in the solution used there, the solution proposed in (1) was used as the reference in implementation and training.

In the course of this project with the use of the Kaldi toolkit a few ASR models were trained and tested with the GoP algorithm.

Results and models can be found in respective directories.

The thesis and report (currently only in Polish) can be found in `reports_and_thesis`.

## Content

This version of the repository contains final files and reports connected to this project (exceptions are the files with the `[draft version]` tag - these files might be a little outdated or not very well organized).

In consecutive directories can be found:
- `GoP_Best_Results_Backup_Example` - files of the final and best GoP run with tdnn_sp_1c_smallset_cmvn model.
- `GoP_logs` - log files from consecutive algorithm runs with descriptions of actions and results.
- `asr_models` - files and models connected to all trained ASR models in the course of this project.
- `best_model_plots` - plots connected to training [Accuracy and Loss] for best models (also used in the report).
- `data [wer_gop_trainstats]` - data in xlsx format - can be used for plotting or analysis. Mainly GoP and WER results and also Loss and Accuracy stats.
- `librispeech_train_logs` - log files from consecutive ASR training runs with a description of actions and results.
- `models_plot_data` - separate data for each model about the training process (can be used for plotting results).
- `other_models_and_data` - mainly data and files connected to smaller models trained and used in the whole process (like mono models).
- `reports_and_thesis` - thesis, reports and presentation (in the Polish language).

## Citing

> (1) Hu, W., Qian, Y., Soong, F.K., & Wang, Y. (2015). Improved mispronunciation detection with deep neural network trained
> acoustic models and transfer learning based logistic regression classifiers. Speech Commun., 67, 154-166.
