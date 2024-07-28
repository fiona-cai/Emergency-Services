import React from 'react';
import location from './location.png';
import settings from './settings.png';
import police from './police.png';
import blue from './Ellipse 5.png';
import health from './ambulance.png';
import red from './Ellipse 6.png';
import fire from './hydrant.png';
import yellow from './Ellipse 7.png';

import exit from './exit.png';

function Overview() {
  // display tasks here
  return (
    <>
        <div className="rootContainer">
            <div className="navbar"></div>
            <div className="rightContainer">
              <p className="title">Emergency overview</p>
              <p className="title2">Here's a summary of the emergency.</p>
              <p className="title2">We’ll give you the solution to their problem.</p>

              <div className='addminus'>
              <img src={blue} alt="blue" className="blueIcon" />
              <img src={police} alt="police" className="policeIcon" />
              <img src={red} alt="red" className="redIcon" />
              <img src={health} alt="health" className="healthIcon" />
              <img src={yellow} alt="yellow" className="yellowIcon" />
              <img src={fire} alt="fire" className="fireIcon" />
              </div>
            </div>
        </div>
        <img src={settings} alt="settings" className="settings"/>
        <img src={location} alt="location" className="location"/>
        <img src={exit} alt="exit" className="exit"/>
    </>
  );
}

export default Overview;
