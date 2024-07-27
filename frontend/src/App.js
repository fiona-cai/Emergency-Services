import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Dashboard from "./Dashboard";
import Root from './Root';
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
      path: "/Dashboard",
      element: <Dashboard/>,
    },
    {
      path: "/",
      element: <Root/>,
    },
  ]);

  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
