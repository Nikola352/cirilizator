import { Typography } from "@material-tailwind/react";
export default function Footer() {
    return(
        
    <footer className=" bg-white p-8">
        <hr className="my-8 border-blue-gray-50" />
        <div className="flex flex-row max-w-7xl pb-8 px-4 mx-auto flex-wrap items-center justify-center gap-y-6 gap-x-12 bg-white text-center md:justify-between">
            <Typography
            as="a"
            href="/"
            className="mr-4 cursor-pointer py-1.5 font-medium text-lg text-primary-100"
            >
            Ћирилизатор<span className="text-primary">.</span>
            </Typography>
            <ul className="flex flex-wrap items-center gap-y-2 gap-x-8">
            <li>
            <Typography
                as="a"
                href="/razvoj"
                color="blue-gray"
                className="font-normal transition-colors hover:text-primary focus:text-primary"
            >
                Развој
            </Typography>
            </li>
            <li>
            <Typography
                as="a"
                href="/dizajn"
                color="blue-gray"
                className="font-normal transition-colors hover:text-primary focus:text-primary"
            >
                Дизајн
            </Typography>
            </li>
            <li>
            <Typography
                as="a"
                href="/resursi"
                color="blue-gray"
                className="font-normal transition-colors hover:text-primary focus:text-primary"
            >
                Ресурси
            </Typography>
            </li>
            <li>
            <Typography
                as="a"
                href="/magazin"
                color="blue-gray"
                className="font-normal transition-colors hover:text-primary focus:text-primary"
            >
                Магазин
            </Typography>
            </li>
            <li>
            <Typography
                as="a"
                href="/zajednica"
                color="blue-gray"
                className="font-normal transition-colors hover:text-primary focus:text-primary"
            >
                Заједница
            </Typography>
            </li>
            
        </ul>
        </div>
        <hr className="my-8 border-blue-gray-50" />
        <Typography color="blue-gray" className="text-center font-normal">
        &copy; 2023 Ћирилизатор<span className="text-primary">.</span>
        </Typography>
    </footer>
    )
}
 

