# p227_network_tools_with_images.py
# Network Tools GUI with Ping, NSlookup, Traceroute, and Save buttons

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

# Save function
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

# Execute command function
def do_command(command):
    url_val = url_entry.get().strip()
    if len(url_val) == 0:
        url_val = "::1"  # Default to localhost IPv6

    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, f"{command} {url_val} working...\n")
    command_textbox.update()

    p = subprocess.Popen(f"{command} {url_val}",
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results.decode())
    command_textbox.insert(tk.END, cmd_errors.decode())
    command_textbox.see(tk.END)

# Main window
root = tk.Tk()
root.title("Network Tools")
root.geometry("900x600")

# === Button frame with grid layout ===
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

ping_image = tk.PhotoImage(file="ping.gif")
ping_image = ping_image.subsample(5, 5)

nslookup_image = tk.PhotoImage(file="nslookup.gif")
nslookup_image = nslookup_image.subsample(5, 5)

traceroute_image = tk.PhotoImage(file="traceroute.gif")
traceroute_image = traceroute_image.subsample(5, 5)

save_image = tk.PhotoImage(file="saveas.gif")
save_image = save_image.subsample(5, 5)

tk.Button(button_frame, image=ping_image, compound="top", text="Ping",
          command=lambda: do_command("ping -c 10")).grid(row=0, column=0, padx=20, pady=10)

tk.Button(button_frame, image=nslookup_image, compound="top", text="NSLookup",
          command=lambda: do_command("nslookup")).grid(row=0, column=1, padx=20, pady=10)

tk.Button(button_frame, image=traceroute_image, compound="top", text="Traceroute",
          command=lambda: do_command("traceroute")).grid(row=0, column=2, padx=20, pady=10)

tk.Button(button_frame, image=save_image, compound="top", text="Save",
          command=mSave).grid(row=0, column=3, padx=20, pady=10)

# === URL entry frame ===
url_frame = tk.Frame(root, pady=10)
url_frame.pack()

tk.Label(url_frame, text="Enter a URL or IP:", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
url_entry = tk.Entry(url_frame, font=("Arial", 12), width=60)
url_entry.pack(side=tk.LEFT, padx=10)

# === Output scrolled text ===
output_frame = tk.Frame(root)
output_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

command_textbox = tksc.ScrolledText(output_frame, height=20, width=110, font=("Courier", 10))
command_textbox.pack(fill=tk.BOTH, expand=True)

root.mainloop()