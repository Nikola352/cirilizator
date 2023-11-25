/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#8338ec',
          50: '#718096',
          100: '#4a5568',
          200: '#2d3748',
          300: '#1a202c',
          400: '#171923',
          500: '#0d131e',
          600: '#0a0f14',
          700: '#070a0f',
          800: '#04070a',
          900: '#010304',
        },
      },
    },
  },
  plugins: [],
}
