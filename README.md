# Machine Learning Lab - Final Project
## Group Members:
- [Kevin Loftis](https://github.com/loftiskg)
- [Ariana Moncada](https://github.com/arianamoncada)
- [Hoda Noorian](https://github.com/Hodanoo)

This repository includes the final project information for the Machine Learning Laboratory - MSDS 621 course.
Our dataset is game play history for the PBS Kids Measure Up! app provided by Kaggle [2019 Data Science Bowl](https://www.kaggle.com/c/data-science-bowl-2019).
Using the PBS Kids Measure Up app game play data, we created a pipeline to predict how many attempts it would take an individual to complete their next Assessment.

# Data Overview 
In this dataset, we are provided with game analytics for the PBS KIDS Measure Up! app. In this app, children navigate a map and complete various levels, which may be activities, video clips, games, or assessments. Each assessment is designed to test a child's comprehension of a certain set of measurement-related skills. There are five assessments: Bird Measurer, Cart Balancer, Cauldron Filler, Chest Sorter, and Mushroom Sorter.

The label and goal of this project is to predict the outcome, which are grouped into 4 groups (labeled accuracy_group in the data):

3: the assessment was solved on the first attempt
2: the assessment was solved on the second attempt
1: the assessment was solved after 3 or more attempts
0: the assessment was never solved

There is around 11 million rows in the training data, with 17,000 unique installation_ids, which can be supposed to be mapped to a single kid. 


# Description of Notebook
Repository for submission notebooks for the Kaggle 2019 Data Science Bowl Competition
