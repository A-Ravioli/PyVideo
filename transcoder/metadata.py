import ffmpeg

class MetadataHandler:
    def __init__(self, input_file):
        self.input_file = input_file

    def get_metadata(self):
        try:
            probe = ffmpeg.probe(self.input_file)
            return probe['format']['tags']
        
        except ffmpeg.Error as e:
            print(f"An error occurred: {e.stderr.decode()}")
            return None

    def set_metadata(self, output_file, title=None, artist=None, genre=None):
        try:
            stream = ffmpeg.input(self.input_file)
            metadata = {}

            if title:
                metadata['title'] = title
            if artist:
                metadata['artist'] = artist
            if genre:
                metadata['genre'] = genre
            
            stream = ffmpeg.output(stream, output_file, **{'metadata:g': metadata})
            ffmpeg.run(stream)
            print(f"Metadata set: {output_file}")
        
        except ffmpeg.Error as e:
            print(f"An error occurred: {e.stderr.decode()}")
