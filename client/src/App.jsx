import './App.css'
import { Button } from "@material-tailwind/react";
import Home from './pages/Home'
import { BrowserRouter as Router, Routes as Switch, Route } from "react-router-dom";
import Navbar from './components/Navbar'
import Footer from './components/Footer';
import Razvoj from './pages/Razvoj';
import Magazin from './pages/Magazin';

function App() {
  return (
    <Router>
      <div className="App ">
        <Navbar />
          <div className="content">
            <Switch>
              <Route path="/" element={<Home />} />
              <Route path="/razvoj" element={<Razvoj />} />
              <Route path="/magazin" element={<Magazin />} />
            </Switch>
          </div>
        <Footer /> 
      </div>
    </Router>
  )
}

export default App
