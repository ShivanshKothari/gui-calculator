from tkinter import *
import os

# ------------------------ WINDOW INTIALISATION -----------------------------
root = Tk()
root.title("Calculator")
img = PhotoImage(file="calculator_icon.gif")
root.tk.call('wm', 'iconphoto', root._w, img)
root.resizable(False, False)
# ----------------------- GLOBAL VARIABLES' DECLARATION -------------------------
resume = ""
t = ""


# ----------------- FUNCTION DEFINITIONS -------------------------------------
def press(n):
    box.configure(state=NORMAL)
    global resume
    if resume != 1:
        box.insert(INSERT, str(n))
        box.configure(state=DISABLED)
    elif resume == 1:
        box.delete(0.0, END)
        box.insert(INSERT, t)
        resume = 0
        box.insert(INSERT, str(n))
        box.configure(state=DISABLED)


def equalpress():
    box.configure(state=NORMAL)
    # noinspection PyBroadException
    try:
        xx = box.get(0.1, END)
        global t
        t = str(eval(xx))
        global resume
        resume = 1
        box.insert(INSERT, "\n=" + t)
        box.configure(state=DISABLED)
    except:
        box.delete(0.0, END)
        box.insert(INSERT, "ERROR")
        box.configure(state=DISABLED)


def all_clear():
    box.configure(state=NORMAL)
    box.delete(0.0, END)
    box.configure(state=DISABLED)
    global resume
    resume = 0
    global t
    t = 0


def clear():
    box.configure(state=NORMAL)
    b = str(box.get(0.0, END))

    b = list(b)
    b = b[:-2]
    box.delete(0.0, END)
    box.insert(INSERT, str("".join(x for x in b)))
    box.configure(state=DISABLED)
    global resume
    resume = 0
    global t
    t = 0
# --------------------------------------------------------------------------------------------------


# ------------------------------ MAIN --------------------------------------------------------------
box = Text(root, height=3, width=19, border=4, font=("Comic Sans MS", 15, 'bold'), bg="Light Grey", fg="Blue")
box.grid(row=0, columnspan=4)
box.configure(state=DISABLED)

e7 = Button(root, text="7", font=("Comic Sans MS", 20), border=3, width=3, bg="#51D3F6", fg="White", command=lambda: press(7))
e7.grid(row=1, sticky=W)

e8 = Button(root, text="8", font=("Comic Sans MS", 20), border=3, width=3, bg="#51D3F6", fg="White", command=lambda: press(8))
e8.grid(row=1, column=1, sticky=W)

e9 = Button(root, text="9", font=("Comic Sans MS", 20), border=3, width=3, bg="#51D3F6", fg="White", command=lambda: press(9))
e9.grid(row=1, column=2, sticky=W)

ep = Button(root, text="+", font=("Comic Sans MS", 20), border=3, width=3, bg="Blue", fg="White", command=lambda: press("+"))
ep.grid(row=1, column=3, sticky=W)

e4 = Button(root, text="4", font=("Comic Sans MS", 20), border=3, width=3, bg="#51D3F6", fg="White", command=lambda: press(4))
e4.grid(row=2, sticky=W)

e5 = Button(root, text="5", font=("Comic Sans MS", 20), border=3, width=3, bg="#51D3F6", fg="White", command=lambda: press(5))
e5.grid(row=2, column=1, sticky=W)

e6 = Button(root, text="6", font=("Comic Sans MS", 20), border=3, width=3, bg="#51D3F6", fg="White", command=lambda: press(6))
e6.grid(row=2, column=2, sticky=W)

es = Button(root, text="-", font=("Comic Sans MS", 20), border=3, width=3, bg="Blue", fg="White", command=lambda: press("-"))
es.grid(row=2, column=3, sticky=W)

e1 = Button(root, text="1", font=("Comic Sans MS", 20), border=3, width=3, bg="#51D3F6", fg="White", command=lambda: press(1))
e1.grid(row=3, sticky=W)

e2 = Button(root, text="2", font=("Comic Sans MS", 20), border=3, width=3, bg="#51D3F6", fg="White", command=lambda: press(2))
e2.grid(row=3, column=1, sticky=W)

e3 = Button(root, text="3", font=("Comic Sans MS", 20), border=3, width=3, bg="#51D3F6", fg="White", command=lambda: press(3))
e3.grid(row=3, column=2, sticky=W)

ed = Button(root, text="X", font=("Comic Sans MS", 20), border=3, width=3, bg="Blue", fg="White", command=lambda: press("*"))
ed.grid(row=3, column=3, sticky=W)

point = Button(root, text=".", font=("Comic Sans MS", 20), border=3, width=3, bg="#51D3F6", fg="White", command=lambda: press("."))
point.grid(row=4, sticky=W)


e0 = Button(root, text="0", font=("Comic Sans MS", 20), border=3, width=3, bg="#51D3F6", fg="White", command=lambda: press(0))
e0.grid(row=4, column=1, sticky=W)

equal = Button(root, text="=", font=("Comic Sans MS", 20), border=3, width=3, bg="Magenta", fg="White", command=equalpress)
equal.grid(row=4, column=2, sticky=W)

em = Button(root, text="/", font=("Comic Sans MS", 20), border=3, width=3, bg="Blue", fg="White", command=lambda: press("/"))
em.grid(row=4, column=3, sticky=W)

all_clear = Button(root, text="C", font=("Comic Sans MS", 20), border=3, width=3, bg="Blue", fg="White", command=all_clear)

all_clear.grid(row=5, sticky=W)

clear = Button(root, text="D", font=("Comic Sans MS", 20), border=3, width=3, bg="Blue", fg="White", command=clear)
clear.grid(row=5, column=1, sticky=W)

fb = Button(root, text="(", font=("Comic Sans MS", 20), border=3, width=3, bg="Blue", fg="White", command=lambda: press("("))
fb.grid(row=5, column=2, sticky=W)

bb = Button(root, text=")", font=("Comic Sans MS", 20), border=3, width=3, bg="Blue", fg="White", command=lambda: press(")"))
bb.grid(row=5, column=3, sticky=W)
root.mainloop()
