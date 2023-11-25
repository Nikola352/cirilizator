import React, { useState } from 'react';

const UTFHandler = () => {
    const [selectedOption, setSelectedOption] = useState('UTFToCyrillic');
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
            <div className='flex flex-row gap-24'>
                <label className='flex flex-row'>
                    <input
                        type="radio"
                        value="UTFToCyrillic"
                        checked={selectedOption === 'UTFToCyrillic'}
                        onChange={handleToggleChange}
                    />
                    <p className='ml-4 fontUsed text-primary-100'>

                        UTF у ћирилицу
                    </p>
                </label>
                <label className='flex flex-row'>
                    <input
                        type="radio"
                        value="cyrillicToUTF"
                        checked={selectedOption === 'cyrillicToUTF'}
                        onChange={handleToggleChange}
                    />
                    <p className='ml-4 fontUsed text-primary-100'>
                        Ћирилица у UTF
                    </p>
                </label>
            </div>
            <div>
        <textarea className='my-4  px-8 pt-6 w-2/3  shadow-lg rounded-xl bg-[#f2f2f275]'
            placeholder="Унесите текст за конверзију."
            value={inputText}
            onChange={handleInputChange}
        />
            </div>
            <div>
                
            </div>
            <div>
        <textarea className='my-4  px-8 pt-6 w-2/3   shadow-lg rounded-xl bg-[#f2f2f275]'
            placeholder="Конвертован текст ће се овде појавити."
            value={outputText}
            readOnly
        />
            </div>
        <button className="button-52  text-white border-2 border-[#0101010]
                    py-4 px-8  my-10" onClick={handleSubmit}>Конвертуј</button>
        </div>
    );
};

export default UTFHandler;