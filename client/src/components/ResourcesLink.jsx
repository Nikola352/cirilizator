export default function ResourcesLink(props){
    return(
        <div>
            <h1 className="text-3xl font-thin text-primary-100">{props.title}</h1>
                <ul className="flex flex-row flex-wrap justify-between mt-8">
                    {props.links.map((link) => (
                        <li key={link.id} className="flex flex-row"><p className="text-primary-400">{link.title}</p><a href={link.link} className="link"> {link.name}</a></li>
                    ))}
                </ul>
        </div>
    )
}