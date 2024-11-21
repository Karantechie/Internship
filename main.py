import cv2

# Load an image
image_path = "images/week1.jpg"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Resize the image
new_width, new_height = 500, 500  # Set your desired dimensionsn 
resized_image = cv2.resize(image, (new_width, new_height))

# Convert the image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Add annotations to the resized image
annotated_image = resized_image.copy()
text = "OpenCV Annotation"
font = cv2.FONT_HERSHEY_SIMPLEX
position = (50, 50)  # Coordinates for the text
font_scale = 1
color = (0, 255, 0)  # Green color in BGR
thickness = 2
cv2.putText(annotated_image, text, position, font, font_scale, color, thickness)

# Draw a rectangle annotation
top_left = (100, 100)  # Top-left corner
bottom_right = (400, 400)  # Bottom-right corner
rectangle_color = (255, 0, 0)  # Blue color in BGR
rectangle_thickness = 3
cv2.rectangle(annotated_image, top_left, bottom_right, rectangle_color, rectangle_thickness)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized_image)
cv2.imshow("Thresholded Image", thresholded_image)
cv2.imshow("Annotated Image", annotated_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the processed images (optional)
cv2.imwrite("images/resized_image.jpg", resized_image)
cv2.imwrite("images/thresholded_image.jpg", thresholded_image)
cv2.imwrite("images/annotated_image.jpg", annotated_image)
