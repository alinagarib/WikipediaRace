// src/App.js

import React from 'react';
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
            <h1>WikiRace!</h1>
            <GraphPath />
        </div>
    );
}

export default App;

