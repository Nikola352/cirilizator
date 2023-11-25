import CardFeature from '../components/CardFeature';
import {Typography} from "@material-tailwind/react";
import React from 'react';
import CTA from './CTA';
export default function FeatureSection() {
    const listFeatures = [
        {
            id: 1,
            title: "Дизајн",
            paragraph: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.",
            image: "https://picsum.photos/seed/1/300/200"
        },
        {
            id: 2,
            title: "Ресурси",
            paragraph: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.",
            image: "https://picsum.photos/seed/2/300/200"
        },
        {
            id: 3,
            title: "Магазин",
            paragraph: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.",
            image: "https://picsum.photos/seed/3/300/200"
        },
        {
            id: 4,
            title: "Заједница",
            paragraph: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.",
            image: "https://picsum.photos/seed/4/300/200"
        }
    ]
    const arrowIcon = <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
    strokeWidth={2}
    className="h-4 w-4"
    >
    <path
        strokeLinecap="round"
        strokeLinejoin="round"
        d="M17.25 8.25L21 12m0 0l-3.75 3.75M21 12H3"
    />
    </svg>
    return(
        <div className='max-w-7xl mx-auto '>
            <Typography className="heading mt-24 mb-16 text-primary-100">
                Садржај
            </Typography>
            <div className='flex flex-col gap-8'>
            {listFeatures.map((feature) => (
                
                <CardFeature key={feature.id} title={feature.title} paragraph={feature.paragraph} image={feature.image} />
                ))}
            </div>
            <div className="flex justify-center my-8">
                <CTA text={"Потражите све фонтове"} img={arrowIcon}/>
            </div>

        </div>
    )
}

    