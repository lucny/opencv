import cv2
import tkinter as tk
from tkinter import simpledialog, messagebox

# Funkce pro zahájení detekce obličejů
def start_detection(ip, port):
    url = f'http://{ip}:{port}/video'
    print(f"Připojování ke {url}...")

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        messagebox.showerror("Chyba", "Nepodařilo se otevřít stream. Zkontroluj IP, port a spojení.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Chyba při čtení obrazu. Ukončuji.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Funkce volaná po kliknutí na tlačítko
def on_start():
    ip = ip_entry.get().strip()
    port = port_entry.get().strip()

    if not ip or not port:
        messagebox.showwarning("Varování", "Vyplň IP adresu i port!")
        return

    start_detection(ip, port)

# Nastavení GUI
root = tk.Tk()
root.title("Nastavení IP kamery")

# Vstup pro IP adresu
tk.Label(root, text="IP adresa mobilu:").pack(pady=5)
ip_entry = tk.Entry(root)
ip_entry.pack(pady=5)

# Vstup pro port
tk.Label(root, text="Port:").pack(pady=5)
port_entry = tk.Entry(root)
port_entry.pack(pady=5)

# Tlačítko Start
start_button = tk.Button(root, text="Spustit detekci", command=on_start)
start_button.pack(pady=20)

root.mainloop()