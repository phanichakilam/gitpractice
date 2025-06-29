import tkinter as tk
from tkinter import messagebox
import threading
import time

# Create main window
root = tk.Tk()
root.title("Rainbow and Indian Flag Boxes (Canvas-Based)")

# Track last interaction time
last_interaction_time = {'time': time.time()}
initial_prompt_shown = {'shown': False}

# Store canvas boxes
boxes = {}

# Row definitions
first_row = [1, 2, 3]
second_row = [4, 5, 6]

# Rainbow colors (ROYGBIV)
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# Indian flag colors
indian_flag_colors = ['orange', 'white', 'green']

def idle_monitor():
    """Monitor idle time and prompt after 10 seconds of inactivity"""
    while True:
        time.sleep(1)
        if time.time() - last_interaction_time['time'] >= 10:
            messagebox.showinfo("Idle Notice", "Please select a box.")
            last_interaction_time['time'] = time.time()

def reset_boxes():
    """Clear all canvas drawings"""
    for box in boxes.values():
        box.delete("all")
        box.create_text(100, 70, text="Touch Box", font=('Arial', 12))

def draw_rainbow(canvas):
    """Draw rainbow stripes inside the canvas"""
    stripe_height = 20
    for idx, color in enumerate(rainbow_colors):
        canvas.create_rectangle(0, idx * stripe_height, 200, (idx + 1) * stripe_height, fill=color, width=0)

def draw_indian_flag(canvas):
    """Draw Indian flag inside the canvas"""
    canvas.create_rectangle(0, 0, 200, 40, fill='orange', width=0)
    canvas.create_rectangle(0, 40, 200, 80, fill='white', width=0)
    canvas.create_rectangle(0, 80, 200, 120, fill='green', width=0)
    # Draw Ashoka Chakra (simplified as a blue circle)
    canvas.create_oval(80, 45, 120, 85, outline='blue', width=3)

def box_clicked(box_number):
    """Handle box click"""
    last_interaction_time['time'] = time.time()
    reset_boxes()

    if box_number in first_row:
        for num in first_row:
            draw_rainbow(boxes[num])

    elif box_number in second_row:
        for num in second_row:
            draw_indian_flag(boxes[num])

def start_program():
    """Show initial prompt once when program starts"""
    if not initial_prompt_shown['shown']:
        messagebox.showinfo("Start", "Please select a box by clicking on any box.")
        initial_prompt_shown['shown'] = True

# Create 6 canvases (3 in each row)
for i in range(2):
    for j in range(3):
        box_number = i * 3 + j + 1
        canvas = tk.Canvas(root, width=200, height=120, bg='white', highlightthickness=2, highlightbackground='black')
        canvas.create_text(100, 70, text="Touch Box", font=('Arial', 12))
        canvas.grid(row=i, column=j, padx=10, pady=10)
        canvas.bind("<Button-1>", lambda event, num=box_number: box_clicked(num))
        boxes[box_number] = canvas

# Show initial prompt after window is ready
root.after(100, start_program)

# Start idle monitoring thread
idle_thread = threading.Thread(target=idle_monitor, daemon=True)
idle_thread.start()

# Start the Tkinter event loop
root.mainloop()
