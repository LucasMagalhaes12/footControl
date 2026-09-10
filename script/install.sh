echo create python venv
python3 -m venv .venv
echo activate env
source .venv/bin/activate
echo install pip packages
pip3 install pyserial pyautogui

