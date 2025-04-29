# 📊 Úvod do OpenCV

## Co je OpenCV?

OpenCV (**Open Source Computer Vision Library**) je mocná knihovna pro práci s počítačovým viděním a zpracováním obrazů. Byla vytvořena za účelem podpory aplikací, jako je rozpoznávání obličejů, detekce objektů, analýza pohybu, práce s videem a fotografie a mnoho dalšího.

Dnes se OpenCV používá v mnoha oblastech: od robotiky a mobilních aplikací až po vědecký výzkum a průmyslovou automatizaci.

## Proč je OpenCV výhodné?

- Je **rychlé**, protože je napsáno v C++ s Python wrapperem.
- Je **otevřené** a **zdarma**.
- Dá se **kombinovat s AI** (například TensorFlow, PyTorch) pro pokročilejší úlohy.
- Funguje **na počítačích, mobilech i embedded zařízeních**.



## Proč používat OpenCV?

- 🔹 **Obrazy a video**: Číst, upravovat, analyzovat a ukládat multimediální data.
- 🔹 **Detekce a analýza**: Najít objekty podle barvy, tvaru nebo jiných vlastností.
- 🔹 **Zábava a vizualizace**: Výsledky jsou ihned viditelé a efektní.
- 🔹 **Základ pro pokročilejší obory**: Strojové učení, neuronové sítě, rozšířená realita.


## Co lze pomocí OpenCV dělat?

- 📸 **Načíst a zobrazit** fotografie a videa.
- 🌈 **Pracovat s barvami** (např. změnit barevný model, filtrovat podle barvy).
- ✂️ **Detekovat objekty** podle obrysů a tvarů.
- 💬 **Reagovat na kliknutí myší** na obrazovku.
- 🌍 **Transformovat obraz** (otočit, zvětšit, zmenšit).


## Jak pracovat s OpenCV v Pythonu?

1. **Instalace knihovny**:
   ```bash
   pip install opencv-python
   ```

2. **Načtení knihovny v kódu**:
   ```python
   import cv2
   ```

3. **Základní príklad**:
   ```python
   import cv2

   img = cv2.imread('obrazek.jpg')
   cv2.imshow('Okno', img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```


## Tipy pro úspěšnou práci:

- Počítač pracuje s barvami trochu jinak než člověk – používá modely jako **RGB** a **HSV**.
- Obrázek je pro počítač vlastně **matice čísel**.
- Každý krok si můžeme ihned **vizuálně ověřit** zobrazením v okně.


# Přehled základních možností OpenCV + praktické příklady využití

---

## 1. **Načítání, zobrazování a ukládání obrázků a videí**
- **Načíst obrázek**: `cv2.imread('obrazek.jpg')`
- **Zobrazit obrázek**: `cv2.imshow('Okno', img)`
- **Uložit obrázek**: `cv2.imwrite('novy_obrazek.jpg', img)`
- **Načíst video nebo kameru**: `cv2.VideoCapture(0)`

🔹 **Praktické využití**:
- Úprava fotek a videí.
- Vytváření vizuálních nástrojů.
- Automatizace práce s médii.

---

## 2. **Změna velikosti, ořezávání a otáčení obrázků**
- **Změnit velikost**: `cv2.resize(img, (šířka, výška))`
- **Ořezat část obrázku**: `výřez = img[y1:y2, x1:x2]`
- **Otočit obrázek**: `cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)`

🔹 **Praktické využití**:
- Příprava datasetů.
- Úprava fotografií pro weby a aplikace.
- Automatické formátování obrázků.

---

## 3. **Převod barevných prostorů (BGR ⇆ HSV, Gray apod.)**
- **BGR na HSV**: `cv2.cvtColor(img, cv2.COLOR_BGR2HSV)`
- **BGR na černobílý (šedý)**: `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`

🔹 **Praktické využití**:
- Snadnější detekce barev.
- Předzpracování pro detekci objektů.

---

## 4. **Detekce hran a kontur**
- **Detekce hran**: `cv2.Canny(gray_img, 100, 200)`
- **Najít kontury**: `cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)`

🔹 **Praktické využití**:
- Rozpoznávání tvarů.
- Skenování dokumentů.
- Automatické vyhledávání objektů.

---

## 5. **Detekce objektů (obličeje, oči, těla)**
- **Haar Cascades**: `face_cascade.detectMultiScale(gray)`

🔹 **Praktické využití**:
- Rozpoznávání lidí ve fotografiích.
- Inteligentní kamery (např. zabezpečení).
- Filtry pro rozpoznávání tváří.

---

## 6. **Maskování barev a barevná filtrace**
- **Vyhledání konkrétní barvy v HSV**: `cv2.inRange(hsv_img, lower_bound, upper_bound)`

🔹 **Praktické využití**:
- Sledování objektů určité barvy.
- Virtuální efekty (green screen).
- Robotické vidění.

---

## 7. **Základní geometrické operace**
- **Kreslení čáry**: `cv2.line(img, (x1, y1), (x2, y2), barva, tloušťka)`
- **Kreslení obdélníku**: `cv2.rectangle(img, (x, y), (x+w, y+h), barva, tloušťka)`
- **Kreslení kruhu**: `cv2.circle(img, střed, poloměr, barva, tloušťka)`

🔹 **Praktické využití**:
- Anotace na fotografiích.
- Vizuální zvýraznění nalezených objektů.

---

## 8. **Základní filtry a efekty**
- **Rozmazání obrazu**: `cv2.GaussianBlur(img, (5,5), 0)`
- **Detekce hran Sobelovým filtrem**: `cv2.Sobel(img, ddepth, dx, dy)`

🔹 **Praktické využití**:
- Předzpracování obrázků.
- Zmírnění šumu ve videích a fotkách.

---

## 9. **Perspektivní transformace a změna tvaru**
- **Affine transformace**: změna tvaru obrazu pomocí matice.
- **Perspective transformace**: `cv2.getPerspectiveTransform()`.

🔹 **Praktické využití**:
- Oprava perspektivy dokumentů.
- Virtuální simulace prostředí.

---

## 10. **Práce s myší a klávesnicí**
- **Sledování kliknutí myší**: `cv2.setMouseCallback('Okno', funkce)`

🔹 **Praktické využití**:
- Interaktivní výběr bodů, oblastí.
- Uživatelská manipulace s obrazem.

---

## 11. **Video analýza: snímek po snímku**
- Zpracování každého snímku z videa zvlášť.
- Měřit pohyb, rychlost objektů.

🔹 **Praktické využití**:
- Sledování pohybujících se aut.
- Sportovní analýzy (góly, běh).

---

## 12. **Sledování objektů (tracking)**
- Použití vestavěných sledovacích algoritmů: např. CSRT, KCF, MIL.

🔹 **Praktické využití**:
- Sledování osob ve videu.
- Robotické sledování pohybujících se cílů.

