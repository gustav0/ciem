$(document).ready(function(){

	$("#id_comeEntreComidas_0").click(function(){
	   $('#div2').removeClass("noDisplayDiv");
	   if($('#div2').height()<1) $('#div2').css("height","+=25");
	});
	$("#id_comeEntreComidas_1").click(function(){
	  $('#div2').css("height","0");
	  $('#div2').addClass("noDisplayDiv");
	});

	$("#id_modificadoAlimentacionReciente_0").click(function(){
	   $('#div3porque').removeClass("noDisplayDiv");
	});
	$("#id_modificadoAlimentacionReciente_1").click(function(){
	  $('#div3porque').addClass("noDisplayDiv");
	});

	$("#id_esAlergicoIntolerante_0").click(function(){
	   $('#div7porque').removeClass("noDisplayDiv");
	});
	$("#id_esAlergicoIntolerante_1").click(function(){
	  $('#div7porque').addClass("noDisplayDiv");
	});

	$("#id_suplementoAlimenticio_0").click(function(){
	   $('#div9').removeClass("noDisplayDiv");
	   if($('#div9').height()<1) $('#div9').css("height","+=25");
	});
	$("#id_suplementoAlimenticio_1").click(function(){
	  $('#div9').css("height","0");
	  $('#div9').addClass("noDisplayDiv");
	});

	$("#id_consumoVariaEmocion_0").click(function(){
	   $('#div10porque').removeClass("noDisplayDiv");
	});
	$("#id_consumoVariaEmocion_1").click(function(){
	  $('#div10porque').addClass("noDisplayDiv");
	});

	$("#id_tieneDieta_0").click(function(){
	   $('#div12').removeClass("noDisplayDiv");
	   if($('#div12').height()<1) $('#div12').css("height","+=25");
	   $('#div13').removeClass("noDisplayDiv");
	   if($('#div13').height()<1) $('#div13').css("height","+=25");
	});
	$("#id_tieneDieta_1").click(function(){
	  $('#div12').css("height","0");
	  $('#div12').addClass("noDisplayDiv");
	  $('#div13').css("height","0");
	  $('#div13').addClass("noDisplayDiv");
	});
	$("#id_comeEntreComidas_1").click();
	$("#id_modificadoAlimentacionReciente_1").click();
	$("#id_esAlergicoIntolerante_1").click();
	$("#id_suplementoAlimenticio_1").click();
	$("#id_consumoVariaEmocion_1").click();
	$("#id_tieneDieta_1").click();
	
});