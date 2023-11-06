  
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
  
  
Each chapter contains one or more files, organized by concepts.  
Happy exploring!

***
## Table of Contents
1. [Display Image](#01-display-image) :white_check_mark:
2. [Basic Image Manipulation](#02-basic-image-manipulation) :white_check_mark:
3. [Image Annotation](#03-image-annotation) :white_check_mark:
4. [Image Enhancement](#04-image-enhancement) :white_check_mark:
5. [Accessing the Camera](#05-accessing-the-camera) :white_check_mark:
6. [Video Writing](#06-video-writing) :white_check_mark:
7. [Image Filtering (Edge Detection)](#07-image-filtering-edge-detection) :white_check_mark:
8. [Image Features and Alignment](#08-image-features-and-alignment) :white_check_mark:
9. [Panorama](#09-panorama) :white_check_mark:
10. [HDR - High Dynamic Range Imaging](#10-hdr---high-dynamic-range-imaging) :white_check_mark:
11. [Object Tracking](#11-object-tracking) :beginner:        I'm there!
12. [Face Detection](#12-face-detection)
13. [TensorFlow Object Detection](#13-tensorflow-object-detection)
14. [Pose Estimation using OpenPose](#14-pose-estimation-using-openpose)
***



  
## 01 Display Image
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

[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/00_display_images)  
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***



## 02 Basic Image Manipulation
In this course I covered how to perform image transformations including:  
  
* Accessing and manipulating images pixels  
* Image resizing  
* Cropping  
* Flipping

[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/01_basic_image_manipulations)  
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***



## 03 Image Annotation
In this notebook, I covered how to annotate images using OpenCV.  
I learned how to peform the following annotations to images.  
  
* Draw lines  
* Draw circles  
* Draw rectangles  
* Add text
  
These are useful when you want to annotate your results for presentations or show a demo of your application.  
Annotations can also be useful during development and debugging.

[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/02_image_annotation)  
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***



## 04 Image Enhancement
Image Processing techniques take advantage of mathematical operations to achieve different results.  
Most often we arrive at an enhanced version of the image using some basic operations.  
We will take a look at some of the fundamental operations often used in computer vision pipelines.  \
In this course, I covered:  
  
* Arithmetic Operations like addition, multiplication  
* Thresholding & Masking  
* Bitwise Operations like OR, AND, XOR  
  
[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/03_image_enhancement)  
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***



## 05 Accessing the Camera
In this short course, I learned how to access to the camera.  
  
[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/04_accessing_the_camera)  
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***



## 06 Video Writing
While building applications, it becomes important to save demo videos of your work as well as many applications themselves might require saving a video clip.  
For example, in a surveiallance application, you might have to save a video clip as soon as you see something unusual happening.  
  
In this course, I describe how to save a video in avi and mp4 formats using openCV.  
  
[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/05_video_writing) 
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***



## 07 Image Filtering (Edge Detection)
In this short course, I learned how to set image filters.  

[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/06_image_filtering) 
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***



## 08 Image Features and Alignment
[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#07_image_features_and_alignment) 
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***



## 09 Panorama
Steps for Creating Panoramas:  
  
* Find keypoints in all images  
* Find pairwise correspondences  
* Estimate pairwise Homographies  
* Refine Homographies  
* Stitch with Blending  

[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#08_panorama) 
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
***
  I'M CURRENTLY WORKING ON THE FOLLOWING CONTENTS!  
***



## 10 HDR - High Dynamic Range Imaging
Here are the different steps involved in creating an HDR (High Dynamic Range) image with OpenCV:
1. Bracketed Image Capture: Capture multiple photos of the same scene at different exposures (underexposed, properly exposed, and overexposed). These images should cover the dynamic range of the scene.
2. Image Reading: Import these images using OpenCV.
3. Image Alignment: Align the images to correct for variations in movement or rotation between shots. This ensures that scene features match correctly.
4. Camera Response Function Estimation: Calculate the camera's response curves for each image to correct for differences in camera sensitivity.
5. Image Fusion: Merge the properly exposed images using an HDR fusion algorithm to obtain a high dynamic range image.
6. Tone Mapping: The resulting HDR image will have a high dynamic range, which may look unusual on standard displays. Apply a tone mapping operation to perceptually reduce the dynamic range, creating a displayable LDR (Low Dynamic Range) image.
7. Saving the Final Image: Save the resulting LDR image, which can be viewed on standard screens.

These steps will guide you through the process of creating an HDR image from a set of bracketed images.  
OpenCV provides tools to perform these steps, making it easier to create HDR images from real shots.
  
This course has been structured differently.  
Each file includes one or more methods, corresponding to a step in the HDR process.  
To compile the entire course, simply run the command 'python3 _init.py'.
[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#09_HDR) 
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***



## 11 Object Tracking
[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#10_object_tracking) 
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***



## 12 Face Detection
[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#11_face_detection) 
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***



## 13 TensorFlow Object Detection
[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#12_TensorFlow_object_detection) 
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***



## 14 Pose Estimation using OpenPose
[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#13_pose_estimation_using_OpenPose) 
***  
<sub>**[Table of Contents](#table-of-contents)**</sub>
***

