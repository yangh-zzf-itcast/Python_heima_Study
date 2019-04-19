from pymysql import connect


class JD(object):
    def __init__(self):
        """创建实例对象初始化，并连接数据库"""
        # 创建connection对象
        self.conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
        # 获取cursor游标对象
        self.cursor = self.conn.cursor()
       
    def __del__(self):
        """销毁对象时，关闭数据库的连接"""
         # 关闭cursor对象和connection对象
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        # 用cursor对象执行sql命令
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)
 

    def show_all_items(self):
        """显示所有的商品及信息"""
        # 操作的sql语句
        sql = "select * from goods;"
        self.execute_sql(sql)
       
    def show_cates(self):
        """显示所有商品的类别"""
        sql = "select name from goods_cates;"
        self.execute_sql(sql)
    
    def show_brands(self):
        """显示所有商品的品牌"""
        sql = "select brand_name from goods_brands;"
        self.execute_sql(sql)

    def add_brands(self):
        """添加一个新的品牌"""
        item_name = input("请输入新商品的品牌：")
        sql = """insert into goods_brands(brand_name) values("%s");""" % item_name
        self.cursor.execute(sql)
        self.conn.commit()
        
    def add_cates(self):
        """添加一个新的商品分类"""
        item_name = input("请输入新商品的分类：")
        sql = """insert into goods_cates(name) values("%s");""" % item_name
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        item_name = input("请输入想要查询的商品：")
        sql = "select * from goods where name = %s;"
        self.cursor.execute(sql, [item_name])
        print(self.cursor.fetchall())

    @staticmethod
    def show_menu():
        print("------京东------")
        print("1.所有的商品")
        print("2.所有的商品类别分类")
        print("3.所有的商品品牌分类")
        print("4.添加一个商品品牌")
        print("5.添加一个商品分类")
        print("6.查询指定商品")
        return input("请输入功能对应的序号：")

    def run(self):
        while True:
            num = self.show_menu()
            if num == "1":
                # 查询所有商品
                self.show_all_items()
            elif num == "2":
                # 查询所有分类
                self.show_cates()
            elif num == "3":
                # 查询所有品牌
                self.show_brands()
            elif num == "4":
                # 添加一个新的品牌
                self.add_brands()
            elif num == "5":
                # 添加一个新的商品分类
                self.add_cates()
            elif num == "6":
                # 根据名字查询商品的信息
                self.get_info_by_name()
            elif num == "0" or num == "q" or num == "Q":
                break
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
