import React from 'react';
import { ButtonGroup, Button } from "@material-tailwind/react";
import { useState } from 'react';
const TextInput = (props) => {
    const run = (e) => {
        // console.log(e.target.value)
        props.onChange(e)
    };
    if(props.type === 'textarea') {
        return (
            <div className="flex flex-col my-4">
                <label className="label">{props.label}</label>
                <textarea onChange={(e) => run(e)} value={props.value} className='my-4 px-6 py-3 h-60   shadow-lg rounded-xl bg-[#f2f2f275] focus:text-primary focus:outline-primary' placeholder={props.placeholder} />
            </div>
        );
    }
    else if(props.type === 'text'){

        return ( 
            <div className="flex flex-col my-4">
            <label className="label">{props.label}</label>
            <input onChange={(e) => run(e)} value={props.value} className='my-4 px-6 py-3  shadow-lg rounded-xl bg-[#f2f2f275] focus:text-primary focus:outline-primary' type="text" placeholder={props.placeholder} />
        </div>
    );
    }
    else if(props.type === 'dropdown'){
        const [activeBtn, setActiveBtn] = useState(1);
        const handleBtnClick = (buttonId,e) => {
            console.log(buttonId)
            props.onChange(buttonId)
            setActiveBtn(buttonId);
        }
        return (
            <div className="flex flex-col my-4">
                <label className="label">{props.label}</label>
                <ButtonGroup variant="outlined" className='mt-4'>
                    {props.options && props.options.map((option) => (
                        <Button  key={option.value}  value={props.value} className={`button-35 mr-4 text-sm  ${activeBtn===option.value ? 'selected':''}`} onClick={() => handleBtnClick(option.value)}  >
                            {option.label}
                        </Button>
                    ))}
                </ButtonGroup>
            </div>
        );
    }
}
export default TextInput;