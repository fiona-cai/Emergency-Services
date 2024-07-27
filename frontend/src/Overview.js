import React from 'react';
import location from './location.png';
import settings from './settings.png';
import exit from './exit.png';

function Overview() {
  // display tasks here
  return (
    <>
        <div className="rootContainer">
            <div className="navbar"></div>
            <div className="rightContainer">
                
            </div>
        </div>
        <img src={settings} alt="settings" className="settings"/>
        <img src={location} alt="location" className="location"/>
        <img src={exit} alt="exit" className="exit"/>
    </>
  );
}

export default Overview;
