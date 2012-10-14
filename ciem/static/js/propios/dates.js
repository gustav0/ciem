$(document).ready(function(){
    $("#id_fecha_nacimiento").datepicker({
    	clickInput:true, 
        startDate:'01-01-1930',
        dateFormat: "dd-mm-yy",
        defaultDate: "01-01-1970",
        changeMonth: true,
		changeYear: true,
		yearRange: "1930:today"
    });

 });
