import tkinter as tk
from tkinter import messagebox

def Konversi_suhu():
    try:
        C = float(entry_celcius.get())

        # Konversi suhu 
        K = 273 + C
        Cs = K - 273
        # Tampilkan hasil
        label_hasil.config(text=f'C: {Cs:.2f} dan K: {K: .2f}')
        messagebox.showinfo('KONVERSI SUHU', f'C: {Cs: .2f}\n K: {K: .2f}')
    except ValueError:
        messagebox.showerror('TERJADI ERORR', 'Masukkan angka yang sesuai!!')

# Membuat window
root = tk.Tk()
root.title('KONVERSI SUHU')
root.geometry('250x100')

# Memasukkan angka pada suhu C
entry_celcius = tk.Entry(root, font=('Arial', 12))
entry_celcius.pack()

# Button 
tk.Button(root, text='Klik', command=Konversi_suhu, width=12, font=('Arial', 12)).pack(pady=5)


# hasil 
label_hasil = tk.Label(root, text='Hasil', font=('Arial', 12))
label_hasil.pack()

root.mainloop()