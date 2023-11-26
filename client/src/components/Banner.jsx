import React from 'react';
import CTA from './CTA';

export default function Banner() {
    return(
        <div className="banner my-24  max-w-[1150px] mx-auto">
            <div className="header-container my-8 ">
                <p className="fontUsed text-primary-100">Poppins</p>
                <h1 className="heading text-[7rem] font-thin">Погледајте шта знамо</h1>
            </div>
            <div className="paragraph-container my-4">
                <p className="fontUsed text-primary-100 my-4">Times-New-Roman</p>
                <p className="paragraph max-w-3xl">Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Consequuntur earum nostrum eos optio ea nam ducimus 
                    repellendus, aut voluptatibus quam inventore esse 
                    quos fuga, explicabo eius excepturi id rerum. Veniam?</p>
            </div>
            <CTA text="Погледајте" />
        </div>
    )
}