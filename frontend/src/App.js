// src/App.js

import React, { useState } from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import GraphPath from './components/graph_paths';
import InputPage from './components/input'; 

function App() {
    const [isClicked, setIsClicked] = useState(false);

    return (
        <Router>
        <div className="App">
            <h1 style = {{fontWeight: 'bold'}}>W I K I P E D I A R A C E ! </h1>
            <h2>Welcome to WikiRace. Explore the paths between two inputs or two
                randomly generated links!
            </h2>
            <div className = 'menubar'>
                <ul>
                    <li onClick={() => setIsClicked(!isClicked)}>
                        <Link to={isClicked ? "/" : "/input"}>
                            {isClicked ? "Go Back" : "Search a Shortest Path"}
                        </Link>
                    </li>
                </ul>  
            </div>
                <div className="graph-container">
                <Routes>
                            <Route path="/" element={<GraphPath />} />
                            <Route path="/input" element={<InputPage />} />
                </Routes>
            </div>
        </div>
        </Router>
    );
}

export default App;

