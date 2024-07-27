import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Overview from "./Overview";
import Root from './Root';
import Medical from './Medical';
import Fire from './Fire';
import Police from './Police';
import './App.css';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";


function App() {
  const [message, setMessage] = useState('feiovewoi');

  /*
  useEffect(() => {
    const testConnection = async () => {
      const response = await axios.get('http://localhost:5000/test');
      setMessage(response.data.message);
    };

    testConnection();
  }, []);
  */
  const router = createBrowserRouter([
    {
      path: "/overview",
      element: <Overview/>,
    },
    {
      path: "/",
      element: <Root/>,
    },
    {
      path: "/medical",
      element: <Medical/>,
    },
    {
      path: "/fire",
      element: <Fire/>,
    },
    {
      path: "/police",
      element: <Police/>,
    },
  ]);

  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
