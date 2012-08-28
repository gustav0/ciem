    $(function(){
    	num=0;
        sum=0;
        check=true;
        $('#selCombo').change(function() {
            var obj = document.getElementById('selCombo');
            $('#calorias').text("Calorias = "+ obj.value);
        });
        $('#addAlimento').click(function(){
            if(check){
                var ali = document.getElementById('tablaCalc');
                var caloriaT = document.createElement('div');
                var alimentoT = document.createElement('div');
                caloriaT.id = 'caloriaT';
                caloriaT.innerHTML='Calorias';
                alimentoT.id = 'alimentoT';
                alimentoT.innerHTML='Nombre';
                ali.appendChild(alimentoT);
                alimentoT.appendChild(caloriaT);
                check=false;
            }
        	var obj = document.getElementById('selCombo');
            var ali = document.getElementById('tablaCalc');
        	var contenedor = document.createElement('div');
            var nombrealimento = document.createElement('div');
           	contenedor.id = 'ali'+num;
            contenedor.className = 'caloriasT'
            nombrealimento.className = 'alimentosT';
        	contenedor.innerHTML=obj.value;
            nombrealimento.innerHTML= obj.options[obj.selectedIndex].text;
            ali.appendChild(nombrealimento);
            nombrealimento.appendChild(contenedor);
            
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