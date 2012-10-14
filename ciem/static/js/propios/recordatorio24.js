$(function(){

  	$('#botonDer1').click(function(){
  		$("#selCombo1").append('<option value="'+$('#input1').val()+'">'+$('#input1').val()+'</option>');
  	});

});