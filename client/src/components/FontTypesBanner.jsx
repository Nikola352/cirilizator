export default function FontTypesBanner() {
    const listFontTypes = [
        {
            id:1,
            title: "Сериф",
            image: "https://assets-global.website-files.com/6262d15e87c1ba75ee7ce234/6264760b0e101413fbe439c8_sans-serif.svg"
        },
        {
            id:2,
            title: "Санс-сериф",
            image: "https://assets-global.website-files.com/6262d15e87c1ba75ee7ce234/6264760b0e101461a5e439c9_serif.svg"
        },
        {
            id:3,
            title: "Скрипт",
            image: "https://assets-global.website-files.com/6262d15e87c1ba75ee7ce234/6264760b0e10143a6de439c6_display.svg"
        },
        {
            id:4,
            title: "Декоративни",
            image: "https://assets-global.website-files.com/6262d15e87c1ba75ee7ce234/6264760b0e10143a6de439c6_display.svg"
        },
        {
            id:5,
            title: "Моно",
            image: "https://assets-global.website-files.com/6262d15e87c1ba75ee7ce234/6264760b0e1014c834e439ca_monospaces.svg"
        },
        {
            id:6,
            title: "Ручно писано",
            image: "https://assets-global.website-files.com/6262d15e87c1ba75ee7ce234/6264760b0e1014a4c7e439c7_handwritingsvg.svg"
        }
    ]
    return(
        <div className="bg-primary min-h-[24rem] hidden xl:block px-8">
            <div className="inner-container max-w-[1500px] mx-auto">
                <div className="flex flex-col text-center justify-center ">
                    <h2 className="text-3xl font-bold text-white my-8 mb-16">Изаберите врсту и претражите</h2>
                    <div className="flex flex-wrap justify-between ">
                        {listFontTypes.map((fontType) => (
                            <div key={fontType.id} className="flex flex-col items-center justify-center w-40 h-40 bg-white rounded-md">
                                <img src={fontType.image} alt="" className="w-20 h-20" />
                                <span className="text-sm  text-primary-100 font-semibold text-center">{fontType.title}</span>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    )
}