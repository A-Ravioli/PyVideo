import ffmpeg
import whisper

class SubtitleHandler:
    def __init__(self, input_file):
        self.input_file = input_file
        self.model = whisper.load_model("base")  # You can choose from tiny, base, small, medium, large

    def add_subtitle(self, subtitle_file, output_file):
        try:
            stream = ffmpeg.input(self.input_file)
            stream = ffmpeg.output(stream, output_file, **{'c:s': 'mov_text'}, subtitle=subtitle_file)
            ffmpeg.run(stream)
            print(f"Subtitle added: {output_file}")
        
        except ffmpeg.Error as e:
            print(f"An error occurred: {e.stderr.decode()}")

    def extract_subtitles(self, output_file):
        try:
            stream = ffmpeg.input(self.input_file)
            stream = ffmpeg.output(stream, output_file, **{'c:s': 'copy'})
            ffmpeg.run(stream)
            print(f"Subtitles extracted: {output_file}")
        
        except ffmpeg.Error as e:
            print(f"An error occurred: {e.stderr.decode()}")

    def generate_subtitles(self, output_srt_file):
        """
        Generate subtitles from the audio in the video file using Whisper.
        
        :param output_srt_file: Name of the output SRT file.
        """
        try:
            # Extract the audio from the video file
            audio_file = "temp_audio.wav"
            ffmpeg.input(self.input_file).output(audio_file, acodec='pcm_s16le', ac=1, ar='16k').run()

            # Transcribe the audio to text using Whisper
            result = self.model.transcribe(audio_file)
            
            # Write the transcription to an SRT file
            with open(output_srt_file, "w", encoding="utf-8") as srt_file:
                for i, segment in enumerate(result['segments']):
                    start = self._format_time(segment['start'])
                    end = self._format_time(segment['end'])
                    text = segment['text'].strip()

                    srt_file.write(f"{i + 1}\n")
                    srt_file.write(f"{start} --> {end}\n")
                    srt_file.write(f"{text}\n\n")

            print(f"Subtitles generated: {output_srt_file}")

        except Exception as e:
            print(f"An error occurred while generating subtitles: {str(e)}")

    @staticmethod
    def _format_time(seconds):
        """
        Helper method to format time in SRT format (HH:MM:SS,MIL).
        
        :param seconds: Time in seconds.
        :return: Formatted time string.
        """
        hours = int(seconds // 3600)
        minutes = i
