```python
import os
import json
from moviepy.editor import VideoFileClip, concatenate_videoclips

class VideoTutorial:
    def __init__(self, tutorial_id, video_path):
        self.tutorial_id = tutorial_id
        self.video_path = video_path
        self.video_clip = VideoFileClip(video_path)

    def get_duration(self):
        return self.video_clip.duration

class VideoTutorialsManager:
    def __init__(self, tutorials_directory):
        self.tutorials_directory = tutorials_directory
        self.tutorials = self.load_tutorials()

    def load_tutorials(self):
        tutorials = {}
        for filename in os.listdir(self.tutorials_directory):
            if filename.endswith(".mp4"):
                tutorial_id = filename[:-4]
                video_path = os.path.join(self.tutorials_directory, filename)
                tutorials[tutorial_id] = VideoTutorial(tutorial_id, video_path)
        return tutorials

    def get_tutorial(self, tutorial_id):
        return self.tutorials.get(tutorial_id)

    def create_playlist(self, tutorial_ids):
        clips = [self.tutorials[tutorial_id].video_clip for tutorial_id in tutorial_ids]
        playlist = concatenate_videoclips(clips)
        return playlist

    def save_playlist(self, tutorial_ids, output_path):
        playlist = self.create_playlist(tutorial_ids)
        playlist.write_videofile(output_path)

    def get_tutorials_metadata(self):
        metadata = {}
        for tutorial_id, tutorial in self.tutorials.items():
            metadata[tutorial_id] = {
                "duration": tutorial.get_duration(),
                "video_path": tutorial.video_path
            }
        return metadata

    def save_tutorials_metadata(self, output_path):
        metadata = self.get_tutorials_metadata()
        with open(output_path, "w") as f:
            json.dump(metadata, f, indent=4)

if __name__ == "__main__":
    manager = VideoTutorialsManager("/path/to/tutorials/directory")
    manager.save_tutorials_metadata("/path/to/metadata.json")
    manager.save_playlist(["tutorial1", "tutorial2", "tutorial3"], "/path/to/playlist.mp4")
```