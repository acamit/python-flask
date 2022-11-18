import pathlib
import zipfile as zp
import os
folder = 'assignments'
if not os.path.exists(folder):
    os.makedirs(folder)

for zip_file in pathlib.Path('./').glob('*.zip'):
    dir_name = f'{folder}/{zip_file.stem}'
    print(dir_name)
    with zp.ZipFile(zip_file, 'r') as z:
        try:
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            z.extractall(path=dir_name)
        except Exception:
            print(f'skipping {dir_name}')
            print(Exception)


