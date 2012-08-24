    $(function(){
    	num=0;
        sum=0;
        $('#selCombo').change(function() {
            var obj = document.getElementById('selCombo');
            $('#calorias').text("Calorias = "+ obj.value);
        });
        $('#addAlimento').click(function(){
        	var obj = document.getElementById('selCombo');
        	var ali = document.getElementById('tablaCalc');
        	var contenedor = document.createElement('div');
           	contenedor.id = 'ali'+num;
        	contenedor.innerHTML=obj.value
        	ali.appendChild(contenedor);
            num++;
            aux=num;
        });
        $('#sumarAlimento').click(function(){
            sum=0;
            var alimento = new Array(aux);
            for(i=0 ; i<aux ; i++){
                getali = document.getElementById('ali'+i).innerHTML;
                alimento[i] = parseFloat(getali);
                sum += alimento[i];
            };
            $('#resultado').text("Resultado = "+ sum);
        });

    });