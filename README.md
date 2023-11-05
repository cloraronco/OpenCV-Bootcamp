  
      _________===========//////////    ONGOING TRAINING    \\\\\\\\\\\===========_________  
  
***
  
# OpenCV-Bootcamp
  
A training to get started with OpenCV 
  
## About OpenCV-bootcamp
This free bootcamp is available on https://opencv.org/.  


### Grading Policy and Certification 
#### Quizzes Breakdown

Out of a total of 14 quizzes, the top 10 will be taken into account for the final evaluation.  
Students will receive one of the two following certificates based on their final course marks:  
<div align="left">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/grade60.png" alt="c" width="381" height="318" style="max-width: 100%;">  
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/grade90.png" alt="c" width="381" height="318" style="max-width: 100%;">  
</div>

## Introduction
OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library.  
It provides a comprehensive set of tools and functions for tasks such as image and video analysis, object detection, face recognition, feature extraction, and more.  
OpenCV is widely used in various applications, including robotics, computer vision research, and computer vision-based software development.  
It is available under the open-source BSD license, making it accessible to a wide range of developers and researchers.  


### Installation
```
$ git clone https://github.com/cloraronco/OpenCV-Bootcamp  
```
Each chapter contains one or more files, organized by concepts.  
Happy exploring!

***
## Table of Contents
1. [Display Image](#display-image) :white_check_mark:
2. [Basic Image Manipulation](#basic-image-manipulation) :white_check_mark:
3. [Image Annotation](#image-annotation) :white_check_mark:
4. [Image Enhancement](#image-enhancement) :white_check_mark:
5. [Accessing the Camera](#accessing-the-camera) :white_check_mark:
6. [Video Writing](#video-writing) :white_check_mark:
7. [Image Filtering (Edge Detection)](#image-filtering-edge-detection) :white_check_mark:
8. [Image Features and Alignment](#image-features-and-alignment) :white_check_mark:
9. [Panorama](#panorama) :white_check_mark:
10. [HDR - High Dynamic Range Imaging](#hdr---high-dynamic-range-imaging) :beginner:        I'm there!
11. [Object Tracking](#object-tracking)
12. [Face Detection](#face-detection)
13. [TensorFlow Object Detection](#tensorFlow-object-detection)
14. [Pose Estimation using OpenPose](#pose-estimation-using-openpose)
***
  
## Display Image
This course helped me take my first steps in learning Image Processing and Computer Vision using OpenCV.  
I learned some important lessons using some simple examples.  
In this notebook, I learned the following:  
  
* Reading an image
* Check image attributes like datatype and shape
* Matrix representation of an image in Numpy
* Color Images and splitting/merging image channels
* Displaying images using matplotlib
* Saving images

#### Documentation
`imread`: [Documentation link](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F4.5.1%2Fd4%2Fda8%2Fgroup__imgcodecs.html%23ga288b8b3da0892bd651fce07b3bbd3a56)  
`imreadModes`: [Documentation link](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F4.5.1%2Fd8%2Fd6a%2Fgroup__imgcodecs__flags.html%23ga61d9b0126a3e57d9277ac48327799c80)  
`split`: [Documentation link](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F4.5.1%2Fd2%2Fde8%2Fgroup__core__array.html%23ga0547c7fed86152d7e9d0096029c8518a)  
`cvtColor`: [Documentation link](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F3.4%2Fd8%2Fd01%2Fgroup__imgproc__color__conversions.html%23ga397ae87e1288a81d2363b61574eb8cab)  
`ColorConversionCodes`: [Documentation link](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F4.5.1%2Fd8%2Fd01%2Fgroup__imgproc__color__conversions.html%23ga4e0972be5de079fed4e3a10e24ef5ef0)  
`imwrite`: [Documentation link](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F4.5.1%2Fd4%2Fda8%2Fgroup__imgcodecs.html%23gabbc7ef1aa2edfaa87772f1202d67e0ce)  
`imwriteFlags`: [Documentation link](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F4.5.1%2Fd8%2Fd6a%2Fgroup__imgcodecs__flags.html%23ga292d81be8d76901bff7988d18d2b42ac)  

More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/00_display_images)
***
## Basic Image Manipulation
In this course I covered how to perform image transformations including:  
  
* Accessing and manipulating images pixels  
* Image resizing  
* Cropping  
* Flipping

More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/01_basic_image_manipulations)  
***
## Image Annotation
In this notebook, I covered how to annotate images using OpenCV.  
I learned how to peform the following annotations to images.  
  
* Draw lines  
* Draw circles  
* Draw rectangles  
* Add text
  
These are useful when you want to annotate your results for presentations or show a demo of your application.  
Annotations can also be useful during development and debugging.

More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/02_image_annotation)  
***
## Image Enhancement
Image Processing techniques take advantage of mathematical operations to achieve different results.  
Most often we arrive at an enhanced version of the image using some basic operations.  
We will take a look at some of the fundamental operations often used in computer vision pipelines.  \
In this course, I covered:  
  
* Arithmetic Operations like addition, multiplication  
* Thresholding & Masking  
* Bitwise Operations like OR, AND, XOR  
  
More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/03_image_enhancement)  
***
## Accessing the Camera
In this short course, I learned how to access to the camera.  
  
More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/04_accessing_the_camera)  
  

***
## Video Writing
While building applications, it becomes important to save demo videos of your work as well as many applications themselves might require saving a video clip.  
For example, in a surveiallance application, you might have to save a video clip as soon as you see something unusual happening.  
  
In this course, I describe how to save a video in avi and mp4 formats using openCV.  
  
More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/05_video_writing) 
***
## Image Filtering (Edge Detection)
In this short course, I learned how to set image filters.  

More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/06_image_filtering) 
***
## Image Features and Alignment
More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#07_image_features_and_alignment) 
***
## Panorama
Steps for Creating Panoramas:  
  
* Find keypoints in all images  
* Find pairwise correspondences  
* Estimate pairwise Homographies  
* Refine Homographies  
* Stitch with Blending  

More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#08_panorama) 
  
***
  I'M CURRENTLY WORKING ON THE FOLLOWING CONTENTS!  
***
## HDR - High Dynamic Range Imaging
More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#09_HDR) 
***
## Object Tracking
More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#10_object_tracking) 
***
## Face Detection
More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#11_face_detection) 
***
## TensorFlow Object Detection
More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#12_TensorFlow_object_detection) 
***
## Pose Estimation using OpenPose
More explanations [here](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#13_pose_estimation_using_OpenPose) 
***

