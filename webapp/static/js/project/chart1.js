$(function () {

function DrawLineChart(xdata)
  {
    data1=[1,2,3,4,5,6,7,8,9,10,11,12];
    data2=[0,0,0,0,0,0,0,0,0,0,0,0];//bedehkar
    data3=[0,0,0,0,0,0,0,0,0,0,0,0];//bestankar
    console.log(xdata.n1[0]);
    for(var i=0;i<xdata.n1.length;i++)
      {

        //data1.push(xdata.n1[i].month);
        //data2.push(xdata.n1[i].val);

        data2[xdata.n1[i].month-1]=xdata.n1[i].val;
      }
      for(var i=0;i<xdata.n2.length;i++)
        {

          data3[xdata.n2[i].month-1]=xdata.n2[i].val;
        }
      console.log(xdata);


    var lineData = {
        labels: data1,
        datasets: [
            {
                label: "Example dataset",
                fillColor: "rgba(220, 20, 60,1)",
                strokeColor: "rgba(220, 20, 60, 0.7)",
                pointColor: "rgba(220, 20, 60, 1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220, 20, 60, 1)",
                data: data2
            },
            {
                label: "Example dataset",
                fillColor: "rgba(30, 144, 255, 1)",
                strokeColor: "rgba(30, 144, 255, 0.7)",
                pointColor: "rgba(30, 144, 255, 1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(30, 144, 255, 1)",
                data: data3
            }
        ]
    };

    var lineOptions = {
        scaleShowGridLines: true,
        scaleGridLineColor: "rgba(0,0,0,.05)",
        scaleGridLineWidth: 1,
        bezierCurve: true,
        bezierCurveTension: 0.4,
        pointDot: true,
        pointDotRadius: 4,
        pointDotStrokeWidth: 1,
        pointHitDetectionRadius: 20,
        datasetStroke: true,
        datasetStrokeWidth: 2,
        datasetFill: true,
        responsive: true,
    };


    var ctx = document.getElementById("lineChart").getContext("2d");
    var myNewChart = new Chart(ctx).Line(lineData, lineOptions);

}
    var hazineDaramadLine= function () {
            //alert("312312");
             $.ajax({
               url: "/Dashboard/lineChart",

               type: "get",
               dataType: 'json',
               success: function (xpie) {
                 DrawLineChart(xpie);
                //DrawOrderPie(xpie);
                //console.log(xpie.n1[0]);


               }
             });
             return false;
           };
           hazineDaramadLine();

}


);
