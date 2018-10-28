//Flot Pie Chart
$(function() {
var drawPieMahsool=function(xdata){
  console.log("dadsadsa");
console.log(xdata.nakh);
  var data = [{
      label: "نخ",
      data: xdata.nakh,
      color: "#4A76C5",
  }, {
      label: "الیاف",
      data: xdata.alyaf,
      color: "#A4A290",
  }, {
      label: "ضایعات",
      data: xdata.zayeat,
      color: "#150704",
  }];

  var plotObj = $.plot($("#flot-pie-chart"), data, {
      series: {
          pie: {
              show: true
          }
      },
      grid: {
          hoverable: true
      },
      tooltip: true,
      tooltipOpts: {
          content: "%p.0%, %s", // show percentages, rounding to 2 decimal places
          shifts: {
              x: 20,
              y: 0
          },
          defaultTheme: false
      }
  });


}//end of drawing
var MahsoolPie= function () {
        //alert("312312");
         $.ajax({
           url: "/Dashboard/pieMahsool",

           type: "get",
           dataType: 'json',
           success: function (xpie) {
             drawPieMahsool(xpie);
            //DrawOrderPie(xpie);
            //console.log(xpie.n1[0]);


           }
         });
         return false;
       };
       MahsoolPie();





});
