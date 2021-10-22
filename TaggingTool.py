import tkinter.messagebox
import tkinter
import pandas as pd
from openpyxl import load_workbook

cevaplar = pd.read_excel("Yazılı_Geri_Bildirimler_wordcloud.xlsx")
print(cevaplar.head())


# Create the default window
#root = tkinter.Tk()
#root.title("Culture Check-Up")
#root.geometry('700x500')

# Variable to keep track of the option
# selected in OptionMenu
#value_inside = tkinter.StringVar(root)

# Set the default value of the variable
#value_inside.set("Lütfen değerlendirmek istediğiniz soru rakamını seçin")

#options_list = ['10', '20', '30']

# Create the optionmenu widget and passing
# the options_list and value_inside to it.
#question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
#question_menu.pack()

for index,row in cevaplar.head().iterrows():
    tkinter.messagebox.showinfo(title="Sarp", message=row["Comment"])
