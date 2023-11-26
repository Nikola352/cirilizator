import React from "react";
import ResourcesLink from "../components/ResourcesLink";
export default function Resursi() {
    const links = [
        {
            id:1,
            title: "Више информација о нечему: ",
            link: "https://www.unicode.org/charts/PDF/U0400.pdf",
            name: "milan"
        },
        {
            id:2,
            title: "Више информација о нечему: ",
            link: "https://www.unicode.org/charts/PDF/U0400.pdf",
            name: "milan"
        },
        {
            id:3,
            title: "Више информација о нечему: ",
            link: "https://www.unicode.org/charts/PDF/U0400.pdf",
            name: "sdfsdf"
        }
    ]
    return (
        <div>

            <div className="max-w-7xl mx-auto px-4 mt-24 mb-16">
                <h1 className="heading">Ресурси</h1>
            </div>
            <hr />
            <div className="link-section flex gap-24 flex-col mt-8 mb-24 px-4">
                <ResourcesLink title={"Корисцни линкови дизајн"} links={links}/>
                <ResourcesLink title={"Корисцни линкови дизајн"} links={links}/>
            </div>
        </div>
    )
}