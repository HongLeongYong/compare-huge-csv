# 分割大 csv 文件成小 csv 文件 by row
import time
import global_variable as gv
import os
import pandas as pd

class FileSettings(object):
    def __init__(self, file_name, row_size=100):
        self.path_name = '\\'.join(file_name.split('\\')[:-1])
        self.file_name = file_name.split('\\')[-1]
        self.row_size = row_size

class FileSplitter(object):
    def __init__(self, file_settings):
        self.file_settings = file_settings

        if type(self.file_settings) != FileSettings:
            raise TypeError('file_settings must be FileSettings')
        
        self.df = pd.read_csv(os.path.join(self.file_settings.path_name, self.file_settings.file_name),
                            dtype = object,
                            header = None,
                            names = gv.csv_columns,
                            chunksize=self.file_settings.row_size)
    
    def split(self, output_directory = '123'):
        if not os.path.exists(os.path.join(self.file_settings.path_name, output_directory)):
            os.mkdir(os.path.join(self.file_settings.path_name, output_directory))
        
        counter = 0
        while True:
            try:
                file_name = '{}/{}/{}_{}_row_{}.csv'.format(
                    self.file_settings.path_name,
                    output_directory,
                    counter,
                    self.file_settings.file_name.split('.')[0],
                    self.file_settings.row_size)
                
                df = next(self.df).to_csv(file_name, index=False, header=True)
                counter += 1

                if counter == 1:
                    print(f'file {counter} done')
                    break
                    
            except StopIteration:
                break
            except Exception as e:
                print('Error: ',e)
                break

        return True
                                
def main():
    helper = FileSplitter(FileSettings(
        file_name = gv.before_huge_csv_file,
        row_size = 1000
        ))
    helper.split('output')

main()