# Tento skript definuje třídu VideoCV pro zpracování videa pomocí OpenCV.
# Třída obsahuje metody pro načtení videa, převod snímků na šedou barvu,
# detekci hran, detekci obličejů, filtraci barev a ukládání zpracovaných snímků.

import cv2
import numpy as np


# Třída pro práci s videem pomocí OpenCV
class VideoCV:
    def __init__(self, path):
        """
        Inicializace třídy VideoCV.
        :param path: Cesta k videosouboru nebo adresa kamery.
        """
        self.cap = cv2.VideoCapture(path)
        if not self.cap.isOpened():
            raise ValueError("Video nelze načíst.")

    def process_video(self, process_frame_function):
        """
        Zpracování videa pomocí dané funkce pro každý snímek.
        :param process_frame_function: Funkce, která převezme snímek a vrátí upravený snímek.
        :return: None
        """
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Konec videa nebo chyba při čtení.")
                break

            processed_frame = process_frame_function(frame)

            cv2.imshow('Processed Video', processed_frame)
            if cv2.waitKey(25) == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    @staticmethod
    def to_gray(frame):
        """
        Převod snímku na odstíny šedi.
        :param frame: Vstupní snímek.
        :return: Šedý snímek.
        """
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def detect_edges(frame, lower=100, upper=200):
        """
        Detekce hran v jednotlivých snímcích pomocí Cannyho detektoru.
        :param frame: Vstupní snímek.
        :param lower: Dolní práh pro Cannyho detekci.
        :param upper: Horní práh pro Cannyho detekci.
        :return: Snímek s detekovanými hranami.
        """
        gray = VideoCV.to_gray(frame)
        edges = cv2.Canny(gray, lower, upper)
        return edges

    @staticmethod
    def detect_faces(frame):
        """
        Detekce obličejů v jednotlivých snímcích.
        :param frame: Vstupní snímek.
        :return: Snímek s detekovanými obličeji.
        """
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = VideoCV.to_gray(frame)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        return frame

    @staticmethod
    def filter_color(frame, lower_bound, upper_bound):
        """
        Filtrace určité barvy v jednotlivých snímcích pomocí HSV.
        :param frame: Vstupní snímek.
        :param lower_bound: Dolní hranice HSV barevného rozsahu.
        :param upper_bound: Horní hranice HSV barevného rozsahu.
        :return: Snímek s filtrovanou barvou.
        """
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, np.array(lower_bound), np.array(upper_bound))
        result = cv2.bitwise_and(frame, frame, mask=mask)
        return result
