char str;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  if(Serial.available() > 0){
    str = Serial.read();

    if(str == 'A'){
      digitalWrite(LED_BUILTIN, HIGH);
    }

    if(str == 'B'){
      digitalWrite(LED_BUILTIN, LOW);
    }

    if(str == 'C'){
      digitalWrite(LED_BUILTIN, HIGH);
      delay(200);
      digitalWrite(LED_BUILTIN, LOW);
      delay(200);
    }
  }
}
