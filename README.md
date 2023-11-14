***
<div align="center">  
  <strong>WORK IN PROGRESS</strong>
</div>  
  
  
***
  
# OpenCV-Bootcamp
  
A training to get started with OpenCV 
  
## About OpenCV-bootcamp
This free bootcamp is available on https://opencv.org/.  


### Grading Policy and Certification 
#### Quizzes Breakdown

Out of a total of 14 quizzes, the top 10 will be taken into account for the final evaluation.  
Students will receive one of the two following certificates based on their final course marks:  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/grade60.png" alt="c" width="45%";>  
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/grade90.png" alt="c" width="45%";>  
</div>


#### Certification
I am proud to have achieved the OpenCV Bootcamp Excellence Certification. I found this training to be highly enriching, well-explained, and comprehensive.  
  
Additionally, documenting this project on GitHub has significantly aided my in-depth understanding of each concept, providing a tangible representation of my skills. Moreover, taking the course in English has enhanced my listening, reading, and written expression skills in the language.  
  
Overall, this certification marks a milestone in my professional growth, and the entire experience has been a valuable opportunity for advancing my computer vision skills.  
  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/OpenCV_Bootcamp_Certificate.png" alt="c" width="90%";>
</div>  

#### Course Marks
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/OpenCV_Bootcamp_Course_Marks.png" alt="c" width="90%";>
</div>  

***  

## Introduction
OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library.  
It provides a comprehensive set of tools and functions for tasks such as image and video analysis, object detection, face recognition, feature extraction, and more.  
OpenCV is widely used in various applications, including robotics, computer vision research, and computer vision-based software development.  
It is available under the open-source BSD license, making it accessible to a wide range of developers and researchers.  
  
  
Before this bootcamp, I underwent a brief training to acquire the fundamentals of Python. This is why the structure and complexity of the code increase as the training progresses.  
  
Each chapter contains one or more files, organized by concepts.  
Happy exploring!

***
## Table of Contents
1. [Display Image](#01-display-image)
2. [Basic Image Manipulation](#02-basic-image-manipulation)
3. [Image Annotation](#03-image-annotation)
4. [Image Enhancement](#04-image-enhancement)
5. [Accessing the Camera](#05-accessing-the-camera)
6. [Video Writing](#06-video-writing)
7. [Image Filtering (Edge Detection)](#07-image-filtering-edge-detection)
8. [Image Features and Alignment](#08-image-features-and-alignment)
9. [Panorama](#09-panorama)
10. [HDR - High Dynamic Range Imaging](#10-hdr---high-dynamic-range-imaging)
11. [Object Tracking](#11-object-tracking)
12. [Face Detection](#12-face-detection)
13. [TensorFlow Object Detection](#13-tensorflow-object-detection)
14. [Pose Estimation using OpenPose](#14-pose-estimation-using-openpose)
[Documentation](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main#documentation-2)  
***



  
## 01 Display Image
Welcome to this course that will guide you through your first steps in the field of image processing and computer vision using the OpenCV library.  
In this initial module, we will explore the fundamental basics and lay the foundation for the upcoming concepts.  
Here's an overview of the topics you'll cover in this initial module:
  
* [Reading an Image](): You will learn how to load an image from a file and bring it into your working environment.  
* [Checking Image Attributes](): Understand the essential attributes of an image, such as data type and image shape.  
  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/check_attributes.png" alt="c" width="30%";>
</div>  
  
* [Matrix Representation](): Discover how images are represented as matrices with NumPy, an essential tool for image processing.  
  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/square2_img.png" alt="c" width="25%";>
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/square2_pixel.png" alt="c" width="40%";>
</div>  
  
* [Color Images](): Explore the concept of color images and how color channels can be split and merged.  
  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/coke_img_BGR.jpg" alt="c" width="25%";>
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/coke_img_RGB.jpg" alt="c" width="25%";>
</div>  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/split_merge_color.jpg" alt="c" width="100%";>
</div>  
  
* [Displaying Images](): Learn how to display images in your environment using the Matplotlib library.  

<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/BGR_to_RGB.jpg" alt="c" width="100%";>
</div>  
  
* [Saving Images](): Find out how to save your images after making modifications.  
  
As you progress through this course, you will gain a strong understanding of the fundamentals of image processing and how to use OpenCV for various operations. So, let's get started and begin with the first module.  
  
[display_images_v1](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/00_display_images/display_images_v1) two big files.
First, launch `_init.py`.  
[display_images_v2](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/00_display_images/display_images_v2) using methods in one file.  
  
Please check `lib/` to understand functions.  
  
### Documentation
| OpenCV | Matplotlib | Numpy |
| --- | --- | --- |
| **Image Reading/Writing** | | |
| [`cv2.imreadModes`](https://docs.opencv.org/4.5.1/d8/d6a/group__imgcodecs__flags.html#ga61d9b0126a3e57d9277ac48327799c80) | | |
| [`cv2.imread`](https://docs.opencv.org/4.5.1/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56) | | |
| [`cv2.imwriteFlags`](https://docs.opencv.org/4.5.1/d8/d6a/group__imgcodecs__flags.html#ga292d81be8d76901bff7988d18d2b42ac) | [`plt.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html) | |
| [`cv2.imwrite`](https://docs.opencv.org/4.5.1/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce) | [`plt.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html) | |
| **Image Displaying** | | |
| [`cv2.namedWindow`](https://docs.opencv.org/4.5.1/d7/dfc/group__highgui.html#ga5afdf8410934fd099df85c75b2e0888b) | [`plt.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html) | |
| [`cv2.imshow`](https://docs.opencv.org/4.5.1/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563) | [`plt.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html) | |
| [`cv2.destroyWindow`](https://docs.opencv.org/4.5.1/d7/dfc/group__highgui.html#ga851ccdd6961022d1d5b4c4f255dbab34) | [`plt.set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.set_title.html) | |
| **User Interaction** | | |
| | [`plt.axis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html) | |
| [`cv2.waitKey`](https://docs.opencv.org/4.5.1/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7) | [`plt.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html) | |
| **Color Conversion** | | |
| [`cv2.cvtColor`](https://docs.opencv.org/4.5.1/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab) | | |
| [`cv2.ColorConversionCodes`](https://docs.opencv.org/4.5.1/d8/d01/group__imgproc__color__conversions.html#ga4e0972be5de079fed4e3a10e24ef5ef0) | | |
| [`cv2.COLOR_BGR2RGB`](https://docs.opencv.org/4.5.1/d8/d01/group__imgproc__color__conversions.html#gga4e0972be5de079fed4e3a10e24ef5ef0ad3db9ff253b87d02efe4887b2f5d77ee) | | |
| [`cv2.COLOR_BGR2HSV`](https://docs.opencv.org/4.5.1/d8/d01/group__imgproc__color__conversions.html#gga4e0972be5de079fed4e3a10e24ef5ef0aa4a7f0ecf2e94150699e48c79139ee12) | | |
| **Image Manipulation** | | |
| [`cv2.split`](https://docs.opencv.org/4.5.1/de/d09/group__cudaarithm__core.html#gaf1714e7a9ea0719c29bf378beaf5f99d) | | [`np.shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape) |
| [`cv2.merge`](https://docs.opencv.org/4.5.1/d2/de8/group__core__array.html#ga61f2f2bde4a0a0154b2333ea504fab1d) | | [`np.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html) |  
  







***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/00_display_images)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 02 Basic Image Manipulation
In this course, I learned various methods of image transformations, exploring essential techniques such as:  
  
1. [Accessing and Manipulating Pixels](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/01_basic_image_manipulations/A_pixels_manipulation.py):  
* Understanding how to access individual pixels in an image.  

<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/square_img.png" alt="c" width="25%";>
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/square_pixel.png" alt="c" width="40%";>
</div>

* Manipulating pixel values for various effects and alterations.  

<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/square1_img.png" alt="c" width="25%";>
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/square1_pixel.png" alt="c" width="40%";>
</div>  


2. [Cropping](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/01_basic_image_manipulations/B_cropping_images.py):  
* Understanding the concept of cropping to extract specific regions of an image.  
* Practical applications of cropping for focusing on relevant details.  

3. [Image Resizing](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/01_basic_image_manipulations/C_resizing_images.py):  
* Techniques for resizing images while maintaining aspect ratios.  
* Applications of resizing for different display and processing requirements.  

4. [Flipping](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/01_basic_image_manipulations/D_flipping_images.py):  
* Exploring methods to flip or mirror images horizontally and vertically.  
* Use cases for flipping in image augmentation and processing pipelines.  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/flip_img.png" alt="c" width="100%";>
</div>  

### Documentation
[cv2.flip](https://docs.opencv.org/3.4/d2/de8/group__core__array.html#gaca7be533e3dac7feb70fc60635adf441)  
[cv2.resize](https://docs.opencv.org/3.4/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d)  
[cv2.INTER_AREA](https://docs.opencv.org/3.4/da/d54/group__imgproc__transform.html#gga5bb5a1fea74ea38e1a5445ca803ff121acf959dca2480cc694ca016b81b442ceb) 
[plt.figure](https://matplotlib.org/stable/api/figure_api.html#module-matplotlib.figure)  
[.copy](https://docs.python.org/fr/3/library/copy.html)  


***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/01_basic_image_manipulations)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 03 Image Annotation
In this notebook, I covered how to annotate images using OpenCV.  
I learned how to peform the following annotations to images.  
  
### [Draw lines](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/02_image_annotation/A_drawing_line.py)  

<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/draw_line.jpg" alt="c" width="50%";>
</div>  

### [Draw circles](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/02_image_annotation/B_drawing_circle.py)  

<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/draw_circle.jpg" alt="c" width="50%";>
</div>  

### [Draw rectangles](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/02_image_annotation/C_drawing_rectangle.py)  

<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/draw_rectangle.jpg" alt="c" width="50%";>
</div>  

### [Add text](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/02_image_annotation/C_drawing_rectangle.py)  

<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/add_text.jpg" alt="c" width="50%";>
</div>  
  
  
These are useful when you want to annotate your results for presentations or show a demo of your application.  
Annotations can also be useful during development and debugging.

### Documentation
[cv2.line](https://docs.opencv.org/3.4/d6/d6e/group__imgproc__draw.html#ga7078a9fae8c7e7d13d24dac2520ae4a2)  
[cv2.circle](https://docs.opencv.org/3.4/d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670)  
[cv2.rectangle](https://docs.opencv.org/3.4/d6/d6e/group__imgproc__draw.html#ga07d2f74cadcf8e305e810ce8eed13bc9)  
[cv2.putTexte](https://docs.opencv.org/3.4/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576)  
[cv2.LINE_AA](https://docs.opencv.org/3.4/d0/de1/group__core.html#ggaf076ef45de481ac96e0ab3dc2c29a777a85fdabe5335c9e6656563dfd7c94fb4f)  
[cv2.LINE_8](https://docs.opencv.org/3.4/d0/de1/group__core.html#ggaf076ef45de481ac96e0ab3dc2c29a777a5d32eda7017db273a37f158e5b51442a)  
[cv2.FONT_HERSHEY_PLAIN](https://docs.opencv.org/3.4/d0/de1/group__core.html#gga0f9314ea6e35f99bb23f29567fc16e11a08cf3b0a37729fbb62a3007d499cbd8b) 

***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/02_image_annotation)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***





## 04 Image Enhancement


Image Processing techniques take advantage of mathematical operations to achieve different results.  
Most often we arrive at an enhanced version of the image using some basic operations.  
We will take a look at some of the fundamental operations often used in computer vision pipelines.  



### [Brightness adjustment or Addition](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/03_image_enhancement/A_addition_or_brightness.py)

Brightness adjustment, also known as addition, is a fundamental image processing operation that involves modifying the intensity values of pixels.  
By adding a constant value to each pixel's intensity, we can control the overall brightness of the image.  
The mathematical expression for this operation is: `New Intensity = Original Intensity x Constant`

<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/brightness.jpg" alt="c" width="80%";>
</div>  
  
This technique is widely used in computer vision pipelines to enhance images, making them brighter or darker as needed.  




### [Contrast or Multiplication, handling overflow](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/03_image_enhancement/B_multiplication_or_contrast.py)  

Contrast adjustment, or multiplication, is a vital image processing operation where pixel intensity values are modified to enhance or diminish contrast.  
By multiplying each pixel's intensity by a constant factor, we control the overall contrast of the image.  
The mathematical expression for this operation is: `New Intensity = Original Intensity x Constant`


<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/contrast_overflow.jpg" alt="c" width="80%";>
</div>  

Handling overflow is crucial during this process. Overflow can occur when the calculated intensity exceeds the maximum representable value.  
Managing overflow ensures that the adjusted contrast is applied effectively without causing unintended distortions.

<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/contrast.jpg" alt="c" width="80%";>
</div>  

In summary, contrast adjustment is a fundamental technique in image enhancement, allowing us to control the visibility of details.  
Addressing overflow concerns is integral to achieving accurate and visually pleasing results in computer vision pipelines.



### [Thresholding & Masking](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/03_image_enhancement/C_image_tresholding.py)  

#### **Thresholding**:

Thresholding involves converting an image into a binary format by setting a threshold value. Pixels with intensities above the threshold are set to one value (e.g., white), while those below are set to another value (e.g., black).  
Thresholding is commonly used for image segmentation, where we want to separate objects or regions of interest from the background. It simplifies the image and highlights specific features.  

#### **Masking**:

Masking involves using a binary image (mask) to selectively apply operations to specific regions of another image. Pixels corresponding to the "on" (white) regions of the mask allow the operation, while "off" (black) regions exclude it.  
Masking is versatile and can be used for various purposes, such as filtering, region-of-interest (ROI) selection, or combining images. It enables targeted processing on specific areas of interest within an image.  

#### **Combining Thresholding and Masking**:

**Workflow:** Often, thresholding is used to create a binary mask, where certain areas are set to white based on intensity criteria. This mask is then applied to another image using masking techniques, allowing selective processing on specific regions.  
  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/threshold.jpg" alt="c" width="80%";>
</div>  

#### **Applications**:

**Image Segmentation:** Thresholding helps segment objects based on intensity, while masking allows selective processing within those objects.  
**Object Detection:** By defining intensity thresholds and masks, specific objects or regions can be isolated for further analysis.  
**Noise Reduction:** Masks can be used to filter out unwanted regions, aiding in noise reduction and improving the signal-to-noise ratio.  
  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/threshold_perform.jpg" alt="c" width="80%";>
</div>  

In summary, "Threshold and masking" are powerful techniques in image processing, providing means to segment and selectively process images based on intensity criteria, contributing to various applications in computer vision and image analysis.  



  
### [Bitwise Operations like OR, AND, XOR](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/03_image_enhancement/D_bitwise_operations.py)  

Bitwise operations like OR (|), AND (&), and XOR (^) are fundamental operations used in image processing to manipulate the individual bits of pixel values.  
  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/bitwise_operator.png" alt="c" width="80%";>
</div>  
  
These operations are particularly powerful when working with binary images or masks. Here's a detailed breakdown:  
  
#### [1. Bitwise OR (|)]()

The OR operation combines the bits of two images. If at least one of the corresponding bits is set (1), the result will have that bit set.  
  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/bitwise_figure.png" alt="c" width="80%";>
</div>  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/bitwise_OR.png" alt="c" width="40%";>
</div>  
  
OR operations are commonly used in image blending, combining information from two images, or creating composite images.  

#### [2. Bitwise AND (&)]()

The AND operation combines the bits of two images. The result has a bit set only if the corresponding bits in both input images are set (1).  
  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/bitwise_figure.png" alt="c" width="80%";>
</div>  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/bitwise_AND.png" alt="c" width="40%";>
</div>  
  
AND operations are useful for masking. When combined with a binary mask, only the pixels where both the mask and the image have a white pixel will be set in the result.  

#### [3. Bitwise XOR (^)]()

Definition: The XOR operation combines the bits of two images. If the corresponding bits are different, the result will have that bit set.  
  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/bitwise_figure.png" alt="c" width="80%";>
</div>  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/bitwise_XOR.png" alt="c" width="40%";>
</div>  
  
XOR operations are often used in applications like image differencing, where changes between two images are highlighted.  


### [Applications](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/03_image_enhancement/E_logo_manipulation.py)

**Image Blending:** Bitwise OR can be employed for blending images or combining specific features.  
  
**Masking:** Bitwise AND is valuable for applying masks, selectively affecting certain regions of an image.  
  
**Image Differencing:** Bitwise XOR can highlight differences between two images.  
  
**Note:** Bitwise operations are particularly efficient in terms of computational resources, making them widely used in computer vision and image processing algorithms.  

<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/logo_transformation1.png" alt="c" width="90%";>
</div>  
<div align="center">
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/logo_transformation2.png" alt="c" width="90%";>
<div align="center">
</div>  
  <img src="https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/utils/logo_transformation3.png" alt="c" width="90%";>
</div>  

  

In summary, bitwise operations like OR, AND, and XOR are essential tools for manipulating image data at the bit level, offering a versatile set of operations for various applications in image processing and computer vision.

  

### Documentation
[cv2.add](https://docs.opencv.org/3.4/d2/de8/group__core__array.html#ga10ac1bfb180e2cfda1701d06c24fdbd6)  
[cv2.subtract](https://docs.opencv.org/3.4/d2/de8/group__core__array.html#gaa0f00d98b4b5edeaeb7b8333b2de353b)  
[cv2.multiply](https://docs.opencv.org/3.4/d2/de8/group__core__array.html#ga979d898a58d7f61c53003e162e7ad89f)  
[cv2.threshold](https://docs.opencv.org/3.4/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57)  
[cv2.adaptiveThreshold](https://docs.opencv.org/3.4/d7/d1b/group__imgproc__misc.html#ga72b913f352e4a1b1b397736707afcde3)  
[cv2.bitwise_and](https://docs.opencv.org/3.4/d2/de8/group__core__array.html#ga60b4d04b251ba5eb1392c34425497e14)  
[cv2.bitwise_or](https://docs.opencv.org/3.4/d2/de8/group__core__array.html#gab85523db362a4e26ff0c703793a719b4)  
[cv2.bitwise_xor](https://docs.opencv.org/3.4/d2/de8/group__core__array.html#ga84b2d8188ce506593dcc3f8cd00e8e2c)  
[cv2.THRESH_BINARY](https://docs.opencv.org/3.4/d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a147222a96556ebc1d948b372bcd7ac59)  
[cv2.ADAPTIVE_THRESH_MEAN_C](https://docs.opencv.org/3.4/d7/d1b/group__imgproc__misc.html#ggaa42a3e6ef26247da787bf34030ed772cad0c5199ae8637a6b195062fea4789fa9)  
[np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones)  
[np.clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip)  
[np.uint8](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8)  
[np.float64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64)  
  
***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/03_image_enhancement)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 05 Accessing the Camera
In this short course, I learned how to access to the camera.  
  
I cannot show examples as I do not have a camera. Refer to the [code](https://github.com/cloraronco/OpenCV-Bootcamp/blob/main/04_accessing_the_camera/00_accessing_camera.py) for more information.

If you are using Windows 10 with WSL, you probably won't have access to your camera from the VM. To enable it, follow this [tutorial](https://github.com/PINTO0309/wsl2_linux_kernel_usbcam_enable_conf).


### Documentation
[cv2.VideoCapture](https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html)  
[cv2.namedWindow](https://docs.opencv.org/3.4/d7/dfc/group__highgui.html#ga5afdf8410934fd099df85c75b2e0888b)  
[cv2.WINDOW_NORMAL](https://docs.opencv.org/3.4/d0/d90/group__highgui__window__flags.html#ggabf7d2c5625bc59ac130287f925557ac3a29e45c5af696f73ce5e153601e5ca0f1)  
[.read](https://docs.python.org/3/library/io.html#io.TextIOBase.read)  
[.release](https://docs.python.org/3/library/threading.html#threading.Lock.release)  
[sys.argv](https://docs.python.org/3/library/sys.html)  
  
***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/04_accessing_the_camera)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 06 Video Writing
While building applications, it becomes important to save demo videos of your work as well as many applications themselves might require saving a video clip.  
For example, in a surveiallance application, you might have to save a video clip as soon as you see something unusual happening.  
  
In this course, I describe how to save a video in avi and mp4 formats using openCV.  

### Documentation
[cv2.VideoWriter](https://docs.opencv.org/3.4/dd/d9e/classcv_1_1VideoWriter.html#ad59c61d8881ba2b2da22cff5487465b5)  
[cv2.VideoWriter_fourcc](https://docs.opencv.org/4.x/dd/d9e/classcv_1_1VideoWriter.html#afec93f94dc6c0b3e28f4dd153bc5a7f0)  
[.isOpened](https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a9d2ca36789e7fcfe7a7be3b328038585)  
[.get](https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#aa6480e6972ef4c00d74814ec841a2939)  
[.write](https://docs.opencv.org/3.4/d7/d7c/structCvTypeInfo.html#a55f7489aa2cbcba7d98079014dc8d6ec)  
[subprocess.call](https://docs.python.org/fr/3/library/subprocess.html)  
  
***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/05_video_writing)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 07 Image Filtering (Edge Detection)
In this short course, I learned how to set image filters.  

### Documentation
[cv2.goodFeaturesToTrack](https://docs.opencv.org/3.4/dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541)  
[cv2.CAP_DSHOW](https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gga023786be1ee68a9105bf2e48c700294dab6ac3effa04f41ed5470375c85a23504)  
[np.float32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32)  
[np.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy-reshape)  

***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/06_image_filtering)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 08 Image Features and Alignment


### Documentation
[cv2.ORB_create](https://docs.opencv.org/3.4/db/d95/classcv_1_1ORB.html)  
[cv2.detectAndCompute](https://docs.opencv.org/3.4/d0/d13/classcv_1_1Feature2D.html#a8be0d1c20b08eb867184b8d74c15a677)  
[cv2.drawKeypoints](https://docs.opencv.org/3.4/d4/d5d/group__features2d__draw.html#gab958f8900dd10f14316521c149a60433)  
[cv2.drawMatches](https://docs.opencv.org/3.4/d4/d5d/group__features2d__draw.html#ga7421b3941617d7267e3f2311582f49e1)  
[cv2.DescriptorMatcher_create](https://docs.opencv.org/3.4/db/d39/classcv_1_1DescriptorMatcher.html)  
[cv2.findHomography](https://docs.opencv.org/3.4/d9/d0c/group__calib3d.html#ga4abc2ece9fab9398f2e560d53c8c9780)  
[cv2.warpPerspective](https://docs.opencv.org/3.4/da/d54/group__imgproc__transform.html#gaf73673a7e8e18ec6963e3774e6a94b87) 
[cv2.COLOR_BGR2GRAY](https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html#gga4e0972be5de079fed4e3a10e24ef5ef0a353a4b8db9040165db4dacb5bcefb6ea)  
[cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS](https://docs.opencv.org/3.4/d4/d5d/group__features2d__draw.html#ga7421b3941617d7267e3f2311582f49e1)  
[cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING](https://docs.opencv.org/3.4/db/d39/classcv_1_1DescriptorMatcher.html)  
[cv2.RANSAC](https://docs.opencv.org/3.4/d9/d0c/group__calib3d.html#gga2a608ac7b6bde0c6a51b53b079f27aa4a724159df258a5d7e29410a6a2f4e6c87)  
[np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros)  
[np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)  
[.match](https://www.programiz.com/python-programming/regex)  
[.queryIdx](https://docs.opencv.org/3.4/d4/de0/classcv_1_1DMatch.html)  
[.trainIdx](https://docs.opencv.org/3.4/d4/de0/classcv_1_1DMatch.html)  
  
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

### Documentation
[cv2.Stitcher_create](https://docs.opencv.org/3.4/d2/d8d/classcv_1_1Stitcher.html#acb32106b3b3e7870d4b39082ab58a26e)  
[.append](https://www.programiz.com/python-programming/methods/list/append)  
[.stitch](https://docs.opencv.org/3.4/d2/d8d/classcv_1_1Stitcher.html)
[glob.glob](https://docs.python.org/fr/3/library/glob.html)  
[math.ceil](https://www.w3schools.com/python/ref_math_ceil.asp#:~:text=The%20math.,floor()%20method.)  
[os.sep](https://www.programcreek.com/python/example/113/os.sep)  
  
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
  
### Documentation
[cv2.createCalibrateDebevec](https://docs.opencv.org/3.4/d6/df5/group__photo__hdr.html#ga7fed9707ad5f2cc0e633888867109f90)  
[cv2.createMergeDebevec](https://docs.opencv.org/3.4/d6/df5/group__photo__hdr.html#gaa8eab36bc764abb2a225db7c945f87f9)  
[cv2.createTonemapDrago](https://docs.opencv.org/3.4/d6/df5/group__photo__hdr.html#ga72bf92bb6b8653ee4be650ac01cf50b6)  
[cv2.createTonemapReinhard](https://docs.opencv.org/3.4/d6/df5/group__photo__hdr.html#gadabe7f6bf1fa96ad0fd644df9182c2fb)  
[cv2.createTonemapMantiuk](https://docs.opencv.org/3.4/d6/df5/group__photo__hdr.html#ga3b3f3bf083b7515802f039a6a70f2d21)  
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)  
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html)  
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html)  
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)  
[plt.plot](https://matplotlib.org/stable/users/prev_whats_new/dflt_style_changes.html#plot)  
[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy-arange)  
[np.squeeze](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy-squeeze)  
[.process](https://docs.opencv.org/3.4/d8/d5e/classcv_1_1Tonemap.html#aa705c3b7226f7028a5c117dffab60fe4)   

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
***
  
### [What is Tracking?](https://github.com/cloraronco/OpenCV-Bootcamp#what-is-tracking)  

Tracking, in the context of computer vision, refers to the process of keeping tabs on one or more objects as they traverse through a series of images or video frames. The key challenge in tracking is to maintain the object's identity while compensating for variations in its appearance and position. Effective tracking requires a combination of techniques, models, and algorithms to ensure accurate and robust results.  

### [Tracking in Computer Vision](https://github.com/cloraronco/OpenCV-Bootcamp#tracking-in-computer-vision)  

In computer vision, tracking plays a pivotal role in various real-world applications. These applications include:    

* [Surveillance](https://github.com/cloraronco/OpenCV-Bootcamp#tracking-in-computer-vision): Tracking objects in video feeds from security cameras to detect and monitor activities.  
* [Autonomous Vehicles](https://github.com/cloraronco/OpenCV-Bootcamp#tracking-in-computer-vision): Enabling vehicles to track the movement of other vehicles, pedestrians, and objects on the road to make informed decisions.  
* [Object Recognition](https://github.com/cloraronco/OpenCV-Bootcamp#tracking-in-computer-vision): Tracking objects as they move within a video frame, aiding in their identification.  
* [Gesture Recognition](https://github.com/cloraronco/OpenCV-Bootcamp#tracking-in-computer-vision): Keeping track of hand movements in real time to recognize gestures and interactions.  
* [Augmented Reality](https://github.com/cloraronco/OpenCV-Bootcamp#tracking-in-computer-vision): Tracking markers or objects in the environment to overlay digital information or virtual objects.  
* [Medical Imaging](https://github.com/cloraronco/OpenCV-Bootcamp#tracking-in-computer-vision): Tracking anatomical structures or medical instruments for diagnostics and surgery.  

### [Motion Model and Appearance Model](https://github.com/cloraronco/OpenCV-Bootcamp#motion-model-and-appearance-model)

To successfully track an object, two essential models are utilized:

* [Motion Model](https://github.com/cloraronco/OpenCV-Bootcamp#motion-model-and-appearance-model): The motion model describes how the object of interest is expected to move from one frame to the next. It predicts the object's position and other parameters in the subsequent frame. This model helps maintain tracking accuracy when there's no drastic change in the object's appearance.

* [Appearance Model](https://github.com/cloraronco/OpenCV-Bootcamp#motion-model-and-appearance-model): The appearance model is focused on how the object looks. It encompasses the object's visual features, such as color, texture, and shape. This model helps to handle situations where the object's appearance changes due to factors like lighting conditions, occlusions, or object deformations.

The combination of the motion model and the appearance model allows tracking algorithms to make predictions about an object's position while simultaneously adapting to changes in its visual characteristics. This hybrid approach is essential for robust and reliable object tracking.

### [OpenCV API Tracker Class](https://github.com/cloraronco/OpenCV-Bootcamp#opencv-api-tracker-class)

OpenCV offers a comprehensive set of tracking algorithms through its Tracker Class API. This API simplifies the process of implementing object tracking by providing access to a range of tracking algorithms and methods. These algorithms are optimized for various tracking scenarios and are designed to work with different types of objects, ensuring flexibility and applicability in a wide range of computer vision projects.  
  
In summary, object tracking is a vital component of computer vision that allows for the continuous monitoring and prediction of an object's position across a sequence of images or video frames. It relies on motion and appearance models to accommodate variations in object movement and appearance. OpenCV's Tracker Class API is a valuable resource for developers seeking efficient and accurate object tracking solutions for diverse applications.  
  
### Documentation
  
***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#10_object_tracking)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 12 Face Detection

Face detection in OpenCV is achieved using the face detection API, which provides various algorithms for this task.  

In this course, we will see an implementation of real-time face detection using OpenCV and its Object Detection (DNN) module.  
The code utilizes a face detection model based on a convolutional neural network (Caffe) to perform real-time face detection from a video source. It uses the features of the OpenCV library for video capture, object detection, and displaying results.
Here is a detailed explanation:  


### [Initialization of Camera and Detection Model](https://github.com/cloraronco/OpenCV-Bootcamp#initialization-of-camera-and-detection-model)

The script takes a command-line argument, which is the number of the video source (0 for the default camera).  
A cv2.VideoCapture object is created to capture the video sequence from the specified source.  
A face detection model is loaded using cv2.dnn.readNetFromCaffe.  
The files deploy.prototxt and res10_300x300_ssd_iter_140000_fp16.caffemodel are used to define the architecture of the model and its weights.  

### [Main Loop for Real-Time Detection](https://github.com/cloraronco/OpenCV-Bootcamp#main-loop-for-real-time-detection)

A while loop is used to process images from the real-time video sequence.  
Captured images are transformed (flipped horizontally in this case) and converted into a "blob" (input object for the neural network).  
The model is fed with the blob to obtain detections.  
Detections are iterated through, and if the confidence of the detection is above a threshold (conf_threshold), a rectangle is drawn around the detected face.  
Confidence information is also displayed next to the rectangle.  

### [Displaying Results](https://github.com/cloraronco/OpenCV-Bootcamp#displaying-results)

Results are displayed in an OpenCV window with live camera feed.  
Inference performance (inference time) is also displayed at the bottom of the image.  
Properly Stopping the Camera and Closing the Window:
The video sequence is released (source.release()), and the OpenCV window is destroyed (cv2.destroyWindow(win_name)).  
  
In summary, this script uses OpenCV and a neural network model to detect faces in real-time from a video sequence coming from the camera or another video source.  
  
### Documentation
  

***
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#11_face_detection)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 13 TensorFlow Object Detection


### Documentation
  

***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#12_TensorFlow_object_detection)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***



## 14 Pose Estimation using OpenPose

  

### Documentation
  

***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/#13_pose_estimation_using_OpenPose)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***

## Documentation

_2  
[cv2.flip]()  
[plt.figure]()  
[cv2.resize]()  
[cv2.INTER_AREA]()  

_3  
[cv2.line]()  
[cv2.circle]()  
[cv2.rectangle]()  
[cv2.putTexte]()  
[cv2.LINE_AA]()  
[cv2.LINE_8]()  
[cv2.FONT_HERSHEY_PLAIN]()  

_4  
[cv2.add]()  
[cv2.subtract]()  
[cv2.multiply]()  
[cv2.threshold]()  
[cv2.adaptiveThreshold]()  
[cv2.bitwise_and]()  
[cv2.bitwise_or]()  
[cv2.bitwise_xor]()
[cv2.THRESH_BINARY]()  
[cv2.ADAPTIVE_THRESH_MEAN_C]()  
[np.ones]()  
[np.clip]()  
[np.uint8]()  
[np.float64]()  

_5  
[cv2.VideoCapture]()  
[cv2.namedWindow]()  
[cv2.WINDOW_NORMAL]()  
[.read]()  
[.release]()  
[sys.argv]()  

_6  
[cv2.VideoWriter]()  
[cv2.VideoWriter_fourcc]()  
[.isOpened]()  
[.get]()  
[.write]()  
[subprocess.call]()  

_7  
[cv2.goodFeaturesToTrack]()  
[cv2.CAP_DSHOW]()  
[np.float32]()  
[np.reshape]()  

_8  
[cv2.ORB_create]()  
[cv2.detectAndCompute]()  
[cv2.drawKeypoints]()  
[cv2.drawMatches]()  
[cv2.DescriptorMatcher_create]()  
[cv2.findHomography]()  
[cv2.warpPerspective]() 
[cv2.COLOR_BGR2GRAY]()  
[cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS]()  
[cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING]()  
[cv2.RANSAC]()  
[np.zeros]()  
[np.array]()  
[.match]()  
[.queryIdx]()  
[.trainIdx]()  

_9  
[cv2.Stitcher_create]()  
[.append]()  
[.stitch]()
[glob.glob]()  
[math.ceil]()  
[os.sep]()   

_10  
[cv2.createCalibrateDebevec]()  
[cv2.createMergeDebevec]()  
[cv2.createTonemapDrago]()  
[cv2.createTonemapReinhard]()  
[cv2.createTonemapMantiuk]()  
[plt.xlabel]()  
[plt.ylabel]()  
[plt.xlim]()  
[plt.grid]()  
[plt.plot]()  
[np.arange]()  
[np.squeeze]()  
[.process]()  

_11
[]()  
[]()  

***  
<sub>**[View code](https://github.com/cloraronco/OpenCV-Bootcamp/tree/main/00_display_images)**</sub>  
<sub>**[Table of Contents](#table-of-contents)**</sub>  
<sub>**[Top of page](#opencv-bootcamp)**</sub>
***
