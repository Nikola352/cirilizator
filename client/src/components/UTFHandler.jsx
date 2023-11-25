import React, { useState } from 'react';

const UTFHandler = () => {
    const [selectedOption, setSelectedOption] = useState('ai');
    const [inputText, setInputText] = useState('');
    const [outputText, setOutputText] = useState('');

    const handleToggleChange = (event) => {
        setSelectedOption(event.target.value);
    };

    const handleInputChange = (event) => {
        setInputText(event.target.value);
    };

    const handleSubmit = () => {
        if (selectedOption === 'UTFToCyrillic') {
            convertUTFToCyrillic();
        } else if (selectedOption === 'cyrillicToUTF') {
            convertCyrillicToUTF();
        }
    };

    const convertUTFToCyrillic = () => {
        const decodedText = decodeURIComponent(inputText);
        setOutputText(decodedText);
    };

    const convertCyrillicToUTF = () => {
        const encodedText = encodeURIComponent(inputText);
        setOutputText(encodedText);
    };

    return (
        <div>
            <div>
                <label>
                    <input
                        type="radio"
                        value="UTFToCyrillic"
                        checked={selectedOption === 'ai'}
                        onChange={handleToggleChange}
                    />
                    UTF у ћирилицу
                </label>
                <label>
                    <input
                        type="radio"
                        value="cyrillicToUTF"
                        checked={selectedOption === 'local'}
                        onChange={handleToggleChange}
                    />
                    Ћирилица у UTF
                </label>
            </div>
            <div>
        <textarea
            placeholder="Унесите текст за конверзију."
            value={inputText}
            onChange={handleInputChange}
        />
            </div>
            <div>
                <button onClick={handleSubmit}>Конвертуј</button>
            </div>
            <div>
        <textarea
            placeholder="Конвертован текст ће се овде појавити."
            value={outputText}
            readOnly
        />
            </div>
        </div>
    );
};

export default UTFHandler;