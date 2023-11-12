import './App.css'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Estimate from "./components/Estimate"
import Home from "./components/Home"
import NavBar from './components/NavBar';

function App() {
  return (
    <Router>
      <NavBar></NavBar>
      <Routes>
        {<Route path="/home" element={<Home />} />}
        <Route path="/estimate" element={<Estimate />} />
      </Routes>
    </Router>
  )
}

export default App
