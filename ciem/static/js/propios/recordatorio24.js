$(function(){
 
 	$('input:text').focus(
    function(){
        $(this).val('');
    });
  	
  	$("#form1").bind("keypress", function(e) {
    	if (e.keyCode == 13) return false;
  	});

  	

 	
	/////////////////BOTON1///////////////////////
  	$('#botonAgregar1').click(function(){
  		if($('#input1').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo1").append('<option value="'+$('#input1').val()+'|'+$('input[name=porcion-desayuno]:checked').val()+'">'+$('#input1').val()+'</option>');
		$('#input1').focus();
		}
	});
  	$('#botonRemover1').click(function(){
  		$("#selCombo1 option:selected").remove();
  	});

  	$('#selCombo1').dblclick(function() {
  		$("#selCombo1 option:selected").remove();
	});

	 	$("#input1").enterKey(function () {
	    if($('#input1').val() == ""){
	  			alert("vacio");
	  		}else{
	  		$("#selCombo1").append('<option value="'+$('#input1').val()+'|'+$('input[name=porcion-desayuno]:checked').val()+'">'+$('#input1').val()+'</option>');
			$('#input1').focus();
			}
	});


  	/////////////////BOTON2///////////////////
  	$('#botonAgregar2').click(function(){
  		if($('#input2').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo2").append('<option value="'+$('#input2').val()+'|'+$('input[name=porcion-merienda1]:checked').val()+'">'+$('#input2').val()+'</option>');
		$('#input2').focus();
		}
	})
  	$('#botonRemover2').click(function(){
  		$("#selCombo2 option:selected").remove();
  	});

  	$('#selCombo2').dblclick(function() {
  		$("#selCombo2 option:selected").remove();
	});

	 	$("#input2").enterKey(function () {
	    if($('#input2').val() == ""){
	  			alert("vacio");
	  		}else{
	  		$("#selCombo2").append('<option value="'+$('#input2').val()+'|'+$('input[name=porcion-merienda1]:checked').val()+'">'+$('#input2').val()+'</option>');
			$('#input2').focus();
			}
	});
  	///////////////////BOTON3////////////////
  	$('#botonAgregar3').click(function(){
  		if($('#input3').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo3").append('<option value="'+$('#input3').val()+'|'+$('input[name=porcion-cane]:checked').val()+'">'+$('#input3').val()+'</option>');
		$('#input3').focus();
		}
	});
  	$('#botonRemover3').click(function(){
  		$("#selCombo1 option:selected").remove();
  	});

  	$('#selCombo3').dblclick(function() {
  		$("#selCombo3 option:selected").remove();
	});

	 	$("#input3").enterKey(function () {
	    if($('#input3').val() == ""){
	  			alert("vacio");
	  		}else{
	  		$("#selCombo3").append('<option value="'+$('#input3').val()+'|'+$('input[name=porcion-cena]:checked').val()+'">'+$('#input3').val()+'</option>');
			$('#input3').focus();
			}
	});

  	//////////////////BOTON4////////////////

  	$('#botonAgregar4').click(function(){
  		if($('#input4').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo4").append('<option value="'+$('#input4').val()+'|'+$('input[name=porcion-merienda2]:checked').val()+'">'+$('#input4').val()+'</option>');
		$('#input4').focus();
		}
	});
  	$('#botonRemover4').click(function(){
  		$("#selCombo4 option:selected").remove();
  	});


  	$('#selCombo4').dblclick(function() {
  		$("#selCombo4 option:selected").remove();
	});

	 	$("#input4").enterKey(function () {
	    if($('#input4').val() == ""){
	  			alert("vacio");
	  		}else{
	  		$("#selCombo4").append('<option value="'+$('#input4').val()+'|'+$('input[name=porcion-merienda2]:checked').val()+'">'+$('#input4').val()+'</option>');
			$('#input4').focus();
			}
	});
  	//////////////////BOTON5////////////////
  	$('#botonAgregar5').click(function(){
  		if($('#input5').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo5").append('<option value="'+$('#input5').val()+'|'+$('input[name=porcion-cena]:checked').val()+'">'+$('#input5').val()+'</option>');
		$('#input5').focus();
		}
	});
  	$('#botonRemover5').click(function(){
  		$("#selCombo5 option:selected").remove();
  	});
  	$('#selCombo5').dblclick(function() {
  		$("#selCombo5 option:selected").remove();
	});


	 	$("#input5").enterKey(function () {
	    if($('#input5').val() == ""){
	  			alert("vacio");
	  		}else{
	  		$("#selCombo5").append('<option value="'+$('#input5').val()+'|'+$('input[name=porcion-cena]:checked').val()+'">'+$('#input5').val()+'</option>');
			$('#input5').focus();
			}
	});
  	  	//////////////////BOTON6////////////////

  	$('#botonAgregar6').click(function(){if($('#input6').val() == ""){
  			alert("vacio");
  		}else{
  		$("#selCombo6").append('<option value="'+$('#input6').val()+'|'+$('input[name=porcion-merienda3]:checked').val()+'">'+$('#input6').val()+'</option>');
		$('#input6').focus();
		}
	});
  	$('#botonRemover6').click(function(){
  		$("#selCombo6 option:selected").remove();
  	});

  	$('#selCombo6').dblclick(function() {
  		$("#selCombo6 option:selected").remove();
	});

	 	$("#input6").enterKey(function () {
	    if($('#input6').val() == ""){
	  			alert("vacio");
	  		}else{
	  		$("#selCombo6").append('<option value="'+$('#input6').val()+'|'+$('input[name=porcion-merienda3]:checked').val()+'">'+$('#input6').val()+'</option>');
			$('#input6').focus();
			}
	});

	 	/////////////////////////POST ALL OPTIONS FROM SELECTS///////////////////////
	$('#botonRecordar').click(function(){
  		$("#selCombo1").each(function(){
            $("#selCombo1 option").attr("selected","selected"); });
    	
  		$("#selCombo2").each(function(){
            $("#selCombo2 option").attr("selected","selected"); });
    	
		$("#selCombo3").each(function(){
            $("#selCombo3 option").attr("selected","selected"); });
    	
		$("#selCombo4").each(function(){
            $("#selCombo4 option").attr("selected","selected"); });
    	
		$("#selCombo5").each(function(){
            $("#selCombo5 option").attr("selected","selected"); });
    	
		$("#selCombo6").each(function(){
            $("#selCombo6 option").attr("selected","selected"); });
    	});

});