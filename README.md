# Image-Manager
This piece of code can serve with the categorization of image based on the faces.
# Usage

Just store the ImageManager.py program in the folder where images are.
# Setup help

Create a conda environment say image and run the program.
Follow the following code:

#**To setup**
conda create -name image
conda activate image
conda install face_recognition
conda install shutil
pip install windows-curses
conda deactivate

#**To run**
conda activate image
python ImageManager.py
conda deactivate


face_recognition package is hard to install because the package require DLIB which is not available by default. So python try to compile is using cmake and other, and you will ultimately fail on this . So easiest is to install conda and create a environment and install face-recogniton there.

Other package reuired is : Shutil
This package is easily available, so it wont case any problem.

# About
This Image manager classify the images unsupervised way.
It essentially finds the face in a image and detect the main face in the image and move them to a respective folder.
The folder are assigned name from 0 to n. 
For the fist face  found it will be moved to the 0th folder and so on respectively.

For those image that do not have any face are moved to other folder.

#Improvement-Required
Here i have used a simple face recognition pyhton library "face_recognition", so the preciation and spped of classificationn depends on it.
Anyon can improve the code by improving the face detection part. 
Moreover the images those do not posses any face can be further classified as notes , screenshots, landscapes.

#**Help-for-imporvement**

Here I detect the main focus of the images by finding the biggest face in the image but here the mistake that may arise is that the biggest face may not be clear enough to compare faces. So the program may mistook two a same person as different based on different photos, although the best match is considered here for the classification. But the program may compare a inferior image to inferior face data thus leaving the best match , ie the required folder.  So the high quality face goes to a high quality face while low quality face go to low quality face althouth the face is of same person.

So imoprovemnt on this is required.

#Need-Better-Face-Detection
Further iprovement is required, the face detection is not good enough here. It classify the faces of same structure into one weather the people are different.

Hint: One may use CNN Models.


"I have classified more than 16K images with the help of this program"
