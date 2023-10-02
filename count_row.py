''' count huge csv rows '''
import time
import global_variable as gv

def csv_count_rows(file_name):
    """Count the number of rows in a CSV file."""
    start_time = time.time()
    print(start_time)

    row_index = -1 # 初始化 row_index
    with open(file_name, encoding='utf-8') as file_handle:
        for row_index in enumerate(file_handle):
            if row_index % 10_000_000 == 0:
                middle_time = time.time()
                print(f'{row_index} rows, use time: {middle_time - start_time} seconds')

    end_time = time.time()
    print(f'end, use time: {end_time - start_time} seconds')
    return row_index + 1

print(f'before file has {csv_count_rows(gv.before_huge_csv_file_01)} rows')
print(f'after file has {csv_count_rows(gv.after_huge_csv_file)} rows')
