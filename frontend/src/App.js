import React, { useEffect, useState } from 'react';
import Login from "./Login.js";
import './App.css';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

import socketIO from 'socket.io-client';

const socket = socketIO.connect('http://localhost:5000');

function App() {
  const [data, setData] = useState({"iwerfdnweinfdes": "efindsin"});
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
      path: "/login",
      element: <Login data={data}/>,
    },
  ]);

  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
