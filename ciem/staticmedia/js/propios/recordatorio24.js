$(document).ready(function(){
	$("#id_horaDesayuno").mask('00:00');
	$("#id_horaMerienda1").mask('00:00');
	$("#id_horaAlmuerzo").mask('00:00');
	$("#id_horaMerienda2").mask('00:00');
	$("#id_horaCena").mask('00:00');
	$("#id_horaMerienda3").mask('00:00');
	$("#id_desayuno_0").click();
 	$("#id_merienda1_0").click();
 	$("#id_almuerzo_0").click();
 	$("#id_merienda2_0").click();
 	$("#id_cena_0").click();
 	$("#id_merienda3_0").click();
	$('input:text').focus(function(){
		$(this).val('');
	});
	$("#form1").bind("keypress", function(e){
		if (e.keyCode == 13) return false;
	});
	$auxAlimento = "";

	/////////////////DESAYUNO///////////////////////
	$('#botonAgregar1').click(function(){
		if($('#input1').val() == ""){
			alert("Debe escribir el nombre de un alimento");
		}else{
			$('#input1').attr('id_a','0');
			$auxAlimento = $('#input1').val();
			$('#alimentosD option').each(function(index) {
				$name = $(this).val();
				if($name==$auxAlimento){
				    alert("conseguí")
	    			$('#input1').attr('id_a',$(this).text())
	    			return false;
	    		}
			});
			$("#selCombo1").append('<option value="'+$('#input1').attr('id_a')+'|'+$('input[name=porcion-desayuno]:checked').val()+'|1">'+$('#input1').val()+' ('+$('input[name=porcion-desayuno]:checked').val()+') '+'</option>');
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
			alert("Debe escribir el nombre de un alimento");
		}else{
			$('#input1').attr('id_a','0');
			$auxAlimento = $('#input1').val();
			$('#alimentosD option').each(function(index) {
				$name = $(this).val();
				if($name==$auxAlimento){
				    alert("conseguí")
	    			$('#input1').attr('id_a',$(this).text())
	    			return false;
	    		}
			});
			$("#selCombo1").append('<option value="'+$('#input1').attr('id_a')+'|'+$('input[name=porcion-desayuno]:checked').val()+'|1">'+$('#input1').val()+' ('+$('input[name=porcion-desayuno]:checked').val()+') '+'</option>');
			$('#input1').focus();
		}
	});

	/////////////////MERIENDA 1///////////////////
	$('#botonAgregar2').click(function(){
		if($('#input2').val() == ""){
			alert("Debe escribir el nombre de un alimento");
		}else{
			$('#input2').attr('id_a','0');
			$auxAlimento = $('#input2').val();
			$('#alimentosM1 option').each(function(index) {
				$name = $(this).val();
				if($name==$auxAlimento){
	    			$('#input2').attr('id_a',$(this).text())
	    			return false;
	    		}
			});
			$("#selCombo2").append('<option value="'+$('#input2').attr('id_a')+'|'+$('input[name=porcion-merienda1]:checked').val()+'|2">'+$('#input2').val()+' ('+$('input[name=porcion-merienda1]:checked').val()+') '+'</option>');
			$('#input2').focus();
		}
	});
	$('#botonRemover2').click(function(){
		$("#selCombo2 option:selected").remove();
	});
	$('#selCombo2').dblclick(function() {
		$("#selCombo2 option:selected").remove();
	});
	$("#input2").enterKey(function () {
		if($('#input2').val() == ""){
			alert("Debe escribir el nombre de un alimento");
		}else{
			$('#input2').attr('id_a','0');
			$auxAlimento = $('#input2').val();
			$('#alimentosM1 option').each(function(index) {
				$name = $(this).val();
				if($name==$auxAlimento){
	    			$('#input2').attr('id_a',$(this).text())
	    			return false;
	    		}
			});
			$("#selCombo2").append('<option value="'+$('#input2').attr('id_a')+'|'+$('input[name=porcion-merienda1]:checked').val()+'|2">'+$('#input2').val()+' ('+$('input[name=porcion-merienda1]:checked').val()+') '+'</option>');
			$('#input2').focus();
		}
	});

	///////////////////ALMUERZO////////////////
	$('#botonAgregar3').click(function(){
		if($('#input3').val() == ""){
			alert("Debe escribir el nombre de un alimento");
		}else{
			$('#input3').attr('id_a','0');
			$auxAlimento = $('#input3').val();
			$('#alimentosA option').each(function(index) {
				$name = $(this).val();
				if($name==$auxAlimento){
	    			$('#input3').attr('id_a',$(this).text())
	    			return false;
	    		}
			});
			$("#selCombo3").append('<option value="'+$('#input3').attr('id_a')+'|'+$('input[name=porcion-almuerzo]:checked').val()+'|3">'+$('#input3').val()+' ('+$('input[name=porcion-almuerzo]:checked').val()+') '+'</option>');
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
			alert("Debe escribir el nombre de un alimento");
		}else{
			$('#input3').attr('id_a','0');
			$auxAlimento = $('#input3').val();
			$('#alimentosA option').each(function(index) {
				$name = $(this).val();
				if($name==$auxAlimento){
	    			$('#input3').attr('id_a',$(this).text())
	    			return false;
	    		}
			});
			$("#selCombo3").append('<option value="'+$('#input3').attr('id_a')+'|'+$('input[name=porcion-almuerzo]:checked').val()+'|3">'+$('#input3').val()+' ('+$('input[name=porcion-almuerzo]:checked').val()+') '+'</option>');
			$('#input3').focus();
		}
	});

	//////////////////MERIENDA 2////////////////
	$('#botonAgregar4').click(function(){
		if($('#input4').val() == ""){
			alert("Debe escribir el nombre de un alimento");
		}else{
			$('#input4').attr('id_a','0');
			$auxAlimento = $('#input4').val();
			$('#alimentosM2 option').each(function(index) {
				$name = $(this).val();
				if($name==$auxAlimento){
	    			$('#input4').attr('id_a',$(this).text())
	    			return false;
	    		}
			});
			$("#selCombo4").append('<option value="'+$('#input4').attr('id_a')+'|'+$('input[name=porcion-merienda2]:checked').val()+'|4">'+$('#input4').val()+' ('+$('input[name=porcion-merienda2]:checked').val()+') '+'</option>');
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
			alert("Debe escribir el nombre de un alimento");
		}else{
			$('#input4').attr('id_a','0');
			$auxAlimento = $('#input4').val();
			$('#alimentosM2 option').each(function(index) {
				$name = $(this).val();
				if($name==$auxAlimento){
	    			$('#input4').attr('id_a',$(this).text())
	    			return false;
	    		}
			});
			$("#selCombo4").append('<option value="'+$('#input4').attr('id_a')+'|'+$('input[name=porcion-merienda2]:checked').val()+'|4">'+$('#input4').val()+' ('+$('input[name=porcion-merienda2]:checked').val()+') '+'</option>');
			$('#input4').focus();
		}
	});

	//////////////////CENA////////////////
	$('#botonAgregar5').click(function(){
		if($('#input5').val() == ""){
			alert("Debe escribir el nombre de un alimento");
		}else{
			$('#input5').attr('id_a','0');
			$auxAlimento = $('#input5').val();
			$('#alimentosC option').each(function(index) {
				$name = $(this).val();
				if($name==$auxAlimento){
	    			$('#input5').attr('id_a',$(this).text())
	    			return false;
	    		}
			});
			$("#selCombo5").append('<option value="'+$('#input5').attr('id_a')+'|'+$('input[name=porcion-cena]:checked').val()+'|5">'+$('#input5').val()+' ('+$('input[name=porcion-cena]:checked').val()+') '+'</option>');
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
			alert("Debe escribir el nombre de un alimento");
		}else{
			$('#input5').attr('id_a','0');
			$auxAlimento = $('#input5').val();
			$('#alimentosC option').each(function(index) {
				$name = $(this).val();
				if($name==$auxAlimento){
	    			$('#input5').attr('id_a',$(this).text())
	    			return false;
	    		}
			});
			$("#selCombo5").append('<option value="'+$('#input5').attr('id_a')+'|'+$('input[name=porcion-cena]:checked').val()+'|5">'+$('#input5').val()+' ('+$('input[name=porcion-cena]:checked').val()+') '+'</option>');
			$('#input5').focus();
		}
	});

	//////////////////MERIENDA 3////////////////
	$('#botonAgregar6').click(function(){
		if($('#input6').val() == ""){
			alert("Debe escribir el nombre de un alimento");
		}else{
			$('#input6').attr('id_a','0');
			$auxAlimento = $('#input6').val();
			$('#alimentosM3 option').each(function(index) {
				$name = $(this).val();
				if($name==$auxAlimento){
	    			$('#input6').attr('id_a',$(this).text())
	    			return false;
	    		}
			});
			$("#selCombo6").append('<option value="'+$('#input6').attr('id_a')+'|'+$('input[name=porcion-merienda3]:checked').val()+'|6">'+$('#input6').val()+' ('+$('input[name=porcion-merienda3]:checked').val()+') '+'</option>');
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
			alert("Debe escribir el nombre de un alimento");
		}else{
			$('#input6').attr('id_a','0');
			$auxAlimento = $('#input6').val();
			$('#alimentosM3 option').each(function(index) {
				$name = $(this).val();
				if($name==$auxAlimento){
	    			$('#input6').attr('id_a',$(this).text())
	    			return false;
	    		}
			});
			$("#selCombo6").append('<option value="'+$('#input6').attr('id_a')+'|'+$('input[name=porcion-merienda3]:checked').val()+'|6">'+$('#input6').val()+' ('+$('input[name=porcion-merienda3]:checked').val()+') '+'</option>');
			$('#input6').focus();
		}
	});

	/////////////////////////POST ALL OPTIONS FROM SELECTS and validations///////////////////////
	$('#botonRecordar').click(function(){
		$("#selCombo1").each(function(){$("#selCombo1 option").attr("selected","selected");});
		$("#selCombo2").each(function(){$("#selCombo2 option").attr("selected","selected");});
		$("#selCombo3").each(function(){$("#selCombo3 option").attr("selected","selected");});
		$("#selCombo4").each(function(){$("#selCombo4 option").attr("selected","selected");});
		$("#selCombo5").each(function(){$("#selCombo5 option").attr("selected","selected");});
		$("#selCombo6").each(function(){$("#selCombo6 option").attr("selected","selected");});
	});
	if($('#id_desayuno_0').attr("checked")=="checked"){$('#id_diasDesayuno').val('7');}
	if($('#id_merienda1_0').attr("checked")=="checked"){$('#id_diasMerienda1').val('7');}
	if($('#id_almuerzo_0').attr("checked")=="checked"){$('#id_diasAlmuerzo').val('7');}
	if($('#id_merienda2_0').attr("checked")=="checked"){$('#id_diasMerienda2').val('7');}
	if($('#id_cena_0').attr("checked")=="checked"){$('#id_diasCena').val('7');}
	if($('#id_merienda3_0').attr("checked")=="checked"){$('#id_diasMerienda3').val('7');}

	$('#id_horaDesayuno').timepicker({
		showPeriod: true,
	    showLeadingZero: true,
	    hourText: 'Hora',
	    minuteText: 'Minutos',
	    amPmText: ['AM', 'PM'],
	    timeSeparator: ':',
	    nowButtonText: 'Hora actual',
	    showNowButton: true,
	    closeButtonText: 'Cerrar',
	    showCloseButton: true,
	});
	$('#id_horaMerienda1').timepicker({
		showPeriod: true,
	    showLeadingZero: true,
	    hourText: 'Hora',
	    minuteText: 'Minutos',
	    amPmText: ['AM', 'PM'],
	    timeSeparator: ':',
	    nowButtonText: 'Hora actual',
	    showNowButton: true,
	    closeButtonText: 'Cerrar',
	    showCloseButton: true,
	});
	$('#id_horaAlmuerzo').timepicker({
		showPeriod: true,
	    showLeadingZero: true,
	    hourText: 'Hora',
	    minuteText: 'Minutos',
	    amPmText: ['AM', 'PM'],
	    timeSeparator: ':',
	    nowButtonText: 'Hora actual',
	    showNowButton: true,
	    closeButtonText: 'Cerrar',
	    showCloseButton: true,
	});
	$('#id_horaMerienda2').timepicker({
	 	showPeriod: true,
	    showLeadingZero: true,
	    hourText: 'Hora',
	    minuteText: 'Minutos',
	    amPmText: ['AM', 'PM'],
	    timeSeparator: ':',
	    nowButtonText: 'Hora actual',
	    showNowButton: true,
	    closeButtonText: 'Cerrar',
	    showCloseButton: true,
	});
	$('#id_horaCena').timepicker({
	 	showPeriod: true,
	    showLeadingZero: true,
	    hourText: 'Hora',
	    minuteText: 'Minutos',
	    amPmText: ['AM', 'PM'],
	    timeSeparator: ':',
	    nowButtonText: 'Hora actual',
	    showNowButton: true,
	    closeButtonText: 'Cerrar',
	    showCloseButton: true,
	});
	$('#id_horaMerienda3').timepicker({
		showPeriod: true,
	    showLeadingZero: true,
	    hourText: 'Hora',
	    minuteText: 'Minutos',
	    amPmText: ['AM', 'PM'],
	    timeSeparator: ':',
	    nowButtonText: 'Hora actual',
	    showNowButton: true,
	    closeButtonText: 'Cerrar',
	    showCloseButton: true,
	});
});