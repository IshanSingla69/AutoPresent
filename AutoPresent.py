import speech_recognition as sr
import pyautogui as pag
import pygetwindow as gw
recognizer = sr.Recognizer()

all_commands = {
    "next slide",
    "previous slide",
    "minimize window",  
    "minimise window",
}

def nextSlide():
    pag.press("right")
def previousSlide():
    pag.press("left")
def minimizeWindow():
    pag.hotkey("win", "down")
def maximizeWindow():
    pag.hotkey("win", "up")

def is_powerpoint_in_focus():
    active_window = gw.getActiveWindow()
    return active_window and "PowerPoint" in active_window.title
        
        
def processCommand(command):
    # break down the comando into words
    words = command.split()
    # check if any contains the word "slide"
    if "slide" in words:
        # check if the previous word is "next"
        if words[words.index("slide") - 1] == "next":
            pag.press("right")
            return True
        # check if the previous word is "previous"
        elif words[words.index("slide") - 1] == "previous":
            pag.press("left")
            return True
    return False
            

# This is the main loop
while True:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        #divide the audio into phrases of 5 seconds
        #audio = recognizer.listen(source, phrase_time_limit=5)
        #listen in background
        audio = recognizer.listen(source,phrase_time_limit=5)

    if is_powerpoint_in_focus():
        
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            if processCommand(text):
                print("Command processed")
            else:
                print("Command not recognized")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    else:
        print("PowerPoint is not in focus")
        print("Please, click on the PowerPoint window")
        print("Press Ctrl+C to exit")
        while not is_powerpoint_in_focus():
            pass
        print("PowerPoint is now in focus")
        print("Listening...")