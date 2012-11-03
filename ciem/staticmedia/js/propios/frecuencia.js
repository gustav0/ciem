$(function(){

			$("#id_form-0-porcion_p").attr('disabled','disabled');
			$("#id_form-0-porcion_m").attr('disabled','disabled');
			$("#id_form-0-porcion_g").attr('disabled','disabled');

			$("#id_form-1-porcion_p").attr('disabled','disabled');
			$("#id_form-1-porcion_m").attr('disabled','disabled');
			$("#id_form-1-porcion_g").attr('disabled','disabled');

			$("#id_form-2-porcion_p").attr('disabled','disabled');
			$("#id_form-2-porcion_m").attr('disabled','disabled');
			$("#id_form-2-porcion_g").attr('disabled','disabled');

			$("#id_form-3-porcion_p").attr('disabled','disabled');
			$("#id_form-3-porcion_m").attr('disabled','disabled');
			$("#id_form-3-porcion_g").attr('disabled','disabled');

			$("#id_form-4-porcion_p").attr('disabled','disabled');
			$("#id_form-4-porcion_m").attr('disabled','disabled');
			$("#id_form-4-porcion_g").attr('disabled','disabled');

			$("#id_form-5-porcion_p").attr('disabled','disabled');
			$("#id_form-5-porcion_m").attr('disabled','disabled');
			$("#id_form-5-porcion_g").attr('disabled','disabled');

			$("#id_form-6-porcion_p").attr('disabled','disabled');
			$("#id_form-6-porcion_m").attr('disabled','disabled');
			$("#id_form-6-porcion_g").attr('disabled','disabled');

			$("#id_form-7-porcion_p").attr('disabled','disabled');
			$("#id_form-7-porcion_m").attr('disabled','disabled');
			$("#id_form-7-porcion_g").attr('disabled','disabled');

			$("#id_form-8-porcion_p").attr('disabled','disabled');
			$("#id_form-8-porcion_m").attr('disabled','disabled');
			$("#id_form-8-porcion_g").attr('disabled','disabled');

			$("#id_form-9-porcion_p").attr('disabled','disabled');
			$("#id_form-9-porcion_m").attr('disabled','disabled');
			$("#id_form-9-porcion_g").attr('disabled','disabled');

			$("#id_form-10-porcion_p").attr('disabled','disabled');
			$("#id_form-10-porcion_m").attr('disabled','disabled');
			$("#id_form-10-porcion_g").attr('disabled','disabled');

			$("#id_form-11-porcion_p").attr('disabled','disabled');
			$("#id_form-11-porcion_m").attr('disabled','disabled');
			$("#id_form-11-porcion_g").attr('disabled','disabled');			

			$("#id_form-12-porcion_p").attr('disabled','disabled');
			$("#id_form-12-porcion_m").attr('disabled','disabled');
			$("#id_form-12-porcion_g").attr('disabled','disabled');

			$("#id_form-13-porcion_p").attr('disabled','disabled');
			$("#id_form-13-porcion_m").attr('disabled','disabled');
			$("#id_form-13-porcion_g").attr('disabled','disabled');

			$("#id_form-14-porcion_p").attr('disabled','disabled');
			$("#id_form-14-porcion_m").attr('disabled','disabled');
			$("#id_form-14-porcion_g").attr('disabled','disabled');

			$("#id_form-15-porcion_p").attr('disabled','disabled');
			$("#id_form-15-porcion_m").attr('disabled','disabled');
			$("#id_form-15-porcion_g").attr('disabled','disabled');

			$("#id_form-16-porcion_p").attr('disabled','disabled');
			$("#id_form-16-porcion_m").attr('disabled','disabled');
			$("#id_form-16-porcion_g").attr('disabled','disabled');

	$("#id_form-0-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-0-porcion_p").attr('disabled','disabled');
			$("#id_form-0-porcion_m").attr('disabled','disabled');
			$("#id_form-0-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-0-porcion_p").removeAttr('disabled');
			$("#id_form-0-porcion_m").removeAttr('disabled');
			$("#id_form-0-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-1-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-1-porcion_p").attr('disabled','disabled');
			$("#id_form-1-porcion_m").attr('disabled','disabled');
			$("#id_form-1-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-1-porcion_p").removeAttr('disabled');
			$("#id_form-1-porcion_m").removeAttr('disabled');
			$("#id_form-1-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-2-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-2-porcion_p").attr('disabled','disabled');
			$("#id_form-2-porcion_m").attr('disabled','disabled');
			$("#id_form-2-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-2-porcion_p").removeAttr('disabled');
			$("#id_form-2-porcion_m").removeAttr('disabled');
			$("#id_form-2-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-3-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-3-porcion_p").attr('disabled','disabled');
			$("#id_form-3-porcion_m").attr('disabled','disabled');
			$("#id_form-3-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-3-porcion_p").removeAttr('disabled');
			$("#id_form-3-porcion_m").removeAttr('disabled');
			$("#id_form-3-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-4-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-4-porcion_p").attr('disabled','disabled');
			$("#id_form-4-porcion_m").attr('disabled','disabled');
			$("#id_form-4-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-4-porcion_p").removeAttr('disabled');
			$("#id_form-4-porcion_m").removeAttr('disabled');
			$("#id_form-4-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-5-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-5-porcion_p").attr('disabled','disabled');
			$("#id_form-5-porcion_m").attr('disabled','disabled');
			$("#id_form-5-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-5-porcion_p").removeAttr('disabled');
			$("#id_form-5-porcion_m").removeAttr('disabled');
			$("#id_form-5-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-6-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-6-porcion_p").attr('disabled','disabled');
			$("#id_form-6-porcion_m").attr('disabled','disabled');
			$("#id_form-6-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-6-porcion_p").removeAttr('disabled');
			$("#id_form-6-porcion_m").removeAttr('disabled');
			$("#id_form-6-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-7-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-7-porcion_p").attr('disabled','disabled');
			$("#id_form-7-porcion_m").attr('disabled','disabled');
			$("#id_form-7-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-7-porcion_p").removeAttr('disabled');
			$("#id_form-7-porcion_m").removeAttr('disabled');
			$("#id_form-7-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-8-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-8-porcion_p").attr('disabled','disabled');
			$("#id_form-8-porcion_m").attr('disabled','disabled');
			$("#id_form-8-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-8-porcion_p").removeAttr('disabled');
			$("#id_form-8-porcion_m").removeAttr('disabled');
			$("#id_form-8-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-9-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-9-porcion_p").attr('disabled','disabled');
			$("#id_form-9-porcion_m").attr('disabled','disabled');
			$("#id_form-9-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-9-porcion_p").removeAttr('disabled');
			$("#id_form-9-porcion_m").removeAttr('disabled');
			$("#id_form-9-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-10-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-10-porcion_p").attr('disabled','disabled');
			$("#id_form-10-porcion_m").attr('disabled','disabled');
			$("#id_form-10-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-10-porcion_p").removeAttr('disabled');
			$("#id_form-10-porcion_m").removeAttr('disabled');
			$("#id_form-10-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-11-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-11-porcion_p").attr('disabled','disabled');
			$("#id_form-11-porcion_m").attr('disabled','disabled');
			$("#id_form-11-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-11-porcion_p").removeAttr('disabled');
			$("#id_form-11-porcion_m").removeAttr('disabled');
			$("#id_form-11-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-12-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-12-porcion_p").attr('disabled','disabled');
			$("#id_form-12-porcion_m").attr('disabled','disabled');
			$("#id_form-12-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-12-porcion_p").removeAttr('disabled');
			$("#id_form-12-porcion_m").removeAttr('disabled');
			$("#id_form-12-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-13-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-13-porcion_p").attr('disabled','disabled');
			$("#id_form-13-porcion_m").attr('disabled','disabled');
			$("#id_form-13-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-13-porcion_p").removeAttr('disabled');
			$("#id_form-13-porcion_m").removeAttr('disabled');
			$("#id_form-13-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-14-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-14-porcion_p").attr('disabled','disabled');
			$("#id_form-14-porcion_m").attr('disabled','disabled');
			$("#id_form-14-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-14-porcion_p").removeAttr('disabled');
			$("#id_form-14-porcion_m").removeAttr('disabled');
			$("#id_form-14-porcion_g").removeAttr('disabled');
		}
	});


	$("#id_form-15-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-15-porcion_p").attr('disabled','disabled');
			$("#id_form-15-porcion_m").attr('disabled','disabled');
			$("#id_form-15-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-15-porcion_p").removeAttr('disabled');
			$("#id_form-15-porcion_m").removeAttr('disabled');
			$("#id_form-15-porcion_g").removeAttr('disabled');
		}
	});

	$("#id_form-16-frecuencia").change(function(){          
		var frecuencia = $(this).find("option:selected").val();
		if (frecuencia == "0"){
			$("#id_form-16-porcion_p").attr('disabled','disabled');
			$("#id_form-16-porcion_m").attr('disabled','disabled');
			$("#id_form-16-porcion_g").attr('disabled','disabled');
		}else{
			$("#id_form-16-porcion_p").removeAttr('disabled');
			$("#id_form-16-porcion_m").removeAttr('disabled');
			$("#id_form-16-porcion_g").removeAttr('disabled');
		}
	});

});