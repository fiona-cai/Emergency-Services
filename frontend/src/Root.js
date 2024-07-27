import React from 'react';
import location from './location.png';
import settings from './settings.png';
import wave from './wave.png';

function Root() {
  // display tasks here
  return (
    <>
        <div className="navbar"></div>
        <img src={location} alt="location" className="location"/>
        <img src={settings} alt="settings" className="settings"/>
        <img src={wave} alt="wave" className="wave"/>
    </>
  );
}

export default Root;
