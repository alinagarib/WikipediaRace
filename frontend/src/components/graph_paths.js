import React, { useState } from 'react';

const GraphPath = () => {
    const [startLink, setStartLink] = useState('');
    const [endLink, setEndLink] = useState('');
    const [pathSolution, setPathSolution] = useState('');
    const [error, setError] = useState('');

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
        })
        .catch(err => {
            setError('Error fetching shortest path.');
        });
    };

    return (
        <div>
            <h2>Graph Path Finder</h2>
            <button onClick={fetchRandomLinks}>Get Random Links</button>
            {startLink && endLink && (
                <div>
                    <p>Start Link: {startLink}</p>
                    <p>End Link: {endLink}</p>
                </div>
            )}
            <button onClick={fetchShortestPath} disabled={!startLink || !endLink}>
                Find Shortest Path
            </button>
            {pathSolution && <p>{pathSolution}</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default GraphPath;
