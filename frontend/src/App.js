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

import socketIO from 'socket.io-client';

const socket = socketIO.connect('http://localhost:5000');

function App() {
  const [data, setData] = useState(null);
  const [display, setDisplay] = useState(false);
  

  // set data to received data (pass through props)
  useEffect(() => {
    socket.on("send", (data) => {
      setData(data);
      setDisplay(false);
      console.log("data has been sent and stored")
    });
    socket.on("display", () => {
      setDisplay(true);
      console.log("data has been confirmed and we are now displaying!")
    })
  }, [socket]);

  // confirm function to send confirmation to backend (pass this through props to overview)
  const onConfirm = () => {
    socket.emit("confirm", {});
  }

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
