import cv2

# List of image paths
image_paths = [
    "C:\\Users\\uppub\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-08-07 120502.png",
    "C:\\Users\\uppub\\OneDrive\\Pictures\\Screenshots\\pngtree-wild-birds-standing-on-the-branch-image_15696515.jpg",
    "C:\\Users\\uppub\\OneDrive\\Pictures\\Screenshots\\OIP.jpg",
    "C:\\Users\\uppub\\OneDrive\\Pictures\\Camera Roll\\OIP.jpg",
    "C:\\Users\\uppub\\OneDrive\\Pictures\\Camera Roll\\OIP (9).jpg",
    "C:\\Users\\uppub\\OneDrive\\Pictures\\Camera Roll\\download.jpg",
    "C:\\Users\\uppub\\Downloads\\download (1).jpg",
    "C:\\Users\\uppub\\Downloads\\OIP.jpg"    
]

# Loop through each image path
for idx, path in enumerate(image_paths):
    # Read an image
    image = cv2.imread(path)
    
    # Check if the image was successfully loaded
    if image is None:
        print(f"Error: Could not read the image at {path}.")
    else:
        # Display the image using OpenCV
        cv2.imshow(f'Image {idx + 1}', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Image",idx+1,"displayed")
