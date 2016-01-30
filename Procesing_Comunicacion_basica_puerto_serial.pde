import processing.serial.*; //inportamos la libreria de procesing
Serial port; //creamos un opjeto serial "port"
void setup(){
  port = new Serial(this, "COM44", 9600); /*definimos "port" como un pueto de comunicon 
                                          en eta maquina mediante el puerto "COM44" a una veocidad es 9600*/
}
void draw(){} // lo aplicamos para mantener el bucle
//llamamos a la funcion keyPressed para leer las teclas
void keyPressed() {
  //cleamos una bariable local pra para definir los casos
  char letter = key;
  //dependidendo de la barable se imprime un caracter en el puerto serial
  switch(letter) {
    case 'w': 
     port.write('0'); 
      break;
    case 'a': 
      port.write('1');  
      break;
    case 's': 
      port.write('2');  
      break;
    case 'd': 
      port.write('3');  
      break;
    default:            
        port.write('8');  
      break;
  }
}