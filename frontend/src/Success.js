import React from 'react';
import location from './location.png';
import settings from './settings.png';
import exit from './exit.png';
import check from './check.png';
import success from './success.png';

function Success() {
  // display tasks here
  return (
    <>
        <div className="rootContainer">
            <div className="navbar"></div>
            <img src={check} alt="check" className="check"/>
            <img src={success} alt="success" className="success"/>
        </div>
        <img src={settings} alt="settings" className="settings"/>
        <img src={location} alt="location" className="location"/>
        <img src={exit} alt="exit" className="exit"/>
    </>
  );
}

export default Success;
