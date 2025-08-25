# Import tkinter to make the GUI window
import tkinter as tk

# Import pyperclip to copy text to clipboard
import pyperclip

# This list contains the special characters shown as buttons
CHARACTERS = ['├', '│', '└', '─', '|', '\\', '📁']

# --- Create the main GUI window ---

# This is the main window of the app
root = tk.Tk()

# Set the title text on the top of the window
root.title("Character Picker")

# Import ctypes to get screen size on Windows
import ctypes

# Get screen size information from the system
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Set the window width to 7% of the screen width
window_width = int(screen_width * 0.07)

# Set the window height to 70% of the screen height
window_height = int(screen_height * 0.7)

# Place the window on the right side of the screen
x_pos = screen_width - window_width
y_pos = int(screen_height * 0.15)

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

# Don't allow the user to resize the window
root.resizable(False, False)

# Set the background color of the window to white
root.configure(bg="white")

# This variable stores the selected character
selected_char = tk.StringVar(value="")

# This stores the last selected button, used to highlight it
selected_button = [None]

# This variable controls whether the window stays always on top
always_on_top = tk.BooleanVar(value=False)

# This function is called when the user clicks on a character button
def on_char_click(char, btn):
    # Save the selected character
    selected_char.set(char)
    
    # Reset all buttons to default style
    for b in buttons:
        b.configure(bg="white", relief="flat")

    # Highlight the clicked button with color and border
    btn.configure(bg="#cce5ff", relief="solid")
    
    # Remember this button as the selected one
    selected_button[0] = btn

# This function copies the selected character to the clipboard
def copy_to_clipboard():
    char = selected_char.get()
    if char:
        try:
            pyperclip.copy(char)
        except Exception as e:
            # Print the error if copying fails
            print(f"Clipboard error: {e}")

# This function is called when the "Always on top" checkbox is toggled
def toggle_always_on_top():
    root.attributes("-topmost", always_on_top.get())

# --- Layout and character buttons ---

# Create a frame to hold the character buttons
char_frame = tk.Frame(root, bg="white")

# Add the frame to the window with padding
char_frame.pack(pady=20, padx=10, expand=True, fill="both")

# List to store all character buttons
buttons = []

# Create a button for each character in the list
for c in CHARACTERS:
    # Make a button with the character as the text
    btn = tk.Button(
        char_frame,             # Place it inside the frame
        text=c,                 # Show the character
        font=("Segoe UI Symbol", 16),  # Use a font that supports symbols
        width=3,                # Set button width
        height=1,               # Set button height
        bg="white",             # Set background color
        relief="flat",          # Make the button flat by default
        command=lambda ch=c, b=None: None  # Temporary placeholder
    )

    # Place the button in the frame with some vertical padding
    btn.pack(pady=4, fill="x")

    # Save the button in the list for later use
    buttons.append(btn)

    # Now set the correct command for this button
    btn.configure(command=lambda ch=c, b=btn: on_char_click(ch, b))

# --- Always on top checkbox ---

# Create a checkbox to let user choose if window stays on top
top_check = tk.Checkbutton(
    root,
    text="Always on top",
    variable=always_on_top,
    command=toggle_always_on_top,
    bg="white",
    wraplength=window_width - 50  # word wrap
)

# Add the checkbox below the character buttons
top_check.pack(pady=(0, 10))

# --- Copy Button ---

# Create a green "Copy" button
copy_btn = tk.Button(
    root,
    text="Copy",
    font=("Segoe UI", 12),
    bg="#4CAF50",   # Green color
    fg="white",     # White text
    relief="flat",
    command=copy_to_clipboard  # Call this function when clicked
)

# Place the copy button with some spacing
copy_btn.pack(pady=10, ipadx=10, ipady=5)

# --- Run the app loop ---

# Start the tkinter main loop to show the window and respond to events
root.mainloop()
