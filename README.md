# CNN-Prototype-1.0
Building a convolutional neural network to classify the given images by preserving their spatial structure 


Note:Actually deep learning is used in many medical fields.

Here we preserve the spatial structure of the images therefore wwe will be able to classify the images.

This Repo is based on a very simple IMAGE CLASSIFICATION
 
In this example we took the case of  cats and dogs.But  if we want to classify any other images,we just need to give the  
CNN,the images which it needs to train and then we can test it to predict the results.

Here we will be doing some image preprocessing to be able to input the images in the neural network.

Since we require all the dependent as well as independent variables,these are images,hence they do not have
a particular structure like rows and columns.
There are many ways to make a particular structure for the program to identify training and test set,dependent and 
independent variables.

There are many ways and one way is to set the images in apporpriate folders and rennaming those images correctly.
This is done using the keras library.

Now first we have a dataset folder in the working directory and in that the images are seperated into 
two folders which are the test set and the training set.And in tht we will have two folders,one for the 
cat and other for the dogs.

Here we have 10000 images of dogs and cats which are divided into
Training - 8000
Test - 2000

Since there is no type of categorical variable here we don't do any categorical encoding..

Hence the data preprocessing part which we used to do are done manually here.


Step - 1:

Importing required keras packages.
1)Sequential : To initialise our neural network either a sequence of layers or as a seq of graphs
2)Convolution2D : 
3)
4)
5)


Project Status: Ongoing
