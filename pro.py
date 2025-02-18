import tkinter as tk
from tkinter import ttk
import cv2
import keyboard
from kh import choose_key, load_key
from ip import select_region
from loger import log_message

# Захоплення зображення з екрану
log_message("Початок роботи програми")
log_message("Захоплення зображення з екрану")
image = np.array(pyautogui.screenshot())
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
image_copy = image.copy()

x_start, y_start, x_end, y_end = None, None, None, None
cropping = False

# Створення вікна tkinter
root = tk.Tk()
root.title("Програма виділення області")
root.geometry("300x300")

selected_key = load_key()

choose_key_button = ttk.Button(root, text="Вибрати клавішу", command=choose_key)
choose_key_button.pack(pady=10)

key_label = ttk.Label(root, text=f"Обрана клавіша: {selected_key if selected_key else 'Не обрано'}")
key_label.pack()

def start_selection():
    if selected_key is None:
        print("Помилка: Не обрано клавішу для виділення.")
        return

    cv2.namedWindow("Screen")
    cv2.setMouseCallback("Screen", select_region)
    log_message("Створено вікно для відображення зображення")

    while True:
        key = keyboard.get_event()
        if key and key.name == selected_key:
            break
        if key and key.name == 'q':
            cv2.destroyAllWindows()
            log_message("Вікно закрито")
            if all(coord is not None for coord in [x_start, y_start, x_end, y_end]):
                print("Координати виділеної області:")
                print(f"x_start: {x_start}, y_start: {y_start}")
                print(f"x_end: {x_end}, y_end: {y_end}")
                log_message(f"Координати: ({x_start}, {y_start}), ({x_end}, {y_end})")
            log_message("Завершення роботи програми")
            return

start_button = ttk.Button(root, text="Запустити виділення", command=start_selection)
start_button.pack(pady=10)

root.mainloop()