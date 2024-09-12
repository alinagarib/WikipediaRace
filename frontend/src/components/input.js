import React, { useState } from 'react';
import './path.css';

function InputPage() {
    const [start, setStart] = useState('');
    const [end, setEnd] = useState('');
    const [pathSolution, setPathSolution] = useState('');
    const [error, setError] = useState('');
    const [isPathSearchedInput, setIsPathSearchedInput] = useState(false);
    const [pathLoading, setPathLoading] = useState(false);
    const [pathLoadingMessage, setPathLoadingMessage] = useState('');

    const fetchShortestPathInput = () => {
        setPathLoadingMessage('Finding the shortest path... XD')
        setPathLoading(true);
        setPathSolution('');
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
                setPathSolution('');
                setPathLoadingMessage('');
            } else {
                setPathSolution(data.solution);
                setError(''); 
                setPathLoadingMessage('');
            }
            setIsPathSearchedInput(true);
        })
        .catch(err => {
            setError('Error fetching shortest path.');
            setPathSolution(''); // Clear path solution in case of error
            setIsPathSearchedInput(true);
        })
        .finally(() => {
            setPathLoading(false); 
        });
    };

    return (
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
                <button style={{marginTop: '10px'}} onClick={fetchShortestPathInput} disabled={!start || !end}>
                    Find Shortest Path
                </button>
                {pathLoading && (
                <p style={{ 
                    width: '800px', 
                    margin: '0 auto', 
                    marginTop: '30px',
                    marginBottom: '30px',
                    textAlign: 'center', 
                    whiteSpace: 'normal', 
                    fontSize: '18px',
                }}>{pathLoadingMessage}</p>
            )}
            </div>

            {isPathSearchedInput && (
                <>
                    {pathSolution && <p style={{ 
                    width: '800px', 
                    margin: '0 auto', 
                    marginTop: '30px',
                    marginBottom: '30px',
                    textAlign: 'center', 
                    whiteSpace: 'normal', 
                    fontSize: '18px',
                    }}>{pathSolution}</p>}
                    {error && <p style={{ color: 'red', fontSize: '15px' }}>{error}</p>}
                </>
            )}
        </div>
    );
}

export default InputPage;