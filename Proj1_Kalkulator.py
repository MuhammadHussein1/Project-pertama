import tkinter as tk 
from tkinter import messagebox

def x():
    try:
        i = a.get()
        total = eval (i)
        hasil.config(text=f'Hasil {total}')
        messagebox.showinfo('Kalkulator', f'{i}: {total}')
        
    except ValueError:
        hasil.config(text='HANYA ANGKA')
        messagebox.showerror('HANYA BISA ANGKA', 'COBA LAGI')
    except ZeroDivisionError:
        hasil.config(text='Tidak bisa dibagi dengan 0')
        messagebox.showerror('TRY AGAIN', f'Tidak bisa kalo dibagi dengan 0')
    except SyntaxError:
        hasil.config('Syntax yang ada masukkan erorr')
        messagebox.showerror('Erorr', 'Coba lagi')
    except Exception as z:
        hasil.config(text='ERORR')
        messagebox.showinfo('KESALAHAN TIDAK BISA MEMASUKKAN ANGKA 1<', f'terjadi kesalahan: {z}')

# GUI 
root = tk.Tk()
root.title('PERCOBAAN PEMBUATAN KALKULATOR')
root.geometry('300x100')

# Input 
a = tk.Entry(root, width=25, font=('Arial', 12))
a.pack()

# Butoon 
tk.Button(root, text='Klik', font=('Arial', 10), width=12, command=x).pack()

# Hasil
hasil = tk.Label(root, text='Hasil -', font=('Arial', 12))
hasil.pack(side='bottom')
hasil.pack(pady=9)

# Messagebox 

root.mainloop()