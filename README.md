# Audio-antideepfake
Attention! The program is in the prototype project state.
Внимание! Программа находится в состоянии проекта-прототипа
_______________________
Introduction 

Machine learning model optimized for the task of fast audio file classification based on the minimum amount of audio file information.
The project aims to be used in active audio calls within companies and individual users.
To solve this problem, a relatively simple model was used, which consists of MFCC and gradient boosting.
The technology of active replenishment of the dataset and additional training will also be applied.

Вступление 

Модель машинного обучения, оптимизированная для задачи быстрой классификации аудиофайлов на основе минимального объема информации об аудиофайлах.
Проект предназначен для использования в активных аудиовызовах внутри компаний и отдельных пользователей.
Для решения этой проблемы была использована относительно простая модель, которая состоит из MFCC и gradient boosting.
Также будет применена технология активного пополнения набора данных и дополнительного обучения.
_______________________
Research

A study of synthesized speech was conducted and scientific articles were analyzed.A study of synthesized speech was conducted and scientific articles on this topic were analyzed. |
From a number of scientific articles, it was found that bispectral analysis is the most accurate data for prediction. 
Empirically, it was found that gradient boosting with hyperparameters that are currently used in the program is effective for such a task.

Исследование

Было проведено исследование синтезированной речи и проанализированы научные статьи.Было проведено исследование синтезированной речи и проанализированы научные статьи на эту тему. |
Из ряда научных статей было выведено, что биспектральный анализ является наиболее точным методом прогнозирования. 
Эмпирически было установлено, что повышение градиента с помощью гиперпараметров, которые в настоящее время используются в программе, эффективно для решения такой задачи.
_______________________
Created 

A study of synthesized speech was conducted and scientific articles were analyzed |
A basic model based on gradient boosting, which was trained on a dataset with 2-second audio files. The dataset was chosen in accordance with the practical tasks of the model.
At the moment, a figure of ~ 75% of predictions has been achieved(Average prediction level of models from scientific papers).

Создано

Было проведено исследование синтезированной речи и проанализированы научные статьи |
Базовая модель, основанная на градиентном ускорении, которая была обучена на наборе данных с 2-секундными аудиофайлами. Набор данных был выбран в соответствии с практическими задачами модели.
На данный момент достигнута цифра в ~75% прогнозов(Средний уровень предсказаний моделей из научных статей).
_______________________
Plans

Expand computer capacity (as it is currently limited by this factor)
Create your own large-scale dataset based on speech datasets and current speech synthesis models.
Increase the percentage of model predictions.
Improvement of the model architecture
Function of communication with instant messengers and phone calls.

Планы

Расширяйте возможности компьютера (поскольку в настоящее время они ограничены этим фактором),
Создать собственный крупномасштабный набор данных на основе наборов речевых данных и текущих моделей синтеза речи.
Увеличьте процент предсказаний модели.
Улучшите функцию архитектуры модели для анализа звонков в мессенджерах  и телефонных звонков.
_______________________
Testing Instructions:

At the moment, only the version without the dataset has been downloaded, so when you run it, you only need to specify the full path to your datasets in the code and combine the model files and executable code into one folder.I'm sorry for the inconvenience.
We suggest using this dataset for this:
https://www.kaggle.com/datasets/mohammedabdeldayem/the-fake-or-real-dataset
Инструкции по тестированию:

На данный момент загружена только версия без набора данных, поэтому при ее запуске вам нужно только указать полный путь к вашим наборам данных в коде и объединить файлы модели и исполняемый код в одну папку.Прошу прощения за предоставленные неудобства.
Предлагаем использовать для этого данный датасет:
https://www.kaggle.com/datasets/mohammedabdeldayem/the-fake-or-real-dataset
_______________________
