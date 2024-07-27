import React from 'react';
import location from './location.png';
import settings from './settings.png';
import wave from './wave.png';

function Root() {
  // display tasks here
  return (
    <>
<link rel="preconnect" href="https://fonts.googleapis.com"></link>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin></link>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet"></link>
<h1>Emergency Services</h1>
<p>Caller’s audio will be transcribed below.</p>
<p>We’ll give you the solution to their problem.</p>
<h2>Transcription</h2>
<h3>“There’s a massive flood over in Waterloo University, me and 5 others are stuck in the Math 3 building, send help please!”</h3>
        <div className="navbar"></div>
        <img src={location} alt="location" className="location"/>
        <img src={settings} alt="settings" className="settings"/>
        <img src={wave} alt="wave" className="wave"/>
         
    </>
  );
}

export default Root;
