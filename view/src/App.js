

import { ImageCarousel } from './js/components/ImageCarousel.component';
import {ParentOperationsPage} from './js/pages/ParentOperationsPage';
import { OperationProvider } from './js/context/OperationProvider';


function App() {
  return (
      <OperationProvider>
        <h1>Image Processing</h1>
        <ImageCarousel />
        <ParentOperationsPage />
      </OperationProvider>
  );
}

export default App;
