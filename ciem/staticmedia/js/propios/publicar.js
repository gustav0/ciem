$(document).ready(function(){
	$("#id_title").keyup(function() {
		 $("#id_slug").val($("#id_title").val());
	});
});
