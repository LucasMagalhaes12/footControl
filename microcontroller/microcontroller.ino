class Button {
	/*
	MODES:
	0 Programs
	1 Audio
	2 Automação
	*/
	private:

	int mode = 0;
	bool buttons[4] = {false, false, false, false};
	int port[4] = {8, 9, A4, A5};


	public:

	void begin() {
		for (int i=0; i<4; i++)
			pinMode(port[i], INPUT_PULLUP);
	}

	void update() {
		for (int i=0; i<4; i++) {
			if (buttons[i] != !digitalRead(port[i]))
				buttons[i] = !buttons[i];

			if (buttons[i]) {
				Serial.print("BUTTON#");
				Serial.println(i);
				delay(200);
			}
		}
	}
};


class Pot {
    private:

	int lastValue;
	int currentValue;
	int port;
	const char * nameOutput;

    public:

	Pot(const char * function, int connectedPort) {
		port = connectedPort;
		nameOutput = function;
		lastValue = analogRead(port);
	}

	void sendMouseInfo() {
		currentValue = analogRead(port);

		if (((currentValue / 100) - 5)) {
			Serial.print(nameOutput);
			Serial.println((currentValue / 100) - 5);
			lastValue = currentValue;
		}
	}

	void sendVolumeInfo() {
		currentValue = analogRead(port);
		if (abs(currentValue - lastValue) > 10) {
			Serial.print(nameOutput);
			Serial.println(currentValue);
			lastValue = currentValue;
		}
	}
};


// Pot volume("VOLUME#", A0);
Pot mouseX("MOUSE#X", A1);
Pot mouseY("MOUSE#Y", A2);
Button buttons;


void setup() {
    Serial.begin(9600);
	buttons.begin();
}


void loop() {
	buttons.update();
	// volume.sendVolumeInfo();
	mouseX.sendMouseInfo();
	mouseY.sendMouseInfo();
}
