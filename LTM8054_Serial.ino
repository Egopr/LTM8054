int lavr;
void setup() {
  
  pinMode(2, OUTPUT);
  Serial.begin(115200);
  digitalWrite(2, LOW);
  pinMode(3, OUTPUT);

}

void loop() {

  
 if (Serial.available() > 0) 
 {
    lavr = Serial.parseInt();
    switch (lavr) {
    case 1:
      digitalWrite(2, LOW);
      digitalWrite(3, HIGH);
      Serial.println("Reley ON");
      break;
    case 2:
      digitalWrite(2, HIGH);
      digitalWrite(3, LOW);
      Serial.println("Relay    OFF");
      break;
  }

}
}
