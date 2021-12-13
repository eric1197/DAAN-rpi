#define LED 10
#define CdsR A7
unsigned long lastT;

void setup() {
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if(Serial.available()>0){
      String a=Serial.readString();
      if(a=="1") digitalWrite(LED, LOW);
      else if (a=="0") digitalWrite(LED, HIGH);
    }
    if(millis()-lastT>1000){
      lastT=millis();
      Serial.println(analogRead(CdsR));
    }
}