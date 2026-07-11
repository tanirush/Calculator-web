import tkinter as tk
import math
from types import SimpleNamespace
import re
buttons=[
    ["7","8","9","+"],
    ["4","5","6","-"],
    ["1","2","3","x"],
    ["","0",".","÷"]
]
z=0 #x
a=75 #y
safe_math = SimpleNamespace(
    sqrt=math.sqrt,
    cbrt=math.cbrt,
    factorial=math.factorial,
    pi=math.pi,
    e=math.e,
)
root=tk.Tk()
label=tk.Label(root,text="",bg="#4C7FCC")
label.place(relwidth=1,relheight=1)
root.title("Calculator")
root.geometry("410x500")
root.resizable(False,False)
text_entry=tk.Entry(font=("arial",20))
text_entry.pack()
def give_input(value):
    
    text_entry.insert(tk.END,value)
def erase():
    u=text_entry.get()
    new_u=u[:-1]
    text_entry.delete(0,tk.END)
    text_entry.insert(tk.END,new_u)
def erase_all():

    text_entry.delete(0,tk.END)
def calculate():
    try:
        question=str(text_entry.get())
        cleaned_input=question.replace("x","*").replace("÷","/")
        while "²√" in cleaned_input:
            start_idx = cleaned_input.find("²√")
            end_idx = cleaned_input.find(")", start_idx)
            inner_value = cleaned_input[start_idx + 3 : end_idx]
            cleaned_input = (
                cleaned_input[:start_idx]
                + f"math.sqrt({inner_value})"
                + cleaned_input[end_idx + 1:]
            )
        while "3√" in cleaned_input:
            start_index=cleaned_input.find("3√")
            end_index=cleaned_input.find(")",start_index)
            inner_index = cleaned_input[start_index + 2:end_index]
            cleaned_input=(
                cleaned_input[:start_index]
                +f"math.cbrt({inner_index})"
                +cleaned_input[end_index + 1:]
            )
        while "!" in cleaned_input:
            match = re.search(r"(\d+)!$", cleaned_input)
            if match:
                number = match.group(1)
                cleaned_input = cleaned_input.replace(
                    f"{number}!",
                    f"math.factorial({number})"
                )
            else:
                break
        answer = eval(
            cleaned_input,
            {"__builtins__": None},
            {
                "math": safe_math,
                "pow": pow,
            }
)
        text_entry.delete(0,tk.END)
        text_entry.insert(0,str(answer))
    except Exception:
        text_entry.delete(0,tk.END)
        text_entry.insert(0,"Error")
def give_square_root_input():
    text_entry.insert(tk.END,"²√()")
def square():
    text_entry.insert(tk.END,"x**2")
def cube():
    text_entry.insert(tk.END,"x**3")
def give_cube_root_input():
    text_entry.insert(tk.END,"3√()")
def give_factorial_input():
    text_entry.insert(tk.END,"x!")
def give_power_input():
    text_entry.insert(tk.END,"pow(x,y)")
def give_pi_input():
    text_entry.insert(tk.END,str(math.pi))
def give_e_input():
    text_entry.insert(tk.END,str(math.e))
def change_all_light_mode():
    for r in buttons_1todivide:
        for btn in r:
            if btn!=None:
                btn.config(fg="#FFFFFF",bg="#69D66E")
    erase_button.config(fg="#FFFFFF",bg="#69D66E")
    erase_all_button.config(fg="#FFFFFF",bg="#69D66E")
    equals.config(fg="#FFFFFF",bg="#69D66E")
    label.config(bg="#4c7fcc")
    square_root.config(fg="#FFFFFF", bg="#69D66E")
    cube_root.config(fg="#FFFFFF", bg="#69D66E")
    factorial.config(fg="#FFFFFF", bg="#69D66E")
    power.config(fg="#FFFFFF", bg="#69D66E")
    pi.config(fg="#FFFFFF", bg="#69D66E")
    e.config(fg="#FFFFFF", bg="#69D66E")
    x_square.config(fg="#FFFFFF",bg="#69d66e")
    x_cube.config(fg="#FFFFFF",bg="#69d66e")
def change_all_dark_mode():
    for r in buttons_1todivide:
        for btn in r:
            if btn!=None:
                btn.config(fg="#000000",bg="#2D2BAB")
    erase_button.config(fg="#000000",bg="#2D2BAB")
    erase_all_button.config(fg="#000000",bg="#2D2BAB")
    equals.config(fg="#000000",bg="#2D2BAB")
    label.config(bg="#450c43")
    square_root.config(fg="#000000", bg="#2D2BAB")
    cube_root.config(fg="#000000", bg="#2D2BAB")
    factorial.config(fg="#000000", bg="#2D2BAB")
    power.config(fg="#000000", bg="#2D2BAB")
    pi.config(fg="#000000", bg="#2D2BAB")
    e.config(fg="#000000", bg="#2D2BAB")
    x_square.config(fg="#000000",bg="#2d2bab")
    x_cube.config(fg="#000000",bg="#2d2bab")
buttons_1todivide=[]
for r in range(4):
    row=[]
    for c in range(4):
        button=buttons[r][c]
        if button!="":
            n=tk.Button(root,text=button,font=("arial",20),fg="#FFFFFF",bg="#69D66E",command=lambda b=button:give_input(b))
            n.place(x=z,y=a)
            row.append(n)
        else:
            row.append(None)
        z+=75
    buttons_1todivide.append(row)
    z=0
    a+=75
erase_button=tk.Button(root,text="⌦",font=("arial",15),fg="#FFFFFF",bg="#69D66E",command=erase)
erase_button.place(x=75,y=375)
erase_all_button=tk.Button(root,text="C",font=("arial",15),fg="#FFFFFF",bg="#69D66E",command=erase_all)
erase_all_button.place(x=150,y=375)
equals=tk.Button(root,text="=",font=("arial",20),fg="#FFFFFF",bg="#69D66E",command=calculate)
equals.place(x=0,y=300)
Light_mode=tk.Button(root,text="Light mode",font=("arial",20),fg="#FFFFFF",bg="#69D66E",command=change_all_light_mode)
Light_mode.place(x=0,y=375+50+10)
Dark_mode=tk.Button(root,text="Dark mode",font=("arial",20),fg="#000000",bg="#2D2BAB",command=change_all_dark_mode)
Dark_mode.place(x=300-50,y=375+50+10)

#math buttons
square_root=tk.Button(root,text="²√",font=("arial",15),fg="#FFFFFF",bg="#69D66E",command=give_square_root_input)
cube_root=tk.Button(root,text="3√",font=("arial",15),fg="#FFFFFF",bg="#69D66E",command=give_cube_root_input)
factorial=tk.Button(root,text="x!",font=("arial",15),fg="#FFFFFF",bg="#69D66E",command=give_factorial_input)
power=tk.Button(root,text="pow()",font=("arial",15),fg="#FFFFFF",bg="#69D66E",command=give_power_input)
pi=tk.Button(root,text="π",font=("arial",15),fg="#FFFFFF",bg="#69D66E",command=give_pi_input)
e=tk.Button(root,text="e",font=("arial",15),fg="#FFFFFF",bg="#69D66E",command=give_e_input)
x_square=tk.Button(root,text="x²",font=("arial",15),fg="#FFFFFF",bg="#69D66E",command=square)
x_cube=tk.Button(root,text="x³",font=("arial",15),fg="#FFFFFF",bg="#69D66E",command=cube)
square_root.place(x=300,y=75)
cube_root.place(x=300,y=150)
factorial.place(x=300,y=225)
pi.place(x=375,y=75)
e.place(x=375,y=150)
x_square.place(x=375,y=150+75)
x_cube.place(x=300,y=225+75)
root.mainloop()