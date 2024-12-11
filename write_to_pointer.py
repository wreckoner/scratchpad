import pyautogui
import pynput.mouse
import time

# Function to get current mouse position
def get_mouse_position():
    mouse_controller = pynput.mouse.Controller()
    return mouse_controller.position

# Function to type text at the current mouse position
def type_at_mouse_position(text):
    # Get current mouse position
    current_pos = get_mouse_position()
    pyautogui.click(current_pos)  # Click at the mouse position (optional but ensures focus)
    pyautogui.typewrite(text)  # Type the user input at the current mouse position

if __name__ == "__main__":
    # Give a prompt and wait for user input
    user_input = input("Enter the text you want to type at the current mouse pointer location: ")

    # Allow a small delay to move the mouse before typing
    time.sleep(5)

    # Type the input at the current mouse location
    type_at_mouse_position(user_input)
