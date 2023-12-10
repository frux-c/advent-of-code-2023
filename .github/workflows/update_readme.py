import os
import re
import pathlib
import subprocess

PATH = pathlib.Path(__file__).parent.parent.parent.absolute()
INPUT_DATA_PATH = os.path.join(PATH, 'input_data')
README_PATH = os.path.join(PATH, 'README.md')
TEMPLATE_PATH = os.path.join(PATH, 'README_TEMPLATE.md')
FILE_PATTERN = re.compile(r'aoc_day\d{2}.py')
README_RESULT_FORMAT = """
#### Day {day}
```bash
{result}
```
"""

def build_readme() -> None:
    with open(TEMPLATE_PATH) as template_file:
        readme = template_file.read()
        # get all the files in the directory
        files = [file for file in os.listdir(PATH) if FILE_PATTERN.match(file)]
        # sort the files by day
        files = sorted(files, key=lambda x: int(x[7:9]))
        for file in files:
            out, err = subprocess.Popen(
                ['python3', os.path.join(PATH, file)], 
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE).communicate()
            if err:
                readme += README_RESULT_FORMAT.format(
                    day=file[7:9],
                    result=err.decode('utf-8')
                )
            else:
                readme += README_RESULT_FORMAT.format(
                    day=file[7:9],
                    result=out.decode('utf-8').strip()
                )
        with open(README_PATH, 'w+') as readme_file:
            readme_file.write(readme)

if __name__ == '__main__':
    build_readme()