import React, { useEffect, useState } from 'react';
import { OperationsController } from '../controller/OperationsController';
import { useOperation } from '../context/OperationProvider';

export const OperationForm = () => {
  const operations = useOperation().operations;
  const addOperation = useOperation().addOperation;
  const [paramValues, setParamValues] = useState({});

  const handleInputChange = (paramName, value) => {
    setParamValues((prevInputs) => ({
      ...prevInputs,
      [paramName]: value,
    }));
    console.log(paramValues);
  };

  return (
    <div>
      <h2>Operations</h2>
      {operations?.map((operation, index) => (
        <div key={index}>
          <h2>{operation?.type}</h2>
          <h3>{operation?.name}</h3>
          <p>Description: {operation?.description}</p>
          <p>Parameters:</p>
          <ul>
            {Object.entries(operation?.parameters)?.map(([paramName, paramType]) => (
              <li key={paramName}>
                {paramName}: <input type={paramType} onChange={(e) => handleInputChange(paramName, e.target.value)}/>
              </li>
            ))}
          </ul>
          <button onClick={() => addOperation({operationName: operation?.name, operationJSON: operation, paramValues: paramValues, setParamValues: setParamValues})}>Add</button>
        </div>
      ))}
    </div>
  );
};
