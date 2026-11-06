#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
from datetime import datetime
import subprocess

# ======================
# BACKUP FUNCTION
# ======================
def backup():
    source = filedialog.askdirectory(title="Select Source Folder")
    destination = filedialog.askdirectory(title="Select Destination Folder")

    if not source or not destination:
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(destination, f"backup_{timestamp}")

    try:
        shutil.copytree(source, dest)
        messagebox.showinfo("Success", f"Backup completed:\n{dest}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ======================
# RECOVERY
# ======================
def recovery():
    messagebox.showinfo("Info", "Launching TestDisk...\nFollow steps inside terminal")
    subprocess.run(['sudo', 'testdisk'])

# ======================
# NETWORK SCAN
# ======================
def scan_network():
    network = simple_input("Enter network (e.g. 192.168.1.0/24):")
    if network:
        os.system(f"nmap -sP {network}")

# ======================
# SYSTEM MONITOR
# ======================
def system_monitor():
    try:
        import psutil
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        messagebox.showinfo("System Info",
            f"CPU: {cpu}%\nRAM: {ram}%\nDisk: {disk}%")
    except ImportError:
        messagebox.showerror("Error", "Install psutil: pip install psutil")

# ======================
# SIMPLE INPUT POPUP
# ======================
def simple_input(prompt):
    popup = tk.Toplevel(root)
    popup.title("Input")

    label = tk.Label(popup, text=prompt)
    label.pack(pady=5)

    entry = tk.Entry(popup, width=30)
    entry.pack(pady=5)

    result = {"value": None}

    def submit():
        result["value"] = entry.get()
        popup.destroy()

    tk.Button(popup, text="OK", command=submit).pack(pady=5)

    root.wait_window(popup)
    return result["value"]

# ======================
# MAIN WINDOW
# ======================
root = tk.Tk()
root.title("Enterprise IT Toolkit")
root.geometry("400x350")

title = tk.Label(root, text="IT Management System", font=("Arial", 16))
title.pack(pady=10)

btn_backup = tk.Button(root, text="Backup Files", width=25, command=backup)
btn_backup.pack(pady=5)

btn_recovery = tk.Button(root, text="Recover Partition", width=25, command=recovery)
btn_recovery.pack(pady=5)

btn_scan = tk.Button(root, text="Network Scan", width=25, command=scan_network)
btn_scan.pack(pady=5)

btn_monitor = tk.Button(root, text="System Monitor", width=25, command=system_monitor)
btn_monitor.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", width=25, command=root.quit)
btn_exit.pack(pady=20)

root.mainloop()
