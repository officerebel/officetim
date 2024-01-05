module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'https://sore-book-production.up.railway.app/',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': '/api'
                }
            }
        }
    }
}

//git