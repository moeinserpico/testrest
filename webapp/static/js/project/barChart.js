$(function () {

function DrawBarChart(xdata)
  {
    data1=[1,2,3,4,5,6,7,8,9,10,11,12];
    data2=[0,0,0,0,0,0,0,0,0,0,0,0];

    console.log(xdata);
    for(var i=0;i<xdata.length;i++)
      {

        //data1.push(xdata.n1[i].month);
        //data2.push(xdata.n1[i].val);

        data2[xdata[i].month-1]=xdata[i].val;
      }

      console.log(xdata);


    var lineData = {
        labels: data1,
        datasets: [
            {
                label: "Example dataset",
                fillColor: "rgba(220,220,220,0.5)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data2
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


    var ctx = document.getElementById("barChart").getContext("2d");
    var myNewChart = new Chart(ctx).Bar(lineData, lineOptions);

}
    var mahsoolBar= function () {
            //alert("312312");
             $.ajax({
               url: "/Dashboard/barChart",

               type: "get",
               dataType: 'json',
               success: function (xpie) {
                 DrawBarChart(xpie);
                //DrawOrderPie(xpie);
                //console.log(xpie.n1[0]);


               }
             });
             return false;
           };
           mahsoolBar();

}


);
