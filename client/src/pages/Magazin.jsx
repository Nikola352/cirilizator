import { useState } from "react";
import { Typography } from "@material-tailwind/react";
import CTA from "../components/CTA";
import BlogCard from "../components/BlogCards";

export default function Magazin(){
    const [activeBtn, setActiveBtn] = useState(1);
    const handleBtnClick = (buttonId) => {
        setActiveBtn(buttonId);
    }
    //TODO: pristupiti bazi dobaviti po kategorijama 2-3 bloga
    //na stranici prikazivati do 9 blogova po kategorijama
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
                    {infoBlogs.map((blog) => (
                        <BlogCard blog={blog} key={blog.key}/>
                        ))}
                </div>
                <div className="btn-container my-8 flex justify-center " >
                    <CTA text={"Сви блогови"}  img={null}/>
                    {/* path="/magazin" izmjenitni path */}
                </div>
        </div>
    )
}