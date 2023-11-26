import {
    Card,
    CardHeader,
    CardBody,
    CardFooter,
    Typography,
    Input,
    Checkbox,
    Button,
  } from "@material-tailwind/react";
export default function Login(){
    return(
        <div className="container">
            <Card className=" shadow-xl mx-auto flex flex-col justify-center items-center w-[27rem]">
                <CardHeader
                    variant="gradient"
                    className="mb-4 grid h-28 place-items-center bg-primary w-96 "
                >
                    <Typography variant="h3" color="white">
                    Sign In
                    </Typography>
                </CardHeader>
                <CardBody className="flex flex-col gap-4 ">
                    <label className='text-primary-100 font-light'>E-пошта</label>
                    <Input  size="lg" className='my-4  p-6 w-96   shadow-lg rounded-xl bg-[#f2f2f275]'
                    placeholder="Унесите e-пошту."
                     />
                    <label className='text-primary-100 font-light'>Шифра</label>
                    <Input  size="xl" className='my-4  p-6  w-96  shadow-lg rounded-xl bg-[#f2f2f275]'
                    placeholder="Унесите шифру." />
                    
                </CardBody>
                <CardFooter className="pt-0">
                    <Button className="hover:bg-primary w-96 py-4 rounded-xl bg-white border-primary border-2 text-primary hover:text-white" fullWidth>
                    Sign In
                    </Button>
                    <Typography variant="small" className="mt-6 flex justify-center">
                    Don&apos;t have an account?
                    <Typography
                        as="a"
                        href="#signup"
                        variant="small"
                        className="ml-1 font-bold text-primary"
                    >
                        Sign up
                    </Typography>
                    </Typography>
                </CardFooter>
            </Card>
        </div>
    )
}