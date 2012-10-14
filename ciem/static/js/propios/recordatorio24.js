$(function(){
 
	/////////////////BOTON1///////////////////////
  	$('#botonDer1').click(function(){
  		if($('#input1').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo1").append('<option value="'+$('#input1').val()+'|'+$('input[name=porcion-desayuno]:checked').val()+'">'+$('#input1').val()+'</option>');
		}
	});
  	$('#botonIzq1').click(function(){
  		$("#selCombo1 option:selected").remove();
  	});
  	/////////////////BOTON2///////////////////
  	$('#botonDer2').click(function(){
  		if($('#input2').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo2").append('<option value="'+$('#input2').val()+'|'+$('input[name=porcion-merienda1]:checked').val()+'">'+$('#input2').val()+'</option>');
		}
	});
  	$('#botonIzq2').click(function(){
  		$("#selCombo2 option:selected").remove();
  	});
  	///////////////////BOTON3////////////////
  	$('#botonDer3').click(function(){
  		if($('#input3').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo3").append('<option value="'+$('#input3').val()+'|'+$('input[name=porcion-almuerzo]:checked').val()+'">'+$('#input3').val()+'</option>');
		}
	});
  	$('#botonIzq3').click(function(){
  		$("#selCombo1 option:selected").remove();
  	});
  	//////////////////BOTON4////////////////

  	$('#botonDer4').click(function(){
  		if($('#input4').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo4").append('<option value="'+$('#input4').val()+'|'+$('input[name=porcion-almuerzo]:checked').val()+'">'+$('#input4').val()+'</option>');
		}
	});
  	$('#botonIzq4').click(function(){
  		$("#selCombo1 option:selected").remove();
  	});


  	//////////////////BOTON5////////////////
  	$('#botonDer5').click(function(){
  		if($('#input5').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo5").append('<option value="'+$('#input5').val()+'|'+$('input[name=porcion-almuerzo]:checked').val()+'">'+$('#input5').val()+'</option>');
		}
	});
  	$('#botonIzq5').click(function(){
  		$("#selCombo1 option:selected").remove();
  	});

  	  	//////////////////BOTON6////////////////

  	$('#botonDer6').click(function(){
  		if($('#input6').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo6").append('<option value="'+$('#input6').val()+'|'+$('input[name=porcion-almuerzo]:checked').val()+'">'+$('#input6').val()+'</option>');
		}
	});
  	$('#botonIzq6').click(function(){
  		$("#selCombo1 option:selected").remove();
  	});
});