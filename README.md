# IT Toolkit

A small desktop utility for common IT tasks, built with Python and Tkinter.

## Features

- **Backup Files** — choose a source and destination folder; the toolkit copies the source into a timestamped `backup_YYYYMMDD_HHMMSS` folder.
- **Recover Partition** — launches TestDisk with `sudo` so you can follow its recovery workflow in the terminal.
- **Network Scan** — runs an Nmap ping scan for the network range you enter.
- **System Monitor** — displays current CPU, memory, and root-disk usage percentages. This feature requires `psutil`.

## Requirements

- Python 3
- Tkinter (often included with Python; some Linux distributions package it separately)
- Nmap for **Network Scan**
- TestDisk for **Recover Partition**
- `psutil` for **System Monitor** (optional)

Install the optional Python dependency with:

```bash
python3 -m pip install psutil
```

Install Nmap and TestDisk using your operating system's package manager if you need those features.

## Run

From the project directory:

```bash
python3 gui_toolkit.py
```

## Notes

- Use **Network Scan** only on networks you own or are authorized to assess.
- **Recover Partition** invokes `sudo` and TestDisk, which can make disk-level changes. Review TestDisk's prompts carefully and ensure you have backups before proceeding.
- The backup action copies files; it does not remove or synchronize files in either folder.
