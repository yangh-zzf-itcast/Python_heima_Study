from pymysql import connect

def main():
    # 创建connection对象
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
    # 获取cursor游标对象
    cursor = conn.cursor()

    for i in range(100000):
        cursor.execute("insert into test_index values('ha-%d')" % i)
        
    conn.commit()

if __name__ == "__main__":
    main()
