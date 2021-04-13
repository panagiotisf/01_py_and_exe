#v3 exit button added


# Import Module
import tkinter as tk
import pyperclip
from tkinter import messagebox


# Create Object
root = tk.Tk()
root.title('Hypotenuse')
#canvas size
canvas1 = tk.Canvas(root, width=400, height=280)

canvas1.pack()

#main label
label0 = tk.Label(root, text='Distance between points 1 and 2')
label0.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label0)

#labels for each entry box (numbered accordingly)
label1 = tk.Label(root, text='Easting X1:')
label1.config(font=('helvetica', 10))
canvas1.create_window(80, 60, window=label1)

label2 = tk.Label(root, text='Northing Y1:')
label2.config(font=('helvetica', 10))
canvas1.create_window(80, 80, window=label2)

label3 = tk.Label(root, text='Easting X2:')
label3.config(font=('helvetica', 10))
canvas1.create_window(80, 110, window=label3)

label4 = tk.Label(root, text='Northing Y2:')
label4.config(font=('helvetica', 10))
canvas1.create_window(80, 130, window=label4)

label7 = tk.Label(root, text='Distance result is copied to clipboard')
label7.config(font=('helvetica', 10))
canvas1.create_window(200, 240, window=label7)

# entry boxes
entry1 = tk.Entry(root)
canvas1.create_window(200, 60, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(200, 80, window=entry2)

entry3 = tk.Entry(root)
canvas1.create_window(200, 110, window=entry3)

entry4 = tk.Entry(root)
canvas1.create_window(200, 130, window=entry4)


#calculations
def getSquareRoot():
    x1 = entry1.get()
    y1 = entry2.get()
    x2 = entry3.get()
    y2 = entry4.get()
    x1=float(x1)
    x2=float(x2)
    y1=float(y1)
    y2=float(y2)
    a = (x1-x2)**2
    b = (y1-y2)**2
    global d
    d = round(((a + b)**0.5), 2)
    root.after(100, pyperclip.copy(d))
    # calculation result within function
    label5 = tk.Label(root, text=d)
    label5.config(width=20, bg='lightgreen', justify='right', font=('helvetica', 12, 'bold'))
    canvas1.create_window(290, 210, window=label5)

    button5 = tk.Button(canvas1, text=' Clear ', command=clear_entries, bg='light grey', fg='black', justify='right', font=('helvetica', 10))
    canvas1.create_window(70, 270, window=button5)



#button for calculation
button1 = tk.Button(text='Calculate Distance', command=getSquareRoot, bg='light grey', fg ='black', font=('helvetica', 10, 'bold'))
canvas1.create_window(200, 165, window=button1)


#label for the calculation result
label6 = tk.Label(root, text='Distance between points:')
label6.config(bg='lightgreen', font=('helvetica', 10, 'bold'))
canvas1.create_window(90, 210, window=label6)



#button for exit
button3 = tk.Button (root, text='Exit Application', command=root.destroy, bg='light grey', fg ='black', justify = 'right', font=('helvetica', 10))
canvas1.create_window(350, 270, window=button3)


def clear_entries():
    entry1.delete(0, 100)
    entry2.delete(0, 100)
    entry3.delete(0, 100)
    entry4.delete(0, 100)


button5 = tk.Button (canvas1, text='clear', command=clear_entries, bg='light grey', fg ='black', justify = 'right', font=('helvetica', 10))
canvas1.create_window(70, 270, window=button5)


# Execute Tkinter
root.mainloop()




