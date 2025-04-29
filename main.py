# Načtení obrázku
import cv2
from imagecv import ImageCV
from videocv import VideoCV

imgcv = ImageCV('media/fotka.jpg')

# Zobrazení originálu
imgcv.show()

# Zobrazení hran
edges = imgcv.detect_edges()
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detekce obličejů
faces_img = imgcv.detect_faces()
cv2.imshow('Faces', faces_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Filtrace červené barvy
red_filtered = imgcv.filter_color([0, 120, 70], [10, 255, 255])
cv2.imshow('Red Filtered', red_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()


def process_frame(frame):
    """
    Funkce, která zpracuje každý snímek videa.
    Můžeš si vybrat libovolnou operaci z VideoCV.
    """
    # Převod na šedou škálu
    gray = VideoCV.to_gray(frame)

    # Detekce hran
    edges = VideoCV.detect_edges(frame)

    # Detekce obličejů
    faces = VideoCV.detect_faces(frame.copy())

    # Filtrace červené barvy
    red_filtered = VideoCV.filter_color(frame, [0, 120, 70], [10, 255, 255])

    # Vyber, co chceš zobrazit:
    return faces  # nebo edges, gray, red_filtered

# Načtení videa (můžeš zkusit vlastní video soubor nebo kameru: 0)
video_path = 'media/hujer.mp4'
vidcv = VideoCV(video_path)

# Zpracování videa
vidcv.process_video(process_frame)
