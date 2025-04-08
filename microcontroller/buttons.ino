int buttonMode = 0;
bool buttons[] = {false, false};



/*

0 Programas
1 Audio
2 Automação

*/



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