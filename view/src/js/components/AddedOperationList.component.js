import React, { useEffect, useState } from 'react';
import { OperationsController } from '../controller/OperationsController';
import { useOperation } from '../context/OperationProvider';
import {Button} from 'react-bootstrap';
import {ImageCarousel} from './ImageCarousel.component';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../../css/added-operation-list.css';

const operationBaseURL = 'http://127.0.0.1:5000/operations';

export const AddedOperationList = () => {
  const operationsController = new OperationsController(operationBaseURL);
  const addedOperations = useOperation().addedOperations;
  const addedOperationsJSON = useOperation().addedOperationsJSON;
  const removeOperation = useOperation().removeOperation;
  const [imagesData, setImageData] = useState([]);
  const [uploadedImage, setUploadedImage] = useState('');

  const uploadImage = async (img) => {
    setUploadedImage(img.name)
  }

  const submit = async () => {
    const image_response = await operationsController.submitOperations({operationsJSON: addedOperationsJSON, inputImage: uploadedImage});
    setImageData(image_response);
  };

  return (
    <div id="added-operations-list">
      <h2>Added Operations List</h2>
      {console.log(addedOperations)}
      <ol>
        {addedOperations?.map((operation, index) => (
          <div key={index}>
            <li >{operation}</li>
            <Button onClick={() => removeOperation(index)}>Remove</Button>
          </div>
        ))}
      </ol>
      <input type='file' onChange={(e) => uploadImage(e.target.files[0])}>
      </input>
      <Button onClick={submit}>Submit</Button>
      {console.log(imagesData)}
      <ImageCarousel imagesData={imagesData}/>
    </div>
  );
};

