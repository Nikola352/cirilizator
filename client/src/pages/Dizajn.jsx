import React, { useEffect } from 'react';
import useFetch from '../hooks/useFetch';
import TextInput from '../components/TextInput';
import { useState } from 'react';
import FontText from '../components/FontText';
import { convertUnicodeToString } from '../util';

export default function Dizajn() {
    const [fonts, setFonts] = useState(null);
    const [fontsNames, setFontsNames] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try{
                const res = await fetch('http://localhost:5000/api/v1/fonts')
                if(res.ok){
                    const data = await res.json()
                    setFonts(data)
                } else{
                    console.log(err);
                }
            } catch(err){
                console.log(err);
            }
        }
        fetchData()
    }, []);

    useEffect(() => {
        console.log(fonts);
        if(fonts === null) return;
        setFontsNames(fonts.map((font) => {
            return convertUnicodeToString(font.font_family);
        }));
    }, [fonts]);



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

    return ( 
        <div>
            <div className="header  my-16 flex flex-row justify-between max-w-[1500px] mx-auto flex-wrap">
                <h1 className="heading md:text-5xl text-3xl w-1/2">Претражите све фонтове:</h1>
                <TextInput type="text"  placeholder="Претражите..." value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
            </div>
            <div className="grid  grid-cols-1 md:grid-cols-2 lg:grid-cols-4 ">
                {fonts && fonts.filter((font) => {
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
                                    <h1 className="text-sm text-primary-50">
                                        <FontText text={font.font_postscript_name} font={fontsNames[index]} />
                                    </h1>
                                    <h1 className="lg:text-4xl text-3xl font-regular text-primary-300">
                                        <FontText text={font.font_family} font={fontsNames[index]} />
                                    </h1>
                                    <p className="text-md text-primary-50 my-4 pr-2">
                                        <FontText text={"Магични свет дубоких шума крије бројна чуда природе и богатства биолошке разноврсности."}
                                         font={fontsNames[index]} />
                                    </p>
                            </div>
                        </a>
                ))}

            </div>
        </div> 
    );
}
 