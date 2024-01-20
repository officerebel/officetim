module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://timtvogt.pythonanywhere.com/',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': '/api'
                }
            }
        }
    }
}

//git
