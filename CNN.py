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


