import React from 'react';
import location from './location.png';
import settings from './settings.png';
import exit from './exit.png';
import yellow from './yellow.png';
import hydrant from './hydrant.png';

function Fire({data}) {
  // display tasks here
  return (
    <>
        <div className="rootContainer">
            <div className="navbar"></div>
            <div className="rightContainer">                
              <p className="title"> Instructions </p>
              <p className="title2">Based on the situation, here are some things you should do</p>
                
            </div>
        </div>
        <img src={settings} alt="settings" className="settings"/>
        <img src={location} alt="location" className="location"/>
        <img src={exit} alt="exit" className="exit"/>
        <img src={yellow} alt="yellow" className="triangle"/>
        <img src={hydrant} alt="hydrant" className="hydrant"/>
    </>
  );
}

export default Fire;
