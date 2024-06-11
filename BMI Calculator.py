import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title('BMI Calculator')
app.geometry('570x350')
app.config(bg='#000')

font1 = ('Arial',30,'bold')
font2 = ('Arial',18,'bold')
font3 = ('Arial',25,'bold')
        

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        if variable2.get() == "ft":
            height *= 30.48
        if variable1.get() == "lbs":
            weight *= 0.453592
        bmi = weight / ((height/100) ** 2)
# Assigning result 
        if bmi >= 30:
            bmi_result1 = ("obese.")
        elif bmi >= 25 < 30:
            bmi_result1 = ("overweight.")
        elif bmi >= 18.5 < 25:
            bmi_result1 = ("normal.")
        else:
            bmi_result1 = ("underweight.")
        result_lable.configure(text=f"Your BMI is: {bmi:.2f} and you are {bmi_result1}")
    except ValueError:
        messagebox.showerror('Error', 'Enter a valid number!')
    except ZeroDivisionError:
        messagebox.showerror('Error', 'Height cannot be 0!')


title_label = customtkinter.CTkLabel(app,font=font1,text='BMI Calculator',text_color='#fff',bg_color='#000')
title_label.place(x=150,y=20)

weight_label = customtkinter.CTkLabel(app,font=font2,text='Weight',text_color='#fff',bg_color='#000')
weight_label.place(x=75,y=80)

height_label = customtkinter.CTkLabel(app,font=font2,text='Height',text_color='#fff',bg_color='#000')
height_label.place(x=275,y=80)

weight_entry = customtkinter.CTkEntry(app,font=font2,text_color='#000',fg_color='#fff')
weight_entry.place(x=75,y=110)

height_entry = customtkinter.CTkEntry(app,font=font2,text_color='#000',fg_color='#fff')
height_entry.place(x=275,y=110)

weight_options = ['kg', 'lbs']
height_options = ['cm', 'ft']
variable1 = StringVar()
variable2 = StringVar()

weight_option = customtkinter.CTkComboBox(app,font=font2,text_color='#000',fg_color='#fff',dropdown_hover_color='#06911f',values=weight_options,variable=variable1,width=80)
weight_option.place(x=180,y=110)
weight_option.set('kg')

height_option = customtkinter.CTkComboBox(app,font=font2,text_color='#000',fg_color='#fff',dropdown_hover_color='#06911f',values=height_options,variable=variable2,width=80)
height_option.place(x=370,y=110)
height_option.set('cm')

calculate_button = customtkinter.CTkButton(app,command=calculate_bmi,font=font2,text_color='#fff',text='Calculate BMI',fg_color='#06911f',bg_color='#000',cursor='hand2',corner_radius=5,width=200)
calculate_button.place(x=190,y=200)

result_lable = customtkinter.CTkLabel(app,text='',font=font3,text_color='#fff',bg_color='#000')
result_lable.place(x=30,y=280)

app.mainloop()