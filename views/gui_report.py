import tkinter as tk
from controllers.cntr_assignment import process_assignment_gui

def open_report_view():
    win = tk.Toplevel()
    win.title("รายงานผลการจัดสรร")
    win.geometry("500x400")

    output = tk.Text(win)
    output.pack()

    report = process_assignment_gui()

    for r in report:
        if r[6]:
            output.insert(tk.END, f"{r[0]} → ได้ที่พัก ศูนย์ {r[6]}\n")
        else:
            output.insert(tk.END, f"{r[0]} ❌ ตกค้าง\n")
