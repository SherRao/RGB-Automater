import mouse;
import pyautogui as keyboard;
import time;
import rgb;

def armourycrate():
    keyboard.press('winleft');
    time.sleep(0.25);
    keyboard.typewrite(rgb.ARMOURY);
    keyboard.press('enter');
    time.sleep(3);
    keyboard.hotkey('winleft', 'up');
    time.sleep(1);

    mouse.move(rgb.ARMOURY_AURA_X, rgb.ARMOURY_AURA_Y);
    time.sleep(0.25);
    mouse.click();
    time.sleep(3);

    mouse.move(rgb.ARMOURY_OFF_X, rgb.ARMOURY_OFF_Y);
    time.sleep(0.25);
    mouse.click();
    time.sleep(0.25);

    mouse.move(rgb.ARMOURY_ESC_X, rgb.ARMOURY_ESC_Y);
    time.sleep(0.25);
    mouse.click();
    time.sleep(0.25);


def fusion(): 
    print("A");
    keyboard.press('winleft');
    time.sleep(0.25);
    keyboard.typewrite(rgb.FUSION);
    time.sleep(0.25);
    keyboard.press('enter');
    time.sleep(3);