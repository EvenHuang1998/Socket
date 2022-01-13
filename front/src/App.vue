<template>

  <a-layout id="components-layout-demo-top-side-2">
    <a-layout-header class="header">
      <h2 class="title">测量系统展示平台</h2>
      <!-- <a-menu theme="dark" mode="horizontal" :default-selected-keys="['1']" :style="{ lineHeight: '64px' }">
        <a-menu-item key="1">
          nav 1
        </a-menu-item>
        <a-menu-item key="2">
          nav 2
        </a-menu-item>
        <a-menu-item key="3">
          nav 3
        </a-menu-item>
      </a-menu> -->
    </a-layout-header>
    <a-layout>
      <a-layout-sider width="200" style="background: #fff">
        <a-menu mode="inline" :default-selected-keys="['1']" :default-open-keys="['sub1']"
          :style="{ height: '100%', borderRight: 0 }">
          <a-sub-menu key="sub1">
            <span slot="title">
              <a-icon type="user" />subnav 1
            </span>
            <a-menu-item key="1">
              option1
            </a-menu-item>
            <a-menu-item key="2">
              option2
            </a-menu-item>
            <a-menu-item key="3">
              option3
            </a-menu-item>
            <a-menu-item key="4">
              option4
            </a-menu-item>
          </a-sub-menu>
          <a-sub-menu key="sub2">
            <span slot="title">
              <a-icon type="laptop" />subnav 2
            </span>
            <a-menu-item key="5">
              option5
            </a-menu-item>
            <a-menu-item key="6">
              option6
            </a-menu-item>
            <a-menu-item key="7">
              option7
            </a-menu-item>
            <a-menu-item key="8">
              option8
            </a-menu-item>
          </a-sub-menu>
          <a-sub-menu key="sub3">
            <span slot="title">
              <a-icon type="notification" />subnav 3
            </span>
            <a-menu-item key="9">
              option9
            </a-menu-item>
            <a-menu-item key="10">
              option10
            </a-menu-item>
            <a-menu-item key="11">
              option11
            </a-menu-item>
            <a-menu-item key="12">
              option12
            </a-menu-item>
          </a-sub-menu>
        </a-menu>
      </a-layout-sider>
      <a-layout style="padding: 0 24px 24px">
        <a-layout-content :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '280px',minWidth:'1500px' }">
          <h2>数据包实时测量</h2>
          <div style="padding: 10px;">
            <a-row :gutter="16">
              <a-col :span="8" v-for="(name,index) in chart_name" :key="index">
                <a-card  :title="name" :bordered="true" :hoverable="true" :style="{marginBottom:'10px'}">
                  <t-vlan-chart  class="Chart"  :chartID="name" :x_data="x"
                    :y_data="y[index]" :testcount="testcount" >
                  </t-vlan-chart>
                </a-card>
              </a-col>
            </a-row>
          </div>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-layout>

        

</template>

 
<script>
import TVlanChart from './Components/TVlanChart.vue';
export default{
  name:"App",
  components: { TVlanChart },
  data(){
    return {
      chart_name:["All","ARP","IPv4","ICMP","TCP","UDP"],
      y:[],
      x:"",
      testcount:0,
      collapsed:false
    }
  },
  component:{
    TVlanChart
  },
  sockets: {
    connect: function () {
      console.log("socket连接成功");
    },
    newdata:function(val){
      this.testcount=(this.testcount+1)%1000
      // console.log('got new data');
      this.x=new Date().toLocaleString();
      this.y=val.data;
    }
  }
}
</script>
 
<style>
.Chart{
  display: inline-block;
}


.title {
  /* width: 180px; */
  color: white;
  /* height: 31px; */
  /* background: rgba(255, 255, 255, 0.2); */
  /* margin: 0 24px 8px 0; */
  padding: 0 20px;
  float: left;
}
</style>