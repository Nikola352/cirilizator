import {
    Card,
    CardHeader,
    CardBody,
    Typography,
    Button,

  } from "@material-tailwind/react";
export default function CardFeature(props) {
    return (
        
        <a href={props.path}>
        <Card className="w-full  max-w-7xl 
            card mx-auto sm:flex-row flex-col shadow-xl">
            <CardBody className="my-8 pr-8">
                <Typography variant="h1"  className="mb-8 text-primary-100 uppercase text-xl ">
                {props.title}
                </Typography>
                <Typography color="gray" className="mb-4 text-sm font-normal text-primary-100">
                {props.paragraph}
                </Typography>
                <a href={props.path} className="inline-block">
                <Button variant="text" className="flex mb-4 p-0 items-center gap-2 text-primary">
                    Learn More
                    <svg
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
                </Button>
                </a>
            </CardBody>
            <CardHeader
                shadow={false}
                floated={false}
                className="m-0 w-full sm:w-4/5 max-h-72"
            >
                <img
                src={props.image}
                alt="card-image"
                className="h-full w-full object-cover "
                />
            </CardHeader>

                
            
        </Card>
            </a>
    );
}
