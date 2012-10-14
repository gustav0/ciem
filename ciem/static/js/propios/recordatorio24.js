$(function(){
 
 	$('input:text').focus(
    function(){
        $(this).val('');
    });
  $("#form1").bind("keypress", function(e) {
    if (e.keyCode == 13) return false;
  });
 	$("#input1").enterKey(function () {
	    if($('#input1').val() == ""){
	  			alert("vacio");
	  		}else{
	  		$("#selCombo1").append('<option value="'+$('#input1').val()+'|'+$('input[name=porcion-desayuno]:checked').val()+'">'+$('#input1').val()+'</option>');
			$('#input1').focus();
			}
	});
 	
	/////////////////BOTON1///////////////////////
  	$('#botonDer1').click(function(){
  		if($('#input1').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo1").append('<option value="'+$('#input1').val()+'|'+$('input[name=porcion-desayuno]:checked').val()+'">'+$('#input1').val()+'</option>');
		$('#input1').focus();
		}
	});
  	$('#botonIzq1').click(function(){
  		$("#selCombo1 option:selected").remove();
  	});

  	$('#selCombo1').dblclick(function() {
  		$("#selCombo1 option:selected").remove();
	});


  	/////////////////BOTON2///////////////////
  	$('#botonDer2').click(function(){
  		if($('#input2').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo2").append('<option value="'+$('#input2').val()+'|'+$('input[name=porcion-merienda1]:checked').val()+'">'+$('#input2').val()+'</option>');
		$('#input2').focus();
		}
	});
  	$('#botonIzq2').click(function(){
  		$("#selCombo2 option:selected").remove();
  	});

  	$('#selCombo2').dblclick(function() {
  		$("#selCombo2 option:selected").remove();
	});
  	///////////////////BOTON3////////////////
  	$('#botonDer3').click(function(){
  		if($('#input3').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo3").append('<option value="'+$('#input3').val()+'|'+$('input[name=porcion-almuerzo]:checked').val()+'">'+$('#input3').val()+'</option>');
		$('#input3').focus();
		}
	});
  	$('#botonIzq3').click(function(){
  		$("#selCombo1 option:selected").remove();
  	});

  	$('#selCombo3').dblclick(function() {
  		$("#selCombo3 option:selected").remove();
	});

  	//////////////////BOTON4////////////////

  	$('#botonDer4').click(function(){
  		if($('#input4').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo4").append('<option value="'+$('#input4').val()+'|'+$('input[name=porcion-almuerzo]:checked').val()+'">'+$('#input4').val()+'</option>');
		$('#input4').focus();
		}
	});
  	$('#botonIzq4').click(function(){
  		$("#selCombo4 option:selected").remove();
  	});


  	$('#selCombo4').dblclick(function() {
  		$("#selCombo4 option:selected").remove();
	});
  	//////////////////BOTON5////////////////
  	$('#botonDer5').click(function(){
  		if($('#input5').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo5").append('<option value="'+$('#input5').val()+'|'+$('input[name=porcion-almuerzo]:checked').val()+'">'+$('#input5').val()+'</option>');
		$('#input5').focus();
		}
	});
  	$('#botonIzq5').click(function(){
  		$("#selCombo5 option:selected").remove();
  	});
  	$('#selCombo5').dblclick(function() {
  		$("#selCombo5 option:selected").remove();
	});
  	  	//////////////////BOTON6////////////////

  	$('#botonDer6').click(function(){
  		if($('#input6').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo6").append('<option value="'+$('#input6').val()+'|'+$('input[name=porcion-almuerzo]:checked').val()+'">'+$('#input6').val()+'</option>');
		$('#input6').focus();
		}
	});
  	$('#botonIzq6').click(function(){
  		$("#selCombo6 option:selected").remove();
  	});

  	$('#selCombo6').dblclick(function() {
  		$("#selCombo6 option:selected").remove();
	});
});