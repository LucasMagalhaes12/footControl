#define button 11

#define potGround A0
#define pot5v A4
#define potRead A2


bool stateButton = false;
int lastPotValue;

void setup() {
    pinMode(button, INPUT_PULLUP);
    Serial.begin(9600);


	pinMode(potGround, OUTPUT);
	pinMode(pot5v, OUTPUT);

	digitalWrite(potGround, LOW);
	digitalWrite(pot5v, HIGH);
	
	lastPotValue = analogRead(potRead);
}


void loop() {
	if (stateButton != !digitalRead(button))
		stateButton = !stateButton;

	if (stateButton) {
		Serial.println("bt2");
		//stateButton = false;
		delay(200);
	}

	char msg = Serial.read();
	if (msg != -1) 
		Serial.println(msg);
	

	int potValue = analogRead(potRead);
	int difference = abs(potValue - lastPotValue);
	if (difference > 100) {
		Serial.print("AUDIO#");
		Serial.println(potValue);
		lastPotValue = potValue;
	}
}
