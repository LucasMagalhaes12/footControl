#define pot A0

int buttonsPort[] = {8, 9};
int lastPotValue;

#define potInput A0

class Pot {
    private:
        int lastValue;
        int currentValue;

    public:
        Pot() {
            lastValue = analogRead(potInput);
		}


		void update() {
			currentValue = analogRead(potInput);
			int difference = abs(currentValue - lastValue);

			if (difference > 10) {
				//Serial.print("AUDIO#");
				//Serial.println(potValue);
				lastValue = currentValue;
			}
		}
};


Pot pot;


void setup() {
	for (int i=0; i<2; i++)
	    pinMode(buttonsPort[i], INPUT_PULLUP);

    Serial.begin(9600);
	

	// lastPotValue = analogRead(pot);
}


void loop() {
	buttonUpdate();
	pot.update();
}
