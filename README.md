# twitter-text-classification
Multi-class text classification of tweets into 'figurative , 'sarcasm', 'irony', and 'regular'.

## Contents
* [Overview](#overview)
* [Motivation](#motivation)
* [Dataset](#dataset)
* [Setup](#setup)
* [Repository files](#repository-files)
* [Model](#model)
* [What did I learn](#what-did-i-learn)

## Overview
A model which classifies the tweeted texts into four figures of speech - figurative, irony, sarcasm, regular.

## Motivation
Although this may seem to be a small classification problem, but for a machine it is crucial to understand the figurative language to understand the context behind any scentence. When figure of speeches are used in the text, the literal meaning is different than the actual meaning. This may cause problem in language related models.

## Dataset
The dataset was downloaded from Kaggle<br>
Website: [twitter dataset](https://www.kaggle.com/nikhiljohnk/tweets-with-sarcasm-and-irony)

## Setup
Windows 10<br>
python 3.7<br>
tensorflow-gpu==2.1.0

## Repository files


## Model
<p align="center">
  <img src="" width="400">
</p>

## What did I learn?
#### Problem: Loss function was decreasing but oscillating
Solution:<br>
Reducing the learning rate, use momentum on SGD (or better, use momentum based optimizers like Adam)
#### Problem: Difference in final values of valdaition and training accuracy
Solution:<br>
Underfitting - val and train accuracy low<br>
Overfitting - high train accuracy, low val accuracy<br>
Good fit - val accuracy close to train accuracy and both are high<br>
Unknown fit - high val accuracy, low train accuracy<br>

My model was facing overfitting, so I increased the batch size and added dropout layers.
