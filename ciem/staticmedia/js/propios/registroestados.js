$(document).ready(function(){
	$("#id_venezuela").attr('disabled','disabled');
	$("#id_pais").change(function(){          
		$pais = $(this).find("option:selected").val();
		$otro = "25";
		$zulia = "24";
		if ($pais != "VE"){
			$("#id_venezuela option[value=" + $otro + "]").show();
			$("#id_venezuela option[value="+$otro+"]").attr("selected",true);
			$("#id_venezuela").attr('disabled','disabled');
		}else{
			$("#id_venezuela").removeAttr('disabled');
			$("#id_venezuela option[value=" + $otro + "]").hide();
			$("#id_venezuela option[value="+$zulia+"]").attr("selected",true);
		}
	});

	$("#formulario").submit(function(){
		$("#id_venezuela").removeAttr('disabled');
	});

});