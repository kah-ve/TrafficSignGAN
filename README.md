# TrafficSignGAN

#### Augmenting existing datasets of traffic signs by using a Generative Adversarial Network to create synthetic images that will increase accuracy and generalization ability of classification models.

## My Notebook
### [Traffic Sign GAN Google Colab Notebook](https://github.com/kah-ve/TrafficSignGAN/blob/master/TrafficSign_Conv2DGAN.ipynb) 

## Introduction
This is an (ongoing) extension of my fall semester senior project on Generative Adversarial Networks (GANs). This time I am exploring a problem in current autonomous vehicles where data is expensive to collect and label, and even with large amounts of it, there still exists the risk of misclassification errors. 

In this project, I attempt to use the generator in the GAN architecture to create synthetic images of already collected and labeled traffic signs. The inspiration for the idea comes from the fact that GANs are capable of generating unique images and understanding the underlying distribution in data, as in the generation of new human faces with [Style GAN](https://arxiv.org/abs/1812.04948), which can be seen at work in this [interactive website](https://thispersondoesnotexist.com/). 

A low cost and effective way to make classification models more robust and generalize better, thereby decreasing likelihood of misclassification errors, may be to train a GAN on the original images with the different traffic signs. I will explore this in two ways.

## Approach

The first way is to separate the traffic signs into different classes and train a Deep Convolutional GAN (DCGAN) on each one. In this setup you already know the label of the image that the generator will output since one class was used. After training, you can collect a certain number of the generator's outputs and add them to the set the new classifier will train on.

The second way is to use a Conditional GAN (CGAN) that will be fed images with labels as well. In this case you can control the output of the generator by feeding in noise that is labeled. After training, you will again collect a certain number of the generator's outputs and add them to the set the new classifier will train on.

After generating the new images, you will train the second classifier on the set of real and generated, then check its accuracy against the model that was trained on real data.

![Flowchart](https://github.com/kah-ve/TrafficSignGAN/blob/master/project_flowchart.png) 

Hypothesis 1: The GAN will add distortion and noise to outputted images, but the traffic sign will still be clear. This will help the model to generalize better, and even possibly predict signs even in bad conditions (weather, blur). 

Hypothesis 2: The GAN will also generate never before seen unique images of the traffic sign dataset. This means that through a low cost software model you are able to increase the accuracy of your classification networks on unseen images as well.

## Results

Currently have some images output using a DCGAN on the whole training dataset. This network was trained as a proof of concept, and I have no way of controlling the output currently. 

Some Output:

![Image1](https://github.com/kah-ve/TrafficSignGAN/blob/master/savedImages/364.png) 

![Image2](https://github.com/kah-ve/TrafficSignGAN/blob/master/savedImages/409.png) 

![Image3](https://github.com/kah-ve/TrafficSignGAN/blob/master/savedImages/666.png)

Further results soon.

## Sources: 

[Chinese Traffic Sign Recognition Database](http://www.nlpr.ia.ac.cn/pal/trafficdata/recognition.html) (Note:  I preprocessed these images to be 32x32 pixels)

[Training a Conditional DC-GAN on CIFAR-10](https://medium.com/@utk.is.here/training-a-conditional-dc-gan-on-cifar-10-fce88395d610)
