/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/**/*.html"],
  theme: {
    extend: {
      fontFamily: { sans: ['Rubik', 'sans-serif'] },
      colors: {
        primary: '#1E3A5F',
        accent: '#4A6FA5',
        surface: '#F8FAFC',
        alt: '#F1F5F9',
      }
    }
  },
  plugins: [],
}
