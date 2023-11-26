
import Markdown from 'react-markdown';
import {useEffect, useState} from "react";
import { useLocation } from "react-router-dom";

export default function BlogPost() {
    const location = useLocation();
    const [blog, setBlog] = useState(location.state?.blog || {});

    useEffect(() => {
        setBlog(location.state?.blog || {});
    }, [location.state]);

    return(
            <div className="max-w-7xl mx-auto flex justify-center flex-col text-center">
                <h1 className='px-32 text-3xl font-serif'>{blog.title}</h1>
                <h2 className='paragraph px-32 text-xs my-4'>Категорија: <span className='font-semibold'>{blog.category}</span></h2>
                <img src={blog.thumbnail}  className="w-1/2 mx-auto h-40 object-cover object-center" alt="Blog post thumbnail"/>
                <Markdown className="markdown px-24 my-4">{blog.description}</Markdown>
            </div>
    )
}