
import {HeaderComponent} from './js/components/Header.component';
import { ImageCarousel } from './js/components/ImageCarousel.component';
import {ParentOperationsPage} from './js/pages/ParentOperationsPage';
import { OperationProvider } from './js/context/OperationProvider';


function App() {
  return (
      <OperationProvider>
        <HeaderComponent/>
        <ImageCarousel />
        <ParentOperationsPage />
      </OperationProvider>
  );
}

export default App;
