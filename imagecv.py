# Tento skript definuje třídu ImageCV pro zpracování obrázků pomocí OpenCV.
# Třída obsahuje metody pro načtení obrázku, převod na odstíny šedi, detekci hran,
# detekci obličejů, filtraci barev, uložení obrázku a vykreslování tvarů.
# Import knihovny OpenCV
import cv2
# Import knihovny NumPy, která je potřebná pro práci s poli a maticemi
# Proč ji potřebujeme? Protože OpenCV používá NumPy pro reprezentaci obrázků jako matice.
import numpy as np


# Třída pro zpracování obrázků pomocí OpenCV
class ImageCV:
    def __init__(self, path):
        """
        Inicializace třídy ImageCV.
        :param path: Cesta k obrázku.
        """
        # Načtení obrázku z dané cesty
        self.image = cv2.imread(path)
        # Kontrola, zda byl obrázek načten správně
        if self.image is None:
            raise ValueError("Obrázek nelze načíst.")
        # Inicializace atributů pro různé barevné prostory
        self.gray = None
        self.hsv = None

    def show(self, window_name="Image"):
        """
        Zobrazení obrázku v okně.
        :param window_name: Název okna pro zobrazení obrázku.
        :return: None
        """
        # Zobrazení obrázku v okně s daným názvem
        cv2.imshow(window_name, self.image)
        # Čekání na stisk klávesy
        cv2.waitKey(0)
        # Zavření všech oken
        cv2.destroyAllWindows()

    def to_gray(self):
        """
        Převod obrázku na odstíny šedi.
        :return: Odstíny šedi obrázku.
        """
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return self.gray

    def to_hsv(self):
        """
        Převod obrázku na HSV barevný prostor.
        :return: HSV obrázku - Hue, Saturation, Value.
        """
        self.hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        return self.hsv

    def detect_edges(self, lower=100, upper=200):
        """
        Detekce hran v obrázku pomocí Cannyho detektoru.
        :param lower: Hranice pro detekci silných hran (dolní práh).
        :param upper: Hranice pro detekci slabých hran (horní práh).
        :return: Obrázek s detekovanými hranami.
        """
        if self.gray is None:
            self.to_gray()
        # Aplikace Cannyho detektoru na obrázek
        edges = cv2.Canny(self.gray, lower, upper)
        return edges

    def auto_canny(self, sigma=0.33):
        """
        Automatická detekce hran pomocí Cannyho algoritmu s adaptivním nastavením prahů.
        :param sigma: Ūrečuje šířku rozmezí kolem mediánu.
        :return: Obrázek s detekovanými hranami, dolní a horní práh.
        """
        if self.gray is None:
            self.to_gray()
        median = np.median(self.gray)
        lower = int(max(0, (1.0 - sigma) * median))
        upper = int(min(255, (1.0 + sigma) * median))
        edged = cv2.Canny(self.gray, lower, upper)
        return edged, lower, upper

    def detect_faces(self):
        """
        Detekce obličejů v obrázku pomocí Haar Cascade Classifier.
        :return: Obrázek s detekovanými obličeji.
        """
        if self.gray is None:
            self.to_gray()
        # Načtení klasifikátoru pro detekci obličejů
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # Kontrola, zda byl klasifikátor načten správně
        # scaleFactor určuje, jak moc se mění velikost obrázku při detekci
        # minNeighbors určuje, kolik sousedních obdélníků musí být detekováno pro potvrzení detekce
        faces = face_cascade.detectMultiScale(self.gray, 1.3, 5)
        # Vykreslení obdélníků kolem detekovaných obličejů
        # Vytvoření kopie obrázku pro zobrazení detekovaných obličejů
        img_copy = self.image.copy()
        # Pro každý detekovaný obličej vykreslíme modrý obdélník pomocí funkce rectangle
        for (x, y, w, h) in faces:
            cv2.rectangle(img_copy, (x, y), (x+w, y+h), (255, 0, 0), 2)
        return img_copy

    def filter_color(self, lower_bound, upper_bound):
        """
        Filtrace barev v obrázku pomocí HSV barevného prostoru.
        :param lower_bound: Určuje dolní hranici barevného rozsahu (např. [0, 100, 100]).
        :param upper_bound: Určuje horní hranici barevného rozsahu (např. [10, 255, 255]).
        :return: Obrázek s filtrovanou barvou.
        """
        if self.hsv is None:
            self.to_hsv()
        # Aplikace masky na obrázek, využití inRange pro určení barevného rozsahu
        # inRange vrací binární masku, kde jsou pixely v daném rozsahu nastaveny na 255 (bílá) a ostatní na 0 (černá)
        # np.array převádí seznam na NumPy pole
        mask = cv2.inRange(self.hsv, np.array(lower_bound), np.array(upper_bound))
        # Aplikace masky na původní obrázek pomocí bitwise_and, kde se zachovají pouze pixely v rozsahu
        # bitwise_and provede logickou operaci AND mezi dvěma obrázky
        # Vytvoření výsledného obrázku, kde jsou zachovány pouze barvy v daném rozsahu
        result = cv2.bitwise_and(self.image, self.image, mask=mask)
        return result

    def save(self, path, img_to_save=None):
        """
        Uloží obrázek na disk.
        :param path: Cesta k uložení souboru (např. 'output.jpg').
        :param img_to_save: (Volitelné) Jiný obrázek než self.image (např. hranový obrázek).
        :return: None
        """
        if img_to_save is None:
            cv2.imwrite(path, self.image)
        else:
            cv2.imwrite(path, img_to_save)

    def draw_rectangle(self, start_point, end_point, color=(0, 255, 0), thickness=2):
        """
        Vykreslení obdélníku na obrázku.
        :param start_point: Počáteční bod obdélníku (x, y).
        :param end_point: Koncový bod obdélníku (x, y).
        :param color: Barevná hodnota (BGR) pro vykreslení obdélníku.
        :param thickness: Tloušťka čáry obdélníku.
        :return: None
        """
        cv2.rectangle(self.image, start_point, end_point, color, thickness)

    def draw_circle(self, center, radius, color=(0, 0, 255), thickness=2):
        """
        Vykreslení kruhu na obrázku.
        :param center: Střed kruhu (x, y).
        :param radius: Poloměr kruhu.
        :param color: Barevná hodnota (BGR) pro vykreslení kruhu.
        :param thickness: Tloušťka čáry kruhu.
        :return: None
        """
        cv2.circle(self.image, center, radius, color, thickness)

    def draw_line(self, start_point, end_point, color=(255, 0, 0), thickness=2):
        """
        Vykreslení čáry na obrázku.
        :param start_point: Počáteční bod čáry (x, y).
        :param end_point: Koncový bod čáry (x, y).
        :param color: Barevná hodnota (BGR) pro vykreslení čáry.
        :param thickness: Tloušťka čáry.
        :return: None
        """
        cv2.line(self.image, start_point, end_point, color, thickness)
