import tkinter as tk
from models.models_shelter import Shelter

def open_shelter_view():
    win = tk.Toplevel()
    win.title("หน้าจัดสรรที่พัก")
    win.geometry("500x400")

    output = tk.Text(win)
    output.pack()

    shelters = Shelter.get_all()

    for s in shelters:
        output.insert(
            tk.END,
            f"ศูนย์ {s[0]} | ความจุ {s[1]} | ระดับเสี่ยง {s[2]} | คนปัจจุบัน {s[3]}\n"
        )
