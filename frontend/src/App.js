// import React from 'react';
// import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
// import HomePage from './components/HomePage';
// import Dashboard from './components/Dashboard';

// function App() {
//   return (
//     <Router>
//       <Switch>
//         <Route path="/" exact component={HomePage} />
//         <Route path="/dashboard" component={Dashboard} />
//       </Switch>
//     </Router>
//   );
// }

// export default App;

import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const testConnection = async () => {
      const response = await axios.get('http://localhost:5000/test');
      setMessage(response.data.message);
    };

    testConnection();
  }, []);

  return (
    <div>
      {message}
    </div>
  );
}

export default App;
