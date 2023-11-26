import axios from 'axios';

const FONT_API_URL = 'https://fonts.googleapis.com/css?family=';

const fetchFontCss = (fontName) => {
  const url = `${FONT_API_URL}${fontName}`;
  return axios.get(url);
};

export default fetchFontCss;