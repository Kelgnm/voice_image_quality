# Voice Image Quality
## Features

- Converts an input image to grayscale.
- Performs SVD decomposition on the image.
- Captures live audio from a microphone.
- Dynamically updates the image reconstruction based on audio volume.
- Uses `matplotlib` for real-time visualization.

The image that i used for this project is called hate.png (from the series Space King), but you can change it in the code

https://github.com/user-attachments/assets/3c6921af-b124-4c47-91ee-c968b4901f8c

## Requirements

- Python 3.12.10
- `numpy`
- `matplotlib`
- `sounddevice`
- `scipy`
- `Pillow`

## Installation

```bash
pip install -r requirements.txt
```
## Usage

```bash
python3 vectors.py
```
- `Opens a window displaying the reconstructed image`
- `Speak into the microphone to increase the number of N value, making the image more detailed`

## Configuration

- `DEVICE: Input device ID for your microphone.`
- `WINDOW: Time window in milliseconds for audio processing.`
- `DOWNSAMPLE: Downsampling factor for audio data.`
- `CHANNELS: List of channels to read from the input device.`
- `INTERVAL: Update interval for the animation in milliseconds.`
