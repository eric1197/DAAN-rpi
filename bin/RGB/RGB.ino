#define LED 8
#define CdsR A7
#define RLED 9
#define GLED 10
#define BLED 11
 
unsigned long lastT;
bool Blink,LEDstate;
int R,G,B,DIP[]={5,4,3,2};
int a;
byte num=0;

void setup() {
    pinMode(LED, OUTPUT);
    pinMode(RLED, OUTPUT);
    pinMode(GLED, OUTPUT);
    pinMode(BLED, OUTPUT);
    for(int i=0; i<4; i++) pinMode(DIP[i], INPUT);
    Serial.begin(9600);
}

void loop() {
    if(Serial.available()>0){
      a=Serial.read();
      if(a=='('){
        R=Serial.parseInt();
        G=Serial.parseInt();
        B=Serial.parseInt();
        analogWrite(RLED,R);
        analogWrite(GLED,G);
        analogWrite(BLED,B);
      }
      else if (a=='1') {LEDstate=1; Blink=0; Serial.println("H");}
      else if (a=='0') {LEDstate=0; Blink=0; Serial.println("L");}
      else if (a=='K') Blink=1;
      digitalWrite(LED, LEDstate);
    }
    num=0;
    for(int i=0; i<4; i++){
      num=(num<<1) + !digitalRead(DIP[i]);
    }
    if(millis()-lastT>1000){
      lastT=millis();
      Serial.print(analogRead(CdsR));
      Serial.print('\t');
      Serial.println(num);
      if(Blink) {digitalWrite(LED, LEDstate); LEDstate=!LEDstate;};
    }
}
