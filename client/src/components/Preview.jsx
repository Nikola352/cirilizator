import React from 'react';
// import {Markup} from 'react-render-markup';
import Markdown from 'react-markdown';

export default function Preview({title, category, image, description}){
    const descriptionString = typeof description === 'object' ? JSON.stringify(description) : description;
    const categoryName = category === '1' ? 'Info' : category === '2' ? 'Dizajn' : 'Resursi';
    console.log(descriptionString)
    return(
        <div className="w-[90%] mx-auto flex justify-center flex-col">
            <h1 className='px-32 text-3xl font-serif'>{title}</h1>
            <h2 className='paragraph px-32 text-xs my-4'>Category: <span className='font-semibold'>{categoryName}</span></h2>
            <img src={image}  className="w-full h-40 object-cover object-center"/>
            <Markdown className="markdown px-24 my-4">{description}</Markdown>

        </div>
    )
}