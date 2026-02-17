import React, { useState } from "react";

function App() {
    const [message, setMessage] = useState("");
    const [response, setResponse] = useState([]);
    const [sortBy, setSortBy] = useState("similarity");

    const sendMessage = async() => {
        if (!message.trim()) return;

        try {
            const res = await fetch(
                `http://127.0.0.1:8000/chat?sort_by=${sortBy}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ message }),
                }
            );

            const data = await res.json();
            setResponse(data.response);
        } catch (error) {
            console.error("Error:", error);
        }
    };

    return ( <
        div style = {
            { padding: "30px", fontFamily: "Arial" } } >
        <
        h1 > AI Shopping Agent < /h1>

        <
        input type = "text"
        placeholder = "Search products..."
        value = { message }
        onChange = {
            (e) => setMessage(e.target.value) }
        style = {
            { padding: "10px", width: "300px" } }
        />

        <
        br / > < br / >

        <
        select value = { sortBy }
        onChange = {
            (e) => setSortBy(e.target.value) }
        style = {
            { padding: "8px" } } >
        <
        option value = "similarity" > Sort by Similarity < /option> <
        option value = "price_low" > Price: Low to High < /option> <
        option value = "price_high" > Price: High to Low < /option> <
        /select>

        <
        br / > < br / >

        <
        button onClick = { sendMessage }
        style = {
            { padding: "10px 20px", cursor: "pointer" } } >
        Search <
        /button>

        <
        div style = {
            { marginTop: "30px" } } > {
            response.length > 0 && ( <
                >
                <
                h3 > Top Recommendations: < /h3> {
                    response.map((item, index) => ( <
                        div key = { index }
                        style = {
                            {
                                border: "1px solid #ccc",
                                padding: "10px",
                                marginBottom: "10px",
                                borderRadius: "5px",
                            }
                        } >
                        <
                        h4 > { item.product_name } < /h4> <
                        p > { item.description } < /p> <
                        p > < b > Price: < /b> ₹{item.price}</p >
                        <
                        p > < b > Score: < /b> {item.score?.toFixed(3)}</p >
                        <
                        /div>
                    ))
                } <
                />
            )
        } <
        /div> <
        /div>
    );
}

export default App;