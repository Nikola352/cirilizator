import { createContext, useState } from "react";
import useRequest from "./hooks/useRequest";

export const UserContext = createContext(null);

export const UserProvider = ({ children }) => {
    const [currentUser, setCurrentUser] = useState(null);
    const [jwt, setJwt] = useState(null);

    const {sendRequest, isPending, error, result: jwtResult} = useRequest('http://localhost:5000/api/v1/login', 'POST');

    const login = async (username, password) => {
        await sendRequest({username, password});
        if(jwtResult){
            setCurrentUser(username);
            setJwt(jwtResult.access_token);
            localStorage.setItem('jwt', jwtResult.access_token);
        } else {
            setCurrentUser(null);
            setJwt(null);
        }
    }

    const logout = () => {
        setCurrentUser(null);
        setJwt(null);
    }

    return (
        <UserContext.Provider
            value={{
                currentUser,
                jwt,
                login,
                logout,
                isPending,
                error,
            }}
        >
            { children }
        </UserContext.Provider>
    )
}