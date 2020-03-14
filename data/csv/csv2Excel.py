# csv转成Excel文件

import pandas as pd
import time


def csv2excel(file_path):
    start_time = time.time()
    file = pd.read_csv(file_path, low_memory=False, dtype="str")
    print(file.head(10))

    if len(file) < 1000000:
        file.to_excel(file_path.replace('.csv', '.xlsx'), index=False)
    else:
        with pd.ExcelWriter(file_path.replace('.csv', '.xlsx')) as writer:
            file[:600000].to_excel(writer, sheet_name="1")
            file[600000:].to_excel(writer, sheet_name="2")

    end_time = time.time()

    print('total coast ' + str(end_time - start_time) + ' s')


if __name__ == '__main__':
    csv2excel("C:Users\\14123\Desktop\icbc\icbc_01.csv")
