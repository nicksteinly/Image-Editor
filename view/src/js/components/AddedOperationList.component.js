import React, { useEffect, useState } from 'react';
import { OperationsController } from '../controller/OperationsController';
import { useOperation } from '../context/OperationProvider';

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
    <div>
      <h2>Operation List</h2>
      {console.log(addedOperations)}
      <ol>
        {addedOperations?.map((operation, index) => (
          <div key={index}>
            <li >{operation}</li>
            <button onClick={() => removeOperation(index)}>Remove</button>
          </div>
        ))}
      </ol>
      <input type='file' onChange={(e) => uploadImage(e.target.files[0])}>
      </input>
      <button onClick={submit}>Submit</button>
      {console.log(imagesData)}
      {imagesData && imagesData.map((imageData, index)   => (
        <div key={index}>
          <img src={`data:image/png;base64,${imageData}`} alt="Your Image" width={'50%'} height={'50%'}/>
        </div>
      ))}
    </div>
  );
};

