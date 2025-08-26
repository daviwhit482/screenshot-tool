import tkinter as tk
import pyautogui
import win32clipboard
import io
import pystray
import threading
import requests
import base64
from PIL import Image, ImageDraw
from pynput import keyboard
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog

# Functions

def image_to_base64(image):
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    
    image_data = buffer.getvalue()
    
    # Convert image to text to upload to ImgBB
    base64_text = base64.b64encode(image_data).decode('utf-8')
    
    return base64_text

def upload_to_imgbb(image):
    API_KEY = "8edacffa18ffa3178d47a7261a44f311"
    
    # Using above function to convert image to text
    image_text = image_to_base64(image)
    
    # ImgBB upload URL
    url = f"https://api.imgbb.com/1/upload?key={API_KEY}"
    
    # What's being sent to ImgBB
    package = {
        'image': image_text
    }
    
    try:
        response = requests.post(url, data=package)
        
        # 200 is status code for OK
        if response.status_code == 200:
            result = response.json()
            image_url = result['data']['url']
            return image_url
        else:
            print(f"Upload failed: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error uploading: {e}")
        return None
    
def show_link_popup(url):
    # Create the new popup window for the URL when you copy with link
    popup = tk.Toplevel(root)
    popup.title("Image Uploaded Successfully!")
    popup.geometry("500x200")
    popup.resizable(False, False)
    
    # Makes it stay on top
    popup.attributes('-topmost', True)
    
    # Success message
    success_label = tk.Label(
        popup, 
        text="Screenshot uploaded! Link: ",
        font=("Arial", 10)
    )
    success_label.pack(pady=10)
    
    # Text box with the URL
    url_entry = tk.Entry(
        popup,
        width=60,
        font=("Arial", 10)
    )
    url_entry.insert(0, url)  # Puts the URL in the text box
    url_entry.pack(pady=10)
    
    # Selects all text automatically
    url_entry.select_range(0, tk.END)
    url_entry.focus()
    
    # Copy to clipboard button
    def copy_url():
        popup.clipboard_clear()
        popup.clipboard_append(url)
        copy_btn.config(text="Copied!")
        popup.after(1000, lambda: copy_btn.config(text="Copy to Clipboard"))
    
    copy_btn = tk.Button(
        popup,
        text="Copy to Clipboard",
        command=copy_url,
        bg="#4CAF50",
        fg="white",
        width=20
    )
    copy_btn.pack(pady=5)
    
    # Close button
    close_btn = tk.Button(
        popup,
        text="Close",
        command=popup.destroy,
        width=20
    )
    close_btn.pack(pady=5)

def take_screenshot_upload():
    screenshot = pyautogui.screenshot()
    
    print("Screenshot taken, uploading...")
    
    # Uses above function to upload
    image_url = upload_to_imgbb(screenshot)
    
    # Checks if the upload was successful
    if image_url:
        print(f"Upload successful: {image_url}")
        
        # Automatically copy URL to clipboard
        root.clipboard_clear()
        root.clipboard_append(image_url)
        
        # Show the popup with the link
        show_link_popup(image_url)
        
    else:
        # Upload failed
        messagebox.showerror("Upload Failed", "Could not upload screenshot to ImgBB. Check your internet connection.")

def create_tray_icon():
    image = Image.new('RGB', (64, 64), color='blue')
    
    draw = ImageDraw.Draw(image)
    draw.rectangle([16, 20, 48, 44], fill='white')
    draw.rectangle([20, 24, 44, 40], fill='black')
    
    return image

def show_main_window():
    root.deiconify()
    root.lift()

def hide_main_window():
    root.withdraw()

def exit_app():
    tray_icon.stop()
    root.quit()

def create_tray_menu():
    menu = pystray.Menu(
        pystray.MenuItem('Capture Screenshot', take_screenshot_clipboard, default=True), # default=True makes it so when left clicking tray icon it does this function
        pystray.MenuItem('Show', show_main_window),
        pystray.MenuItem('Hide', hide_main_window),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem('Exit', exit_app)
    )
    return menu

def start_tray_icon():
    global tray_icon

    tray_icon = pystray.Icon(
        name = "Screenshot Tool",
        icon = create_tray_icon(),
        title = "Screenshot Tool - Right click for options",
        menu=create_tray_menu()
    )

    tray_icon.run()

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
root.geometry("250x320")
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

button3 = tk.Button(
    root,
    text="Upload & Share",
    font=("Arial", 12),
    bg="#FF9800",  # Orange background  
    fg="white",
    width=18,
    height=2,
    relief="ridge",
    command=take_screenshot_upload
)

button.pack(pady=10, expand=True)
button2.pack(pady=5, expand=True)
button3.pack(pady=5, expand=True)

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

# Start tray icon in a separate thread
tray_thread = threading.Thread(target=start_tray_icon, daemon=True)
tray_thread.start()

# Running the application
root.mainloop()