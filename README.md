# Audio-antideepfake
Attention! The program is in the MVP project state. 
Machine learning model optimized for the task of fast audio file classification based on the minimum amount of audio file information.
The project aims to be used in active audio calls within companies and individual users.
To solve this problem, a relatively simple model was used, which consists of MFCC and gradient boosting.
The technology of active replenishment of the dataset and additional training will also be applied.

Research

A study of synthesized speech was conducted and scientific articles were analyzed.A study of synthesized speech was conducted and scientific articles on this topic were analyzed. 
From a number of scientific articles, it was found that bispectral analysis is the most accurate data for prediction. 
Empirically, it was found that gradient boosting with hyperparameters that are currently used in the program is effective for such a task.

Created

A study of synthesized speech was conducted and scientific articles were analyzed
A basic model based on gradient boosting, which was trained on a dataset with 2-second audio files. The dataset was chosen in accordance with the practical tasks of the model.
At the moment, a figure of ~ 70% of predictions has been achieved.

Plans

Expand computer capacity (as it is currently limited by this factor)
Create your own large-scale dataset based on speech datasets and current speech synthesis models.
Increase the percentage of model predictions.
Improvement of the model architecture
Function of communication with instant messengers and phone calls.
