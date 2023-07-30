
import './App.css';
import { ImageSpaceComponent } from './js/components/ImageSpace.component';
import {ParentOperationsPage} from './js/pages/ParentOperationsPage';
import { OperationProvider } from './js/context/OperationProvider';


function App() {
  return (
    <OperationProvider>
      <ParentOperationsPage />
    </OperationProvider>
  );
}

export default App;
