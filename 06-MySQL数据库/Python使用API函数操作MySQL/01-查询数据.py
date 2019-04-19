from pymysql import connect


class JD(object):
    def __init__(self):
        pass

    
    def show_all_items():
        """显示所有的商品及信息"""
        # 创建connection对象
        conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
        # 获取cursor游标对象
        cursor = conn.cursor()
        # 操作的sql语句
        sql = "select * from goods;"
        # 用cursor对象执行sql命令
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)

        # 关闭cursor对象和connection对象
        cursor.close()
        conn.close()


    def show_cates():
        """显示所有商品的类别"""
        conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
        cursor = conn.cursor()
        sql = "select name from goods_cates"
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)
        # 关闭cursor对象和connection对象
        cursor.close()
        conn.close()


    def run(self):
        while True:
            print("------京东------")
            print("1.所有的商品")
            print("2.所有的商品类别分类")
            print("3.所有的商品品牌分类")
            num = input("请输入功能对应的序号：")
            
            if num == "1":
                self.show_all_items()
            elif num == "2":
                self.show_cates()
            elif num == "3":
                pass
            else:
                print("输入有误，重新输入...")


# 让main对象或者main函数越简单越好
def main():
    # 1.创建一个京东商城对象
    jd = JD()

    # 2.调用这个对象的run方法，让其运行
    jd.run()

if __name__ == "__main__":
    main()
