import {useEffect, useState} from "react";
import { Typography } from "@material-tailwind/react";
import CTA from "../components/CTA";
import BlogCard from "../components/BlogCards";
import useFetch from "../hooks/useFetch.js";
import BackendService from "../services/BackendService.js";

export default function Magazin(){
    const [activeBtn, setActiveBtn] = useState(1);
    const handleBtnClick = (buttonId) => {
        setActiveBtn(buttonId);
    }
    const [blogPosts, setBlogPosts] = useState([]);

    useEffect(() => {
        BackendService.getBlogPosts().then((result) => {
            setBlogPosts(result);
        });
    }, []);

    return(
        <div className="max-w-7xl mx-auto my-24">
                <Typography className="heading mt-24 mb-16 ml-4 text-primary-100"> Информације </Typography>
                {/* TODO: dodati kategorije i filtriranje na klik */}
                <div className="sections md:w-1/2 mx-auto flex justify-around items-center gap-8 my-16 flex-wrap w-11/12">
                    <button className={`button-35 ${activeBtn===1 ? 'selected':''}`} onClick={() => handleBtnClick(1)} >All</button>
                    <button className={`button-35 ${activeBtn===2 ? 'selected':''}`} onClick={() => handleBtnClick(2)} >Info</button>
                    <button className={`button-35 ${activeBtn===3 ? 'selected':''}`} onClick={() => handleBtnClick(3)} >Design</button>
                    <button className={`button-35 ${activeBtn===4 ? 'selected':''}`} onClick={() => handleBtnClick(4)} >Marketing</button>
                </div>
                <div className="cards flex max-w-7xl mx-auto flex-row gap-16 flex-wrap justify-around">
                    {blogPosts.map((blog) => (
                        <BlogCard blog={blog} key={blog.id}/>
                        ))}
                </div>
        </div>
    )
}