import React, { useEffect, useState } from 'react';
import { OperationsController } from '../controller/OperationsController';
import { useOperation } from '../context/OperationProvider';
import {Accordion} from 'react-bootstrap';
import {Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../../css/operations-form.css';

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
    <div id='operations-form-container'>
      <h2>Operations</h2>
      <Accordion>
      {operations?.map((operation, index) => (
        <Accordion.Item key={index} eventKey={index}>
          <Accordion.Header><h3>{operation?.name}</h3></Accordion.Header>
          <Accordion.Body>
            <p>Description: {operation?.description}</p>
            <p>Parameters:</p>
            <ul>
            {Object.entries(operation?.parameters)?.map(([paramName, paramType]) => (
                  <li key={paramName}>
                    {paramName}: <input type={paramType} onChange={(e) => handleInputChange(paramName, e.target.value)}/>
                  </li>
                ))}
            </ul>
            <Button onClick={() => addOperation({operationName: operation?.name, operationJSON: operation, paramValues: paramValues, setParamValues: setParamValues})}>Add</Button>
          </Accordion.Body>
        </Accordion.Item>
      ))}
      </Accordion>
    </div>
  );
};
