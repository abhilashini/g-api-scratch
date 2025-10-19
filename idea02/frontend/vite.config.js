import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  root: './',
  publicDir: 'public',
  build: {
    outDir: 'dist',
  },
  server: {
    port: 3000,
    open: true,
    // *** NEW PROXY CONFIGURATION ***
    proxy: {
      // Proxy requests starting with '/api' to the Flask server running on port 5000
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        // The rewrite is crucial: it removes the '/api' prefix from the URL 
        // sent to the Flask server (e.g., /api/process-music -> /process-music)
        // Since your Flask routes start with /api, we do NOT need to rewrite, 
        // but we'll include it commented out as a common practice note:
        // rewrite: (path) => path.replace(/^\/api/, '')
      },
    },
    // *** END PROXY CONFIGURATION ***
  },
});