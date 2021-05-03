import tkinter as tk
import math

from decimal import Decimal


root = tk.Tk()
root.title("Orbit Calculator")
root.iconphoto(False, tk.PhotoImage(file="or_bit.png"))


class Orbit:

    def __init__(self, master):
        self.main_frame = tk.Frame(master) # create a frame window
        self.main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        # variables declaration
        self.op_sign = tk.StringVar()
        self._digit = tk.StringVar()
        self._disp = tk.StringVar()
        self._result = tk.StringVar()
        self.final_res = 0
        # method invokings
        self.create_widgets(master)
      

    def create_widgets(self, master):
        # display frame at the top
        # entry_frame = tk.Frame(self.main_frame, relief="sunken", pady=5)
        # entry_frame.grid(row=0, column=0, sticky=(tk.E, tk.W))
        # entry frame 
        self.inp = tk.Entry(self.main_frame, font=("arial", 20, "bold"),bg="powder blue", fg="#000", bd=30, insertwidth=4, justify="right")
        self.inp.grid(row=0, columnspan=7, ipady=5, pady=0.5, sticky=(tk.W, tk.E))
        # math operator frame
        # math_frame = tk.Frame(self.main_frame, relief="raised", pady=3)
        # math_frame.grid(row=1, column=0, sticky=(tk.E, tk.W))
        # operator buttons
        self.div_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="/", command=lambda : self.char_handler("/"))
        self.div_btn.grid(row=1, column=0)
       
        self.mul_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="x", command=lambda : self.char_handler("*"))
        self.mul_btn.grid(row=1, column=1)
       
        self.add_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="+", command=lambda : self.char_handler("+"))
        self.add_btn.grid(row=1, column=2)
        
        self.min_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="-", command=lambda : self.char_handler("-"))
        self.min_btn.grid(row=1, column=3)
        
        self.opb_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="(", command=lambda : self.char_handler("("))
        self.opb_btn.grid(row=1, column=4)
        
        self.clb_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text=")", command=lambda : self.char_handler(")"))
        self.clb_btn.grid(row=1, column=5)

        self.del_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="C", command=self.clearEntry)
        self.del_btn.grid(row=1, column=6)
        
        # body frame
        # body_frame = tk.Frame(self.main_frame, relief="raised", pady=3)
        # body_frame.grid(row=2, column=0, ipadx=400, sticky=(tk.E, tk.W))
        # math functions frame
        # func_frame = tk.Frame(body_frame, relief="raised", pady=3)
        # func_frame.grid(row=0, column=0, ipadx=50, sticky=(tk.E, tk.W, tk.S))
        # function buttons
        # 1 column:
        sin_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="sin", command=lambda : self.funcOps("math.sin("))
        sin_btn.grid(row=2, column=0)
       
        in_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="In")
        in_btn.grid(row=3, column=0)
       
        pow_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="^", command=lambda : self.funcOps("**"))
        pow_btn.grid(row=4, column=0)
        
        pi_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="Pi", command=lambda : self.funcOps("math.pi"))
        pi_btn.grid(row=5, column=0)
        # 2 column:
        cos_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="cos", command=lambda : self.funcOps("math.cos("))
        cos_btn.grid(row=2, column=1)
        
        log_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="Log", command=lambda : self.funcOps("math.log10("))
        log_btn.grid(row=3, column=1)
       
        exp_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="Exp", command=lambda : self.funcOps("*10**"))
        exp_btn.grid(row=4, column=1)
       
        rs_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="RS")
        rs_btn.grid(row=5, column=1)
        # 3 column
        tan_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="tan", command=lambda : self.funcOps("math.tan("))
        tan_btn.grid(row=2, column=2)
       
        fac_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="n!", command=lambda : self.funcOps("!"))
        fac_btn.grid(row=3, column=2)
        
        sqrt_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="√", command=lambda : self.funcOps("math.sqrt("))
        sqrt_btn.grid(row=4, column=2)
       
        mod_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="%", command=lambda : self.char_handler("%"))
        mod_btn.grid(row=5, column=2)
        
        # digits frame
        # dig_frame = tk.Frame(body_frame, relief="raised", pady=3)
        # dig_frame.grid(row=0, column=1, ipadx=50, sticky=(tk.E, tk.W, tk.S))
        # digit buttons
        # 1 column:
        btn_7 = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="7", command=lambda : self.digits_handler(7))
        btn_7.grid(row=2, column=4)
       
        btn_4 = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="4", command=lambda : self.digits_handler(4))
        btn_4.grid(row=3, column=4)
       
        btn_1 = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="1", command=lambda : self.digits_handler(1))
        btn_1.grid(row=4, column=4)
        
        dot_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text=".", command=lambda : self.char_handler("."))
        dot_btn.grid(row=5, column=4)
        # 2 column:
        btn_8 = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="8", command=lambda : self.digits_handler(8))
        btn_8.grid(row=2, column=5)
        
        btn_5 = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="5", command=lambda : self.digits_handler(5))
        btn_5.grid(row=3, column=5)
       
        btn_2 = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="2", command=lambda : self.digits_handler(2))
        btn_2.grid(row=4, column=5)
       
        btn_0 = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="0", command=lambda : self.digits_handler(0))
        btn_0.grid(row=5, column=5)
        # 3 column
        btn_9 = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="9", command=lambda : self.digits_handler(9))
        btn_9.grid(row=2, column=6)
       
        btn_6 = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="6", command=lambda : self.digits_handler(6))
        btn_6.grid(row=3, column=6)
        
        btn_3 = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="3", command=lambda : self.digits_handler(3))
        btn_3.grid(row=4, column=6)
       
        equ_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="=", command=lambda : self.char_handler("="))
        equ_btn.grid(row=5, column=6)
        
        # switch frame
        # switch_frame = tk.Frame(self.main_frame, relief="raised", pady=3)
        # switch_frame.grid(row=6, columnspan=6, sticky=(tk.E, tk.W))
        # switch buttons
        inv_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="INV")
        inv_btn.grid(row=6, column=1, pady=5, sticky=tk.W)
        
        sci_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="SCI")
        sci_btn.grid(row=6, column=3, pady=5, sticky=(tk.W, tk.E))
       
        std_btn = tk.Button(self.main_frame,font=("arial", 20, "bold"), bg="powder blue", fg="#000", bd=5, padx=5, text="STD")
        std_btn.grid(row=6, column=5, pady=5, sticky=tk.E)
        
    # digits handler
    def digits_handler(self, digit):
        digit = str(digit)
        data = self._digit.get()
        data1 = self._disp.get()

        data += digit
        data1 += digit

        self._digit.set(data)
        self._disp.set(data1)
        self.inp["textvariable"] = self._disp
    
    # character handler
    def char_handler(self, char):
        data = ""
        if char == ".":
            data = self._digit.get()
            if data == "":
                data = "0." # to add a '0.' when only a '.' is clicked
                self._digit.set(data)
                self._disp.set(data)
                self.inp["textvariable"] = self._disp
            else:
                data += char
                self._digit.set(data)
                self._disp.set(data)
                # self.inp["textvariable"] = self._digit
                self.inp["textvariable"] = self._disp

        elif char == "=":
            self.final_res = eval(self._digit.get())
            self._result.set(str(self.final_res))
            self.inp["textvariable"] = self._result
            self._digit.set("")
            self._disp.set("")

        else:
            data = self._digit.get()
            data1 = self._disp.get()

            data += char
            data1 += char

            self._digit.set(data)
            self._disp.set(data1)
            self.inp["textvariable"] = self._disp
    

    def funcOps(self, _dat):
        data = self._digit.get()
        data1 = self._disp.get()

        if _dat == "math.pi":
            data += _dat
            data1 += _dat[5:] # to get the chars from the 5th till the end i.e math.pi gets 'pi' only
        
        # to calculate factorial
        elif _dat == "!":
            data1 += "!"
            
            ra = 1 # rare increment value
            fr = 2 # front increment value
            dig = ""
            for n in range(len(data1)):
                d = data1[n-fr:n-ra] # to get the 2nd last value from data1, i.e data1 = "2*5!"
                if d.isdigit():
                    dig += str(d)
                else:
                    di = Decimal(dig)
                    res = self.factorial(di)
                    data = data.replace(str(di), str(res)) # to replace the fac val di with the res of fac
                ra += 2
                fr += 2
        elif _dat == "math.sqrt(":
            data1 += "√("
            data += _dat
        elif _dat == "**":
            data1 += "^"
            data += "**"
        elif _dat == "*10**":
            data1 += "e"
            data += "*10**"
            self._digit.set(data)
            self._disp.set(data1)
            self.inp["textvariable"] = self._disp
        else:
            data1 += (_dat[5:8] + "(") #to remove the 'math.' part of a function i.e math.sin( & + brace 
            data += _dat               #get only chars between 5 & 9 and exclude the rest i.e math.log10(

        self._digit.set(data)
        self._disp.set(data1)
        self.inp["textvariable"] = self._disp

    # factorial culculator   
    def factorial(self, d):
        if d == 0:
            return 1
        else:
            return d*self.factorial(d - 1)

    # to clear the entry widget
    def clearEntry(self):
        data = ""
        self._digit.set(data)
        self._disp.set(data)
        self.inp["textvariable"] = self._disp


app = Orbit(root)
root.mainloop()
