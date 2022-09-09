# Image-Manager
This piece of code can serve with the categorization of imae based on the faces
# Usage

Just store the ImageManager.py program in the folder where images are.
# Setup help

Create a conda Environment say image and run the program.
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


face_recognition package is hard to install because the package require DLIB which is not availabel by default. So python try to compile is using cmake and other, and you will ultimately fail on this . So easiest is to install conda and create a environment and install face-recogniton there.

Other package reuired is : Shutil
This package is easily available, so it wont case any problem.

Other requirements are mentioned in the "requirement.txt". 
# About
This Image manager classify the images unisupervised way.
It essentiall finds the face in a image and detect the main face in the image and move them to a respective folder.
The folder are assigned anme from 0 to n. 
For the fist face  found it will be moved to the 0th folder and so on respectively.

For those image that do not have any face are moved to other folder.

#improvement-Required
Here i have used a simple face recognition pyhton library "face_recognition", so the preciation and spped of classificationn depends on it.
Anyon can imporve the code by imporving the face detection part. 
Moreove the images those do not posses any face can further classified as notes , screenshots, landscapes.

#**Help-for-imporvement**

Here i detect the main focus of the images by finding the biggest face in the image but here the mistake that may arise is the biggestt face may not be clear enough to compare faces. So the program may mistook two a same person as different based on different photos, altho the best match is considered here for the classification. But the program may compare a inferior image to inferior face data thus leaving the best match , ie the required folder.  So the high qulaty face go to a high qualtiy face while low quality face go to low quality face althouth the face is of same person.

So imoprovemnt on this is required.

#Need-Better-Face-Detection
further iprovement required  is better face detecion the face classification is not good enough here. It classify the faces of same structure into one weather the people are different.

Hint: One may use CNN Models.


"I have classified more than 16K images with the help of this program"
