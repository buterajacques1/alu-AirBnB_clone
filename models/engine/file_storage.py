import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass

            from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

from models import storage


class BaseModel:
    ...

    def save(self):
        storage.new(self)
        storage.save()

    def __init__(self, *args, **kwargs):
        ...
        storage.new(self)