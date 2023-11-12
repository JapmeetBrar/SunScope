import './App.css'
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';

import Estimate from "./components/Estimate"
import Home from "./components/Home"
import NavBar from './components/NavBar';
import { Contact } from './components/Contact';

function App() {
  return (
    <Router>
      <NavBar></NavBar>
      <Routes>
        <Route path='/' element={<Navigate to='/home' replace={true}/>} />
        <Route path="/home" element={<Home />} />
        <Route path="/estimate" element={<Estimate />} />
        <Route path="/contact" element={<Contact />}/>
      </Routes>
    </Router>
  )
}

export default App
