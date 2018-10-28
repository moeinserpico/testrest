
$(function () {


  var loadForm =function (btn1) {
    var btn=0;
    //console.log(btn1);
    if($(btn1).attr("type")=="click")
     btn=$(this);
    else {
      btn=btn1;
    }
    console.log($(btn).attr("type"));
    console.log($(btn).attr("data-url"));
    return $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        //alert(btn.attr("data-url"));
        //alert("321321");
        // /$("#modal-amar").modal("hide");
        $("#modal-company").modal("show");
      },
      success: function (data) {
        //alert("3123@!");
        $("#modal-company .modal-content").html(data.html_amar_form);

      }
    });



};
//$("#modal-company").on("submit", ".js-company-create-form",
var saveForm= function () {
   var form = $(this);
   console.log(form.attr("action"));
   $.ajax({
     url: form.attr("action"),
     data: form.serialize(),
     type: form.attr("method"),
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
   return false;
 };
//////////////////////////////

//############# Time Change ############################
 var getListAmarLastTime= function (n) {

    myurl="";
    if(n===2)
      myurl='ListCurrentWeek';
    else if(n===3) {
      myurl='ListCurrentMonth';
    }
    else {
       myurl='ListCurrentDay';
    }

    $.ajax({
      url: myurl,

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
    return false;
  };

  //############# Time Radio Button هفته###################
  $('#option2').change(function(){

    getListAmarLastTime(2);
});
//################### ماه #####################
$('#option3').change(function(){

  getListAmarLastTime(3);
});

$('#option1').change(function(){

  getListAmarLastTime(1);
});
////////#########################




//////////////////////////////////

 var myWoLoader= function(){
   btn=$(this);



   //$.when(loadForm(btn)).done(initLoad,initWoAmarLoad,initWoMeterLoad,initWoMiscLoad,initWoNotifyLoad,initWoFileLoad);
   //$.when(loadForm(btn)).done(initAmarFileLoad,initAmarAssetLoad,initAmarPartLoad );
   loadForm(btn);

   //initLoad();
 }


 $('#btnAmarSearch').pDatepicker({
                 format: 'YYYY-MM-DD',
                 autoClose: true,

                 initialValueType: 'gregorian'
             });

$(".js-create-amar").click(myWoLoader);
$("#modal-company").on("submit", ".js-amar-create-form", saveForm);

// Update book
$("#company-table").on("click", ".js-update-amar", myWoLoader);
$("#modal-company").on("submit", ".js-amar-update-form", saveForm);
// Delete book
$("#company-table").on("click", ".js-delete-amar", loadForm);
$("#modal-company").on("submit", ".js-amar-delete-form", saveForm);
//$("#company-table").on("click", ".js-update-wo", initxLoad);
});
