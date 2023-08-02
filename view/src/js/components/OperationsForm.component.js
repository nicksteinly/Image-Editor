import React, { useEffect, useState } from 'react';
import { OperationsController } from '../controller/OperationsController';
import { useOperation } from '../context/OperationProvider';
import {Accordion} from 'react-bootstrap';
import {Button} from 'react-bootstrap';
import '../../css/operations-form.css';

export const OperationForm = () => {
  const operationsJSON = useOperation().operations;
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
        {Object.entries(operationsJSON)?.map(([operationType, operationList], typeIndex) => (
          <Accordion.Item key={typeIndex} eventKey={typeIndex}>
            <Accordion.Header><h4>{operationType}</h4></Accordion.Header>
            <Accordion.Body>
              <Accordion>
                {operationList?.map((operation, index) => (
                  <Accordion.Item key={index} eventKey={typeIndex + "-" + index}>
                    <Accordion.Header>
                      {operation?.name}
                    </Accordion.Header>
                    <div id="accordion-inputs">
                      {Object.entries(operation?.parameters)?.map(([paramName, paramType]) => (
                        <h6>{paramName}: <input class='parameter-input' type={paramType} onChange={(e) => handleInputChange(paramName, e.target.value)} /></h6>
                      ))}
                      <Button variant="outline-primary" onClick={() => addOperation({ operationType: operationType, operationName: operation?.name, operationJSON: operation, paramValues: paramValues, setParamValues: setParamValues })}>Add</Button>
                    </div>
                    <Accordion.Body>
                      <p> {operation?.description}</p>
                    </Accordion.Body>
                  </Accordion.Item>
                ))}
              </Accordion>
            </Accordion.Body>
          </Accordion.Item>
        ))}
      </Accordion>
    </div>
  );
  }  