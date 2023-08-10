import React from 'react';
import { OperationForm } from '../components/OperationsForm.component';
import { AddedOperationList } from '../components/AddedOperationList.component';
import { OperationProvider } from '../context/OperationProvider';
import { HeaderComponent } from '../components/Header.component';
import { ImageCarousel } from '../components/ImageCarousel.component';
import '../../css/parent-operations-page.css';

export const ImageProcessingPage = () => {

  return (
      <OperationProvider>
        <HeaderComponent header={"Image Processing"} />
        <ImageCarousel />
        <div id='operations-container'>
          <OperationForm />
          <AddedOperationList />
        </div>
      </OperationProvider>
  );
};