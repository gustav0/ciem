$(document).ready(function(){

  $("#link1").click(function(){
       $('#formulario').attr('action', '?d=1');
       $('#formulario').submit();
  });

});

$(document).ready(function(){

  $("#link2").click(function(){
       $('#formulario').attr('action', '?d=2');
       $('#formulario').submit();
  });

});

$(document).ready(function(){

  $("#link3").click(function(){
       $('#formulario').attr('action', '?d=3');
  });

});