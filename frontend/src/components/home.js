import React from 'react';
import '../App.css';
import GraphPath from './graph_paths';
import { useNavigate } from 'react-router-dom';

function Home () {
    const navigate = useNavigate();

    return (
        <div>
        <h1 style = {{fontWeight: 'bold'}}>W I K I P E D I A R A C E ! </h1>
            <h2>Welcome to WikiRace. Click the button below to find the shortest
                path betweeen two inputs, otherwise get two random links and observe thier shortest path!
            </h2>
            <div className = 'menubar'>
            <button onClick={() => navigate('/input')}>Search a Shortest Path</button>
            </div>
            <div className="graph-container">
                <GraphPath></GraphPath>
        </div>
        </div>
    );

};

export default Home;
