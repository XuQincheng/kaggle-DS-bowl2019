# Machine Learning Lab - Final Project
## Group Members:
- [Kevin Loftis](https://github.com/loftiskg)
- [Ariana Moncada](https://github.com/arianamoncada)
- [Hoda Noorian](https://github.com/Hodanoo)

This repository includes the final project information for the Machine Learning Laboratory - MSDS 699 course.
Our dataset is game play history for the PBS Kids Measure Up! app provided by Kaggle [2019 Data Science Bowl](https://www.kaggle.com/c/data-science-bowl-2019).
Using the PBS Kids Measure Up app game play data, we created a pipeline to predict how many attempts it would take an individual to complete their next Assessment.

# Data Overview 
In this dataset, we are provided with game analytics for the PBS KIDS Measure Up! app. In this app, children navigate a map and complete various levels, which may be activities, video clips, games, or assessments. Each assessment is designed to test a child's comprehension of a certain set of measurement-related skills. There are five assessments: Bird Measurer, Cart Balancer, Cauldron Filler, Chest Sorter, and Mushroom Sorter.

The objective of this project is to predict a users **next** Assessment outcome using their previous game history. The categorical labels we have in our dataset are defined into 4 groups (labeled as *accuracy_group* in the data):

3: the assessment was solved on the first attempt

2: the assessment was solved on the second attempt

1: the assessment was solved after 3 or more attempts

0: the assessment was never solved

There are roughly 11 million rows in the training data, with 17,000 unique installation_ids, which can be assumed to map to a single user. 


# Notebook
Contains the submission notebook with the data processing and modeling pipeline that will result in writing predictions to a .csv file for the Kaggle 2019 Data Science Bowl Competition.

To get started with the notebook create the conda environment with the include `environment.yml` file. This will make sure that you have all of the neccessary packages installed.  To do this run the following command while in this directory:

```
conda env create -f environment.yml
```
