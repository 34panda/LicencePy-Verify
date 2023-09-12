import sys
import sqlicense_plates as sqlicenses
import plate_recognition as pr

# path to image of license plate
image_path = "img1.jpg"

# display work in progress notification
sys.stdout.write("Analysis... ")
sys.stdout.flush()

# using plate_recognition to convert image info to text
license_texts = pr.img_to_text(image_path)

# remove work in progress notification
sys.stdout.write("\r                     \r")
sys.stdout.flush()

# using SQL database operations to verify if texts inside list (possible license plates numbers) are present within DB.
for text in license_texts:
    result = sqlicenses.check_license_plate(text)
    if result:
        print(result)
