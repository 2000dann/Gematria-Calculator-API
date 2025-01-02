import React from "react";

const ResultsDisplay = ({ result }) => {
    if (!result) return null;

    return (
        <div>
            <h3>Result</h3>
            <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
    );
};

export default ResultsDisplay;
