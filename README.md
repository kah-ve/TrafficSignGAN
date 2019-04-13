# TrafficSignGAN

#### Augmenting existing datasets of traffic signs by using a Generative Adversarial Network to create synthetic images that will increase the accuracy and generalization ability of classification models.

## My Notebooks (Using Google Drive and Google Colab)
### [Traffic Sign GAN Notebook](https://github.com/kah-ve/TrafficSignGAN/blob/master/TrafficSign-Conv2DGAN.ipynb) 
#### This notebook fulfills the training and image generation aspect of the project. Separate notebook that will compare accuracy rates between models is in the making.

### [CNN Model Classifier Notebook](https://github.com/kah-ve/TrafficSignGAN/blob/master/TrafficSign_CNN.ipynb) 
#### This notebook is used to train CNN models (or others if you'd like) on the real images and the real + generated images, then test them to see the difference in prediction accuracy.

## Introduction
This is an (ongoing) extension of my fall semester senior project on Generative Adversarial Networks (GANs). This time I am exploring a problem in current autonomous vehicles where data is expensive to collect and label, and even with large amounts of it, there still exists the risk of misclassification errors. 

In this project, I attempt to use the generator in the GAN architecture to create synthetic images of already collected and labeled traffic signs. The inspiration for the idea comes from the fact that GANs are capable of generating unique images and understanding the underlying distribution in data, as in the generation of new human faces with [Style GAN](https://arxiv.org/abs/1812.04948), which can be seen at work in this [interactive website](https://thispersondoesnotexist.com/). 

A low cost and effective way to make classification models more robust and generalize better, thereby decreasing likelihood of misclassification errors, may be to train a classifier on the real images alongside the generated ones that a GAN would output. I will explore this in two ways.

## Approach

The first way is to separate the traffic signs into different classes and train a Deep Convolutional GAN (DCGAN) on each one. In this setup you already know the label of the image that the generator will output since one class was used. After training, you can collect a certain number of the generator's outputs and add them to the set the new classifier will train on.

The second way is to use a Conditional GAN (CGAN) that will be fed images with labels as well. In this case you can control the output of the generator by feeding in noise that is labeled. After training, you will again collect a certain number of the generator's outputs and add them to the set the new classifier will train on.

With these outputted images from the GAN, you will train a second classifier on the set of real and generated images, then check its accuracy against the model that was trained on real data.

![Flowchart](https://github.com/kah-ve/TrafficSignGAN/blob/master/miscImages/project_flowchart.png) 

Hypothesis 1: The GAN will add distortion and noise to outputted images, but the traffic signs will still be clear. This will help the model to generalize better, and even possibly predict signs in bad conditions (weather, blur). 

Hypothesis 2: The GAN will also generate never before seen unique images of the traffic sign dataset. This means that through a low cost software model you are able to increase the accuracy of your classification networks on unseen images as well.

## Results 
### (USING FIRST APPROACH, i.e. training with a DCGAN on one class at a time)

I trained the GAN on the classes I had the most images for as a first step. The top 10 classes (link to data can be found at bottom of this page) are as follows in my dataset.

**Class 28: 446 images**

**Class 54: 324 images**

**Class 3: 260 images**

**Class 5: 194 images**

**Class 55: 162 images**

**Class 35: 156 images**

**Class 7: 152 images**

**Class 30: 150 images**

**Class 16: 142 images**

**Class 11: 138 images**

After training the DCGAN on the separate classes, I took the trained model and outputted 500 single images each. These were generated from random noise inputted into the generator network. They are not included here, but I have included the final trained models' outputs for a few of the classes (rest in folder finalOutputsPerClass).

### Class 11
![](https://github.com/kah-ve/TrafficSignGAN/blob/master/finalOutputsPerClass/class_11.png)

### Class 16
![](https://github.com/kah-ve/TrafficSignGAN/blob/master/finalOutputsPerClass/class_16.png)

### Class 54
![](https://github.com/kah-ve/TrafficSignGAN/blob/master/finalOutputsPerClass/class_54.png)

### Class 7
![](https://github.com/kah-ve/TrafficSignGAN/blob/master/finalOutputsPerClass/class_7.png)

## Results
So we have 4500 Generated Images and 2124 real images. We are testing on 772 images. To do this I used a few different CNN models and got these results:

![](https://github.com/kah-ve/TrafficSignGAN/blob/master/miscImages/ModelResults.PNG)

These are the accuracies of the different models averaged over 10 runs. We see that the generated images are helping the classifier make better predictions. The difference may not be huge, but it is consistent. Furthermore, the testing that was used has images that are all processed and clean. A sample of the few images: 

![](https://github.com/kah-ve/TrafficSignGAN/blob/master/miscImages/SampleTestImages.PNG)

Since these images are already clear, it makes sense that a classifier trained only on the real images is good enough to predict these well. We don't actually need the ability to generalize better, which is what the GAN images supplemented model would help with. 

Lastly, we should note that despite the distortions and warping in the generated images, they don't hurt the classifier from making good predictions. In fact, we have 4500 generated images vs 2124 real images, so the generated images are drowning the real ones in the model. If the generated images were bad, they would've ruined the model. We don't see this happening, and actually see a little of the opposite.

### Disclaimer

I also tried training random CNN models on the two different datasets. I did this by just adding or removing layers, or finding a model used for black and white image classification, but the results on those were volatile, so I stuck with more recognizable models. It is to be ntoed, however, that you can't just run any model on the generated + real images and hope to get better results.

Currently I have 450 additional images for each class. Next step is to train a model on the real datasets for each class and also the 500 generated ones, then test the model against a classifier only trained on the real dataset.

Those results will be available soon.

## Sources: 

[Chinese Traffic Sign Recognition Database](http://www.nlpr.ia.ac.cn/pal/trafficdata/recognition.html) (Note:  I preprocessed these images to be 32x32 pixels)

[Training a Conditional DC-GAN on CIFAR-10](https://medium.com/@utk.is.here/training-a-conditional-dc-gan-on-cifar-10-fce88395d610) (Used the same network model and training code)
