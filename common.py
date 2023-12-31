import os
import pathlib
import time

class FileParser:
    FILE_ABSOLUTE_PATH = pathlib.Path(__file__).parent.absolute()
    def __init__(self, file_path:str = None):
        self.file_path = os.path.join(self.FILE_ABSOLUTE_PATH, 'input_data') \
            if file_path is None else file_path

    def get_data_as_string(self, file_name:str) -> str:
        ctx = None
        with open(os.path.join(self.file_path, file_name)) as file:
            ctx = file.read()
        # clean white spaces
        return ctx.strip()
    

class PartContext:
    def __init__(self, part_name:str, file_name:str):
        self.part_name = part_name
        self.data = FileParser().get_data_as_string(file_name)
        self.start_time, self.end_time = None, None
        self.answer = None


    def __enter__(self):
        self.start_time = time.time()
        print(f'Starting part {self.part_name}')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end_time = time.time()
        print(f'Answer: {self.answer}')
        print(f'Part {self.part_name} took {self.end_time - self.start_time:.5f} seconds')
        if exc_type:
            print(f'Part {self.part_name} failed with error: {exc_value}')
        return True