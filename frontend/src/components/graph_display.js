import React, { useEffect, useState } from 'react';
import { Graph } from 'react-d3-graph';

const GraphDisplay = () => {
    const [graphData, setGraphData] = useState({ nodes: [], links: [] });

    // Fetch graph data from the Django API
    useEffect(() => {
        fetch('/api/graph/')
            .then((response) => response.json())
            .then((data) => {
                setGraphData({
                    nodes: data.nodes,
                    links: data.links,
                });
            });
    }, []);

    // Define graph configuration options
    const config = {
        nodeHighlightBehavior: true,
        node: {
            color: 'lightgreen',
            size: 300,
            highlightStrokeColor: 'blue',
        },
        link: {
            highlightColor: 'lightblue',
        },
    };

    return (
        <div>
            <h2>Graph Visualization</h2>
            <Graph
                id="graph-id" // id is mandatory, unique identifier for the graph
                data={graphData}
                config={config}
            />
        </div>
    );
};

export default GraphDisplay;
