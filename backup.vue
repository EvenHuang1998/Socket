
// export default {
//   name:'app',
//   data() {
//     return {
//       msg: "",
//       log_list: [],
//       i:[]
//     };
//   },
//   sockets: {
//     connect: function () {
//       console.log("socket 连接成功");
//     },
//     message: function (val) {
//       console.log("返回:" + val);
//       this.log_list.push(val);
//     },
//     new_data:function(val){
//       if(this.i.length==10){
//         this.i.splice(0,this.i.length);
//       }
//       this.i.push(val.data);
//     }
//   },
//   mounted() {
//     this.drawLine()
//   },
//   methods: {
//     drawLine(){
//       let myChart=echarts.init(document.getElementById("myChart"))
//       title:{
//         text:'折线图堆叠'
//       }
//       tooltip:{
//         trigger:'axis'
//       }

//     }
//   },
// };

// APP Backup
< template >
    <div id='myChart' :style="{width:'1000px',height:'300px'}"></div>
</template >

 
<script>

  // var echarts = require('echarts');
  export default{
    data() {
      return {
      //echarts实例
        chart: "",
        result:[],
        count:1,
        option:{
          title:{
            text:'Vue-Echarts'
          },
          legend:{
            data:['val']
          },
          xAxis:{
            data:[]
          },
          yAxis:[
            {
              type: "value"
            }
          ],
          series: [
            {
              name: "val",
              type: "line",
              // data: [1,2,3,5,6]
              data:[]
            }
          ]
        }
      }
    },
    sockets: {
      connect: function () {
        console.log("socket 连接成功");
      },
      newdata:function(val){
        this.count+=1;
        if(this.option.series[0].data.length==20){
          this.option.series[0].data.shift();
          this.option.xAxis.data.shift();
        }
        this.option.series[0].data.push(val.data);
        this.option.xAxis.data.push(this.count);
        // this.option.series[0].data=val.data
      }
    },
    methods:{
        init(){
            this.chart = this.$echarts.init(document.getElementById('myChart'));
            this.chart.clear();//如果图表有修改需求建议加上此方法先清后画
            this.chart.setOption(this.option);
        }
    },
    watch:{
      option:{
        handler(newVal,oldVal){
          if(this.chart){
            if(newVal){
              // this.chart.clear();
              this.chart.setOption(newVal);
            }
            else{
              // this.chart.clear();
              this.chart.setOption(oldVal);
            }
          }
          else{
            this.init()
          }
        },
        deep:true
      }
    },
    mounted(){
        this.init();
    }
  }
</script>
 
<style>
/* #myChart{
  margin: ;
} */
</style>