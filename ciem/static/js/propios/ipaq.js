$(document).ready(function(){

    $("#id_p2b_trabajo_0").click(function(){
       $('#sp1').removeClass("noDiplayDiv");
       if($('#sp1').height()<1){
       $('#sp1').css("height","+=46");
       }
    });
    $("#id_p2b_trabajo_1").click(function(){
      $('#sp1').css("height","0");
      $('#sp1').addClass("noDiplayDiv");
    });
    $("#id_p4b_trabajo_0").click(function(){
       $('#sp2').removeClass("noDiplayDiv");
    });
    $("#id_p4b_trabajo_1").click(function(){
       $('#sp2').addClass("noDiplayDiv");
    });
    $("#id_p6b_trabajo_0").click(function(){
       $('#sp3').removeClass("noDiplayDiv");
    });
    $("#id_p6b_trabajo_1").click(function(){
       $('#sp3').addClass("noDiplayDiv");
    });
    $("#id_p8b_transporte_0").click(function(){
       $('#sp4').removeClass("noDiplayDiv");
    });	
    $("#id_p8b_transporte_1").click(function(){
       $('#sp4').addClass("noDiplayDiv");
    });	
    $("#id_p10b_transporte_0").click(function(){
       $('#sp5').removeClass("noDiplayDiv");
    });	
    $("#id_p10b_transporte_1").click(function(){
       $('#sp5').addClass("noDiplayDiv");
    });	
    $("#id_p12b_transporte_0").click(function(){
       $('#sp6').removeClass("noDiplayDiv");
    });		
    $("#id_p12b_transporte_1").click(function(){
       $('#sp6').addClass("noDiplayDiv");
    });	
    $("#id_p14b_hogar_0").click(function(){
       $('#sp7').removeClass("noDiplayDiv");
    });		
    $("#id_p14b_hogar_1").click(function(){
       $('#sp7').addClass("noDiplayDiv");
    });	
    $("#id_p16b_hogar_0").click(function(){
       $('#sp8').removeClass("noDiplayDiv");
    });		
    $("#id_p16b_hogar_1").click(function(){
       $('#sp8').addClass("noDiplayDiv");
    });	
    $("#id_p18b_hogar_0").click(function(){
       $('#sp9').removeClass("noDiplayDiv");
    });		
    $("#id_p18b_hogar_1").click(function(){
       $('#sp9').addClass("noDiplayDiv");
    });		
    $("#id_p20b_recreacion_0").click(function(){
       $('#sp10').removeClass("noDiplayDiv");
    });		
    $("#id_p20b_recreacion_1").click(function(){
       $('#sp10').addClass("noDiplayDiv");
    });
    $("#id_p22b_recreacion_0").click(function(){
       $('#sp11').removeClass("noDiplayDiv");
    });		
    $("#id_p22b_recreacion_1").click(function(){
       $('#sp11').addClass("noDiplayDiv");
    });	
    $("#id_p24b_recreacion_0").click(function(){
       $('#sp12').removeClass("noDiplayDiv");
    });		
    $("#id_p24b_recreacion_1").click(function(){
       $('#sp12').addClass("noDiplayDiv");
    });		
    $("#id_p26b_sentado_0").click(function(){
       $('#sp13').removeClass("noDiplayDiv");
    });		
    $("#id_p26b_sentado_1").click(function(){
       $('#sp13').addClass("noDiplayDiv");
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
    $("#id_p26b_sentado_1").click();
});