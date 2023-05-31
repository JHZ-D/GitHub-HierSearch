module.exports = {
  devServer: {
    open: true,
    proxy: {
      '/api': {
        // target: 'http://localhost:3001', // 接口域名
        target: 'http://162.105.16.191:5000',
        changeOrigin: true, // 是否跨域
        ws: true, // 是否代理 websockets
        pathRewrite: { // 路径重置
          '^/api': ''
        }
      }
    }
  }
}
