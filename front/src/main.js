import Vue from 'vue'
import App from './App'
Vue.config.productionTip = false

// 引入socket.io
import VueSocketIO from 'vue-socket.io'
import echarts from 'echarts'
Vue.prototype.$echarts = echarts
Vue.use(new VueSocketIO({
  debug: false,
  // connection: 'http://10.21.0.148:5000'
  connection:'http://127.0.0.1:5000'
}))

//引入antui
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
Vue.use(Antd)

/* eslint-disable no-new */
new Vue({
  render: h => h(App),
}).$mount('#app')
