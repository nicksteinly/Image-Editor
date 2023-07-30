import React, { useState } from 'react';
import { OperationForm } from '../components/OperationsForm.component';
import { AddedOperationList } from '../components/AddedOperationList.component';

export const ParentOperationsPage = () => {
  
  return (
    <div>
      <OperationForm />
      <AddedOperationList />
    </div>
  );
};