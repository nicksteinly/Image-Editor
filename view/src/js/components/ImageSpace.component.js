import React, {useState}  from 'react';
import {EdgeDetectionController} from '../controller/EdgeDetectionController';
import '../../css/image-space.css';
import hogwartsEmblem from '../../resources/images/hogwarts-emblem.png';

const baseURL = 'http://127.0.0.1:5000/edge_detection';

export const ImageSpaceComponent = () => {
  const edgeDetectionController = new EdgeDetectionController(baseURL);
  const inputImagePath = '../../resources/images/hogwarts-emblem.png';
  const cannyDetection = async () => { 
    const outputImagePath = await edgeDetectionController.cannyDetection({inputImagePath: inputImagePath});
  }

return (
  <div>
    <img src={require(hogwartsEmblem)} className="image-space"/>
    <br/>
    <button onClick={cannyDetection}>Canny Detection</button>
  </div>
)}
