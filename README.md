# TrafficSignGAN

#### Augmenting existing datasets of traffic signs by using a Generative Adversarial Network to create synthetic images that will increase the accuracy and generalization ability of classification models.

## My Notebook
### [Traffic Sign GAN Google Colab Notebook](https://github.com/kah-ve/TrafficSignGAN/blob/master/TrafficSign-Conv2DGAN.ipynb) 
#### This notebook fulfills the training and image generation aspect of the project. Separate notebook that will compare accuracy rates between models is in the making.

## Introduction
This is an (ongoing) extension of my fall semester senior project on Generative Adversarial Networks (GANs). This time I am exploring a problem in current autonomous vehicles where data is expensive to collect and label, and even with large amounts of it, there still exists the risk of misclassification errors. 

In this project, I attempt to use the generator in the GAN architecture to create synthetic images of already collected and labeled traffic signs. The inspiration for the idea comes from the fact that GANs are capable of generating unique images and understanding the underlying distribution in data, as in the generation of new human faces with [Style GAN](https://arxiv.org/abs/1812.04948), which can be seen at work in this [interactive website](https://thispersondoesnotexist.com/). 

A low cost and effective way to make classification models more robust and generalize better, thereby decreasing likelihood of misclassification errors, may be to train a classifier on the real images alongside the generated ones that a GAN would output. I will explore this in two ways.

## Approach

The first way is to separate the traffic signs into different classes and train a Deep Convolutional GAN (DCGAN) on each one. In this setup you already know the label of the image that the generator will output since one class was used. After training, you can collect a certain number of the generator's outputs and add them to the set the new classifier will train on.

The second way is to use a Conditional GAN (CGAN) that will be fed images with labels as well. In this case you can control the output of the generator by feeding in noise that is labeled. After training, you will again collect a certain number of the generator's outputs and add them to the set the new classifier will train on.

With these outputted images from the GAN, you will train a second classifier on the set of real and generated images, then check its accuracy against the model that was trained on real data.

![Flowchart](https://github.com/kah-ve/TrafficSignGAN/blob/master/project_flowchart.png) 

Hypothesis 1: The GAN will add distortion and noise to outputted images, but the traffic signs will still be clear. This will help the model to generalize better, and even possibly predict signs in bad conditions (weather, blur). 

Hypothesis 2: The GAN will also generate never before seen unique images of the traffic sign dataset. This means that through a low cost software model you are able to increase the accuracy of your classification networks on unseen images as well.

## Results 
### (USING FIRST APPROACH, i.e. training with a DCGAN on one class at a time)

I trained the GAN on the classes I had the most images for as a first step. The top 10 classes (link to data can be found at bottom of readme) are as follows in my dataset.

**Class 28: 446 images**

**Class 54: 324**

**Class 3: 260**

**Class 5: 194**

**Class 55: 162**

**Class 35: 156**

**Class 7: 152**

**Class 30: 150**

**Class 16: 142**

**Class 11: 138**

After training on the DCGAN on the separate classes, I took the trained model and outputted 500 single images generated from random noise inputted into the generator network. Those are not included here, but here are the grouped pictures of the final trained models outputs for a few of the classes (rest in folder finalOutputsPerClass).

### Class 11
![](https://github.com/kah-ve/TrafficSignGAN/blob/master/finalOutputsPerClass/class_11.png)

### Class 16
![](https://github.com/kah-ve/TrafficSignGAN/blob/master/finalOutputsPerClass/class_16.png)

### Class 28
![](https://github.com/kah-ve/TrafficSignGAN/blob/master/finalOutputsPerClass/class_28.png)

### Class 7
![](https://github.com/kah-ve/TrafficSignGAN/blob/master/finalOutputsPerClass/class_7.png)

Currently I have 500 additional images for each class. Next step is to train a model on the real datasets for each class and also the 500 generated ones, then test the model against a classifier only trained on the real dataset.

Those results will be forthcoming momentarily.

## Sources: 

[Chinese Traffic Sign Recognition Database](http://www.nlpr.ia.ac.cn/pal/trafficdata/recognition.html) (Note:  I preprocessed these images to be 32x32 pixels)

[Training a Conditional DC-GAN on CIFAR-10](https://medium.com/@utk.is.here/training-a-conditional-dc-gan-on-cifar-10-fce88395d610) (Used the same network model and training code)
