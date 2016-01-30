/*El programa es una fincion auxiliar del controlados de motores l298n.   
	Desde el progamam principal se yamara a la funcion "motores" e ira acompañada dos numeros entero los cules
	indicaran el sentido y la velocidad de los motores, si todo es correcto el programa principal recivira el numero 1,
	encamvio si algo falla los errores seran macados de la sigiente manera.
_________________________________________________________________________________________________________________________
Errores.________________________________________________ 		| Pines.____________________|	____________________
	Numero 	Motibo										|		| MD	8		/	MI 	7	| 	|___AVISO___		|
	  2		El valor de la velocidad no es adecuado.	|		| 		9		/		6	|	|Definis los Pines 	|
	  3		El valor del sentido no esta definido.		|		|		5				VI 	|	|de cada motor.		|
	  4 	Falta el valor de velocidad.				|		|___________________________|	|___________________|		
	  5 	Flata el valor del sentido.					|						Proyecto:	Base
________________________________________________________|						Creador:	NoX
*/

int motores (int Velocidad , int Sentido){
//Declaracion de pines 
	pinMode(8, OUTPUT);
	pinMode(9, OUTPUT);
	pinMode(7, OUTPUT);
	pinMode(6, OUTPUT);
	pinMode(5, OUTPUT);
 
// Comprobacion de errores

	if(Velocidad <= 0 || Velocidad > 225){
		if(Velocidad == 0 ){return 4; } else {return 2;} }

	else if (Sentido !=9 || Sentido !=6 || Sentido !=10 || Sentido !=5 || Sentido !=11){
		if (Sentido == 0){return 5;} else {return 3;} }
;
	else {  if(Velocidad > 100) {Velocidad = 100;}  //si y solo si los motores seon de 3V
		// Declaracion de casos
		switch(Sentido){
			case 9: // avanti
				digitalWrite (8, 1);
				digitalWrite (9, 0;
				digitalWrite (7, 0);
				digitalWrite (6, 1);
					analogWrite(5,Velocidad);
					
			break;

			case 6: // indietro
				digitalWrite (8, 0);
				digitalWrite (9, 1);
				digitalWrite (7, 1);
				digitalWrite (6, 0);
					analogWrite(5,Velocidad);
					
			break;

			case 10: // svoltare a destra
				digitalWrite (8, 1);
				digitalWrite (9, 0);
				digitalWrite (7, 1);
				digitalWrite (6, 0);
					analogWrite(5,Velocidad);
					
			break;

			case 5: // svoltare a sinistra
				digitalWrite (8, 0);
				digitalWrite (9, 1);
				digitalWrite (7, 0);
				digitalWrite (6, 1);
					analogWrite(5,Velocidad);
					
			break;

			case 11: //smettere
				digitalWrite (8, 0);
				digitalWrite (9, 0);
				digitalWrite (7, 0);
				digitalWrite (6, 0);
					analogWrite(5,0);
					analogWrite(VI,0);
			break;
		return 1;
		}
	}
}
