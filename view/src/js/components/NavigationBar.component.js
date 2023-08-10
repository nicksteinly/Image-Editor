import React from 'react';
import { navData } from '../lib/navData';
import { NavLink } from 'react-router-dom';
import "../../css/navigation-bar.css"

export function NavigationBar() {


  return (
    <div id={'side-nav'}>
        {navData.map(item =>{
            return <NavLink key={item.id} id={'side-item'} to={item.link}>
                      <span >{item.text}</span>
                    </NavLink>
        })}
    </div>
  )
    

}

