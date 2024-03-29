import React from "react";
export default function CTA(props) {
  const run = () => {
    props.handleSubmit()
  };
  
  return (
    <div >
      <a href={props.path} className="inline-block">
        <button onClick={run}
        className="CTA button-52 text-white border-2 border-[#0101010]
        py-4 px-8  my-10 flex flex-row items-center gap-4">
          {props.text}{props.img}</button>
        </a>
    </div>
  );
}