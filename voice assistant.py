import tkinter as tk
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Text-to-Speech engine setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

# Recognizer setup
recognizer = sr.Recognizer()

# Functions
def speak(text):
    output_box.insert(tk.END, f"Assistant: {text}\n")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with sr.Microphone() as source:
            speak("Listening...")
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            output_box.insert(tk.END, f"You: {command}\n")
            process_command(command)
    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
    except sr.RequestError:
        speak("Could not request results. Check your internet.")
    except Exception as e:
        speak(f"Error: {str(e)}")

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time_now}")
    elif "date" in command:
        date_now = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {date_now}")
    elif "search" in command:
        speak("What would you like to search for?")
        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio).lower()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching Google for {query}")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        root.quit()
    else:
        speak("Sorry, I don't understand that command yet.")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("400x500")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Voice Assistant", font=("Arial", 18)).pack(pady=10)

output_box = tk.Text(root, height=20, wrap=tk.WORD)
output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

listen_button = tk.Button(root, text="Speak", font=("Arial", 12), bg="blue", fg="white", command=listen_command)
listen_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit)
exit_button.pack(pady=5)

root.mainloop()