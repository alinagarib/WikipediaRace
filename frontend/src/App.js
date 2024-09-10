// src/App.js

import React from 'react';
import './App.css';
// import GraphDisplay from './components/graph_display';

// function App() {
//     return (
//         <div className="App">
//             <GraphDisplay />
//         </div>
//     );
// }

// export default App;

import GraphPath from './components/graph_paths';

function App() {
    return (
        <div className="App">
            <h1 style = {{fontWight: 'bold'}}>W I K I P E D I A R A C E ! </h1>
            <h2>Welcome to WikiRace. Click the button below to get two random links and 
                find out the fastest path between the two links!</h2>
                <div className="graph-container">
            <GraphPath></GraphPath>
            </div>
        </div>
    );
}

export default App;

