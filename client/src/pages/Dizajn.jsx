import React from 'react';
import useFetch from '../hooks/useFetch';
import TextInput from '../components/TextInput';
import { useState } from 'react';

export default function Dizajn() {
    const { data: fonts, isPending, error } = useFetch('http://localhost:5000/api/v1/fonts');
    const [searchTerm, setSearchTerm] = useState("");
    console.log(searchTerm);
    /*
    font = {
        'font_family': string,
        'font_subfamily': string,
        'font_full_name': string,
        'font_postscript_name': string,
    }
     */
     const fontss = [
        {
          font_family: 'Arial',
          font_subfamily: 'Regular',
          font_full_name: 'Arial Regular',
          font_postscript_name: 'Arial-Regular',
        },
        {
          font_family: 'Times New Roman',
          font_subfamily: 'Bold',
          font_full_name: 'Times New Roman Bold',
          font_postscript_name: 'TimesNewRoman-Bold',
        },
        {
          font_family: 'Helvetica',
          font_subfamily: 'Italic',
          font_full_name: 'Helvetica Italic',
          font_postscript_name: 'Helvetica-Italic',
        },
        {
            font_family: 'Helvetica',
            font_subfamily: 'Italic',
            font_full_name: 'Helvetica Italic',
            font_postscript_name: 'Helvetica-Italic',
          },
        // Add more fonts as needed
      ];

    return ( 
        <div>
            <div className="header  my-16 flex flex-row justify-between max-w-[1500px] mx-auto flex-wrap">
                <h1 className="heading md:text-5xl text-3xl w-1/2">Претражите све фонтове:</h1>
                <TextInput type="text"  placeholder="Претражите..." value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
            </div>
            <div className="grid  grid-cols-1 md:grid-cols-2 lg:grid-cols-4 ">
                {fontss && fontss.filter((font) => {
                    if (searchTerm === "") {
                        return font;
                    } else if (font.font_family.toLowerCase().includes(searchTerm.toLowerCase())) {
                        return font;
                    }
                }).map((font, index) => (
                        <a href="/dizajn" key={index}>
                            <div className="font-card flex flex-col h-60 pl-8 justify-center border-[1px] border-black p-4 overflow-hidden">
                                    {/* <h1 className="text-xl text-primary-50">{font.font_subfamily}</h1> */}
                                    {/* font name bellow */}
                                    <h1 className="text-sm text-primary-50">{font.font_full_name}</h1>
                                    <h1 className="lg:text-4xl text-3xl font-regular text-primary-300">{font.font_family}</h1>
                                    <p className="text-md text-primary-50 my-4 pr-2">Магични свет дубоких шума крије 
                                    бројна чуда природе и богатства биолошке разноврсности.</p>
                            </div>
                        </a>
                ))}

            </div>
        </div> 
    );
}
 