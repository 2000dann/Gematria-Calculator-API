import React, { useState } from "react";
import axios from "axios";

const GematriaCalculator = ({ onResult }) => {
    const [text, setText] = useState("");
    const [method, setMethod] = useState("hebrew");

    const handleCalculate = async () => {
        if (!text.trim()) {
            alert("Please enter text.");
            return;
        }
        try {
            const response = await axios.get("http://127.0.0.1:8000/gematria", {
                params: { text, system: method },
            });
            onResult(response.data);
        } catch (error) {
            console.error("Calculation failed:", error);
            alert("Error calculating Gematria.");
        }
    };

    return (
        <div>
            <textarea
                placeholder="Enter text..."
                value={text}
                onChange={(e) => setText(e.target.value)}
            />
            <select value={method} onChange={(e) => setMethod(e.target.value)}>
                <option value="hebrew">Hebrew</option>
                <option value="english">English</option>
            </select>
            <button onClick={handleCalculate}>Calculate</button>
        </div>
    );
};

export default GematriaCalculator;
