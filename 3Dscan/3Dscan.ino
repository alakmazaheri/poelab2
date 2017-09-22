#include <Servo.h>

const byte analogInPin = A0;
float sensor_value; 
float sensor_value1;
float sensor_value2;
float sensor_value3;
int pos;
int i;
Servo servo1; 
Servo servo2;

void setup() {
  Serial.begin(9600);
  servo1.attach(9); 
  servo2.attach(10);
}

void loop() {
 for (i = 90; i < 120; i+=5 ){
  for (pos = 60; pos <= 120; pos += 1) { // pans from 60 to 120 degrees
    servo1.write(pos); 
    delay(30); sensor_value1 = analogRead(analogInPin); 
    delay(50); sensor_value2 = analogRead(analogInPin); 
    delay(50); sensor_value3 = analogRead(analogInPin);
    sensor_value = (sensor_value1 + sensor_value2 + sensor_value3)/3;
    Serial.println(pos);
    Serial.println(sensor_value);
    delay(50);
  }

  servo2.write(i); delay(30);
  i += 5;
  
  for (pos = 120; pos >= 60; pos -= 1) { // goes from 180 degrees to 0 degrees
    servo1.write(pos);
    delay(30); sensor_value1 = analogRead(analogInPin);
    delay(50); sensor_value2 = analogRead(analogInPin);
    delay(50); sensor_value3 = analogRead(analogInPin);
    sensor_value = (sensor_value1 + sensor_value2 + sensor_value3)/3;
    
    Serial.println(pos);
    Serial.println(sensor_value);
    delay(50);
  }

  servo2.write(i); delay(30);
  
 }
 Serial.println(666);
 while(true){}

}
