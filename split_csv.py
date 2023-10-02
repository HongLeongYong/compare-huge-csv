"""
Module to split large CSV files into smaller CSV files by row.
"""

import os
import pandas as pd
import global_variable as gv

class FileSettings:
    """Class to hold file settings."""
    def __init__(self, file_name, row_size=100):
        self.path_name = '\\'.join(file_name.split('\\')[:-1])
        self.file_name = file_name.split('\\')[-1]
        self.row_size = row_size

class FileSplitter:
    """Class to split files."""
    def __init__(self, file_settings):
        if not isinstance(file_settings, FileSettings):
            raise TypeError('file_settings must be FileSettings')
        self.file_settings = file_settings
        self.data_frame = pd.read_csv(
            os.path.join(self.file_settings.path_name, self.file_settings.file_name),
            dtype=object,
            header=None,
            names=gv.CSV_COLUMNS,
            chunksize=self.file_settings.row_size
        )

    def split(self, output_directory='output'):
        """Method to split the file."""
        if not os.path.exists(os.path.join(self.file_settings.path_name, output_directory)):
            os.mkdir(os.path.join(self.file_settings.path_name, output_directory))
        counter = 0
        try:
            for chunk in self.data_frame:
                file_name = f'{self.file_settings.path_name}/{output_directory}/{counter}_{self.file_settings.file_name.split(".")[0]}_row_{self.file_settings.row_size}.csv'
                chunk.to_csv(file_name, index=False, header=True)
                counter += 1
                print(f'file {counter} done')
        except Exception as exc:
            print('Error:', exc)

def main():
    """Main function."""
    helper = FileSplitter(FileSettings(
        file_name=gv.BEFORE_HUGE_CSV_FILE,
        row_size=1000
    ))
    helper.split('output')

if __name__ == "__main__":
    main()
