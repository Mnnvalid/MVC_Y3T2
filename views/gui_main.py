import tkinter as tk
from views.gui_citizen import open_citizen_view
from views.gui_shelter import open_shelter_view
from views.gui_report import open_report_view

root = tk.Tk()
root.title("ระบบจัดการศูนย์พักพิง")

tk.Button(root, text="หน้าลงทะเบียนประชาชน", command=open_citizen_view).pack()
tk.Button(root, text="หน้าจัดสรรที่พัก", command=open_shelter_view).pack()
tk.Button(root, text="หน้ารายงานผล", command=open_report_view).pack()

root.mainloop()
