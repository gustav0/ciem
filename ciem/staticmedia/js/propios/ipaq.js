$(document).ready(function(){

    $("#id_p2b_trabajo_0").click(function(){
       $('#sp1').removeClass("noDiplayDiv");
       if($('#sp1').height()<1) $('#sp1').css("height","+=92");
    });
    $("#id_p2b_trabajo_1").click(function(){
      $('#sp1').css("height","0");
      $('#sp1').addClass("noDiplayDiv");
    });
    $("#id_p4b_trabajo_0").click(function(){
       $('#sp2').removeClass("noDiplayDiv");
       if($('#sp2').height()<1) $('#sp2').css("height","+=92");
    });
    $("#id_p4b_trabajo_1").click(function(){
      $('#sp2').css("height","0");
      $('#sp2').addClass("noDiplayDiv");
    });
    $("#id_p6b_trabajo_0").click(function(){
       $('#sp3').removeClass("noDiplayDiv");
       if($('#sp3').height()<1) $('#sp3').css("height","+=92");
    });
    $("#id_p6b_trabajo_1").click(function(){
      $('#sp3').css("height","0");
      $('#sp3').addClass("noDiplayDiv");
    });
    $("#id_p8b_transporte_0").click(function(){
       $('#sp4').removeClass("noDiplayDiv");
       if($('#sp4').height()<1) $('#sp4').css("height","+=92");
    });	
    $("#id_p8b_transporte_1").click(function(){
      $('#sp4').css("height","0");
      $('#sp4').addClass("noDiplayDiv");
    });	
    $("#id_p10b_transporte_0").click(function(){
       $('#sp5').removeClass("noDiplayDiv");
       if($('#sp5').height()<1) $('#sp5').css("height","+=92");
    });	
    $("#id_p10b_transporte_1").click(function(){
      $('#sp5').css("height","0");
      $('#sp5').addClass("noDiplayDiv");
    });	
    $("#id_p12b_transporte_0").click(function(){
       $('#sp6').removeClass("noDiplayDiv");
       if($('#sp6').height()<1) $('#sp6').css("height","+=92");
    });		
    $("#id_p12b_transporte_1").click(function(){
      $('#sp6').css("height","0");
      $('#sp6').addClass("noDiplayDiv");
    });	
    $("#id_p14b_hogar_0").click(function(){
       $('#sp7').removeClass("noDiplayDiv");
       if($('#sp7').height()<1) $('#sp7').css("height","+=92");
    });		
    $("#id_p14b_hogar_1").click(function(){
      $('#sp7').css("height","0");
      $('#sp7').addClass("noDiplayDiv");
    });	
    $("#id_p16b_hogar_0").click(function(){
       $('#sp8').removeClass("noDiplayDiv");
       if($('#sp8').height()<1) $('#sp8').css("height","+=92");
    });		
    $("#id_p16b_hogar_1").click(function(){
      $('#sp8').css("height","0");
      $('#sp8').addClass("noDiplayDiv");
    });	
    $("#id_p18b_hogar_0").click(function(){
       $('#sp9').removeClass("noDiplayDiv");
       if($('#sp9').height()<1) $('#sp9').css("height","+=92");
    });		
    $("#id_p18b_hogar_1").click(function(){
      $('#sp9').css("height","0");
      $('#sp9').addClass("noDiplayDiv");
    });		
    $("#id_p20b_recreacion_0").click(function(){
       $('#sp10').removeClass("noDiplayDiv");
       if($('#sp10').height()<1) $('#sp10').css("height","+=92");
    });		
    $("#id_p20b_recreacion_1").click(function(){
      $('#sp10').css("height","0");
      $('#sp10').addClass("noDiplayDiv");
    });
    $("#id_p22b_recreacion_0").click(function(){
       $('#sp11').removeClass("noDiplayDiv");
       if($('#sp11').height()<1) $('#sp11').css("height","+=92");
    });		
    $("#id_p22b_recreacion_1").click(function(){
      $('#sp11').css("height","0");
      $('#sp11').addClass("noDiplayDiv");
    });	
    $("#id_p24b_recreacion_0").click(function(){
       $('#sp12').removeClass("noDiplayDiv");
       if($('#sp12').height()<1) $('#sp12').css("height","+=92");
    });		
    $("#id_p24b_recreacion_1").click(function(){
      $('#sp12').css("height","0");
      $('#sp12').addClass("noDiplayDiv");
    });		
	
    $("#id_p2b_trabajo_1").click();
    $("#id_p4b_trabajo_1").click();
    $("#id_p6b_trabajo_1").click();
    $("#id_p8b_transporte_1").click();	
    $("#id_p10b_transporte_1").click();
    $("#id_p12b_transporte_1").click();
    $("#id_p14b_hogar_1").click();
    $("#id_p16b_hogar_1").click();
    $("#id_p18b_hogar_1").click();
    $("#id_p20b_recreacion_1").click();
    $("#id_p22b_recreacion_1").click();
    $("#id_p24b_recreacion_1").click();
});