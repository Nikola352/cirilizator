import React, { useState, useEffect } from 'react';
import CTA from './CTA';

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
            <h2 className='heading mb-4'>Придружите нам се на Дискорд серверу:</h2>
            <div className="container">

                
                <ul className='my-4 min-h-[25rem] p-16 border-2 rounded-3xl border-[#1E1F22] bg-primary overflow-hidden '>
                    {messages.map((message, index) => (
                        <li key={index} className='my-2'><span className='font-bold text-xl my-2 text-white'>{message.author}</span >: <span className='text-2xl text-white '>{message.content}</span></li>
                        
                    ))}
                    
                </ul>
                <CTA  path={"https://discord.gg/9MVF4Dkr47"} text={"Уђи у групу"}/>
            </div>
        </div>
    );
};

export default ChatComponent;
