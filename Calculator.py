import tkinter as tk
from tkinter import ttk

# Set up the window
window = tk.Tk()
window.geometry("325x500")
window.title("Calculator")
window.resizable(False, False)  # Fixed syntax: removed '='
window.attributes("-toolwindow", True)
window.config(background="#000000")

# Set up style
style = ttk.Style()
style.theme_use("clam")  # Required for background and border colors

style.configure(
    "Num.TButton",
    font=("Inter", 14, "bold"),
    background="#4682B4",
    foreground="#000000",
    padding=5,
    borderwidth=2,
    relief="solid",
    bordercolor="#123456",
)

style.configure(
    "Op.TButton",
    font=("Inter", 14, "bold"),
    background="#4169E1",
    foreground="#000000",
    padding=5,
    borderwidth=2,
    relief="solid",
    bordercolor="#123456",
)

# Dark frame background to match the window
style.configure("Calc.TFrame", background="#000000")

# Top display entry box (height 90px)
entry_box = ttk.Entry(window, font=("Inter", 24, "bold"), justify="right")
entry_box.place(x=10, y=10, width=305, height=80)

# Frame holding all buttons (remaining 400px height)
buttons_frame = ttk.Frame(window, style="Calc.TFrame")
buttons_frame.place(x=10, y=100, width=305, height=390)

# Button Functions
eqn=""

def clicknum(num):
    global eqn
    result = entry_box.get()
    entry_box.insert(tk.END,str(num))
    eqn+=str(num)

def clickop(op):
    global eqn
    result = entry_box.get()
    entry_box.insert(tk.END,op)
    eqn+=op

def clear():
    global eqn
    entry_box.delete(0,tk.END)
    eqn=""

def evaluate():
    global eqn
    ans = eval(eqn)
    entry_box.delete(0,tk.END)
    eqn=""
    entry_box.insert(0,ans)
    
 

# Grid coordinate helper values:
# Available width: 305px -> 4 columns of 71px width + 7px gaps
# Available height: 390px -> 5 rows of 70px height + 8px gaps
col_x = [0, 78, 156, 234]
row_y = [0, 78, 156, 234, 312]
btn_w = 71
btn_h = 70

# Row 1: (, ), C, /
open_brac = ttk.Button(buttons_frame, text="(", style="Op.TButton", command = lambda:clickop("("))
open_brac.place(x=col_x[0], y=row_y[0], width=btn_w, height=btn_h)

close_brac = ttk.Button(buttons_frame, text=")", style="Op.TButton", command = lambda:clickop(")"))
close_brac.place(x=col_x[1], y=row_y[0], width=btn_w, height=btn_h)

clear_btn = ttk.Button(buttons_frame, text="C", style="Op.TButton", command = lambda:clear())
clear_btn.place(x=col_x[2], y=row_y[0], width=btn_w, height=btn_h)

div = ttk.Button(buttons_frame, text="/", style="Op.TButton", command = lambda:clickop("/"))
div.place(x=col_x[3], y=row_y[0], width=btn_w, height=btn_h)

# Row 2: 7, 8, 9, x
sev = ttk.Button(buttons_frame, text="7", style="Num.TButton", command = lambda:clicknum(7))
sev.place(x=col_x[0], y=row_y[1], width=btn_w, height=btn_h)

eig = ttk.Button(buttons_frame, text="8", style="Num.TButton", command = lambda:clicknum(8))
eig.place(x=col_x[1], y=row_y[1], width=btn_w, height=btn_h)

nine = ttk.Button(buttons_frame, text="9", style="Num.TButton", command = lambda:clicknum(9))
nine.place(x=col_x[2], y=row_y[1], width=btn_w, height=btn_h)

mul = ttk.Button(buttons_frame, text="x", style="Op.TButton", command = lambda:clickop("*"))
mul.place(x=col_x[3], y=row_y[1], width=btn_w, height=btn_h)

# Row 3: 4, 5, 6, +
four = ttk.Button(buttons_frame, text="4", style="Num.TButton", command = lambda:clicknum(4))
four.place(x=col_x[0], y=row_y[2], width=btn_w, height=btn_h)

fiv = ttk.Button(buttons_frame, text="5", style="Num.TButton", command = lambda:clicknum(5))
fiv.place(x=col_x[1], y=row_y[2], width=btn_w, height=btn_h)

six = ttk.Button(buttons_frame, text="6", style="Num.TButton", command = lambda:clicknum(6))
six.place(x=col_x[2], y=row_y[2], width=btn_w, height=btn_h)

add = ttk.Button(buttons_frame, text="+", style="Op.TButton", command = lambda:clickop("+"))
add.place(x=col_x[3], y=row_y[2], width=btn_w, height=btn_h)

# Row 4: 1, 2, 3, -
one = ttk.Button(buttons_frame, text="1", style="Num.TButton", command = lambda:clicknum(1))
one.place(x=col_x[0], y=row_y[3], width=btn_w, height=btn_h)

two = ttk.Button(buttons_frame, text="2", style="Num.TButton", command = lambda:clicknum(2))
two.place(x=col_x[1], y=row_y[3], width=btn_w, height=btn_h)

three = ttk.Button(buttons_frame, text="3", style="Num.TButton", command = lambda:clicknum(3))
three.place(x=col_x[2], y=row_y[3], width=btn_w, height=btn_h)

sub = ttk.Button(buttons_frame, text="-", style="Op.TButton", command = lambda:clickop("-"))
sub.place(x=col_x[3], y=row_y[3], width=btn_w, height=btn_h)

# Row 5: ., 0, = (spans 2 columns to fill the bottom right cleanly)
dec_point = ttk.Button(buttons_frame, text=".", style="Num.TButton", command = lambda:clickop("."))
dec_point.place(x=col_x[0], y=row_y[4], width=btn_w, height=btn_h)

zero = ttk.Button(buttons_frame, text="0", style="Num.TButton", command = lambda:clicknum(0))
zero.place(x=col_x[1], y=row_y[4], width=btn_w, height=btn_h)

cal = ttk.Button(buttons_frame, text="=", style="Op.TButton", command = lambda:evaluate())
cal.place(x=col_x[2], y=row_y[4], width=(btn_w * 2) + 7, height=btn_h)

window.mainloop()
