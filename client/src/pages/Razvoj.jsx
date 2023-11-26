import React, {useEffect, useState} from "react";
import Transliterator from "../components/Transliterator";
import UTFHandler from "../components/UTFHandler";
import BlogCard from "../components/BlogCards";
import { Typography } from "@material-tailwind/react";
import CTA from "../components/CTA";
import BackendService from "../services/BackendService.js";
export default function Razvoj() {
    const [blogPosts, setBlogPosts] = useState([]);

    useEffect(() => {
        BackendService.getBlogPosts().then((result) => {
            console.log(result);
            setBlogPosts(result.filter((blogPost) => blogPost.category === "info"));
        });
    }, []);
    
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
                {blogPosts.slice(0, 3).map((blog) => (
                    <BlogCard blog={blog} key={blog.key}/>
                    ))}
            </div>
            <div className="btn-container my-8 flex justify-center " >
                <CTA text={"Сви блогови"} path="/magazin" img={null}/>
            </div>
        </div>
    )
}