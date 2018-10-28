//Flot Pie Chart
$(function() {
var drawLineHazine=function(xdata){
  console.log("azizam");
  console.log(xdata[0].month);
  data1=[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0]]
  for(var i=0;i<xdata.length;i++)
  {
    data1[xdata[i].month-1][1]=xdata[i].val;
  }

  var barOptions = {
       series: {
           lines: {
               show: true,
               lineWidth: 2,
               fill: true,
               fillColor: {
                   colors: [{
                       opacity: 0.0
                   }, {
                       opacity: 0.0
                   }]
               }
           }
       },
       xaxis: {
           tickDecimals: 0
       },
       colors: ["#ff0000"],
       grid: {
           color: "#999999",
           hoverable: true,
           clickable: true,
           tickColor: "#D4D4D4",
           borderWidth:0
       },
       legend: {
           show: false
       },
       tooltip: true,
       tooltipOpts: {
           content: "x: %x, y: %y"
       }
   };

   var barData = {
       label: "bar",
       data: data1
   };
   $.plot($("#flot-line-chart"), [barData], barOptions);
  }
  var HazineLine= function () {
          //alert("312312");
           $.ajax({
             url: "/Dashboard/lineHazine",

             type: "get",
             dataType: 'json',
             success: function (xpie) {
               drawLineHazine(xpie);
              //DrawOrderPie(xpie);
              //console.log(xpie.n1[0]);


             }
           });
           return false;
         };
         HazineLine();





  ;
});


//end of drawing
