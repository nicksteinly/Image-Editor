import React from 'react';  
import '../../css/header.css';

export const HeaderComponent = ({header}) => {


  return(
    <div id="header-container">
      <h1>{header}</h1>
    </div>
  )
}