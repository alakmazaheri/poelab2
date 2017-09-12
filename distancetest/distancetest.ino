const byte analogInPin = A0;
float sensor_value;

void setup() {
  Serial.begin(9600);
}

void loop() {
  sensor_value = analogRead(analogInPin);
  Serial.println(sensor_value);
}
