#include <Servo.h>
Servo servo;
int pushButton = 2;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  // make the pushbutton's pin an input:
  pinMode(pushButton, INPUT);
  servo.attach(7);
}

void loop() {
  // put your main code here, to run repeatedly:

  int buttonState = digitalRead(pushButton);

  if( buttonState == 0 )
  {
    servo.write(175);
    delay(500);
  }
  else if( buttonState == 1 )
  {
    servo.write(100);
    delay(500);
  }
}
