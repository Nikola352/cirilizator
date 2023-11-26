
const TextInput = ({value, setValue, label, name, error=null, required=false, type="text", min, max}) => {
    return ( 
        <div className="text-input relative m-6">
            { type === "textarea" ? (
                <textarea
                    name={name} required={required}
                    placeholder={label}
                    value={value}
                    onChange={(e) => setValue(e.target.value)}
                    className={`text-secondary-600 h-40 text-lg border-secondary-400 border rounded-l
                        focus:outline-none focus:border-primary-500 border-b-2 p-2
                        peer placeholder:text-transparent
                        ${error ? 'border-error': ''}`}
                />
            ) : (
                <input 
                    type={type}
                    name={name} required={required}
                    placeholder={label}
                    value={value} 
                    onChange={(e) => setValue(e.target.value)} 
                    min={min} max={max}
                    className={`text-secondary-600 h-10 text-l
                        focus:outline-none focus:border-primary-500 border-b-2
                        peer placeholder:text-transparent
                        ${error ? 'border-error': ''}`}
                />
                )}
            {label && (
                <label htmlFor={name}
                    className={`absolute left-0 ${type==='textarea' ? '-top-5' : '-top-3.5'} text-secondary-400 text-sm transition-all
                        peer-placeholder-shown:text-base peer-placeholder-shown:top-2
                        ${type==='textarea' ? 'peer-focus:-top-5' : 'peer-focus:-top-3.5'} peer-focus:text-sm
                        pointer-text pointer-events-none`}
                >{label}</label>
            )}
            {error && (
                <p className="text-sm text-error">{error}</p>
            )}
        </div>
    );
}