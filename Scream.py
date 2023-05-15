import cv2
import numpy as np
import pyaudio
import audioop
import time

# Load image#1 and resize it to a desired size
img1 = cv2.imread("caramellotus_BLK.png")
desired_size = (4128, 2752)
img1 = cv2.resize(img1, desired_size)

# Load image#2 and resize it to the same size as image#1
img2 = cv2.imread("caramellotus.png")
img2 = cv2.resize(img2, desired_size)

# Load image#3 and resize it to the same size as image#1
img3 = cv2.imread("prize.jpeg")
img3 = cv2.resize(img3, desired_size)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Initialize a running average of volume levels
avg_volume = 0.0
alpha = 0.9

# Initialize a flag to indicate whether image2 is fully revealed
img2_revealed = False

# Initialize a timer for displaying image3
img3_timer = None

# Open the microphone and set the sample rate and chunk size
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=4096)

# Loop until the program is terminated
while True:
    # Read a chunk of audio data from the microphone
    data = stream.read(4096)
    
    # Calculate the volume level of the audio data
    rms = audioop.rms(data, 2)
    
    # Calculate the percentage of the maximum volume level
    volume = min(rms / 700.0, 1.0)
    
    # Add the current volume level to the running average
    avg_volume = alpha * avg_volume + (1 - alpha) * volume
    # Calculate the number of rows to reveal based on the running average of volume levels
    num_rows = int(avg_volume * img2.shape[0])
    
    # Create a copy of image1 with all rows revealed
    new_image = img1.copy()
    
    # If image2 is not yet fully revealed, reveal rows of image2 from the bottom
    if not img2_revealed:
        if avg_volume > 0.1:
            new_image[-num_rows:, :, :] = img2[-num_rows:, :, :]
        
        # Check if all rows of image2 are now revealed
        if avg_volume>0.9:
            while avg_volume < 1.1:
                avg_volume += 0.05
            if avg_volume > 1:
                img3_timer = time.time()
                img2_revealed = True
            
    
    # If image2 is fully revealed, display image3 for 3 seconds
    else:
        # Check if 3 seconds have elapsed since image3 was displayed
        if time.time() - img3_timer >= 5:
            img2_revealed = False
            img3_timer = None
        else:
            new_image = img3.copy()
    
    # Display the current image
    cv2.imshow("Image", new_image)
    
    # Subtract a constant value from the running average of volume levels in each iteration
    avg_volume = max(avg_volume - 0.01, 0.0)
    
    # Check for key presses and exit the program if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
stream.stop_stream()
stream.close()
p.terminate()
cv2.destroyAllWindows()
