import './App.css'
import { Button } from "@material-tailwind/react";
import Home from './pages/Home'
import {BrowserRouter as Router, Routes as Switch, Route, Routes} from "react-router-dom";
import { useState, useEffect } from 'react';
import Navbar from './components/Navbar'
import Footer from './components/Footer';
import Razvoj from './pages/Razvoj';
import Magazin from './pages/Magazin';
import Resursi from './pages/Resursi';
import Zajednica from './pages/Zajednica';
import Login from './pages/Login';
import Admin from './pages/Admin';
import Dizajn from './pages/Dizajn';
import BlogPost from './pages/BlogPost';






function App() {
  const [showNavFooter, setShowNavFooter] = useState(true);
  useEffect(() => {
    const currPath = window.location.pathname;
    if (currPath === "/login") {
      setShowNavFooter(false);
    } else {
      setShowNavFooter(true);
    }
  })
  return (
    <Router>
      <div className="App ">
        {showNavFooter && <Navbar />}
          <div className="content">
            <Routes>
              {console.log(window.location.pathname)}
              <Route path="/" element={<Home />} />
              <Route path="/razvoj" element={<Razvoj />} />
              <Route path="/magazin" element={<Magazin />} />
              <Route path="/resursi" element={<Resursi />} />
              <Route path="/dizajn" element={<Dizajn />} />
              {/* TODO */}
              <Route path="/blogs/:id" element={<BlogPost />} />
              <Route path="/zajednica" element={<Zajednica />} />
              <Route path="/admin" element={<Admin />} />
              <Route path="/login" element={<Login />} />
            </Routes>
          </div>
        {showNavFooter && <Footer />} 
      </div>
    </Router>
  )
}

export default App
