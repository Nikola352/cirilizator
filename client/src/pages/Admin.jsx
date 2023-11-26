import React from 'react';
import TextInput from '../components/TextInput';
import CTA from '../components/CTA';
import { useState } from 'react';
import DialogComponent from '../components/DialogComponent';
import Preview from '../components/Preview';


export default function Admin() {
    const [open, setOpen] = useState(false);
    const [error, setError] = useState(true);
    const [errors, setErrors] = useState({});

    const [title, setTitle] = useState("");
    const [category, setCategory] = useState("");
    const [image, setImage] = useState("");
    const [description, setDescription] = useState("");

    const options = [
        {
            label: 'Info',
            value: '1'
        },
        {
            label: 'Dizajn',
            value: '2'
        },
        {
            label: 'Resursi',
            value: '3'
        }
    ];
    const handleSubmit = () => {
        if(title === "" || category === "" || image === "" || description === ""){
            setErrors({
                title: title === "" ? "Наслов је обавезан" : null,
                category: category === "" ? "Категорија је обавезна" : null,
                image: image === "" ? "Слика је обавезна" : null,
                description: description === "" ? "Опис је обавезан" : null,
            })
            setError(true);
            return;
        }
        else{
            setErrors({
                title: null,
                category: null,
                image: null,
                description: null,
            })
            setError(false);
            setOpen(!open);
        }
        
        // setOpen(!open);
    }
    const successMessage = "Успешно сте креирали нови блог!"
    const errorMessage = "Дошло је до грешке приликом креирања новог блога!"
    return(
        <div className='max-w-[1500px] mx-auto px-4 my-16'>
            <h1 className="heading">Креирај нови блог:</h1>
            <div className="flex flex-wrap flex-row  justify-between gap-4">
                <div className="inputs  max-w-[700px] w-full">
                    <TextInput label="Наслов" placeholder="Унесите наслов" type="text" value={title} onChange={(e) => setTitle(e.target.value)} />
                    {errors.title && <p className="text-red-500 text-sm">{errors.title}</p>}
                    <TextInput label="Категорија" placeholder="Унесите категорију" type="dropdown" options={options} value={category} onChange={(id) => setCategory(id)}/>
                    {errors.category && <p className="text-red-500 text-sm">{errors.category}</p>}
                    <TextInput label="Слика" placeholder="Унесите слику" type="text" value={image} onChange={(e) => setImage(e.target.value)}/>
                    {errors.image && <p className="text-red-500 text-sm">{errors.image}</p>}
                    <TextInput label="Опис" placeholder="Унесите опис" type="textarea" value={description} onChange={(e) => setDescription(e.target.value)} />
                    {errors.description && <p className="text-red-500 text-sm">{errors.description}</p>}
                    <div className="btn-container block">
                        <CTA text={"Сачувај"} handleSubmit={handleSubmit} img={null}/>
                    </div>

                </div>
                
                <div className="preview flex flex-col items-center w-full lg:w-1/2 shadow-xl ml-4">
                    <h1 className='text-3xl text-primary-50 mb-16'>Preview</h1>
                    <Preview title={title} category={category} image={image} description={description}/>
                </div>
                <DialogComponent open={open} setOpen={setOpen} handleSubmit={handleSubmit} text={errorMessage} error={error}/>





                
            </div>
        </div>
    )
}