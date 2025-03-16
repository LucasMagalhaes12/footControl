#define pot A0


int lastPotValue;
int buttonsPort[] = {8, 9};
bool buttons[] = {false, false};


void buttonUpdate() {
	for (int i=0; i<2; i++) {
		if (buttons[i] != !digitalRead(buttonsPort[i]))
			buttons[i] = !buttons[i];

		if (buttons[i]) {
			Serial.print("BUTTON#");
			Serial.println(i);
			delay(200);
		}
	}
}


void potUpdate() {
	int potValue = analogRead(pot);
	int difference = abs(potValue - lastPotValue);

	if (difference > 10) {
		Serial.print("AUDIO#");
		Serial.println(potValue);
		lastPotValue = potValue;
	}
}


void readMsg() {
	char msg = Serial.read();
	if (msg != -1) 
		Serial.println(msg);
}


void setup() {
	for (int i=0; i<2; i++)
	    pinMode(buttonsPort[i], INPUT_PULLUP);

    Serial.begin(9600);
	lastPotValue = analogRead(pot);
}


void loop() {
	buttonUpdate();
	potUpdate();

}
