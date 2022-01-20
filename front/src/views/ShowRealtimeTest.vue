<template>
<div>
    <h2>数据包实时测量</h2>
    <div style="padding: 10px;">
        <a-row :gutter="16">
            <a-col :span="8" v-for="(name,index) in chart_name" :key="index">
                <a-card  :title="name" :bordered="true" :hoverable="true" :style="{marginBottom:'10px'}">
                    <t-vlan-chart
                        class="Chart"  
                        :chartID="name" 
                        :x_data="x"
                        :y_data="y[index]" 
                        :testcount="testcount" >
                    </t-vlan-chart>
                </a-card>
            </a-col>
        </a-row>
    </div>
</div>
</template>

<script>
import TVlanChart from '../Components/TVlanChart.vue';
export default {
    name:"ShowRealtimeTest",
    components:{TVlanChart},
    data(){
        return{
            chart_name:["All","ARP","IPv4","ICMP","TCP","UDP"],
            y:[],
            x:"",
            testcount:0
        }
        
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

<style scoped>
.Chart{
  display: inline-block;
}
</style>