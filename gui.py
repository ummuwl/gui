from tkinter import*


main_window = Tk()

label1 = Label(main_window, text="Nilai a")
label2 = Label(main_window, text="Nilai b")
label3 = Label(main_window, text="Nilai p")

Entry1 = Entry(main_window)
Entry2 = Entry(main_window)
Entry3 = Entry(main_window)

label1.grid(row=2, column=0, sticky=E)
label2.grid(row=3, column=0, sticky=E)
label3.grid(row=4, column=0, sticky=E)

Entry1.grid(row=2, column=1)
Entry2.grid(row=3, column=1)
Entry3.grid(row=4, column=1)
   

tombol1 = Button(main_window, text="Cek Diskriminan")
tombol2 = Button(main_window, text="Titik Kurva Elliptik")
tombol1.grid(row=11, column=1)
tombol2.grid(row=11, column=2)




main_window.mainloop()
