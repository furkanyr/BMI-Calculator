import tkinter

root = tkinter.Tk()
root.title("BMI Calculator")
root.minsize(275, 250)
root.resizable(False, False)

info_label = tkinter.Label()
label1 = tkinter.Label(text="Enter Your Weight (kg)", font=("Calibri", 10, "normal"), pady=10)
label2 = tkinter.Label(text="Enter Your Height (cm)", font=("Calibri", 10, "normal"), pady=10)
error1 = tkinter.Label(text="Enter both Weight and Height!", font=("Calibri", 10, "normal"), pady=10)
error2 = tkinter.Label(text="Enter a Valid Number!", font=("Calibri", 10, "normal"), pady=10)
error3 = tkinter.Label(text="Height or Weight cannot be equal to 0", font=("Calibri", 10, "normal"), pady=10)

kg = tkinter.Entry()
height = tkinter.Entry()

label1.pack()
kg.pack()
kg.focus()
label2.pack()
height.pack()

def calc_button_clicked():
    error1.pack_forget()
    error2.pack_forget()
    error3.pack_forget()
    info_label.pack_forget()
    flag = str()

    if len(kg.get()) == 0 or len(height.get()) == 0:
        error1.pack()
    elif kg.get().isdigit() == False or height.get().isdigit() == False:
        error2.pack()
    elif int(kg.get()) == 0 or int(height.get()) == 0:
        error3.pack()
    else:
        bmi = (int(kg.get()) * 10000) / (int(height.get()) * int(height.get()))
        if bmi <= 16:
            flag = "Severe Thinness"
        elif bmi <= 17:
            flag = "Moderate Thinness"
        elif bmi <= 18.5:
            flag = "Mild Thinness"
        elif bmi <= 25:
            flag = "Normal"
        elif bmi <= 30:
            flag = "Overweight"
        elif bmi <= 35:
            flag = "Obese Class I"
        elif bmi <= 40:
            flag = "Obese Class II"
        elif bmi > 40:
            flag = "Obese Class III"
        info_label.config(text=f"Your BMI is {bmi:.2f}.You are in {flag}", font=("Calibri", 10, "normal"), pady=10)
        info_label.pack()


calc_button = tkinter.Button(text="Calculate", bg="#B3B3B3", pady=10, width=17, command=calc_button_clicked)
calc_button.pack()

root.mainloop()