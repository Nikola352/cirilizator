import CardFeature from '../components/CardFeature';
import {Typography} from "@material-tailwind/react";
import React from 'react';
import CTA from './CTA';
export default function FeatureSection() {
    const listFeatures = [
        {
            id: 0,
            title: "Развој",
            paragraph: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.",
            image: "https://assets-global.website-files.com/628803debd8bd01d1d3543bd/628d017c295477e8efed147e_mobile-app-development-course-image-learnbook-webflow-ecommerce-template.png",
            path: "/razvoj"
        },
        {
            id: 1,
            title: "Дизајн",
            paragraph: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.",
            image: "https://assets-global.website-files.com/628803debd8bd01d1d3543bd/628cfcf4fddf44a789dab2ee_brand-and-identity-design-course-image-learnbook-webflow-ecommerce-template.png",
            path: "/dizajn"
        },
        {
            id: 2,
            title: "Ресурси",
            paragraph: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.",
            image: "https://assets-global.website-files.com/628803debd8bd01d1d3543bd/628d02521b85267a2bfcf036_web-design-and-development-course-image-learnbook-webflow-ecommerce-template.png",
            path: "/resursi"
        },
        {
            id: 4,
            title: "Заједница",
            paragraph: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.",
            image: "https://assets-global.website-files.com/628803debd8bd01d1d3543bd/628d0200d1995d672132ffc6_marketing-analytics-course-image-learnbook-webflow-ecommerce-template.png",
            path: "/zajednica"
        },
        {
            id: 3,
            title: "Магазин",
            paragraph: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.",
            image: "https://img.freepik.com/free-vector/flat-design-glossary-illustration_23-2150354390.jpg?w=1380&t=st=1700996621~exp=1700997221~hmac=6ea1f637f91ffa2d62b4878c71497567c389076f7864ba45323ddfde9302e503",
            path: "/magazin"
        },
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
                
                <CardFeature key={feature.id} title={feature.title} paragraph={feature.paragraph} image={feature.image} path={feature.path} />
                ))}
            </div>
            <div className="flex justify-center my-8">
                <CTA text={"Потражите све фонтове"} img={arrowIcon} path={"/dizajn"}/>
            </div>

        </div>
    )
}

    