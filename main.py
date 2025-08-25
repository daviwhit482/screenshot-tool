import tkinter as tk
import pyautogui
import win32clipboard
import io
from pynput import keyboard
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog

# Functions
def take_screenshot_clipboard():
    screenshot = pyautogui.screenshot()
    copy_to_clipboard(screenshot)
    print("Screenshot was taken!")

    messagebox.showinfo("Success", "Screenshot copied to clipboard!")

def copy_to_clipboard(image):
    # Convert the image to bitmap format
    output = io.BytesIO()
    image.save(output, 'BMP')
    data = output.getvalue()[14:]  # Remove the BMP header

    # Put on clipboard
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

    print("Screenshot copied to clipboard!")

def on_key_press(key):
    if key == keyboard.Key.f12:
        take_screenshot_clipboard()
    
def take_screenshot_save():
    screenshot = pyautogui.screenshot()

    # Timestamp for filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    default_filename = f"screenshot_{timestamp}.png"

    # Ask user for save location
    filename = filedialog.asksaveasfilename(
        defaultextension=".png",
        initialfile=default_filename,
        filetypes=[("PNG files", "*.png"),("JPEG files", "*.jpg;*.jpeg"),("BMP files", "*.bmp"),("All files", "*.*")]
    )

    if filename:
        screenshot.save(filename)
        messagebox.showinfo("Success", f"Screenshot saved as {filename}!")
        print(f"Screenshot saved as {filename}!")
    else:
        print("Save cancelled.")

# Keyboard listener for F12 shortcut

listener = keyboard.Listener(on_press=on_key_press)
listener.start()

# Creating window
root = tk.Tk()
root.title("Screenshot Tool")
root.geometry("250x250")
root.resizable(False, False)

# Adding buttons
button = tk.Button(
    root,
    text="Copy to Clipboard",
    font=("Arial", 12),
    bg ="#95D8FF",  # Green background
    fg="white",       # White text
    width=18,
    height=2,
    relief="ridge",
    command=take_screenshot_clipboard
)
button2 = tk.Button(
    root,
    text="Save to File",
    font=("Arial", 12),
    bg ="#95D8FF",  # Green background
    fg="white",       # White text
    width=18,
    height=2,
    relief="ridge",
    command=take_screenshot_save
)

button.pack(pady=10, expand=True)
button2.pack(pady=5, expand=True)

root.configure(bg="#f0f0f0")  # Light grey background

# Adding labels

f12_label = tk.Label(
    root,
    text="(Or F12 to copy to clipboard)",
    font=("Arial", 8)
)
f12_label.pack(side=tk.BOTTOM, pady=10)

made_by_label = tk.Label(
    root,
    text="Made by David White",
    font=("Arial", 8)
)
made_by_label.pack(side=tk.BOTTOM, pady=10)

# Running the application

root.mainloop()