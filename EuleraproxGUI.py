import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def solve_ode():
    t0 = float(t0_entry.get())
    y0 = float(y0_entry.get())
    h = float(h_entry.get())
    max_t = float(max_t_entry.get())
    f = f_entry.get()

    ts = [t0]
    ys = [y0]
    t = t0
    y = y0

    for i in range(int(max_t / h)):
        fn = eval(f)
        y = y + h * fn
        t = t + h
        ts.append(round(t, 4))
        ys.append(round(y, 4))

    # Update the table
    table.delete(*table.get_children())
    for i in range(len(ts)):
        table.insert("", i, values=(ts[i], ys[i]))

    # Update the graph
    canvas.figure.clf()
    ax = canvas.figure.add_subplot(111)
    ax.plot(ts, ys, color="red")
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    ax.set_xlim(
        min(ts) - (max(ts) - min(ts)) / 100, max(ts) + (max(ts) - min(ts)) / 100
    )
    ax.set_ylim(
        min(ys) - (max(ys) - min(ys)) / 100, max(ys) + (max(ys) - min(ys)) / 100
    )
    canvas.draw()


# Create the main window
root = tk.Tk()
root.title("ODE Solver")

# Create the input fields
t0_label = tk.Label(root, text="t\u2080")
t0_label.grid(row=0, column=0)
t0_entry = tk.Entry(root)
t0_entry.grid(row=0, column=1)

y0_label = tk.Label(root, text="y(t\u2080)")
y0_label.grid(row=1, column=0)
y0_entry = tk.Entry(root)
y0_entry.grid(row=1, column=1)

h_label = tk.Label(root, text="\u0394t")
h_label.grid(row=2, column=0)
h_entry = tk.Entry(root)
h_entry.grid(row=2, column=1)

max_t_label = tk.Label(root, text="t\u2098\u2090\u2093")
max_t_label.grid(row=3, column=0)
max_t_entry = tk.Entry(root)
max_t_entry.grid(row=3, column=1)

f_label = tk.Label(root, text="f(t,y)")
f_label.grid(row=4, column=0)
f_entry = tk.Entry(root)
f_entry.grid(row=4, column=1)

# Create the Solve button
solve_button = tk.Button(root, text="Solve", command=solve_ode)
solve_button.grid(row=5, column=0)

# Create the table
table_frame = ttk.Frame(root)
table_frame.grid(row=6, column=0, columnspan=2)

table = ttk.Treeview(table_frame, columns=("t", "y"), show="headings")
table.column("t", width=200, anchor="center")
table.column("y", width=200, anchor="center")
table.heading("t", text="t")
table.heading("y", text="y")
table.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
scrollbar.pack(side="right", fill="y")
table.configure(yscrollcommand=scrollbar.set)

# Create the graph area
figure = plt.Figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.get_tk_widget().grid(row=0, column=2, rowspan=7, padx=20, pady=20)

root.mainloop()
