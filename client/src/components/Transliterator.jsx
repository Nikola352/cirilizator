import React, { useState } from 'react';
import BackendService from '../services/BackendService.js';
import { Radio } from "@material-tailwind/react";
import { Textarea } from "@material-tailwind/react";
import CTA from './CTA.jsx';

const Transliterator = () => {
    const [selectedOption, setSelectedOption] = useState('ai');
    const [inputText, setInputText] = useState('');
    const [outputText, setOutputText] = useState('');
    const latinToCyrillicMap = {
        'a': 'а', 'b': 'б', 'c': 'ц', 'č': 'ч', 'ć': 'ћ', 'd': 'д', 'đ': 'ђ',
        'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'х', 'i': 'и', 'j': 'ј', 'k': 'к',
        'l': 'л', 'lj': 'љ', 'm': 'м', 'n': 'н', 'nj': 'њ', 'o': 'о', 'p': 'п',
        'r': 'р', 's': 'с', 'š': 'ш', 't': 'т', 'u': 'у', 'v': 'в', 'z': 'з',
        'ž': 'ж', 'A': 'А', 'B': 'Б', 'C': 'Ц', 'Č': 'Ч', 'Ć': 'Ћ', 'D': 'Д',
        'Đ': 'Ђ', 'E': 'Е', 'F': 'Ф', 'G': 'Г', 'H': 'Х', 'I': 'И', 'J': 'Ј',
        'K': 'К', 'L': 'Л', 'Lj': 'Љ', 'M': 'М', 'N': 'Н', 'Nj': 'Њ', 'O': 'О',
        'P': 'П', 'R': 'Р', 'S': 'С', 'Š': 'Ш', 'T': 'Т', 'U': 'У', 'V': 'В',
        'Z': 'З', 'Ž': 'Ж'
    };

    const handleToggleChange = (event) => {
        setSelectedOption(event.target.value);
    };

    const handleInputChange = (event) => {
        setInputText(event.target.value);
    };

    const handleSubmit = () => {
        console.log("Button clicked!");
        if (selectedOption === 'ai') {
            processTextWithAI();
        } else if (selectedOption === 'local') {
            processTextLocally();
        }
    };

    const processTextWithAI = async () => {
        try {
            setOutputText(await BackendService.transliterateText(inputText));
        } catch (error) {
            console.error('Error when transliterating text with AI:', error);
        }
    };

    const processTextLocally = () => {
        setOutputText(inputText.replace(/(?:lj|nj|dž|[a-zA-ZčćđšžČĆĐŠŽ])/g, function (match) {
            return latinToCyrillicMap[match] || match;
        }));
    };

    return (
        <div >
            <div className='flex flex-row gap-24'>
                <label className='flex flex-row'>
                    <input
                        type="radio"
                        value="ai"
                        checked={selectedOption === 'ai'}
                        onChange={handleToggleChange}
                    />
                    <p className='ml-4 fontUsed text-primary-100'>
                        Вештачка интелигенција
                    </p>
                </label>
                <label className='flex flex-row'>
                    <input
                        type="radio"
                        value="local"
                        checked={selectedOption === 'local'}
                        onChange={handleToggleChange}
                    />
                    <p className='ml-4 fontUsed text-primary-100'>
                        Локално
                    </p>
                </label>
            </div>
            <div>
        <Textarea className='my-4  p-8 w-full h-60 shadow-lg rounded-xl bg-[#f2f2f275]'
            placeholder="Унесите текст на латиници."
            value={inputText}
            onChange={handleInputChange}
        />
            </div>
            <div>
                <button className="button-52  text-white border-2 border-[#0101010]
                    py-4 px-8  my-10" onClick={handleSubmit}>Преведи</button>
                {/* <CTA clickHandler={handleSubmit} text='Транслитерирај'/> */}
            </div>
            <div>
        <Textarea
            className='my-4 w-full  p-8 h-60 shadow-lg rounded-xl bg-[#f2f2f275]'
            placeholder="Транслитериран текст ће се овде појавити."
            value={outputText}
            readOnly
        />
            </div>
        </div>
    );
};

export default Transliterator;