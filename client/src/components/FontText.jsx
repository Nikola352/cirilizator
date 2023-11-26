import React from 'react';

const FontText = ({ text, font }) => {
  const style = {
    fontFamily: font,
  };

  return <span style={style}>{text}</span>;
};

export default FontText;