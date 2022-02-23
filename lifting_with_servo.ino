#include <Servo.h>
Servo servo;

int pos = 0;
void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

  servo.attach(13);
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue = analogRead(A0);
  
  if(sensorValue > 950)
  {
    for(pos = 100; pos <= 155; pos += 1)
    {
      servo.write(pos);
      delay(10);
    }
    delay(500);
    for(pos = 155; pos >= 100; pos -= 1)
    {
      servo.write(pos);
      delay(10);
    }
    delay(500);
  }
  
}
