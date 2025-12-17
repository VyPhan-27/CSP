# p227_starter_one_button_shell.py

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter.filedialog import asksaveasfilename

def mSave():
    filename = asksaveasfilename(defaultextension='.txt',
                                 filetypes=(('Text files', '*.txt'),
                                            ('Python files', '*.py *.pyw'),
                                            ('All files', '*.*')))
    if filename is None:
        return
    with open(filename, mode='w') as file:
        text_to_save = command_textbox.get("1.0", tk.END)
        file.write(text_to_save)

def do_command(command):
    url_val = url_entry.get().strip()
    if len(url_val) == 0:
        url_val = "::1"

    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, f"{command} {url_val} working...\n")
    command_textbox.update()

    if command == "traceroute":
        full_command = ["traceroute", "-m", "15", "-w", "2", "-q", "1", url_val]
    elif command == "ping -c 10":
        full_command = ["ping", "-c", "6", url_val]
    else:
        full_command = command.split() + [url_val]

    try:
        result = subprocess.run(full_command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                timeout=30,
                                text=True)
        output = result.stdout
        error = result.stderr
    except subprocess.TimeoutExpired:
        output = ""
        error = "Command timed out)"
    except Exception as e:
        output = ""
        error = f"Error: {str(e)}"

    command_textbox.insert(tk.END, output)
    if error:
        command_textbox.insert(tk.END, error)
    command_textbox.see(tk.END)

# Main window - Grinch green background
root = tk.Tk()
root.title("Grinch Network Tools")
root.geometry("900x600")
root.configure(bg="#228B22")  # Grinch green

button_frame = tk.Frame(root, bg="#228B22")  # Green frame
button_frame.pack(pady=20)

ping_image = tk.PhotoImage(file="ping.gif")
ping_image = ping_image.subsample(5, 5)

nslookup_image = tk.PhotoImage(file="nslookup.gif")
nslookup_image = nslookup_image.subsample(5, 5)

traceroute_image = tk.PhotoImage(file="traceroute.gif")
traceroute_image = traceroute_image.subsample(5, 5)

save_image = tk.PhotoImage(file="saveas.gif")
save_image = save_image.subsample(5, 5)

# Buttons with black text on green background
tk.Button(button_frame, image=ping_image, compound="top", text="Ping", bg="green", fg="black",
          command=lambda: do_command("ping -c 10")).grid(row=0, column=0, padx=20, pady=10)

tk.Button(button_frame, image=nslookup_image, compound="top", text="NSLookup", bg="green", fg="black",
          command=lambda: do_command("nslookup")).grid(row=0, column=1, padx=20, pady=10)

tk.Button(button_frame, image=traceroute_image, compound="top", text="Traceroute", bg="green", fg="black",
          command=lambda: do_command("traceroute")).grid(row=0, column=2, padx=20, pady=10)

tk.Button(button_frame, image=save_image, compound="top", text="Save", bg="green", fg="black",
          command=mSave).grid(row=0, column=3, padx=20, pady=10)

# URL entry frame - green background
url_frame = tk.Frame(root, pady=10, bg="green")
url_frame.pack()

tk.Label(url_frame, text="Enter a URL or IP:", font=("Arial", 12), bg="green", fg="white").pack(side=tk.LEFT, padx=10)

# RED input field (Grinch heart!)
url_entry = tk.Entry(url_frame, font=("Arial", 12), width=60, bg="red", fg="white", insertbackground="white")
url_entry.pack(side=tk.LEFT, padx=10)

# Output frame - green background
output_frame = tk.Frame(root, bg="green")
output_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Scrolled text - green with white text
command_textbox = tksc.ScrolledText(output_frame, height=20, width=110, font=("Courier", 10),
                                   bg="red", fg="white", insertbackground="white")
command_textbox.pack(fill=tk.BOTH, expand=True)

root.mainloop()