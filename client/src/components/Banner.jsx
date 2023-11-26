import React from 'react';
import CTA from './CTA';

export default function Banner() {
    return(
        <div className="banner my-24  max-w-[1150px] mx-auto">
            <div className="header-container my-8 ">
                <p className="fontUsed text-primary-100">Poppins</p>
                <h1 className="heading lg:text-[6rem] text-6xl leading-[4rem] lg:leading-[6rem] font-thin">Савети за употребу ћирилице на интернету</h1>
            </div>
            <div className="paragraph-container my-4">
                <p className="fontUsed text-primary-100 my-4">Times-New-Roman</p>
                <p className="paragraph max-w-3xl">Добродошли на сајт који вам пружа корисне 
                савете о правилној употреби ћирилице на интернету. Сазнајте како боље представити 
                ваш садржај користећи ћириличко писмо и како олакшати комуникацију са посетиоцима.</p>
            </div>
            <CTA text="Погледајте" path={"/magazin"} />
        </div>
    )
}