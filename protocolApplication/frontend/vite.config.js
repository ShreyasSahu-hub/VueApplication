import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vitejs.dev/config/
//export default defineConfig({
//  plugins: [vue()],
//})

export default defineConfig(({ command, mode }) => {
        return {
            plugins: [
                vue(),
            ],
            build: {
                emptyOutDir: true,
                outDir: '../static/protocolApplication/vue',
            },
            base: (mode == 'development') ? 'http://localhost:5173/' : '/static/protocolApplication/vue/',
        }
    }
)
