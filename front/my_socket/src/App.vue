<template>
    <div id='app'>

      <t-vlan-chart v-for="(name,index) in chart_name" 
                    class="Chart"
                    :key="index" 
                    :chartID="name" 
                    :x_data="x"
                    :y_data="y[index]"
                    :testcount="testcount" 
                    :chartName="name">
      </t-vlan-chart>
    </div>
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
      testcount:0
    }
  },
  component:{
    TVlanChart
  },
  sockets: {
    connect: function () {
      console.log("socket 连接成功");
    },
    newdata:function(val){
      this.testcount=(this.testcount+1)%1000
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
</style>