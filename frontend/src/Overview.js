import React from 'react';
import {useState} from 'react';
import location from './location.png';
import settings from './settings.png';
import police from './police.png';
import blue from './Ellipse 5.png';
import health from './ambulance.png';
import red from './Ellipse 6.png';
import fire from './hydrant.png';
import yellow from './Ellipse 7.png';
import add from './Group 698.png';
import minus from './Group 699.png';

import exit from './exit.png';

function Overview({data}) {
  const [polices, setPolices] = useState(0);
  const [fires, setFires] = useState(0);
  const [medics, setMedics] = useState(0);

  // display tasks here
  return (
    <>
        <div className="rootContainer">
            <div className="navbar"></div>
            <div className="rightContainer">
              <p className="title">Emergency overview</p>
              <p className="title2">Here's a summary of the emergency.</p>

              <div className='addminus'>
              <img src={blue} alt="blue" className="blueIcon" />
              <img src={police} alt="police" className="policeIcon" />
              <img src={red} alt="red" className="redIcon" />
              <img src={health} alt="health" className="healthIcon" />
              <img src={yellow} alt="yellow" className="yellowIcon" />
              <img src={fire} alt="fire" className="fireIcon" />
              <img src={add} alt="add" className="addIcon" onClick={() => {setPolices(polices+1)}}/>
              <img src={minus} alt="minus" className="minusIcon" onClick={() => {setPolices(polices-1)}}/>
              <img src={add} alt="add" className="addIcon2" onClick={() => {setMedics(medics+1)}}/>
              <img src={minus} alt="minus" className="minusIcon2" onClick={() => {setMedics(medics-1)}}/>
              <img src={add} alt="add" className="addIcon3" onClick={() => {setFires(fires+1)}}/>
              <img src={minus} alt="minus" className="minusIcon3" onClick={() => {setFires(fires-1)}}/>
              <h3 className='polices'>{polices}</h3>
              <h3 className='medics'>{medics}</h3>
              <h3 className='fires'>{fires}</h3>
              <div className="Overview">
                {Object.entries(data).map(([key, value]) => (
                  <p key={key}>{`${key}: ${value}`}</p>
                ))}
              </div>
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
