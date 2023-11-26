
import Markdown from 'react-markdown';
export default function BlogPost({title, category, thumbnail, description}){
    return(
            <div className="max-w-7xl mx-auto flex justify-center flex-col text-center">
                <h1 className='px-32 text-3xl font-serif'>{title}</h1>
                <h2 className='paragraph px-32 text-xs my-4'>Category: <span className='font-semibold'>{category}</span></h2>
                <img src={thumbnail}  className="w-1/2 mx-auto h-40 object-cover object-center"/>
                <Markdown className="markdown px-24 my-4">{description}</Markdown>
            </div>
    )
}