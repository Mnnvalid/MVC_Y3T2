import tkinter as tk
from controllers.cntr_citizen import list_citizens

def open_citizen_view():
    win = tk.Toplevel()
    win.title("หน้าลงทะเบียนประชาชน")
    win.geometry("500x400")

    output = tk.Text(win)
    output.pack()

    def show_all():
        output.delete("1.0", tk.END)
        for c in list_citizens():
            output.insert(tk.END, f"{c[0]} อายุ:{c[2]} ประเภท:{c[5]}\n")

    def show_by_type(ctype):
        output.delete("1.0", tk.END)
        for c in list_citizens():
            if c[5] == ctype:
                output.insert(tk.END, f"{c[0]} อายุ:{c[2]} ประเภท:{c[5]}\n")

    tk.Button(win, text="แสดงทั้งหมด", command=show_all).pack()
    tk.Button(win, text="GENERAL", command=lambda: show_by_type("GENERAL")).pack()
    tk.Button(win, text="RISK", command=lambda: show_by_type("RISK")).pack()
    tk.Button(win, text="VIP", command=lambda: show_by_type("VIP")).pack()
