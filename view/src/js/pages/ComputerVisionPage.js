import React from 'react';
import { HeaderComponent } from '../components/Header.component';
import { NavLink } from 'react-router-dom';

export const ComputerVisionPage = () => {
  const BASE_URL = "/computer-vision";
  const pageContent = {
    margin: "0 10% 0 10%",
  }

  return (
      <>
        <HeaderComponent header={"Computer Vision"} />
        <div style={pageContent}>
        <p>
          <strong>1. Image Processing:</strong>
          <ul>
            <li>Filtering and Enhancement: Applying filters to images to remove noise, enhance features, and improve quality.</li>
            <li>Histogram Equalization: Adjusting the intensity distribution to enhance contrast and details.</li>
            <li>Morphological Operations: Operations like dilation and erosion to manipulate the shape of objects in an image.</li>
            <li>Image Pyramids: Creating multi-scale representations of images for various purposes.</li>
          </ul>
        </p>

        <p>
          <strong>2. Feature Extraction:</strong>
          <ul>
            <li>Edge Detection: Detecting abrupt changes in intensity, often indicating object boundaries.</li>
            <li>Corner Detection: Identifying corner points in images that are distinct and informative.</li>
            <li>Blob Detection: Identifying regions with similar intensity characteristics.</li>
            <li>Feature Descriptors: Representing image patches using compact descriptors.</li>
          </ul>
        </p>

        <p>
          <strong>3. Image Segmentation:</strong>
          <ul>
            <li>Clustering: Grouping similar pixels or regions based on various criteria.</li>
            <li>Thresholding: Dividing an image into regions based on intensity values.</li>
            <li>Watershed Segmentation: Treating intensity gradients as a topographic surface to separate objects.</li>
          </ul>
        </p>

        <p>
          <strong>4. Object Detection:</strong>
          <ul>
            <li><NavLink to={`${BASE_URL}/template-matching`}>Template Matching:</NavLink>Finding instances of a template within an image.</li>
            <li>Haar Cascade Detection: Using a trained classifier to detect objects using features like edges and corners.</li>
            <li>Histogram of Oriented Gradients (HOG): Extracting and analyzing gradients to detect objects.</li>
          </ul>
        </p>

        <p>
          <strong>5. Object Recognition:</strong>
          <ul>
            <li>Feature Matching: Matching features between images to recognize objects.</li>
            <li>Deep Learning: Using convolutional neural networks (CNNs) to classify and recognize objects.</li>
            <li>Image Retrieval: Finding similar images based on content or features.</li>
          </ul>
        </p>

        <p>
          <strong>6. Motion Analysis:</strong>
          <ul>
            <li>Optical Flow: Estimating the motion of objects between consecutive frames.</li>
            <li>Object Tracking: Following objects' trajectories across frames.</li>
            <li>Activity Recognition: Identifying and understanding human activities in videos.</li>
          </ul>
        </p>

        <p>
          <strong>7. Camera Calibration:</strong>
          <ul>
            <li>Intrinsic Parameters: Determining camera-specific parameters like focal length and principal point.</li>
            <li>Extrinsic Parameters: Calculating the position and orientation of the camera in the world.</li>
          </ul>
        </p>

        <p>
          <strong>8. 3D Reconstruction:</strong>
          <ul>
            <li>Stereo Vision: Estimating depth using multiple cameras or images.</li>
            <li>Structure from Motion (SfM): Reconstructing 3D scenes from 2D image sequences.</li>
            <li>LiDAR and Depth Sensors: Using depth information for accurate 3D reconstruction.</li>
          </ul>
        </p>

        <p>
          <strong>9. Image Stitching and Panorama:</strong>
          <ul>
            <li>Combining multiple images to create a seamless panorama.</li>
            <li>Homography Estimation: Finding the transformation between two overlapping images.</li>
          </ul>
        </p>

        <p>
          <strong>10. Image Generation and Synthesis:</strong>
          <ul>
            <li>Generative Adversarial Networks (GANs): Creating new images based on learned patterns.</li>
            <li>Style Transfer: Applying the artistic style of one image to another.</li>
          </ul>
        </p>
        </div>
      </>
  );
}