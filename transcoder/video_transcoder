import ffmpeg

class VideoTranscoder:
    def __init__(self, input_file):
        self.input_file = input_file

    def transcode(self, output_file, codec='libx264', resolution=None, bitrate=None, framerate=None, preset='medium', format=None):
        """
        Transcode the video to the desired format and settings.
        
        :param output_file: Name of the output file.
        :param codec: Video codec to use (e.g., 'libx264', 'libx265').
        :param resolution: Target resolution (e.g., '1920x1080').
        :param bitrate: Target bitrate (e.g., '2M').
        :param framerate: Target framerate (e.g., 30).
        :param preset: Preset for video encoding speed/quality (e.g., 'fast', 'medium', 'slow').
        :param format: Desired output format (e.g., 'mp4', 'mkv', 'mov').
        """
        try:
            stream = ffmpeg.input(self.input_file)
            
            if resolution:
                stream = ffmpeg.filter(stream, 'scale', resolution)
            
            if framerate:
                stream = ffmpeg.filter(stream, 'fps', framerate)
            
            if format:
                output_file = f"{output_file}.{format}"
            
            stream = ffmpeg.output(stream, output_file, vcodec=codec, video_bitrate=bitrate, preset=preset)
            
            if format:
                stream = ffmpeg.output(stream, output_file, format=format)
            
            ffmpeg.run(stream)
            print(f"Transcoding complete: {output_file}")
        
        except ffmpeg.Error as e:
            print(f"An error occurred: {e.stderr.decode()}")

    def convert_to_mkv(self, output_file):
        """
        Convert the video to MKV format.
        
        :param output_file: Name of the output file without extension.
        """
        self.transcode(output_file, format='mkv')

    def convert_to_mp4(self, output_file):
        """
        Convert the video to MP4 format.
        
        :param output_file: Name of the output file without extension.
        """
        self.transcode(output_file, format='mp4')

    def convert_to_mov(self, output_file):
        """
        Convert the video to MOV format.
        
        :param output_file: Name of the output file without extension.
        """
        self.transcode(output_file, format='mov')

    def get_info(self):
        """
        Get metadata and information about the input video file.
        """
        try:
            probe = ffmpeg.probe(self.input_file)
            return probe
        
        except ffmpeg.Error as e:
            print(f"An error occurred: {e.stderr.decode()}")
            return None
