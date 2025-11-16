// --- Netlify Function: netlify/functions/generate.js ---
// This is your new, secure "middle-man" server.
// It receives the request from your website, adds the
// secret API key, and then talks to Google.

exports.handler = async (event) => {
    // 1. Only allow POST requests
    if (event.httpMethod !== 'POST') {
        return { statusCode: 405, body: 'Method Not Allowed' };
    }

    // 2. Get the API key SECURELY from Netlify's settings
    // We will set this up in the Netlify dashboard.
    const apiKey = process.env.GEMINI_API_KEY;

    if (!apiKey) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: 'API key is not configured.' })
        };
    }

    // 3. Get the data (systemPrompt, userQuery) from the website
    const { systemPrompt, userQuery } = JSON.parse(event.body);

    const googleApiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=${apiKey}`;

    // 4. Construct the payload for the *real* Gemini API
    const payload = {
        contents: [{ parts: [{ text: userQuery }] }],
        systemInstruction: {
            parts: [{ text: systemPrompt }]
        },
    };

    try {
        // 5. Call the Google API from the server
        const response = await fetch(googleApiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const errorData = await response.json();
            return {
                statusCode: response.status,
                body: JSON.stringify({ error: errorData.error?.message || 'Gemini API Error' })
            };
        }

        // 6. Send the successful response back to your website
        const result = await response.json();
        return {
            statusCode: 200,
            body: JSON.stringify(result)
        };

    } catch (error) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: error.message || 'An unknown error occurred.' })
        };
    }
};