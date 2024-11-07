import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    open: false, // Prevents Vite from trying to open the browser
    host: true,  // Ensures Vite binds to 0.0.0.0 so it's accessible outside the container
  },
})
