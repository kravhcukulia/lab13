import tkinter as tk
from math import sqrt

def calculate(event=None):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Напівпериметр
        p = (a + b + c) / 2

        # Площа трикутника
        S = sqrt(p * (p - a) * (p - b) * (p - c))

        # Висота до сторони b
        hb = (2 * S) / b

        # Бісектриса до сторони a
        wa = sqrt(b * c * (1 - (a**2) / ((b + c)**2)))

        label_hb.config(text=f"Висота hb: {hb:.2f}")
        label_wa.config(text=f"Бісектриса wa: {wa:.2f}")
    except Exception as e:
        label_hb.config(text="Помилка в обчисленнях")
        label_wa.config(text=str(e))

root = tk.Tk()
root.title("Проект: Трикутник")
root.geometry("400x300")

# Зображення
label_image = tk.Label(root)
label_image.pack()

try:
    photo = tk.PhotoImage(file="C:/Users/Asus/Desktop/lab13/lab13.;2.2")
    label_image.configure(image=photo)
    label_image.image = photo  # зберігаємо посилання, щоб не зникло
except Exception as e:
    label_image.config(text="Не вдалося завантажити зображення")

# Поля вводу
tk.Label(root, text="Сторона a:").place(x=20, y=20)
entry_a = tk.Entry(root)
entry_a.place(x=100, y=20)

tk.Label(root, text="Сторона b:").place(x=20, y=60)
entry_b = tk.Entry(root)
entry_b.place(x=100, y=60)

tk.Label(root, text="Сторона c:").place(x=20, y=100)
entry_c = tk.Entry(root)
entry_c.place(x=100, y=100)

# Кнопка
btn = tk.Button(root, text="Обчислити")
btn.place(x=150, y=140)
btn.bind('<Button-1>', calculate)

# Результати
label_hb = tk.Label(root, text="")
label_hb.place(x=20, y=180)

label_wa = tk.Label(root, text="")
label_wa.place(x=20, y=220)

root.mainloop()
