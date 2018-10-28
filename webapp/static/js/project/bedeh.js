
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
        // /$("#modal-bedeh").modal("hide");
        $("#modal-company").modal("show");
      },
      success: function (data) {
        //alert("3123@!");
        $("#modal-company .modal-content").html(data.html_bedeh_form);

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
         $("#tbody_company").html(data.html_bedeh_list);
         $("#modal-company").modal("hide");
        // console.log(data.html_bedeh_list);
       }
       else {


       }
     }
   });
   return false;
 };


 var myWoLoader= function(){
   btn=$(this);



   //$.when(loadForm(btn)).done(initLoad,initWoAmarLoad,initWoMeterLoad,initWoMiscLoad,initWoNotifyLoad,initWoFileLoad);
   //$.when(loadForm(btn)).done(initAmarFileLoad,initAmarAssetLoad,initAmarPartLoad );
   loadForm(btn);

   //initLoad();
 }



$(".js-create-bedeh").click(myWoLoader);
$("#modal-company").on("submit", ".js-bedeh-create-form", saveForm);

// Update book
$("#company-table").on("click", ".js-update-bedeh", myWoLoader);
$("#modal-company").on("submit", ".js-bedeh-update-form", saveForm);
// Delete book
$("#company-table").on("click", ".js-delete-bedeh", loadForm);
$("#modal-company").on("submit", ".js-bedeh-delete-form", saveForm);
//$("#company-table").on("click", ".js-update-wo", initxLoad);
});
