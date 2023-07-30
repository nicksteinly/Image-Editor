import React, { useEffect, useState } from 'react';
import { OperationsController } from '../controller/OperationsController';
import { useOperation } from '../context/OperationProvider';

const operationBaseURL = 'http://127.0.0.1:5000/operations';

export const AddedOperationList = () => {
  const operationsController = new OperationsController(operationBaseURL);
  const addedOperations = useOperation().addedOperations;
  const removeOperation = useOperation().removeOperation;

  const submit = async () => {
    operationsController.submitOperations(addedOperations);
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
      <button onClick={submit}>Submit</button>
    </div>
  );
};

