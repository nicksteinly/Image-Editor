import React, { useState } from 'react';
import { OperationForm } from '../components/OperationsForm.component';
import { AddedOperationList } from '../components/AddedOperationList.component';
import '../../css/parent-operations-page.css';

export const ParentOperationsPage = () => {

  return (
    <div id='operations-container'>
      <OperationForm />
      <AddedOperationList />
    </div>
  );
};