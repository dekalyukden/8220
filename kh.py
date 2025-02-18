import json
import keyboard
from loger import log_message  # Імпортуємо функцію логування

# Функції для збереження та завантаження клавіші
def save_key(key):
    with open('config.json', 'w') as f:
        json.dump({'selected_key': key}, f)

def load_key():
    try:
        with open('config.json', 'r') as f:
            data = json.load(f)
            return data['selected_key']
    except FileNotFoundError:
        return None

# Функція для вибору клавіші
def choose_key():
    global selected_key
    key_label.config(text="Чекаю натискання клавіші...")
    key_label.update()

    try:
        def on_press(event):
            global selected_key
            selected_key = event.name
            save_key(selected_key)
            key_label.config(text=f"Обрана клавіша: {selected_key}")
            keyboard.unhook_all()
            log_message(f"Обрано клавішу: {selected_key}")  # Логуємо обрану клавішу

        keyboard.on_press(on_press)
    except Exception as e:
        key_label.config(text=f"Помилка: {e}")
        log_message(f"Помилка вибору клавіші: {e}")  # Логуємо помилку