import React, { useCallback, useEffect } from 'react';
import CTA from './CTA';
import { convertUnicodeToString } from '../util';
import FontText from './FontText';
import fetchFontCss from '../services/FontsService';

export default function Banner() {
    const [titleFont, setTitleFont] = React.useState("Popins");
    const [paragraphFont, setParagraphFont] = React.useState("Times New Roman");

    const fetchFonts = useCallback(async () => {
        try{
            const res = await fetch('http://localhost:5000/api/v1/fonts/pair')
            if(res.ok){
                const data = await res.json()
                setTitleFont(convertUnicodeToString(data.font.font_family));
                setParagraphFont(convertUnicodeToString(data.matching.font_family));
            } else{
                console.log(err);
            }
        } catch(err){
            console.log(err);
        }
    }, []);
    
    useEffect(() => {
        fetchFonts();
    }, [fetchFonts]);

    useEffect(() => {
        fetchFontCss(titleFont);
    }, [titleFont]);

    useEffect(() => {
        fetchFontCss(paragraphFont);
    }, [paragraphFont]);

    return(
        <div className="banner my-24  max-w-[1150px] mx-auto">
            <div className="header-container my-8 ">
                <p className="fontUsed text-primary-100">
                    <FontText text={titleFont} font={titleFont} />
                </p>
                <h1 className="heading lg:text-[6rem] text-6xl leading-[4rem] lg:leading-[6rem] font-thin">
                    <FontText text={'Савети за употребу ћирилице на интернету'} font={titleFont} />
                </h1>
            </div>
            <div className="paragraph-container my-4">
                <p className="fontUsed text-primary-100 my-4">
                    <FontText text={paragraphFont} font={paragraphFont} />
                </p>
                <p className="paragraph max-w-3xl">
                    <FontText 
                        text={'Добродошли на сајт који вам пружа корисне савете о правилној употреби ћирилице на интернету. Сазнајте како боље представити ваш садржај користећи ћириличко писмо и како олакшати комуникацију са посетиоцима.'}
                        font={paragraphFont} 
                    />
                </p>
            </div>
            <CTA text="Погледајте" handleSubmit={fetchFonts} />
        </div>
    )
}