/*En este programa crearemos base de comunicacion entre el arduino y un ordenador mediante un puerto seria.

          |-------------------------------------|
          |   AVISO                             |
          | Debes yamar a la viblioteca en el   |
          | progama principal.                  |
          | -->import processing.serial.*;<--   |
          |-------------------------------------|
*/
int comunicacion(int Sentido){

Serial port;                             // Creas un opjeto Serial                            
  port = new Serial(this, Serial.list()[0], 9600);        //Declaramos las culidades del puerto

//Emision
port.write(Sentido);
return(Sentido);
}
