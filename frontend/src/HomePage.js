import React, { useState } from 'react';
import axios from 'axios';

function HomePage() {
  const [text, setText] = useState('');

  const handleEmergency = async () => {
    const { data } = await axios.post('/emergency', { text });
    // update dashboards with data
  };

  return (
    <div>
      <button onClick={handleEmergency}>Report Emergency</button>
    </div>
  );
}

export default HomePage;
