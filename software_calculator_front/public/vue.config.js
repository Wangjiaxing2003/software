// // const { defineConfig } = require('@vue/cli-service')
// // const path=require('path')
// module.exports = defineConfig({
//   transpileDependencies: true,
//   baseUrl:'',
//   assetsDir:'static',
//   productionSourceMap:false,
//   devServer: {
//     proxy: {
//       '/api': {
//         target: 'http://localhost:5000',
//         changeOrigin: true,
//         pathRewrite: {
//           '/api': ''
//         }
//       }
//     }
//   }
//
//   // devServer: {
//   //   host: true,
//   //   open: true,    //设置服务启动时是否自动打开浏览器
//   //   cors: true,    //允许跨域
//   //   proxy:{
//   //     '/api':{
//   //       target:'http://127.0.0.1:5000',
//   //       changeOrigin:true,//开启代理，允许跨域
//   //       secure:false,// 如果是https接口，需要配置这个参数
//   //       rewrite: (path) => path.replace(/^\/api/, ""),//设置重写路径
//   //     }
//   //   }
//   })


module.exports = {
  devServer: {
    proxy: {
      "/api": {
        target: 'http://localhost:5000',
        changeOrigin: true
      }
    }
  }
}

//})

