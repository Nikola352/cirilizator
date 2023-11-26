import React from "react";
import ResourcesLink from "../components/ResourcesLink";
export default function Resursi() {
    const links_general = [
        {
            id: 1,
            title: "",
            link: "https://latinicaucirilicu.rs/cirilicni-fontovi",
            name: "Листа ћириличних фонтова"
        },
        {
            id: 2,
            title: "",
            link: "https://stickers.viber.com/pages/custom-sticker-packs/11ee77cb2b4dbea4b59cff474b635a44435cad9ec3dc5457",
            name: "Ћириличне вибер налепнице"
        },
    ]

    const links_design = [
        {
            id: 1,
            title: "",
            link: "https://www.unicode.org/charts/PDF/U0400.pdf",
            name: "Листа ћириличних фонтова са преводиоцем"
        },
    ]

    const links_tools = [
        {
            id: 1,
            title: "",
            link: "https://latinicaucirilicu.rs/ispravljanje-celave-latinice",
            name: "Исправљач ћелаве латинице"
        },
        {
            id: 1,
            title: "",
            link: "https://latinicaucirilicu.rs/konvertor-za-word",
            name: "Конвертор за ворд"
        },
        {
            id: 1,
            title: "",
            link: "https://latinicaucirilicu.rs/konvertor-za-excel",
            name: "Конвертор за ексел"
        },


    ]
    return (
        <div>

            <div className="max-w-7xl mx-auto px-4 mt-24 mb-16">
                <h1 className="heading">Ресурси</h1>
            </div>
            <hr />
            <div className="link-section flex gap-24 flex-col mt-8 mb-24 px-4">
                <ResourcesLink title={"Корисни линкови (опште)"} links={links_general}/>
                <ResourcesLink title={"Корисни линкови (дизајн)"} links={links_design}/>
                <ResourcesLink title={"Корисни линкови (алати)"} links={links_tools}/>
            </div>
        </div>
    )
}