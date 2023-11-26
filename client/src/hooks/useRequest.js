import { useState } from "react";

const useRequest = (url, method) => { 
    const [isPending, setIsPending] = useState(false);
    const [error, setError] = useState(null);
    const [result, setResult] = useState(null);
    const [sentData, setSentData] = useState(null);
    
    const sendRequest = async (data) => {
        setIsPending(true);
        try{
            setSentData(data);
            fetch(url, {
                method: method,
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(data)
            }).then(res => {
                if(res.ok){
                    setResult(res.json());
                    setError(null);
                } else{
                    throw Error("Could not write data");
                }
            });
        } catch(err){
            setError(err.message);
        } finally{
            setIsPending(false);
        }
    }

    return { sendRequest, isPending, error, result, sentData }
}

export default useRequest;