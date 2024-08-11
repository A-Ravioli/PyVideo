import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

from transcoder.video_transcoder import VideoTranscoder
from transcoder.subtitle_handler import SubtitleHandler

class VideoEditorGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Video Editor GUI")
        self.geometry("600x400")

        self.file_path = None

        # Drag and Drop Area
        self.drop_area = tk.Label(self, text="Drag and Drop a Video File Here", relief="groove", height=2)
        self.drop_area.pack(pady=20, padx=20, fill="both")
        self.drop_area.bind("<Button-1>", self.select_file)

        # Feature Selection
        self.feature_label = tk.Label(self, text="Choose an action:")
        self.feature_label.pack(pady=10)

        self.feature_combobox = ttk.Combobox(self, state="readonly", width=50)
        self.feature_combobox['values'] = [
            "Trim Video",
            "Concatenate Videos",
            "Adjust Speed",
            "Add Text Overlay",
            "Add Watermark",
            "Stabilize Video",
            "Extract Frames",
            "Replace Audio",
            "Add Fade In/Out",
            "Picture in Picture",
            "Rotate Video",
            "Flip Video",
            "Change Aspect Ratio",
            "Adjust Brightness/Contrast",
            "Apply Filter",
            "Normalize Audio",
            "Generate Subtitles",
            "Burn-In Subtitles",
            "Remove Green Screen",
            "Create GIF",
            "Generate Thumbnail"
        ]
        self.feature_combobox.pack(pady=5)

        # Run Button
        self.run_button = tk.Button(self, text="Run", command=self.run_action)
        self.run_button.pack(pady=20)

    def select_file(self, event=None):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.mkv *.mov")])
        if file_path:
            self.file_path = file_path
            self.drop_area.config(text=os.path.basename(file_path))

    def run_action(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a video file.")
            return

        selected_action = self.feature_combobox.get()
        if not selected_action:
            messagebox.showerror("Error", "Please choose an action.")
            return

        output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if not output_file:
            return

        try:
            transcoder = VideoTranscoder(self.file_path)
            subtitle_handler = SubtitleHandler(self.file_path)

            if selected_action == "Trim Video":
                start_time = float(input("Enter start time (in seconds): "))
                end_time = float(input("Enter end time (in seconds): "))
                transcoder.trim_video(output_file, start_time, end_time)

            elif selected_action == "Concatenate Videos":
                file_list = filedialog.askopenfilenames(title="Select Videos to Concatenate")
                transcoder.concatenate_videos(file_list, output_file)

            elif selected_action == "Adjust Speed":
                speed_factor = float(input("Enter speed factor (e.g., 0.5 for slow motion, 2 for fast motion): "))
                transcoder.adjust_speed(output_file, speed_factor)

            elif selected_action == "Add Text Overlay":
                text = input("Enter text to overlay: ")
                position = input("Enter position (x:y): ")
                font_size = int(input("Enter font size: "))
                color = input("Enter text color: ")
                transcoder.add_text_overlay(output_file, text, position, font_size, color)

            elif selected_action == "Add Watermark":
                watermark_file = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
                position = input("Enter position (x:y): ")
                transcoder.add_watermark(output_file, watermark_file, position)

            elif selected_action == "Stabilize Video":
                transcoder.stabilize_video(output_file)

            elif selected_action == "Extract Frames":
                frame_rate = int(input("Enter frame rate for extraction (e.g., 1 for 1 frame per second): "))
                transcoder.extract_frames(output_file, frame_rate)

            elif selected_action == "Replace Audio":
                audio_file = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav *.aac")])
                transcoder.replace_audio(audio_file, output_file)

            elif selected_action == "Add Fade In/Out":
                fade_in = int(input("Enter fade-in duration in seconds: "))
                fade_out = int(input("Enter fade-out duration in seconds: "))
                transcoder.add_fade_in_out(output_file, fade_in, fade_out)

            elif selected_action == "Picture in Picture":
                overlay_video = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.mkv *.mov")])
                position = input("Enter position for PiP video (x:y): ")
                transcoder.picture_in_picture(overlay_video, output_file, position)

            elif selected_action == "Rotate Video":
                angle = int(input("Enter rotation angle (e.g., 90, 180): "))
                transcoder.rotate_video(output_file, angle)

            elif selected_action == "Flip Video":
                direction = input("Enter flip direction (horizontal or vertical): ")
                transcoder.flip_video(output_file, direction)

            elif selected_action == "Change Aspect Ratio":
                aspect_ratio = input("Enter target aspect ratio (e.g., 16:9): ")
                transcoder.change_aspect_ratio(output_file, aspect_ratio)

            elif selected_action == "Adjust Brightness/Contrast":
                brightness = float(input("Enter brightness adjustment (-1 to 1): "))
                contrast = float(input("Enter contrast adjustment (-1 to 1): "))
                transcoder.adjust_brightness_contrast(output_file, brightness, contrast)

            elif selected_action == "Apply Filter":
                filter_name = input("Enter filter name (e.g., 'hue'): ")
                filter_params = input("Enter filter parameters (e.g., 'h=90'): ")
                transcoder.apply_filter(output_file, filter_name, filter_params)

            elif selected_action == "Normalize Audio":
                transcoder.normalize_audio(output_file)

            elif selected_action == "Generate Subtitles":
                subtitle_file = filedialog.asksaveasfilename(defaultextension=".srt", filetypes=[("SRT files", "*.srt")])
                subtitle_handler.generate_subtitles(subtitle_file)

            elif selected_action == "Burn-In Subtitles":
                subtitle_file = filedialog.askopenfilename(filetypes=[("SRT files", "*.srt")])
                subtitle_handler.burn_in_subtitles(subtitle_file, output_file)

            elif selected_action == "Remove Green Screen":
                transcoder.remove_green_screen(output_file)

            elif selected_action == "Create GIF":
                start_time = float(input("Enter start time for GIF (in seconds): "))
                duration = float(input("Enter duration of the GIF (in seconds): "))
                transcoder.create_gif(output_file, start_time, duration)

            elif selected_action == "Generate Thumbnail":
                time_position = float(input("Enter time position for thumbnail (in seconds): "))
                transcoder.generate_thumbnail(output_file, time_position)

            messagebox.showinfo("Success", f"{selected_action} completed successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = VideoEditorGUI()
    app.mainloop()
