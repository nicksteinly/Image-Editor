import React from 'react';
import { Route } from 'react-router-dom';
import { Routes } from 'react-router-dom';
import { PageLayout } from './js/components/PageLayout.component';
import { ImageProcessingPage } from './js/pages/ImageProcessingPage';
import { ComputerVisionPage } from './js/pages/ComputerVisionPage';
import { TemplateMatchingPage } from './js/pages/TemplateMatchingPage';

export const PageRouter = () => {

  return (
    <Routes>
      <Route element={<PageLayout />}>
        <Route path="/image-processing" element={<ImageProcessingPage />} />
        <Route path="/computer-vision" element={<ComputerVisionPage />} />
        <Route path="/computer-vision/template-matching" element={<TemplateMatchingPage/>} />
        <Route path="*" element={<h1>Not Found</h1>} />
      </Route>
    </Routes>
  );
};