int IN1 = 9;
int IN2 = 8;
int IN3 = 7;    // Input3 conectada al pin 5
int IN4 = 6;    // Input4 conectada al pin 4 
int ENB = 5; // ENB conectada al pin 3 de Arduino
char val ;
char valan;
 #include <SoftwareSerial.h>    // Libreria importada
#define rxPin 10    
#define txPin 11
SoftwareSerial BTSerial(rxPin, txPin); // RX, TX declaracion de un opjeto Serial

  
void setup()
{
 pinMode (ENB, OUTPUT);
 pinMode (IN1, OUTPUT);
 pinMode (IN2, OUTPUT);
 pinMode (IN3, OUTPUT);
 pinMode (IN4, OUTPUT);
 delay(500);
  BTSerial.flush();
  delay(500);
  BTSerial.begin(38400);
  Serial.begin(9600);
  delay(100);
}
void loop()
{
  if(BTSerial.available()) {  //cuando el puento del modulo este enviando  
   val = BTSerial.read();   //lo guando en la variable "myChar"
    Serial.print(val);      //lo mando por el puerto serialde arduino
  }
  if (val != valan){
  switch(val){
  case '0':
  Serial.print("0 funciona");
  digitalWrite (IN1, HIGH);
  digitalWrite (IN2, LOW);  
  digitalWrite (IN3, HIGH);
  digitalWrite (IN4, LOW);
  analogWrite(ENB,250);
    break;
   case '1':
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, HIGH);  
  digitalWrite (IN3, HIGH);
  digitalWrite (IN4, LOW);
  analogWrite(ENB,250);
  break;
  
   case '2':
  digitalWrite (IN1, HIGH);
  digitalWrite (IN2, LOW);  
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, HIGH);
  analogWrite(ENB,250);
  break;
  
   case '3':
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, HIGH);  
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, HIGH);
  analogWrite(ENB,250);
  break;
  
  default:
  analogWrite(ENB,0);
  break; 
  }
val=valan;
}
else {}
}

