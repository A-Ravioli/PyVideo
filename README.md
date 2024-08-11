# PyVideo

Python-based video editing and manipulation tool that provides a comprehensive suite of features for video processing. Comes with a Tkinter GUI that lets you drag and drop video files, choose from a variety of editing options, and apply those functions.
Certainly! Below is a comprehensive `README.md` file for your video editing and manipulation package with a Tkinter GUI.

## Features

### Core Video Editing Features

- **Trim Video**: Cut a segment of the video by specifying start and end times.
- **Concatenate Videos**: Combine multiple video files into one.
- **Adjust Speed**: Speed up or slow down the video playback.
- **Add Text Overlay**: Overlay text on the video with customizable position, font size, and color.
- **Add Watermark**: Add an image watermark to the video at a specified position.
- **Stabilize Video**: Remove shakiness from the video.
- **Extract Frames**: Extract individual frames from the video as images.
- **Replace Audio**: Replace the existing audio track in the video with a different audio file.
- **Add Fade In/Out**: Apply fade in and/or fade out effects to the video.
- **Picture in Picture (PiP)**: Overlay one video on top of another.
- **Rotate Video**: Rotate the video by specified angles (e.g., 90, 180 degrees).
- **Flip Video**: Flip the video horizontally or vertically.
- **Change Aspect Ratio**: Adjust the aspect ratio of the video.
- **Adjust Brightness/Contrast**: Modify the brightness and contrast of the video.
- **Apply Filter**: Apply various filters to the video (e.g., hue adjustment).
- **Normalize Audio**: Normalize the audio levels of the video.

### Subtitle Handling

- **Generate Subtitles**: Automatically generate subtitles from the video’s audio using Whisper, an open-source audio-to-text model.
- **Burn-In Subtitles**: Permanently embed subtitles into the video.
- **Extract Subtitles**: Extract embedded subtitles from the video.

### Advanced Features

- **Remove Green Screen**: Remove green screen backgrounds from the video.
- **Create GIF**: Convert a portion of the video into an animated GIF.
- **Generate Thumbnail**: Extract a specific frame from the video to create a thumbnail image.

## Installation

### Prerequisites

- Python 3.6 or higher
- FFmpeg installed and available in your system's PATH

### Required Python Packages

Install the necessary Python packages:

```bash
pip install ffmpeg-python whisper tkinter
```

### Download or Clone the Repository

```bash
git clone https://github.com/yourusername/VideoEditorGUI.git
cd VideoEditorGUI
```

## Usage

### Running the GUI

To launch the GUI, simply run the following command:

```bash
python video_editor_gui.py
```

### How to Use

1. **Drag and Drop** a video file into the GUI or click the drag-and-drop area to select a video file.
2. **Choose an Action** from the dropdown menu, such as trimming the video, adding a watermark, or generating subtitles.
3. **Specify Parameters** if needed (e.g., start time for trimming, text for overlay).
4. **Select the Output File** where the processed video will be saved.
5. **Run the Action** by clicking the "Run" button. The processed video will be saved to the specified output file.

## Example Workflow

1. **Trim Video**: Select the "Trim Video" action, enter the start and end times, and specify the output file.
2. **Generate Subtitles**: Choose "Generate Subtitles," and the program will automatically create an SRT file with the subtitles.
3. **Burn-In Subtitles**: Select "Burn-In Subtitles," choose the SRT file, and specify the output video file.

## Project Structure

```
VideoEditorGUI/
│
├── transcoder/
│   ├── __init__.py
│   ├── video_transcoder.py
│   ├── audio_transcoder.py
│   ├── subtitle_handler.py
│   ├── metadata.py
│   ├── batch_processor.py
│   └── utils.py
│
├── tests/
│   └── test.py
│
├── video_editor_gui.py
├── setup.py
├── README.md
└── LICENSE
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **FFmpeg**: The powerful multimedia processing tool that powers most of the video and audio manipulations.
- **Whisper**: The open-source model used for generating subtitles from audio.
- **Tkinter**: The Python library used for building the GUI.
