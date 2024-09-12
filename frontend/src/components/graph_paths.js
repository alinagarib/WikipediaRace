import React, { useState } from 'react';
import './path.css';

const GraphPath = () => {
    const [startLink, setStartLink] = useState('');
    const [endLink, setEndLink] = useState('');
    const [pathSolution, setPathSolution] = useState('');
    const [error, setError] = useState('');
    const [isPathSearched, setIsPathSearched] = useState(false);
    const [gotRandomLinks, setGotLinks] = useState(false);
    const [loadingMessage, setLoadingMessage] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [pathLoadingMessage, setPathLoadingMessage] = useState('')
    const [pathLoading, setPathLoading] = useState(false);

    const fetchRandomLinks = () => {
        setLoadingMessage('Fetching links! Please be patient >^.^<');
        setStartLink('');
        setEndLink('');
        setPathSolution('');
        setIsLoading(true);
        fetch('/api/random-links/')
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    setError(data.error);
                    setLoadingMessage('');
                } else {
                    setStartLink(data.start_link);
                    setEndLink(data.end_link);
                    setError('');
                    setLoadingMessage('');
                }
                setGotLinks(true);
            })
            .catch(err => {
                setError('Error fetching random links.');
                setLoadingMessage('');
            })
            .finally(() => {
                setIsLoading(false); 
            });
    };

    const fetchShortestPath = () => {
        setPathLoadingMessage('Finding the shortest path... XD')
        setPathLoading(true);
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
                setPathSolution('');
                setPathLoadingMessage('');
            } else {
                setPathSolution(data.solution);
                setError('');
                setPathLoadingMessage('');
            }
            setIsPathSearched(true);
        })
        .catch(err => {
            setError('Error fetching shortest path.');
            setPathSolution('');
            setIsPathSearched(true);
        })
        .finally(() => {
            setPathLoading(false); 
        });
    };


    return (
        <div>
            <button onClick={fetchRandomLinks}>Get Random Links</button>
            {isLoading && (
                <p style={{ 
                    width: '800px', 
                    margin: '0 auto', 
                    marginTop: '30px',
                    marginBottom: '30px',
                    textAlign: 'center', 
                    whiteSpace: 'normal', 
                    fontSize: '18px',
                    }}>{loadingMessage}</p>
            )}
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

            {isPathSearched && (
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
};

export default GraphPath;