// api.js

// Function to send the rule (AST) and user data to the backend for evaluation
// api.js

// Function to send the rule string to the backend for rule creation
export const createRule = async (rule) => {
    try {
        const response = await fetch("/create_rule", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ rule_string: rule }),  // Ensure rule is a string
        });

        // Check for response status
        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        return await response.json();
    } catch (error) {
        console.error("Failed to create rule:", error);
        return { success: false, message: error.message };
    }
};

// Function to send the rule (AST) and user data to the backend for evaluation
export const evaluateRule = async (ast, data) => {
    try {
        const response = await fetch("/evaluate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ast: ast, data: data }),  // Send AST and data
        });

        // Check for response status
        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        return await response.json();
    } catch (error) {
        console.error("Failed to evaluate rule:", error);
        return { success: false, message: error.message };
    }
};

// Sample data to evaluate
const ast = {
    type: "operator",
    operator: "AND",
    left: {
        type: "operator",
        operator: "OR",
        left: {
            type: "operator",
            operator: ">",
            left: { type: "operand", value: "age" },
            right: { type: "operand", value: 30 }
        },
        right: {
            type: "operator",
            operator: "<",
            left: { type: "operand", value: "age" },
            right: { type: "operand", value: 25 }
        }
    },
    right: {
        type: "operator",
        operator: ">",
        left: { type: "operand", value: "salary" },
        right: { type: "operand", value: 50000 }
    }
};

// Example usage
const userData = {
    age: 28,
    salary: 60000,
    department: "Sales"
};

// Call createRule and evaluateRule with sample data
(async () => {
    const createResponse = await createRule("your_rule_string_here");
    console.log(createResponse);

    const evaluateResponse = await evaluateRule(ast, userData);
    console.log(evaluateResponse);
})();
