import {
    Card,
    CardHeader,
    CardBody,
    Typography,
  } from "@material-tailwind/react";
import {useEffect, useState} from "react";

export default function BlogCard(props) {
    const [imageSrc, setImageSrc] = useState("../assets/default_blog_post_thumbnail.png");

    useEffect(() => {
        console.log("default src: " + imageSrc);
    })
    useEffect(() => {
        // Attempt to load the actual image
        const img = new Image();
        img.onload = () => {
            // If the image is successfully loaded, update the image source
            setImageSrc(props.blog.thumbnail);
            console.log("updated src: ");
        };
        img.src = props.blog.thumbnail;
    }, [props.blog.thumbnail]);

    return(
        <a href={`/blog/${props.key}`}>
            <Card className="max-w-[24rem] overflow-hidden shadow-xl cursor-pointer">
                <CardHeader
                    floated={false}
                    shadow={false}
                    color="transparent"
                    className="m-0 rounded-none"
                >
                    <img
                    src={imageSrc}
                    alt="Blog post thumbnail"
                    // onError={(event) => {
                    //     event.target.src = "../assets/default_blog_post_thumbnail.png";
                    // }}
                    />
                </CardHeader>
                <CardBody className="px-4 py-8">
                    <Typography variant="h4" className="text-primary-100">
                    {props.blog.title}
                    </Typography>
                    <Typography variant="small"  className="mt-3 font-normal text-primary-100">
                    {props.blog.text}
                    </Typography>
                </CardBody>
                
            </Card>
        </a>
    )
}