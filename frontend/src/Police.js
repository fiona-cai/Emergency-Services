import React from 'react';
import location from './location.png';
import settings from './settings.png';
import exit from './exit.png';
import blue from './blue.png';
import police from './police.png';
import suitcase from './case.png';
import cross from './cross.png';
import radar from './radar.png';

function Police({data}) {
  // display tasks here
  return (
    <>
        <div className="rootContainer">
            <div className="navbar"></div>
            <div className="rightContainer">
              <p className="title"> Instructions </p>
              <p className="title2">Based on the situation, here are some things you should do</p>
              <p className="instructions" style={{"position": "absolute", "top": "260px", "left": "90px"}}>euhfibdjdjnw</p>
              <p className="instructions" style={{"position": "absolute", "top": "435px", "left": "90px"}}>fduhsiasjkduh</p>
              <p className="instructions" style={{"position": "absolute", "top": "610px", "left": "90px"}}>fduhsiasjkduh</p>
            </div>
        </div>
        <img src={settings} alt="settings" className="settings"/>
        <img src={location} alt="location" className="location"/>
        <img src={exit} alt="exit" className="exit"/>
        <img src={blue} alt="blue" className="triangle"/>
        <img src={police} alt="police" className="police"/>
        <img src={suitcase} alt="suitcase" className="icon1"/>
        <img src={radar} alt="radar" className="icon2"/>
        <img src={cross} alt="cross" className="icon3"/>
    </>
  );
}

export default Police;
