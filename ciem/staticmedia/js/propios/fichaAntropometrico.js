function cargarContenido(nombre,fecha,peso,cirCi,cirCa,estatura,hiper,diabetes,cancer,trigli){
	var contenedor;
	contenedor = document.getElementById("info");
	texto = "<div style=\"font-weight:bold;margin-bottom:10px;color: #3F3F3F;\">Creado por "+nombre+" el "+fecha+"</div>"+
	"<div class=\"variableMas\"><div class=\"varLabel\">Peso: </div><div class=\"varContenido\">"+peso+" Kg</div></div>"+
	"<div class=\"variableMas\"><div class=\"varLabel\">Circunferencia de cintura: </div><div class=\"varContenido\">"+cirCi+" cm</div></div>"+
	"<div class=\"variableMas\"><div class=\"varLabel\">Circunferencia de cadera: </div><div class=\"varContenido\">"+cirCa+" cm</div></div>"+
	"<div class=\"variableMas\"><div class=\"varLabel\">Estatura: </div><div class=\"varContenido\"> "+estatura+" cm</div></div>"+
	"<div class=\"variableMas\"><div class=\"varLabel\">Hipertención: </div><div class=\"varContenido\"> "+hiper+"</div></div>"+
	"<div class=\"variableMas\"><div class=\"varLabel\">Diábetes: </div><div class=\"varContenido\"> "+diabetes+"</div></div>"+
	"<div class=\"variableMas\"><div class=\"varLabel\">Cancer: </div><div class=\"varContenido\"> "+cancer+"</div></div>"+
	"<div class=\"variableMas\"><div class=\"varLabel\">Triglicéridos: </div><div class=\"varContenido\"> "+trigli+"</div></div>"
	;
	contenedor.innerHTML = texto

	setVisible('pop');
}