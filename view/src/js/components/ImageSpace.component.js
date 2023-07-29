import React, {useState}  from 'react';
import {EdgeDetectionController} from '../controller/EdgeDetectionController';
import {BackgroundRemovalController} from '../controller/BackgroundRemovalController';
import { RecolorationController } from '../controller/RecolorationController';
import '../../css/image-space.css';

const edgeDetectionBaseURL = 'http://127.0.0.1:5000/edge_detection';
const backgroundRemovalBaseURL = 'http://127.0.0.1:5000/background_removal';
const recolorationBaseURL = 'http://127.0.0.1:5000/recoloration';

export const ImageSpaceComponent = () => {
  const edgeDetectionController = new EdgeDetectionController(edgeDetectionBaseURL);
  const backgroundRemovalController = new BackgroundRemovalController(backgroundRemovalBaseURL);
  const recolorationController = new RecolorationController(recolorationBaseURL);
  const [imagePath, setImagePath] = useState('');
  const initialEmblemPath = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/firetruck.jpeg';
  const edgeDetectionFunctions = async () => { 
    const outerOutlineDetection = await edgeDetectionController.outerOutlineDetection({inputImagePath: initialEmblemPath});
    const cannyEdgePath = await edgeDetectionController.cannyDetection({inputImagePath: initialEmblemPath});
    const thickEdgesPath = await edgeDetectionController.thickenEdges({inputImagePath: cannyEdgePath, kernelSize: 5, iterations: 1});
    const recoloration = await recolorationController.recolor_white_pixels({inputImagePath: thickEdgesPath, color: '0F52BA'});
    const outputImagePath2 = await backgroundRemovalController.removeBlackBackground({inputImagePath: recoloration});
    const removeColor = await recolorationController.filter_out_color({inputImagePath: initialEmblemPath, targetColor: 'D30000', threshold: .5});
    const filter_by_color = await recolorationController.filter_by_color({inputImagePath: initialEmblemPath, targetColor: 'D30000', threshold: 100});
  }

return (
  <div>
    <img src={imagePath} className="image-space"/>
    <br/>
    <button onClick={edgeDetectionFunctions}>Canny Detection</button>
  </div>
)}
