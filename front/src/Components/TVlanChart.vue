<template>
    <div :id="chartID" :style="style"></div>
</template>

<script>
export default {
    name:'TVlanChart',
    data(){
        return{
            chart:""
        }
    },
    sockets:{
        connect:function(){
            console.log("chart component socket连接成功")
        }
    },
    props:{
        testcount:{
            type:Number
        },
        y_data:{
            type:Number
        },
        x_data:{
            type:String
        },
        chartID:{
            type:String,
        },
        width:{
            type:String,
            default:"500px"
        },
        height:{
            type:String,
            default:"500px"
        },
        chartName:{
            type:String
        },
        option:{
            type:Object,
            //Object类型的prop值一定要用函数return出来，不然会报错。原理和data是一样的，
            //使用闭包保证一个vue实例拥有自己的一份props
            default(){
                return{
                    title:{
                        left:"center",
                        text:this.chartName
                    },
                    legend:{
                        show:false,
                        data:[this.chartName],
                    },
                    xAxis:{
                        data:[],
                        axisLabel:{
                            rotate:80,
                            interval:0
                        }
                    },
                    grid:{//Drawing grid in Cartesian coordinate system
                        // show:true,//Whether to display rectangular coordinate grid. [default: false]
                        // left:"20%",//The distance from the grid component to the left of the container.
                        // right:"30px",
                        // borderColor:"#c45455 ",//grid border color
                        bottom:"30%" //
                    },
                    yAxis:{
                        type:"value"
                    },
                    series:[
                        {
                            name:this.chartName,
                            type:"line",
                            data:[],
                            label:{
                                show:true,
                                position:"top",
                                textStyle:{
                                    fontSize:10
                                }
                            }
                        }
                    ]

                }
            }
        }
    },
    computed:{
        style(){
            return {
                height:this.height,
                width:this.width
            }
        }
    },
    methods:{
        updateOption(){
            if(this.option.series[0].data.length==20){
                this.option.series[0].data.shift();
                this.option.xAxis.data.shift();
            }
            this.option.series[0].data.push(this.y_data);
            this.option.xAxis.data.push(this.x_data);
        }
    },
    watch:{
        testcount:{
            handler(newVal){
                if(this.chart){
                    if(newVal){
                        this.updateOption();
                        this.chart.setOption(this.option);
                    }
                    // else{
                    //     console.log(oldVal);
                    // }
                }
                else{
                    this.init()
                }
            },
            deep:true
        }
    },
    mounted(){
        this.chart=this.$echarts.init(document.getElementById(this.chartID));
        this.chart.setOption(this.option);
    }
}
</script>

<style scoped>

</style>