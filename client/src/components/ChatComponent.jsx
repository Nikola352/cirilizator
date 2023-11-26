import React, { useState, useEffect } from 'react';

const ChatComponent = () => {
    const [messages, setMessages] = useState([]);

    const fetchMessages = async () => {
        try {
            const apiEndpoint = import.meta.env.VITE_API_ENDPOINT;

            if (!apiEndpoint) {
                throw new Error('API endpoint not specified in the environment variables.');
            }
            const response = await fetch(apiEndpoint + 'discord_messages');
            const data = await response.json();
            setMessages(data);
        } catch (error) {
            console.error('Error fetching messages:', error);
        }
    };

    useEffect(() => {
        fetchMessages();
        const intervalId = setInterval(fetchMessages, 5000);

        return () => clearInterval(intervalId);  // Cleanup on component unmount
    }, []);

    return (
        <div>
            <h2>Recent Messages</h2>
            <ul>
                {messages.map((message, index) => (
                    <li key={index}>{message.author}: {message.content}</li>
                ))}
            </ul>
        </div>
    );
};

export default ChatComponent;
