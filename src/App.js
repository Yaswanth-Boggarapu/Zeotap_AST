// frontend/src/App.js
import React, { useState } from "react";
import { createRule, evaluateRule } from "./services/api";

const App = () => {
    const [rule, setRule] = useState("");
    const [data, setData] = useState({});
    const [result, setResult] = useState(null);

    const handleCreateRule = async () => {
        const response = await createRule(rule);
        console.log("Rule created:", response);
    };

    const handleEvaluateRule = async () => {
        const response = await evaluateRule(data);
        setResult(response.result);
    };


    return (
        <div>
            <h1>Rule Engine</h1>
            <div>
                <h2>Create Rule</h2>
                <input type="text" value={rule} onChange={(e) => setRule(e.target.value)} />
                <button onClick={handleCreateRule}>Create Rule</button>
            </div>
            <div>
                <h2>Evaluate Rule</h2>
                {/* Add fields for user data input */}
                <button onClick={handleEvaluateRule}>Evaluate</button>
                {result !== null && <p>Result: {result ? "True" : "False"}</p>}
            </div>
        </div>
    );
};

export default App;
