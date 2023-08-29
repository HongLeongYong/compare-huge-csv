# count huge csv rows
# the fastest way is use open
import time
import global_variable as gv

def csv_count_rows(file_name):
    start_time = time.time()
    print(start_time)

    with open(file_name, encoding='utf-8') as f:
        for i, l in enumerate(f):
            if i % 10_000_000 == 0:
                middle_time = time.time()
                print(f'{i} rows, use time: {middle_time - start_time} seconds')
            pass

    end_time = time.time()
    print(f'end, use time: {end_time - start_time} seconds')
    return i + 1

print(f'before file has {csv_count_rows(gv.before_huge_csv_file)} rows')
print(f'after file has {csv_count_rows(gv.after_huge_csv_file)} rows')