import React, { useState } from 'react';
import './path.css';

const GraphPath = () => {
    const [startLink, setStartLink] = useState('');
    const [endLink, setEndLink] = useState('');
    const [start, setStart] = useState('');
    const [end, setEnd] = useState('');
    const [pathSolution, setPathSolution] = useState('');
    const [error, setError] = useState('');
    const [isPathSearched, setIsPathSearched] = useState(false);
    const [isPathSearchedInput, setIsPathSearchedInput] = useState(false);
    const [gotRandomLinks, setGotLinks] = useState(false);

    const fetchRandomLinks = () => {
        fetch('/api/random-links/')
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    setError(data.error);
                } else {
                    setStartLink(data.start_link);
                    setEndLink(data.end_link);
                    setError('');
                }
                setGotLinks(true);
            })
            .catch(err => {
                setError('Error fetching random links.');
            });
    };

    const fetchShortestPath = () => {
        fetch('/api/shortest-path/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                start_link: startLink,
                end_link: endLink,
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                setError(data.error);
            } else {
                setPathSolution(data.solution);
                setError('');
            }
            setIsPathSearched(true);
        })
        .catch(err => {
            setError('Error fetching shortest path.');
            setPathSolution(''); // Clear path solution in case of error
            setIsPathSearched(true);
        });
    };

    const fetchShortestPathInput = () => {
        fetch('/api/shortest-path/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                start_link: start,
                end_link: end,
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                setError(data.error);
            } else {
                setPathSolution(data.solution);
                setError('');
                setIsPathSearchedInput(true); 
            }
        })
        .catch(err => {
            setError('Error fetching shortest path.');
            setPathSolution(''); // Clear path solution in case of error
            setIsPathSearchedInput(true);
        });
    };

    return (
        <div>
            <button onClick={fetchRandomLinks}>Get Random Links</button>
            {startLink && endLink && (
                <div>
                    <p>Start Link: 
                        <a href={`https://en.wikipedia.org/wiki/${startLink}`} target="_blank" rel="noopener noreferrer">
                            {startLink}
                        </a>
                    </p>
                    <p>End Link: 
                        <a href={`https://en.wikipedia.org/wiki/${endLink}`} target="_blank" rel="noopener noreferrer">
                            {endLink}
                        </a>
                    </p>  
                </div>
            )}

            {gotRandomLinks && (
            <button onClick={fetchShortestPath} disabled={!startLink || !endLink}>
                Find Shortest Path
            </button>
            )}

            {isPathSearched && (
                <>
                    {pathSolution && <p style={{ 
                    width: '800px', /* Define the width with px */
                    margin: '0 auto', /* Center the element horizontally */
                    marginTop: '30px',
                    marginBottom: '30px',
                    textAlign: 'center', /* Center the text content */
                    whiteSpace: 'normal' /* Allow text to wrap onto multiple lines */
                    }}>{pathSolution}</p>}
                    {error && <p style={{ color: 'red' }}>{error}</p>}
                </>
            )}
            <div>
            <label htmlFor="start">Start Link: </label>
            <input 
                type="text" 
                id="start" 
                name="start" 
                value={start} 
                onChange={(e) => setStart(e.target.value)}  // Capture the input value for startLink
            />
            
            <div>
            <label htmlFor="end">End Link: </label>
            <input 
                type="text" 
                id="end" 
                name="end" 
                value={end} 
                onChange={(e) => setEnd(e.target.value)}  // Capture the input value for endLink
            />
            </div>
            <div>
            <button2 onClick={fetchShortestPathInput} disabled={!start || !end}>
                Find Shortest Path
            </button2>
            </div>

            {isPathSearchedInput && (
                <>
                    {pathSolution && <p>{pathSolution}</p>}
                    {error && <p style={{ color: 'red' }}>{error}</p>}
                </>
            )}
        </div>
        </div>
    );
};

export default GraphPath;
