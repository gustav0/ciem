$(function(){
	$("#id_pais").change(function(){          
		var pais = $(this).find("option:selected").val();
		var otro = "25";
		var title = "24";
		if (pais != "VE"){
			$("#id_venezuela option[value=" + otro + "]").show();
			$("#id_venezuela option[value="+otro+"]").attr("selected",true);
			$("#id_venezuela").attr('disabled','disabled');
		}else{

			$("#id_venezuela").removeAttr('disabled');
			$("#id_venezuela option[value=" + otro + "]").hide();
			$("#id_venezuela option[value="+title+"]").attr("selected",true);
		}
	});

});