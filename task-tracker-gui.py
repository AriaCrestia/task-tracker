import tkinter as tk
from tkinter import ttk

def del_frm_current_tasks():
    frm_current_tasks.destroy()
    repack_frm_current_tasks()
def repack_frm_current_tasks():
    task = ent_new_task.get()
    task_list.append(task)
    frm_current_tasks = tk.Frame(master=task_tracker_win)    
    loop_ctrl = 0
    lbl_task = ['lbl_task_1', 'lbl_task_2', 'lbl_task_3', 'lbl_task_4', 'lbl_task_5', 'lbl_task_6', 'lbl_task_7', 'lbl_task_8']
    while (loop_ctrl != len(task_list)):
        if (loop_ctrl < 8):
            lbl_task[loop_ctrl] = ttk.Label(master=frm_current_tasks, text=task_list[loop_ctrl])
            lbl_task[loop_ctrl].pack()
            loop_ctrl += 1
        else:
            lbl_task_8 = ttk.Label(master=frm_current_tasks, text="You cannot have more than 8 tasks at once")
            lbl_task_8.pack()
            break
    frm_current_tasks.pack()

task_list = []

task_tracker_win = tk.Tk()
task_tracker_win.title("Task Tracker")
task_tracker_win.resizable(width=False, height=False)

frm_new_task = tk.Frame(master=task_tracker_win)

lbl_title = ttk.Label(master=frm_new_task, text="Task Tracker", justify="center", underline=1, padding=5)
lbl_title.pack()

lbl_new_task = ttk.Label(master=frm_new_task, text="New task:", padding=5)
lbl_new_task.pack(side="left", anchor='n')

ent_new_task = ttk.Entry(master=frm_new_task)
ent_new_task.pack(padx=5, pady=5)

btn_new_task = ttk.Button(master=frm_new_task, text="Add task", command=del_frm_current_tasks)
btn_new_task.pack(side='right', padx=5, anchor='n')

frm_new_task.pack()

frm_current_tasks = tk.Frame(master=task_tracker_win)

lbl_status = ttk.Label(master=frm_current_tasks, text="No tasks active")
lbl_status.pack()

frm_current_tasks.pack(pady=20)

task_tracker_win.mainloop()