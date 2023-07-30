import React, { useState } from 'react';
import { OperationForm } from '../components/OperationsForm.component';
import { AddedOperationList } from '../components/AddedOperationList.component';

export const ParentOperationsPage = () => {
  const [operationAdded, setOperationAdded] = useState([]);

  const addOperationToList = (operation) => {
    console.log(operation);
    setOperationAdded([...operationAdded, operation]);
  };

  return (
    <div>
      <OperationForm />
      <AddedOperationList addOperation={operationAdded} />
    </div>
  );
};