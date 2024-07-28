import React from 'react';
import location from './location.png';
import settings from './settings.png';
import exit from './exit.png';
import blue from './blue.png';
import police from './police.png';

function Police() {
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
        <img src={blue} alt="blue" className="triangle"/>
        <img src={police} alt="police" className="police"/>
    </>
  );
}

export default Police;
