import React from 'react'

export class EdgeDetectionController{
  constructor(baseURL){
    this.baseURL = baseURL
  }

  async cannyDetection({inputImagePath}) {
    await fetch(`${this.baseURL}/edge_detection_Canny`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      withCredentials: true,
      body: JSON.stringify({imagePath: inputImagePath}), 
    })
    .then((response) => response.json())
    .then((data) => {
      return data.outputImagePath
    })
    .catch((error) => {
      console.log(`${this.baseURL}/edge_detection_Canny`);
      console.error('Error:', error);
    });
  }
}