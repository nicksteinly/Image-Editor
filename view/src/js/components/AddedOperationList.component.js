import React, { useEffect, useState } from 'react';
import { OperationsController } from '../controller/OperationsController';
import { useOperation } from '../context/OperationProvider';
import {Button} from 'react-bootstrap';
import {InputGroup} from 'react-bootstrap';
import '../../css/added-operation-list.css';

const operationBaseURL = 'http://127.0.0.1:5000/operations';

export const AddedOperationList = () => {
  const operationsController = new OperationsController(operationBaseURL);
  const addedOperations = useOperation().addedOperations;
  const addedOperationsJSON = useOperation().addedOperationsJSON;
  const removeOperation = useOperation().removeOperation;
  const updateImagesData = useOperation().updateImagesData;
  const [imagesData, setImageData] = useState([]);
  const [uploadedImage, setUploadedImage] = useState('');

  const uploadImage = async (img) => {
    setUploadedImage(img.name)
  }

  const submit = async () => {
    const imageResponse = await operationsController.submitOperations({operationsJSON: addedOperationsJSON, inputImage: uploadedImage});
    updateImagesData(imageResponse);
  };

  return (
    <div id="added-operations-list">
      <h2>Selected Operations</h2>
      <br/>
      <ol>
        {addedOperations?.map((operation, index) => (
          <div key={index}>
            <li >
              {operation}
              &nbsp;
              <Button variant="outline-primary" onClick={() => removeOperation(index)}>Remove</Button>
            </li>
            <br/>
          </div>
        ))}
      </ol>
        <div class="mb-3">
          <label for="formFile" class="form-label">Upload Image</label>
          <input class="form-control" type="file" id="formFile"/>
        </div>
      <Button variant="outline-primary" onClick={submit}>Submit</Button>
    </div>
  );
};

