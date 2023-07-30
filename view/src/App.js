
import './App.css';
import { ImageSpaceComponent } from './js/components/ImageSpace.component';
import {ImageCarousel} from './js/components/ImageCarousel.component';
import {ParentOperationsPage} from './js/pages/ParentOperationsPage';
import { OperationProvider } from './js/context/OperationProvider';


function App() {
  return (
    <>
      <OperationProvider>
        <ParentOperationsPage />
      </OperationProvider>
      <ImageCarousel/>
    </>

  );
}

export default App;
