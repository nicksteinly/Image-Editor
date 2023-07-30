import React, { useEffect, useState } from 'react';
import { OperationsController } from '../controller/OperationsController';
import { useOperation } from '../context/OperationProvider';

const operationBaseURL = 'http://127.0.0.1:5000/operations';

export const OperationForm = () => {
  const operations = useOperation().operations;
  const addOperation = useOperation().addOperation;

  return (
    <div>
      <h2>Operations</h2>
      {operations?.map((operation, index) => (
        <div key={index}>
          <h3>{operation?.name}</h3>
          <p>Description: {operation?.description}</p>
          <p>Parameters:</p>
          <ul>
            {Object.entries(operation?.parameters)?.map(([paramName, paramType]) => (
              <li key={paramName}>
                {paramName}: <input type={paramType} />
              </li>
            ))}
          </ul>
          <button onClick={() => addOperation(operation?.name)}>Add</button>
        </div>
      ))}
    </div>
  );
};
