from tensorflow import keras
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

# Reading an image using OpenCV 
img = cv2.imread('photo.jpg', cv2.IMREAD_GRAYSCALE) 
cv2.imshow('image', img) 

# Reading in the MNIST Data

