/** @type {import('tailwindcss').Config} */
module.exports = {
  content: {
    files: ["./public/**/*.html"],
    // The Hebrew pages carry the compiled stylesheet inlined between these
    // markers. Without stripping it, Tailwind scans its own output as page
    // content and generates extra utilities from tokens inside the CSS.
    transform: {
      html: (content) =>
        content.replace(/<!-- inline-css:start -->[\s\S]*?<!-- inline-css:end -->/g, ''),
    },
  },
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
