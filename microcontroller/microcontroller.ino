

Pot pot;
Button buttons;


void setup() {
    Serial.begin(9600);
	buttons.begin();
}


void loop() {
	buttons.update();
//	pot.update();
}


class Pot {
    private:

	int lastValue;
	int currentValue;
	int difference;
	int port = A0;

    public:

	Pot() {
		lastValue = analogRead(port);
	}

	void update() {
		currentValue = analogRead(port);
		difference = abs(currentValue - lastValue);

		if (difference > 10) {
			//Serial.print("AUDIO#");
			//Serial.println(potValue);
			lastValue = currentValue;
		}
	}
};


class Button {
	/*
	MODES:
	0 Programs
	1 Audio
	2 Automação
	*/

	private:

	int mode = 0;
	bool buttons[2] = {false, false};
	int port[2] = {8, 9};

	public:

	void begin() {
		for (int i=0; i<2; i++)
			pinMode(port[i], INPUT_PULLUP);
	}

	void update() {
		for (int i=0; i<2; i++) {
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
