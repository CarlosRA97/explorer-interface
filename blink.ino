/* Este programa crea un parpadeo en el pin 13 de arduino, dicho pin esta unido a un led de manera que no es necesario 
formar un montaje para comprobarlo*/
boolean estado = false; //declaras una bariable logica

void setup(){
	pinMode(13, OUTPUT); // declaras el pin de salida
}

void loop(){
	estado = !estado;
	digitalWrite(13, estado);// decraras el estado del pin
	delay(1000); //detienes el programa un tiempo (nanosegundos)
}
