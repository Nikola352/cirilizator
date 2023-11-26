import { useState, useEffect } from "react"

const useFetch = (url) => {
    const [data, setData] = useState(null)
    const [isPending, setIsPending] = useState(true)
    const [error, setError] = useState(null)
    
    useEffect(() => {
        const fetchData = async () => {
            try{
                const res = await fetch(url)
                if(res.ok){
                    const data = await res.json()
                    setData(data)
                    setIsPending(false)
                    setError(null)
                } else{
                    throw Error("Could not fetch data")
                }
            } catch(err){
                setError(err.message)
                setIsPending(false)
            }
        }
        fetchData()
    }, [url]);

    return {data, isPending, error}
}

export default useFetch;