import ctypes
from tkinter import *
from tkinter import messagebox

lib = ctypes.CDLL("../build/partitioner.dll")
lib.init_partitions()

lib.create_partition.argtypes = [ctypes.c_int]
lib.create_partition.restype = ctypes.c_int

lib.delete_partition.argtypes = [ctypes.c_int]
lib.delete_partition.restype = ctypes.c_int

lib.get_partitions.argtypes = [ctypes.POINTER(ctypes.c_int)]

def create():
    try:
        size = int(entry.get())
        idx = lib.create_partition(size)
        if idx >= 0:
            messagebox.showinfo("Success", f"Partition {idx} created")
        elif idx == -2:
            messagebox.showerror("Error", "Not enough space")
        else:
            messagebox.showerror("Error", "No slot available")
        view()
    except ValueError:
        messagebox.showerror("Error", "Invalid size")

def delete():
    try:
        idx = int(entry.get())
        result = lib.delete_partition(idx)
        if result == 0:
            messagebox.showinfo("Deleted", f"Partition {idx} deleted")
        else:
            messagebox.showerror("Error", "Invalid index")
        view()
    except ValueError:
        messagebox.showerror("Error", "Invalid index")

def view():
    buffer = (ctypes.c_int * 30)()
    lib.get_partitions(buffer)
    result = ""
    for i in range(10):
        used, start, size = buffer[i*3], buffer[i*3+1], buffer[i*3+2]
        if used:
            result += f"Partition {i}: Start = {start}, Size = {size}\n"
    output.delete(1.0, END)
    output.insert(END, result)

root = Tk()
root.title("Dynamic Disk Partitioner")

Label(root, text="Size/Index:").pack()
entry = Entry(root)
entry.pack()

Button(root, text="Create Partition", command=create).pack()
Button(root, text="Delete Partition", command=delete).pack()
Button(root, text="View Partitions", command=view).pack()

output = Text(root, height=10, width=40)
output.pack()

view()
root.mainloop()