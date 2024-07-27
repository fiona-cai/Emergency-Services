import React from 'react';
import location from './location.png';
import settings from './settings.png';
import wave from './wave.png';
import exit from './exit.png';

function Root() {
  // display tasks here
  return (
    <>
        <div className="rootContainer">
            <div className="navbar"></div>
            <div className="rightContainer">
                <p className="title">Emergency Services</p>
                <p className="title2">Caller’s audio will be transcribed below.</p>
                <p className="title2">We’ll give you the solution to their problem.</p>
                <p className="subtitle">Transcription:</p>
                <p className="transcription">“There’s a massive flood over in the University of Waterloo , me and 5 others are stuck in the Math 3 building, send help please!”</p>
            </div>
        </div>
        <img src={wave} alt="wave" className="wave"/>
        <img src={settings} alt="settings" className="settings"/>
        <img src={location} alt="location" className="location"/>
        <img src={exit} alt="exit" className="exit"/>
    </>
  );
}

export default Root;
