import { Outlet } from 'react-router-dom';
import { NavigationBar } from './NavigationBar.component';

export const PageLayout = () => (
  <>
    <NavigationBar />  
    <div className="contentPane">
      <Outlet /> 
    </div>     
  </>
);