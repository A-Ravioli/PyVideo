import ffmpeg

class AudioTranscoder:
    def __init__(self, input_file):
        self.input_file = input_file

    def transcode(self, output_file, codec='aac', bitrate='192k'):
        try:
            stream = ffmpeg.input(self.input_file)
            stream = ffmpeg.output(stream, output_file, acodec=codec, audio_bitrate=bitrate)
            ffmpeg.run(stream)
            print(f"Audio transcoding complete: {output_file}")
        
        except ffmpeg.Error as e:
            print(f"An error occurred: {e.stderr.decode()}")
