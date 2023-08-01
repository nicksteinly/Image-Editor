import React, { Component }  from 'react';

import { useState } from "react";
import { createContext, useContext } from 'react';
import { useEffect } from 'react';
import { OperationsController } from '../controller/OperationsController';

const operationBaseURL = 'http://127.0.0.1:5000/operations';
const OperationContext = createContext();

export const OperationProvider = ({ children }) => {
  const operationsController = new OperationsController(operationBaseURL);
  const [operations, setOperations] = useState([]);
  const [addedOperations, setAddedOperations] = useState([]);
  const [addedOperationsJSON, setAddedOperationsJSON] = useState([]);
  const [imagesData, setImagesData] = useState([]);

  useEffect(() => {
    // Define an asynchronous function inside useEffect
    const fetchData = async () => {
      try {
        const operations = await operationsController.getOperations();
        setOperations(operations);
      } catch (error) {
        // Handle any errors that might occur during the API call
        console.error('Error fetching operation names:', error);
      }
    };

    // Call the asynchronous function immediately inside useEffect
    fetchData();
  }, []); // Empty dependency array means this will run only once on mount

  const addOperation = ({operationName, operationJSON, paramValues, setParamValues}) => {
    for (const [paramName, paramValue] of Object.entries(paramValues)) {
      operationJSON.parameters[paramName] = paramValue;
    }
    setAddedOperations([...addedOperations, operationName]);
    setAddedOperationsJSON([...addedOperationsJSON, operationJSON]);
    setParamValues({});
    console.log(addedOperationsJSON);
    console.log(operationJSON);
  };

  const removeOperation = (index) => {
    console.log(index);
    // Create a copy of the addedOperations array to avoid directly modifying the state array
    const updatedOperations = [...addedOperations];
    // Remove the element at the specified index using splice
    updatedOperations.splice(index, 1);
    addedOperationsJSON.splice(index, 1);
    // Update the state with the modified array
    setAddedOperations(updatedOperations);
    setAddedOperationsJSON({addedOperationsJSON});
  };

  const updateImagesData = (imagesData) => {
    setImagesData(imagesData);
  };

  return (
    <OperationContext.Provider value={{ operations, addOperation, removeOperation, addedOperations, addedOperationsJSON, imagesData, updateImagesData }}>
      {children}
    </OperationContext.Provider>
  );

}

export const useOperation = () => {
  return useContext(OperationContext);
};
