import { useState, useContext } from "react";
import { UserContext } from "../UserContext";

const useRequest = (url, method) => { 
    const [isPending, setIsPending] = useState(false);
    const [error, setError] = useState(null);
    const [result, setResult] = useState(null);
    const [sentData, setSentData] = useState(null);
    
    const sendRequest = async (data) => {
        setIsPending(true);
        const jwt = localStorage.getItem("jwt");
        try{
            setSentData(data);
            let res = await fetch(url, {
                method: method,
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + jwt,
                },
                body: JSON.stringify(data)
            });
            if(res.ok){
                setResult(await res.json());
                setError(null);
            } else {
                setResult(null);
                setError(null);
            }
        } catch(err){
            console.log(err);
            setError(err.message);
        } finally{
            setIsPending(false);
        }
    }

    return { sendRequest, isPending, error, result, sentData }
}

export default useRequest;