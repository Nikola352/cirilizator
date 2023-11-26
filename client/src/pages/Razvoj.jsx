import React from "react";
import Transliterator from "../components/Transliterator";
import UTFHandler from "../components/UTFHandler";
import BlogCard from "../components/BlogCards";
import { Typography } from "@material-tailwind/react";
import CTA from "../components/CTA";
export default function Razvoj(){
    //TODO: pristupiti bazi dobaviti po kategorijama 2-3 bloga
    const infoBlogs = [
        {
            key: 1,
            title: "Cao",
            text: "ldsfsldfk slskdf;l kssldkfsl",
            category: "Info",
            thumbnail: "https://assets-global.website-files.com/628803debd8bd01d1d3543bd/628d02cf335abecbf83361d4_graphic-design-101-course-image-learnbook-webflow-ecommerce-template-p-500.png"
        },
        {
            key: 2,
            title: "Cao",
            text: "ldsfsldfk slskdf;l kssldkfsl",
            category: "Info",
            thumbnail: "https://assets-global.website-files.com/628803debd8bd01d1d3543bd/628d02cf335abecbf83361d4_graphic-design-101-course-image-learnbook-webflow-ecommerce-template-p-500.png"
        },
        {
            key: 3,
            title: "Cao",
            text: "ldsfsldfk slskdf;l kssldkfsl",
            category: "Info",
            thumbnail: "https://assets-global.website-files.com/628803debd8bd01d1d3543bd/628d02cf335abecbf83361d4_graphic-design-101-course-image-learnbook-webflow-ecommerce-template-p-500.png"
        }
    ]
    
    return(
        <div className="razvoj">
            <div className='my-24  max-w-[1150px] mx-auto'>
                <Transliterator />
                <div className="container my-32">
                    <UTFHandler />
                </div>
                <Typography className="heading mt-24 mb-16 text-primary-100"> Информације </Typography>
                
            </div>
            <div className="cards flex max-w-7xl mx-auto flex-row gap-16">
                {infoBlogs.map((blog) => (
                    <BlogCard blog={blog} key={blog.key}/>
                    ))}
            </div>
            <div className="btn-container my-8 flex justify-center " >
                <CTA text={"Сви блогови"} path="/magazin" img={null}/>
            </div>
        </div>
    )
}