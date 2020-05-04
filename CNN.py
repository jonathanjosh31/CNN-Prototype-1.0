'''
Convolutional Neural Network
                - Jonathan Joseph


Note :Data preproceesing has been done manually as mentioned in the notes.
'''

#Building the CNN

#Importing required keras packages.
from tensorflow.keras.models import Sequential      #Since CNN is a seq of layers we use this 
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense

#Initialisation of the CNN by making a classifier which is a Sequential object
cnn_classifier = Sequential()

#Layer 1 - Convolutional Layer
cnn_classifier.add(Convolution2D(32,3,3,input_shape = (64,64,3),activation = 'relu'))    #Here we added a new method to the classifier object which is of Convolution2d

#Layer 2 - Pooling Layer
'''
Mainly reduces the size of our pooling Map
We use Max Pooling Here.For More Pooling details please refer the pdfs attached.
All those convolution layers size will be reduced by half.
'''

cnn_classifier.add(MaxPooling2D(pool_size = (2,2)))


