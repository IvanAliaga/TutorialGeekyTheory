/* 
   SENSOR_ULTRASONIDO.ino
   Creada por Ivan Aliaga, el 14 de Octubre del 2013
   HC-SR04 Sensor de Ultrasonido
   Arduino + Python - Envíar un correo electrónico
   Tutorial para http://www.geekytheory.com
   VCC al arduino 5v
   GND al arduino GND
   Echo del Arduino pin 8 Trig para Arduino pin 7
   Proyecto modificado de Virtualmix
   Más información: http://goo.gl/kJ8Gl
 */
#define trigPin 8                                         //Definimos Trigger pin
#define echoPin 7                                         //Definimos Echo pin

int rangoMaximo = 40;                                     //Rango máximo necesitado
int rangoMinimo = 0;                                      //Rango mínimo necesitado
int duracion, distancia;
void setup() {
    Serial.begin (9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop() {   
    digitalWrite(trigPin, HIGH);                          //El siguiente ciclo trigPin / echoPin
    delayMicroseconds(1000);                              //se utiliza para determinar la distancia del
    digitalWrite(trigPin, LOW);                           //objeto más cercano haciendo rebotar ondas sonoras fuera de ella
    duracion = pulseIn(echoPin, HIGH);                    //Determina la duración
    
    distancia = (duracion/2) / 29.1;                      //Calcula la distancia en cm
    if (distancia >= rangoMaximo || distancia <= rangoMinimo){
      Serial.println("La casa está segura.");             //Envía a la computadora por el puerto serial el mensaje: 'La casa está segura.'
    } else {
      Serial.println("Hay un intruso en la casa.");        //Envía a la computadora por el puerto serial el mensaje: 'Hay un intruso en la casa.'
    }
    delay(500);                                           // Hace un retardo de 0.5 segundos antes de la próxima lectura.
}
