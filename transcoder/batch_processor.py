from concurrent.futures import ThreadPoolExecutor
from transcoder.video_transcoder import VideoTranscoder
from transcoder.audio_transcoder import AudioTranscoder

class BatchProcessor:
    def __init__(self, file_list):
        self.file_list = file_list

    def process_videos(self, output_dir, codec='libx264', resolution=None, bitrate=None, framerate=None, preset='medium', format='mp4', threads=4):
        def process_file(input_file):
            transcoder = VideoTranscoder(input_file)
            output_file = f"{output_dir}/{input_file.split('/')[-1].split('.')[0]}_output"
            transcoder.transcode(output_file, codec, resolution, bitrate, framerate, preset, format)
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(process_file, self.file_list)

    def process_audios(self, output_dir, codec='aac', bitrate='192k', threads=4):
        def process_file(input_file):
            transcoder = AudioTranscoder(input_file)
            output_file = f"{output_dir}/{input_file.split('/')[-1].split('.')[0]}_output.aac"
            transcoder.transcode(output_file, codec, bitrate)
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(process_file, self.file_list)
