# Behavioral Cloning Project


Overview
---
This repository contains starting files for the Behavioral Cloning Project.

In this project, I will use what I've learned about deep neural networks and convolutional neural networks to clone driving behavior. I will train, validate and test a model using Keras. The model will output a steering angle to an autonomous vehicle.

I use Udacity simulator where you can steer a car around a track for data collection. I'll use image data and steering angles to train a neural network and then use this model to drive the car autonomously around the track.


the project inculdes five files: 
* model.py (script used to create and train the model)
* drive.py (script to drive the car)
* modelf.h5 (a trained Keras model)

This README file describes how to output the video in the "Details About Files In This Directory" section.

The Project
---
The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior 
* Design, train and validate a model that predicts a steering angle from image data
* Use the model to drive the vehicle autonomously around the first track in the simulator. The vehicle should remain on the road for an entire loop around the track.







```sh
python drive.py model.h5 run1
```

The fourth argument, `run1`, is the directory in which to save the images seen by the agent. If the directory already exists, it'll be overwritten.

```sh
ls run1

```

The image file name is a timestamp of when the image was seen. This information is used by `video.py` to create a chronological video of the agent driving.

### `video.py`

```sh
python video.py run1
```


