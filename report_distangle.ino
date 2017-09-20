#include <Servo.h>

const byte analogInPin = A0;
float sensor_value; 
int pos = 0;    // variable to store the servo position
int i = 0;
Servo servo1; 

void setup() {
  Serial.begin(9600);
  servo1.attach(9); 
}

void loop() {
 for (i = 0; i < 3; i++){
  for (pos = 60; pos <= 120; pos += 1) { // goes from 0 degrees to 180 degrees
    servo1.write(pos);
    delay(15);
    sensor_value = analogRead(analogInPin);
    if(pos % 5 == 0){
      Serial.println(pos);
      Serial.println(sensor_value);
      Serial.println("----------");
    }
    delay(50);
  }
  for (pos = 120; pos >= 60; pos -= 1) { // goes from 180 degrees to 0 degrees
    servo1.write(pos);
    delay(15);
    sensor_value = analogRead(analogInPin);
    if(pos % 5 == 0){
      Serial.println(pos);
      Serial.println(sensor_value);
      Serial.println("----------");
    }
    delay(50);
  }
 }
 while(true)
 {}

}

