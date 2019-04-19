from pymysql import connect
import time

class JD(object):
    def __init__(self):
        """创建实例对象初始化，并连接数据库"""
        # 创建connection对象
        self.conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
        # 获取cursor游标对象
        self.cursor = self.conn.cursor()
        # 标志用户登录状态, 默认0未登录, 登录用户id为空
        self.customer_state = 0
        self.login_customer_id = ""
       
    def __del__(self):
        """销毁对象时，关闭数据库的连接"""
         # 关闭cursor对象和connection对象
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        """执行查询显示命令"""
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
        """获取指定商品的信息"""
        item_name = input("请输入想要查询的商品：")
        sql = "select * from goods where name = %s;"
        self.cursor.execute(sql, [item_name])
        print(self.cursor.fetchall())

    def register_customer(self):
        """注册新用户"""
        # 注册用户就是给customers表插入数据
        id = 0
        name = input("请输入您的账号姓名：")
        address = input("请输入您的收货地址：")
        tel = input("请输入您的电话号码：")
        passwd = input("请输入您的密码：") 
        sql = """insert into customers(name,address,tel,passwd) values("%s","%s","%s","%s");""" % (name, address, tel, passwd)
        self.cursor.execute(sql)
        self.conn.commit()

    def login_customers(self):
        """用户登录"""
        name = input("请输入您的账号姓名：")
        passwd = input("请输入您的密码：")
        sql = """select id from customers where name="%s" and passwd="%s";""" % (name, passwd)
        self.cursor.execute(sql)
        # 如果登录成功返回用户id，反之失败为空
        tmp = self.cursor.fetchone()
        if tmp is not None:
            print("登陆成功！")
            # 修改用户状态
            self.customer_state = 1
            self.login_customer_id = tmp[0]
        else:
            print("登陆失败，返回菜单请重新登录！")

    def exit_customers(self):
        """用户注销"""
        self.customer_state = 0
        self.login_customer_id = ""

    def order(self):
        """用户下订单"""
        # 首先判断用户是否登录
        if self.customer_state == 0:
            print("您好，请先登录您的账户")
        else:
            # 当前登录用户id
            customer_id = int(self.login_customer_id)
            # 当前下单时间
            time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            # 先展示商品
            self.show_all_items()
            # 让顾客选择商品
            items_id = int(input("请输入您要购买的商品id："))
            items_quantity = int(input("请输入您要买的商品的数量；"))
            # 下订单就是向订单表与订单详情表中添加数据
            # 首先添加订单表
            sql = """insert into orders(order_date_time, customer_id) values("%s", "%d");""" % (time_str, customer_id)
            self.cursor.execute(sql)
            self.conn.commit()
            
            # 然后添加订单详情表数据
            sql = "select id from orders;"
            self.cursor.execute(sql)
            tmp = self.cursor.fetchall()
            last = len(tmp)
            # 最后插入的订单号
            order_id,  = tmp[last-1]
            print("订单号", order_id)
            sql = """insert into order_details(order_id, good_id, quantity) values("%d", "%d", "%d");""" % (order_id, items_id, items_quantity)
            self.cursor.execute(sql)
            self.conn.commit()

    def show_customers(self):
        print(self.login_customer_id)

    @staticmethod
    def show_menu():
        print("------京东------")
        print("1.所有的商品")
        print("2.所有的商品类别分类")
        print("3.所有的商品品牌分类")
        print("4.添加一个商品品牌")
        print("5.添加一个商品分类")
        print("6.查询指定商品")
        print("7.注册用户")
        print("8.用户登陆")
        print("9.用户下订单")
        print("10.退出登录")
        print("11.显示当前登录用户id")
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
            elif num == "7":
                # 注册新用户
                self.register_customer()
            elif num == "8":
                # 用户登录
                self.login_customers()
            elif num == "9":
                # 用户下订单
                self.order()
            elif num == "10":
                # 用户注销，退出登录
                self.exit_customers()
            elif num == "11":
                # 显示当前用户id
                self.show_customers()
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
