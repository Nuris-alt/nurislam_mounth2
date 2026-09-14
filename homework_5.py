from abc import ABC, abstractmethod
class File(ABC):
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def get_file_info(self):
        pass

class TextFile(File):
    def open(self):
        print("текстовый файл открыт")

    def get_file_info(self):
        print("ТЕКСТ")

class ImageFile(File):
    def open(self):
        print("файл изображения открыт")

    def get_file_info(self):
        print(" ( ͡° ͜ʖ ͡°)")

class AudioFile(File):
    def open(self):
        print("звуковой файл открыт")

    def get_file_info(self):
        print("играет ваш плейлист")

class VideoFile(File):
    def open(self):
        print("видео файл открыт")

    def get_file_info(self):
        print("возпроизводятся ваши сохранённые видео")

files = [
    TextFile(),
    ImageFile(),
    AudioFile(),
    VideoFile(),
]

for file in files:
    file.open()
    file.get_file_info()

