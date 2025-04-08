void readMsg() {
	char msg = Serial.read();
	if (msg != -1) 
		Serial.println(msg);
}