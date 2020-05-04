# CNN-Prototype-1.0
<h3>Building a convolutional neural network to classify the given images by preserving their spatial structure</h3>


Note:Actually deep learning is used in many medical fields.

Here we preserve the spatial structure of the images therefore wwe will be able to classify the images.

<h4>Summary:</h4>
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


<h2>Step - 1:</h2>

Importing required keras packages.
1)<h5>Sequential :</h5> To initialise our neural network either a sequence of layers or as a seq of graphs
2)<h5>Convolution2D :</h5> Used to make the convolution process,I.E adding the convolutional layers.Images are 2d,but some videos  can be 3D.Hence to deal with the images we use this package.
3)<h5>MaxPooling2D :</h5> Used to make the pooling process.here we use max pooling.Hence this will add our pooling layers.
4)<h5>Flatten :</h5> USed to flatten the pooling layers,hence giving as the input layers for the ANN which is going to be attached.
5)<h5>Dense :</h5> To add fully connected layers in the ANN.

<h2>Step 2 :</h2>

Initialising the CNN which is ofcourse creating a classifier by creating a Sequential Object.

<h2>Step 3 :</h2>

Making the convolution process.

<h5>Syntax:</h5>
classifier.add(Conv2D(filters, input_shape(3,256,256), activation=None))

<h6>filters</h6> - no of filters + (dimensionality(no of rows and col) of each filter). Filters are nothing but the no of feature detectors we are gonna add to our CNN.ANd in the CNN, No of feature maps = No of feature detectors.
Commonly the no of feature detectors are given as 32 iif your working on your cpu.If your working on your GPU then you can add more feature detectors 

<h6>input_shape</h6> = example input_shape(3,256,256) measn we are giving 3 channels which are RGB and images of size 256x256.But if you are on your CPU you can give 64x64.
Also if you are using tensorflow backend it should be like input_shape(256,256,3)
But if you are using theano backend it should be like input_shape(3,256,256) . I.E order channges in each backend.

and <h6>activation</h6> is used here to apply rectifier function on this so that we give non-linearity to the image so that the image is preserved.

<h2>Step 4 : </h2>

Making the Pooling process.
This pooling is mainly done to mainly reduce the no of nodes to be given in the ANN,
so that the time complexity and as well as the computation time is reduced without losing the performance  

<h5>Syntax:</h5>
classifier.add(MaxPooling2D(pool_size))

<h6>pool_size</h6> - Size of the pooling Map which is going to be formed from the convolutional layers.Recommended size will be 2x2 since it is small as well the main info will still be preserved in each of the pooling layer.


<h3>Project Status:<h3> Ongoing
