import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Button } from "@material-tailwind/react";
import Home from './pages/Home'

function App() {
  const [count, setCount] = useState(0);

  // call the backend API
  const callBackendAPI = async () => {
    const response = await fetch('localhost:5000/api');
    const body = await response.json();

    if (response.status !== 200) {
      throw Error(body.message)
    }
    return body;
  };

  useEffect(() => {
    callBackendAPI()
      .then(res => console.log(res.express))
      .catch(err => console.log(err));
  });

  return (
    <div className="App ">
      <Home />
      
    </div>
  )
}

export default App
