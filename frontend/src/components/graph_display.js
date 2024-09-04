import React, { useEffect, useState } from 'react';
import { Graph } from 'react-d3-graph';

const GraphDisplay = () => {
    const [graphData, setGraphData] = useState({ nodes: [], links: [] });
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);

    // Fetch graph data from the Django API with pagination
    const fetchGraphData = (page) => {
        fetch(`/api/graph/?page=${page}`)
            .then((response) => response.json())
            .then((data) => {
                setGraphData({
                    nodes: [...graphData.nodes, ...data.nodes],  // Append new nodes
                    links: [...graphData.links, ...data.links],  // Append new links
                });
                setTotalPages(data.total_pages);
            });
    };

    useEffect(() => {
        fetchGraphData(currentPage);  // Fetch initial data
    }, [currentPage]);

    // Function to load more data (next page)
    const loadMoreData = () => {
        if (currentPage < totalPages) {
            setCurrentPage(currentPage + 1);
        }
    };

    // Graph configuration options
    const config = {
        staticGraph: false,
        nodeHighlightBehavior: true,
        maxNodesPerFrame: 200,  // Set a limit on how many nodes are rendered
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
                id="graph-id"  // Unique ID for the graph
                data={graphData}  // Data prop contains nodes and links
                config={config}  // Pass the config object here
            />
            {currentPage < totalPages && (
                <button onClick={loadMoreData}>Load More</button>  // Button to load more data
            )}
        </div>
    );
};

export default GraphDisplay;
