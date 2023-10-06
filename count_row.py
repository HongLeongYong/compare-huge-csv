''' count huge csv rows '''
import time
import global_variable as gv

def csv_count_rows(file_name):
    """
    Count the number of rows in a CSV file.
    """
    row_index = -1  # 初始化 row_index
    with open(file_name, encoding='utf-8') as file_handle:
        for index, _ in enumerate(file_handle):
            row_index = index
    return row_index + 1

def __main__():
    start_time = time.time()
    print(start_time)

    print(f'before file has {csv_count_rows(gv.BEFORE_HUGE_CSV_FILE)} rows')
    print(f'after file has {csv_count_rows(gv.AFTER_HUGE_CSV_FILE)} rows')

    end_time = time.time()
    print(f'end, use time: {end_time - start_time} seconds')
