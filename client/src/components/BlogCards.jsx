import {
    Card,
    CardHeader,
    CardBody,
    CardFooter,
    Typography,
    Avatar,
    Tooltip,
  } from "@material-tailwind/react";

export default function BlogCard(props){
    return(
        <Card className="max-w-[24rem] overflow-hidden shadow-xl cursor-pointer">
            <CardHeader
                floated={false}
                shadow={false}
                color="transparent"
                className="m-0 rounded-none"
            >
                <img
                src={props.blog.thumbnail}
                alt="ui/ux review check"
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
    )
}