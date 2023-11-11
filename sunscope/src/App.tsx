import './App.css'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

// import NavBar from "./components/NavBar"
// import About from "./components/About"
// import Estimate from "./components/Estimate"
import Home from "./components/Home"

function App() {
  return (
    <Router>
      {/* <NavBar /> */}
      <Routes>
        {<Route path="/" element={<Home />} />}
        {/* <Route path="/about" element={<About />} /> */}
        {/* <Route path="/estimate" element={<Estimate />} /> */}
        {/* <Route path="/contact" element={<Contact />} /> */}
        <h1 className='text-3xl font-bold underline'>SunScope</h1>
      </Routes>
    </Router>
  )
}

export default App
