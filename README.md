<div align="center">

# Medical Dataset Classification

<br>

[![made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

</div>

This is my submission for the [Tech Weekend Data Science Challenge](https://www.kaggle.com/c/tech-weekend-data-science-hackathon) on Kaggle.

## Problem Statement

We are living in an “information age”. Terabytes of data are produced every day. Data mining is the process which turns a collection of data into knowledge. The health care industry generates a huge amount of data daily. However, most of it is not effectively used. Efficient tools to extract knowledge from these databases for clinical detection of diseases or other purposes are not much prevalent. With the rise of Data Science and Machine Learning it is possible to make sense of huge data and provide assitance to doctors. This Tech Weekend we challenge the participants to predict if a person given his/her attributes has a heart disease or not.

## Implementation

- Since it is a classification problem, after visualizing and analyzing the dataset, I decided to start off with a **KNN** implementation which gave me a **61%** accuracy.
- Then I decided to use **Logistic Regression** which increased my accuracy upto 83% which further went upto **87%** after setting class weight as balanced in Scikit-learn.
- After some research and Googling, I decided to use **Random Forests** and it worked perfectly giving me an accuracy of **89.856%**.
- The Notebook containing the source code can be found [here.](https://github.com/KaustubhDamania/Medical-Dataset-Classification-Kaggle/blob/master/Untitled.ipynb) The training/testing dataset can be found in dataset.zip.



## Contributing

Open to `enhancements` and `bugs`

## Note

This was my first contest on Kaggle and I hope to participate in more such contests. :smile:
