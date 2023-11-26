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
import { useContext, useEffect, useState } from "react";
import DialogComponent from "../components/DialogComponent";
import { UserContext } from "../UserContext";

export default function Login(){

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const [open, setOpen] = useState(false);
    const [errorMessage, setErrorMessage] = useState("Морате унети корисничко име и шифру!");

    const { login, isPending, error, currentUser: currUser } = useContext(UserContext);

    const handleSubmit = (e) => {
        e.preventDefault();
        if(username == "" || password == ""){
            setErrorMessage("Морате унети корисничко име и шифру!");
            setOpen(true);
            return;
        }
        login(username, password);
    }

    useEffect(() => {
        console.log(error, currUser, isPending);
        if(error){
            setErrorMessage("Погрешно корисничко име или шифра!");
            setOpen(true);
        } else if(currUser && !isPending){
            window.location.href = "/admin";
        }
    }, [error, currUser, isPending]);

    return(
        <form className="container" onSubmit={handleSubmit}>
            <Card className=" shadow-xl mx-auto flex flex-col justify-center items-center w-[27rem]">
                <CardHeader
                    variant="gradient"
                    className="mb-4 grid h-28 place-items-center bg-primary w-96 "
                >
                    <Typography variant="h3" color="white">
                    Пријава
                    </Typography>
                </CardHeader>
                <CardBody className="flex flex-col gap-4 my-4">
                    <label className='text-primary-100 font-light pt-4'>Корисничко име</label>
                    <Input  size="lg" className='my-4  p-6 w-[23rem]  mt-0  shadow-lg rounded-xl bg-[#f2f2f275]'
                    placeholder="Унесите корисничко име."
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                     />
                    <label className='text-primary-100 font-light pt-4'>Шифра</label>
                    <Input type="password" size="lg" className='my-4  p-6 w-96 mt-0  shadow-lg rounded-xl bg-[#f2f2f275]'
                    placeholder="Унесите шифру."
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                     />
                    
                </CardBody>
                <CardFooter className="pt-0">
                    <Button type="submit" className="hover:bg-primary w-96 py-4 rounded-xl bg-white border-primary border-2 text-primary hover:text-white" fullWidth>
                    Пријави се
                    </Button>
                </CardFooter>
            </Card>

            <DialogComponent open={open} setOpen={setOpen} handleSubmit={() => setOpen(false)} text={errorMessage} error={true}/>
        </form>
    )
}