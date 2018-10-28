
$(function () {


 var getAmar=function(id)
 {
   $.ajax({
     url: '/Amar/Rep/'+id+'/Get',

     type: 'GET',
     dataType: 'json',
     success: function (data) {
       if (data.form_is_valid) {
         //alert("Company created!");  // <-- This is just a placeholder for now for testing
         $("#tbody_company").empty();
         $("#tbody_company").html(data.html_amar_list);
         $("#modal-company").modal("hide");
        // console.log(data.html_amar_list);
       }
       else {


       }
     }
   });
 }





 $("input[name='options']").change(function(){
  // getAmar(1);
   //alert("321312");
   var x=$("input[name='options']:checked").val()
   switch(x)
   {
     case "1":
     
     getAmar(1);

     break;
     case "2":
     getAmar(2);

     break;
     case "3":
     getAmar(3);
     break;
   }
     // Do something interesting here
 });



//$("#company-table").on("click", ".js-update-wo", initxLoad);
});
