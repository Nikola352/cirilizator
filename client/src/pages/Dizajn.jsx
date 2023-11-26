export default function Dizajn() {
    const { data: fonts, isPending, error } = useFetch('http://localhost:5000/api/v1/fonts');
    /*
    font = {
        'font_family': string,
        'font_subfamily': string,
        'font_full_name': string,
        'font_postscript_name': string,
    }
     */

    return ( 
        <div>
            <h1>Dizajn</h1>
        </div> 
    );
}
 