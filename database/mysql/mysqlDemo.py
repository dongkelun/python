# 连接MYSQL示例

from sqlalchemy import create_engine
import pandas as pd


def get_db(url):
    return create_engine(url, connect_args={'charset': 'utf8'}, encoding='utf8')


def get_df(sql, url="mysql://root:Root-123456@192.168.44.128:3306/test"):
    db = get_db(url)
    df = pd.read_sql_query(sql, db)
    return df


if __name__ == '__main__':
    db_url = "mysql://root:Root-123456@192.168.44.128:3306/test"
    data1 = get_df("select * from test", db_url)
    data2 = get_df("select * from test where id BETWEEN '%s' and '%s'" % (6, 10), db_url)

    print(data1.head(10))
    print(data2)
