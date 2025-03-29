const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');

const app = express();
app.use(cors());

app.post('/proxy', async (req, res) => {
    const { prompt } = req.body;
    const response = await fetch('https://api.deepseek.com/v1/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer sk-83a062b1fccb4f4bb48b42dda1d8cae9`,
        },
        body: JSON.stringify({
            prompt,
            max_tokens: 150,
            temperature: 0.7,
        }),
    });
    const data = await response.json();
    res.json(data);
});

app.listen(3000, () => console.log('Proxy server running on http://localhost:3000'));