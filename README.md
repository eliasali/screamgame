# Audio Visualizer with Image Transition

This code is an audio visualizer that displays images based on the volume level of the audio input. It uses OpenCV (cv2) for image processing, PyAudio for audio input/output, and NumPy for numerical operations.

## Prerequisites

- Python 3.x
- OpenCV (cv2) library
- NumPy library
- PyAudio library

## How to Run the Code

1. Make sure you have the necessary images:
   - "caramellotus_BLK.png"
   - "caramellotus.png"
   - "prize.jpeg"

2. Install the required libraries:

`pip install opencv-python
pip install numpy
pip install pyaudio
`

3. Run the code:

`python audio_visualizer.py`

## Code Explanation

1. **Image Loading and Resizing:**
- The code loads three images: "caramellotus_BLK.png," "caramellotus.png," and "prize.jpeg" using the `cv2.imread()` function.
- The desired size for the images is specified as (4128, 2752).
- Each image is resized to the desired size using `cv2.resize()`.

2. **PyAudio Initialization:**
- PyAudio is initialized using `pyaudio.PyAudio()`.

3. **Variable Initialization:**
- `avg_volume` represents the running average of volume levels.
- `alpha` is a weight used to calculate the running average.
- `img2_revealed` is a flag indicating whether `img2` is fully revealed.
- `img3_timer` is a timer used to display `img3`.

4. **Audio Input Initialization:**
- The microphone is opened for audio input using `p.open()`.
- The sample rate is set to 44100, and the chunk size is set to 4096.

5. **Main Loop:**
- The main loop continues until the program is terminated.
- Inside the loop, a chunk of audio data is read from the microphone using `stream.read()`.
- The volume level of the audio data is calculated using `audioop.rms()`.
- The volume level is normalized to a percentage of the maximum volume level.
- The current volume level is added to the running average using the `avg_volume` formula.
- The number of rows to reveal based on the running average is calculated.
- A copy of `img1` is created as `new_image`.
- If `img2` is not fully revealed, rows of `img2` are revealed based on the volume level.
- If all rows of `img2` are revealed, the `img3_timer` is started, and `img2_revealed` is set to `True`.
- If `img2` is fully revealed, `img3` is displayed for a certain duration.
- The current image (`new_image`) is displayed using `cv2.imshow()`.
- The running average of volume levels is decreased by a constant value in each iteration.
- The program checks for key presses, and if the user presses 'q', the program is terminated.

6. **Cleanup:**
- The audio input stream is stopped and closed using `stream.stop_stream()` and `stream.close()`.
- PyAudio is terminated using `p.terminate()`.
- All OpenCV windows are destroyed using `cv2.destroyAllWindows()`.


Feel free to customize the code and images according to your preferences. Enjoy the audio visualizer!

## Cleanup

To stop the program, press 'q' on the keyboard. The program will clean up the resources and close the application window.

If you encounter any issues or have any questions, please feel free to reach out.
