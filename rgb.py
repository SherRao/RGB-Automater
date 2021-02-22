import mouse;
import pyautogui;
import time;
import rgb_off;
import rgb_on;

# Constants used for typing program names .
ARMOURY = "ARMOURY CRATE"
FUSION = "RGBFusion 2.0";

# Constants used for different coordinates of different buttons on the ASUS ArmouryCrate software. 
ARMOURY_AURA_X = 315;
ARMOURY_AURA_Y = 130;
ARMOURY_OFF_X = 463;
ARMOURY_OFF_Y = 412;
#ARMOURY_ON_X = 463;
#ARMOURY_ON_Y = 412;
ARMOURY_ESC_X = 1652;
ARMOURY_ESC_Y = 10;

# Constants used for different coordinates of different buttons on the Gigabyte RGBFusion 2.0 software. 
FUSION_OFF_X = 961;
FUISON_OFF_Y = 711;
#FUSION_ON_X = 961;
#FUISON_ON_Y = 711;
#FUISON_ESC_X = 1652;
#FUISON_ESC_Y = 10;

"""
Prompts the user on what they would like to do.
"""
def main():
    buttons = ['Turn Off', 'Turn On', 'Debug'];
    user_in = pyautogui.confirm(text='What would you like to do?', title='RGB Automater', buttons=buttons);
    if(user_in == buttons[0]):
        rgb_off.armourycrate();
        rgb_off.fusion();

    elif(user_in == buttons[1]):
        return;

    else:
        print_pos();

"""
Constantly prints the position of the mouse cursor to allow debugging.
"""
def print_pos():
    while(True):
        print(mouse.get_position());


if(__name__ == "__main__"):
    main();