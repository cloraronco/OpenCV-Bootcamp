  
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
11. [Object Tracking](#11-object-tracking) :white_check_mark:
12. [Face Detection](#12-face-detection) :beginner:        I'm there!
13. [TensorFlow Object Detection](#13-tensorflow-object-detection)
14. [Pose Estimation using OpenPose](#14-pose-estimation-using-openpose)
***



  
## 01 Display Image
Welcome to this course that will guide you through your first steps in the field of image processing and computer vision using the OpenCV library.  
In this initial module, we will explore the fundamental basics and lay the foundation for the upcoming concepts.  
Here's an overview of the topics you'll cover in this initial module:
  
* [Reading an Image](): You will learn how to load an image from a file and bring it into your working environment.  
* [Checking Image Attributes](): Understand the essential attributes of an image, such as data type and image shape.  
* [Matrix Representation](): Discover how images are represented as matrices with NumPy, an essential tool for image processing.  
* [Color Images](): Explore the concept of color images and how color channels can be split and merged.  
* [Displaying Images](): Learn how to display images in your environment using the Matplotlib library.  
* [Saving Images](): Find out how to save your images after making modifications.  
  
As you progress through this course, you will gain a strong understanding of the fundamentals of image processing and how to use OpenCV for various operations. So, let's get started and begin with the first module.  
[display_images_v1](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/00_display_images/display_images_v1) two big files.  
[display_images_v2](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/00_display_images/display_images_v2) using methods in one file.  
Please check `lib/` to understand functions. 

#### Documentation
[`cv2.imread`](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F4.5.1%2Fd4%2Fda8%2Fgroup__imgcodecs.html%23ga288b8b3da0892bd651fce07b3bbd3a56)  
[`cv2.imreadModes`](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F4.5.1%2Fd8%2Fd6a%2Fgroup__imgcodecs__flags.html%23ga61d9b0126a3e57d9277ac48327799c80)  
[`cv2.split`](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F4.5.1%2Fd2%2Fde8%2Fgroup__core__array.html%23ga0547c7fed86152d7e9d0096029c8518a)  
[`cv2.cvtColor`](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F3.4%2Fd8%2Fd01%2Fgroup__imgproc__color__conversions.html%23ga397ae87e1288a81d2363b61574eb8cab)  
[`cv2.ColorConversionCodes`](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F4.5.1%2Fd8%2Fd01%2Fgroup__imgproc__color__conversions.html%23ga4e0972be5de079fed4e3a10e24ef5ef0)  
[`cv2.imwrite`](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F4.5.1%2Fd4%2Fda8%2Fgroup__imgcodecs.html%23gabbc7ef1aa2edfaa87772f1202d67e0ce)  
[`cv2.imwriteFlags`](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.opencv.org%2F4.5.1%2Fd8%2Fd6a%2Fgroup__imgcodecs__flags.html%23ga292d81be8d76901bff7988d18d2b42ac)  

***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/00_display_images)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 02 Basic Image Manipulation
In this course I covered how to perform image transformations including:  
  
* Accessing and manipulating images pixels  
* Image resizing  
* Cropping  
* Flipping

***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/01_basic_image_manipulations)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
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

***  
<sub>**(https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/02_image_annotation)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 04 Image Enhancement
Image Processing techniques take advantage of mathematical operations to achieve different results.  
Most often we arrive at an enhanced version of the image using some basic operations.  
We will take a look at some of the fundamental operations often used in computer vision pipelines.  \
In this course, I covered:  
  
* Arithmetic Operations like addition, multiplication  
* Thresholding & Masking  
* Bitwise Operations like OR, AND, XOR  
  
***  
<sub>**(https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/03_image_enhancement)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 05 Accessing the Camera
In this short course, I learned how to access to the camera.  
  
***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/04_accessing_the_camera)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 06 Video Writing
While building applications, it becomes important to save demo videos of your work as well as many applications themselves might require saving a video clip.  
For example, in a surveiallance application, you might have to save a video clip as soon as you see something unusual happening.  
  
In this course, I describe how to save a video in avi and mp4 formats using openCV.  
  
***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/05_video_writing)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 07 Image Filtering (Edge Detection)
In this short course, I learned how to set image filters.  

***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/06_image_filtering)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 08 Image Features and Alignment
***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#07_image_features_and_alignment)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 09 Panorama
Steps for Creating Panoramas:  
  
* Find keypoints in all images  
* Find pairwise correspondences  
* Estimate pairwise Homographies  
* Refine Homographies  
* Stitch with Blending  

***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#08_panorama)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***


## 10 HDR - High Dynamic Range Imaging
This course has been structured differently.  
Each file includes one or more methods, corresponding to a step in the HDR process.  
To compile the entire course, simply run the command `python3 _init.py`.  
  
Here are the different steps involved in creating an HDR (High Dynamic Range) image with OpenCV:
1. [Bracketed Image Capture](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/A_capture_multi_explosures.py): Capture multiple photos of the same scene at different exposures (underexposed, properly exposed, and overexposed). These images should cover the dynamic range of the scene.
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/import/img_0.25.jpg" alt="c" width="200" height="140" style="max-width: 100%;">  
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/import/img_0.033.jpg" alt="c" width="200" height="140" style="max-width: 100%;">  
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/import/img_2.5.jpg" alt="c" width="200" height="140" style="max-width: 100%;">  
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/import/img_15.jpg" alt="c" width="200" height="140" style="max-width: 100%;">  
</div>  

2. [Image Reading](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/A_capture_multi_explosures.py): Import these images using OpenCV.
3. [Image Alignment](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/B_align_images.py): Align the images to correct for variations in movement or rotation between shots. This ensures that scene features match correctly.
4. [Camera Response Function Estimation](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/C_estimate_camera_response_function.py): Calculate the camera's response curves for each image to correct for differences in camera sensitivity.
<p align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/estimate_camera_response_function.png" alt="c" width="80%">
</p>

5. [Image Fusion](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/D_merge_exposure_into_HDR_image.py): Merge the properly exposed images using an HDR fusion algorithm to obtain a high dynamic range image.
6. [Tone Mapping](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/E_tonnemapping.py): The resulting HDR image will have a high dynamic range, which may look unusual on standard displays. Apply a tone mapping operation to perceptually reduce the dynamic range, creating a displayable LDR (Low Dynamic Range) image.  The best tonemapping method depends on the type of scene you're dealing with and your artistic preferences. Experiment with these methods to find the one that best suits your HDR images. Reinhard is commonly used for its simplicity, while Mantiuk is suitable for high-contrast scenes, Drago for low-contrast scenes.
<p align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/ldr-Drago.jpg" alt="c" width="45%">
  <br>
  <strong>Tonnemapping with Drago</strong>
</p>

<p align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/ldr-Mantiuk.jpg" alt="c" width="45%">
  <br>
  <strong>Tonnemapping with Mantiuk</strong>
</p>

<p align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/ldr-Reinhard.jpg" alt="c" width="45%">
  <br>
  <strong>Tonnemapping with Reinhard</strong>
</p>

7. [Saving the Final Image](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/09_HDR/E_tonnemapping.py): Save the resulting LDR image, which can be viewed on standard screens.


These steps will guide you through the process of creating an HDR image from a set of bracketed images.  
OpenCV provides tools to perform these steps, making it easier to create HDR images from real shots.
  
***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/09_HDR)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



***
  I'M CURRENTLY WORKING ON THE FOLLOWING CONTENTS!  
***
## 11 Object Tracking

Object tracking is a fundamental task in the field of computer vision that involves following the movement or position of objects in a sequence of images or frames, typically extracted from videos. It is a critical component in various applications such as surveillance, autonomous navigation, augmented reality, and more.  
The primary goal of object tracking is to continuously monitor and predict the location of a specific object as it moves through the frames, even when the object undergoes changes in scale, rotation, or lighting conditions.  

<sub>**[What is Tracking?](https://github.com/cloraronco/OpenCV-Bootcamp#what-is-tracking)**</sub>  
<sub>**[Tracking in Computer Vision](https://github.com/cloraronco/OpenCV-Bootcamp#tracking-in-computer-vision)**</sub>  
<sub>**[Motion Model and Appearance Model](https://github.com/cloraronco/OpenCV-Bootcamp#motion-model-and-appearance-model)**</sub>  
<sub>**[OpenCV API Tracker Class](https://github.com/cloraronco/OpenCV-Bootcamp#opencv-api-tracker-class)**</sub>  
---
  
### [What is Tracking?](https://github.com/cloraronco/OpenCV-Bootcamp#what-is-tracking)  

Tracking, in the context of computer vision, refers to the process of keeping tabs on one or more objects as they traverse through a series of images or video frames. The key challenge in tracking is to maintain the object's identity while compensating for variations in its appearance and position. Effective tracking requires a combination of techniques, models, and algorithms to ensure accurate and robust results.  

### [Tracking in Computer Vision](https://github.com/cloraronco/OpenCV-Bootcamp#tracking-in-computer-vision)  

In computer vision, tracking plays a pivotal role in various real-world applications. These applications include:    

* Surveillance: Tracking objects in video feeds from security cameras to detect and monitor activities.  
* Autonomous Vehicles: Enabling vehicles to track the movement of other vehicles, pedestrians, and objects on the road to make informed decisions.  
* Object Recognition: Tracking objects as they move within a video frame, aiding in their identification.  
* Gesture Recognition: Keeping track of hand movements in real time to recognize gestures and interactions.  
* Augmented Reality: Tracking markers or objects in the environment to overlay digital information or virtual objects.  
* Medical Imaging: Tracking anatomical structures or medical instruments for diagnostics and surgery.  

### [Motion Model and Appearance Model](https://github.com/cloraronco/OpenCV-Bootcamp#motion-model-and-appearance-model)

To successfully track an object, two essential models are utilized:

* Motion Model: The motion model describes how the object of interest is expected to move from one frame to the next. It predicts the object's position and other parameters in the subsequent frame. This model helps maintain tracking accuracy when there's no drastic change in the object's appearance.

* Appearance Model: The appearance model is focused on how the object looks. It encompasses the object's visual features, such as color, texture, and shape. This model helps to handle situations where the object's appearance changes due to factors like lighting conditions, occlusions, or object deformations.

The combination of the motion model and the appearance model allows tracking algorithms to make predictions about an object's position while simultaneously adapting to changes in its visual characteristics. This hybrid approach is essential for robust and reliable object tracking.

### [OpenCV API Tracker Class](https://github.com/cloraronco/OpenCV-Bootcamp#opencv-api-tracker-class)

OpenCV offers a comprehensive set of tracking algorithms through its Tracker Class API. This API simplifies the process of implementing object tracking by providing access to a range of tracking algorithms and methods. These algorithms are optimized for various tracking scenarios and are designed to work with different types of objects, ensuring flexibility and applicability in a wide range of computer vision projects.  
  
In summary, object tracking is a vital component of computer vision that allows for the continuous monitoring and prediction of an object's position across a sequence of images or video frames. It relies on motion and appearance models to accommodate variations in object movement and appearance. OpenCV's Tracker Class API is a valuable resource for developers seeking efficient and accurate object tracking solutions for diverse applications.
***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#10_object_tracking)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 12 Face Detection
***  
This code is an implementation of real-time face detection using OpenCV and its Object Detection (DNN) module. Here is a detailed explanation:


Initialization of Camera and Detection Model:

The script takes a command-line argument, which is the number of the video source (0 for the default camera).
A cv2.VideoCapture object is created to capture the video sequence from the specified source.
A face detection model is loaded using cv2.dnn.readNetFromCaffe. The files deploy.prototxt and res10_300x300_ssd_iter_140000_fp16.caffemodel are used to define the architecture of the model and its weights.
Main Loop for Real-Time Detection:

A while loop is used to process images from the real-time video sequence.
Captured images are transformed (flipped horizontally in this case) and converted into a "blob" (input object for the neural network).
The model is fed with the blob to obtain detections.
Detections are iterated through, and if the confidence of the detection is above a threshold (conf_threshold), a rectangle is drawn around the detected face.
Confidence information is also displayed next to the rectangle.
Displaying Results:

Results are displayed in an OpenCV window with live camera feed.
Inference performance (inference time) is also displayed at the bottom of the image.
Properly Stopping the Camera and Closing the Window:

The video sequence is released (source.release()), and the OpenCV window is destroyed (cv2.destroyWindow(win_name)).
In summary, this script uses OpenCV and a neural network model to detect faces in real-time from a video sequence coming from the camera or another video source.
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#11_face_detection)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 13 TensorFlow Object Detection
***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#12_TensorFlow_object_detection)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 14 Pose Estimation using OpenPose
***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#13_pose_estimation_using_OpenPose)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***

