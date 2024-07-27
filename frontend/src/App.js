import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Dashboard from "./Dashboard";
import Homepage from './Homepage';
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
      element: <Homepage/>,
    },
  ]);

  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
