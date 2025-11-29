#  Invisibile Cloak Using OpenCV

This project demonstrates an **invisibility cloak effect** using Python, OpenCV, and NumPy. The effect makes a **royal blue-colored cloak** appear invisible by replacing its area with a pre-captured background image in real-time.

---

## Files in this Repository

1. **background.py**

   * Captures the background image from your webcam.
   * Saves it as `image.jpg` for use in the main invisibility effect.

2. **invisible_cloak.py**

   * Implements the invisibility effect.
   * Detects royal blue-colored areas (cloak) and replaces them with the captured background image.
   * Displays the live webcam feed with the invisibility effect.

---

## Requirements

* Python 3.x
* OpenCV
* NumPy

Install dependencies with pip:

```bash
pip install opencv-python numpy
```

---

## How to Run

### Step 1: Capture Background

Run `background.py` to capture the static background image:

```bash
python background.py
```

* A window will show the live webcam feed.
* Press `q` to capture and save the background as `image.jpg`.

### Step 2: Run Invisibility Cloak

Run `invisible_cloak.py` to see the invisibility effect:

```bash
python invisible_cloak.py
```

* Wear a **royal blue cloak or object**.
* The blue portions will appear invisible, showing the captured background instead.
* Press `q` to exit.

---

## How It Works

1. Capture the background frame without the cloak.
2. Convert live webcam frames to **HSV color space**.
3. Detect royal blue color using a color mask.

   * Typical HSV range for royal blue:

     ```python
     lower_blue = np.array([100, 150, 0])
     upper_blue = np.array([140, 255, 255])
     ```
4. Apply morphological transformations to clean the mask.
5. Replace detected blue areas with the background using bitwise operations.
6. Display the final output in real-time.

---

