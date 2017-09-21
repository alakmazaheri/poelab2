#include <Servo.h>

const byte analogInPin = A0;
float sensor_value; 
float sensor_value1;
float sensor_value2;
float sensor_value3;
int pos = 0;    // variable to store the servo position
int i = 0;
Servo servo1; 

void setup() {
  Serial.begin(9600);
  servo1.attach(9); 
}

void loop() {
 for (i = 0; i < 1; i++){
  for (pos = 60; pos <= 120; pos += 1) { // goes from 0 degrees to 180 degrees
    servo1.write(pos);
    delay(30);
    sensor_value1 = analogRead(analogInPin);
    delay(50);
    sensor_value2 = analogRead(analogInPin);
    delay(50);
    sensor_value3 = analogRead(analogInPin);
    sensor_value = (sensor_value1 + sensor_value2 + sensor_value3)/3;
    
    if(pos % 1 == 0){
      Serial.println(pos);
      Serial.println(sensor_value);
    }
    delay(50);
  }
  for (pos = 120; pos >= 60; pos -= 1) { // goes from 180 degrees to 0 degrees
    servo1.write(pos);
    delay(30);
    sensor_value1 = analogRead(analogInPin);
    delay(50);
    sensor_value2 = analogRead(analogInPin);
    delay(50);
    sensor_value3 = analogRead(analogInPin);
    sensor_value = (sensor_value1 + sensor_value2 + sensor_value3)/3;
    
    if(pos % 1 == 0){
      Serial.println(pos);
      Serial.println(sensor_value);
    }
    delay(50);
  }
 }
 Serial.println(42);
 while(true)
 {}

}

