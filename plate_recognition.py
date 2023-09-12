## Here goes code for recognizing license plates number from image and converting it into usable text.

import cv2
import pytesseract

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'Path\to\tesseract.exe'

# Load the image
image = cv2.imread("img1.jpg")
#cv2.imshow("Original Image", image)

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray Image", gray_image)

# Apply some preprocessing (GaussianBlur)
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
#cv2.imshow("Blurred Image", blur_image)

# Edge detection (Canny)
edges = cv2.Canny(blur_image, 50, 150)
cv2.imshow("Edges", edges)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    # Get rectangle bounding contour
    x, y, w, h = cv2.boundingRect(contour)

    # Assume license plate has specific dimensions
    if w > 50 and h > 20:
        # Crop the license plate area
        license_plate = gray_image[y:y + h, x:x + w]
        #cv2.imshow("Cropped License Plate", license_plate)

        # OCR
        text = pytesseract.image_to_string(license_plate, config='--psm 8')

        # Filter OCR output, keep alphanumeric characters only
        filtered_text = ''.join(e for e in text if e.isalnum())

        print(f"License Plate Number: {filtered_text}")

cv2.waitKey(0)
cv2.destroyAllWindows()