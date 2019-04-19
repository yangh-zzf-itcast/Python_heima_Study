import re
from pymysql import connect
import urllib.parse

URL_FUNC_DICT = dict()

# 函数列表
func_list = list()

# 应用装饰器自动添加字典
def route(url):
    """自动生成请求对应函数的字典"""
    def set_func(func):
        # func_list.append(func)  # 添加一个装饰器，列表中就会添加一个函数引用
        # 相当于 URL_FUNC_DICT["/index.py"] = index
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func

@route("/index.html")
def index(ret):
    """主页展示商品信息以及订单的添加"""
    # 前段人员负责，我们只需要调用前段写好的css/js/html页面即可
    # 复杂的页面，利用这种方式进行展示

    with open("./templates/index.html") as f:
        content = f.read()  # 页面模板
    
    # my_goods_info = "这是我的商品"
    # # 替换数据
    # content = re.sub(r"\{%content%\}", my_goods_info, content)

    # 获取MySQL数据
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
    # 获取cursor游标对象
    cursor = conn.cursor()
    cursor.execute("select * from goods;")
    goods_infos = cursor.fetchall()
    cursor.close()
    conn.close()

    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/add/%s.html"> <span class="glyphicon glyphicon-aria-hidden="true""></span>添加</a>
            </td>
        </tr>
    """
    
    html = ""
    for line_info in goods_infos:
        html += tr_template % (line_info[0], line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6],line_info[0])
        
    
    # content = re.sub(r"\{%content%\}", str(goods_infos), content)
    content = re.sub(r"\{%content%\}", html, content)
    
    return content


@route("/login.html")
def login(ret):
    return "这是登录页"


@route("/center.html")
def center(ret):
    """个人中心页展示订单，以及订单的修改和删除"""
    with open("./templates/center.html") as f:
        content = f.read()  # 页面模板
   
    # 获取MySQL数据
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
    # 获取cursor游标对象
    cursor = conn.cursor()
    cursor.execute("select g.id,g.name,g.cate_id,g.brand_id,g.price,b.quantity,b.Ps from goods g inner join buy_goods b on g.id = b.goods_id;")
    goods_infos = cursor.fetchall()
    cursor.close()
    conn.close()

    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td> 
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-aria-hidden="true""></span>修改</a>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/del/%s.html"> <span class="glyphicon glyphicon-aria-hidden="true""></span>删除</a>
            </td> 
        </tr>
    """
    
    html = ""
    for line_info in goods_infos:
        html += tr_template % (line_info[0], line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6],line_info[0],line_info[0])
    # content = re.sub(r"\{%content%\}", str(goods_infos), content):
    content = re.sub(r"\{%content%\}", html, content)
    
    return content

# 给路由添加正则表达式的原因：在实际开发中，rul中往往会带有很多参数，例如/add/000007.html中000007就是参数
# 如果没有正则的话，那么就需要编写N次@route进行添加url对应的函数 到字典中，字典中的键值就会有N个，浪费空间
# 而采用了正则之后，只需要编写1次@route就可以完成多url，例如/add/00007.html /add/000036.html等对应同一个函数，此时键值对个数会少很多

@route(r"/add/(\d+)\.html")
def add_buy_goods(ret):
    """添加订单功能函数"""
    # 1. 获取商品号
    buy_goods_id = ret.group(1)

    # 2. 在商品表内 判断下是否有这个商品
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
    # 获取cursor游标对象
    cursor = conn.cursor()
    sql = """select * from goods where id = %s;"""
    cursor.execute(sql, (buy_goods_id,))
    # 如果找不到这个商品，那么认为是非法的请求
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return "大哥手下留情,没有这件商品..."
   
    # 3. 在订单表内 判断一下是否已经购买了这个商品
    sql = """select * from goods g inner join buy_goods b on g.id = b.goods_id where g.id = %s;"""
    cursor.execute(sql, (buy_goods_id, ))
    # 如果查出来了，那么表示已经购买了
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return "已经购买过了，小心重复购买"

    # 如果商品存在，且还没有购买过，添加订单
    sql = """insert into buy_goods(goods_id) value(%s)"""
    cursor.execute(sql, (buy_goods_id, ))
    # 修改需要提交事务
    conn.commit()

    cursor.close()
    conn.close()

    return "添加订单成功 ...." 

@route(r"/del/(\d+)\.html")
def del_buy_goods(ret):
    """删除订单功能函数"""
    # 1. 获取商品号
    buy_goods_id = ret.group(1)

    # 2. 在商品表内 判断下是否有这个商品
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
    # 获取cursor游标对象
    cursor = conn.cursor()
    sql = """select * from goods where id = %s;"""
    cursor.execute(sql, (buy_goods_id,))
    # 如果找不到这个商品，那么认为是非法的请求
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return "大哥手下留情,没有这件商品..."
   
    # 3. 在订单表内 判断一下是否已经购买了这个商品
    sql = """select * from goods g inner join buy_goods b on g.id = b.goods_id where g.id = %s;"""
    cursor.execute(sql, (buy_goods_id, ))
    # 如果没查出来了，那么表示没有购买，表示非法删除
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return "没有购买过了，无法删除"

    # 如果商品存在，订单存在，取消关注
    sql = """delete from buy_goods where goods_id=%s;"""
    cursor.execute(sql, (buy_goods_id, ))
    # 修改需要提交事务
    conn.commit()

    cursor.close()
    conn.close()

    return "删除订单成功 ...." 

# 本质：新开一个页面提交修改
# 修改一共需要两步，实际开发中也是这样的
@route(r"/update/(\d+)\.html")
def show_update_page(ret):
    """显示修改订单的那个界面函数"""   
    # 1.获取商品号
    buy_goods_id = ret.group(1)

    # 2.打开页面模板
    # 修改的页面模板没有写好
    with open("./templates/update.html") as f:
        content = f.read()  # 页面模板

    # 3.根据股票代码查询相关的备注信息
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
    cursor = conn.cursor()
    sql = "select Ps from buy_goods where goods_id=%s;"
    cursor.execute(sql, (buy_goods_id, ))
    goods_infos = cursor.fetchone()
    note_info = goods_infos[0]  # 获取这个订单对应的备注信息
    cursor.close()
    conn.close()
 
    content = re.sub(r"\{%note_info%\}", note_info, content)
    content = re.sub(r"\{%buy_goods_id%\}", buy_goods_id, content)

    return content

@route(r"/update/(\d+)/(.*)\.html")
def save_update_page(ret):
    """保存修改的信息"""
    # 1.获取商品号
    buy_goods_id = ret.group(1)

    # 2.获取提交的修改信息
    comment = ret.group(2)
    # 浏览器发送给服务的是编码之后的，框架接收到的是一堆编码，需要对其进行解码 unquote解码；quote编码
    comment = urllib.parse.unquote(comment)

    # 3.根据股票修改相关的备注信息
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
    cursor = conn.cursor()
    sql = "update buy_goods set Ps = %s where goods_id=%s;"
    cursor.execute(sql, (comment, buy_goods_id))
    
    # 在实际开发中，提交修改信息要判断是不是符合规范，有没有sql注入问题，有没有病毒等，这里简化操作
    conn.commit()

    cursor.close()
    conn.close()
 
    return "修改订单备注成功..."

# 手动添加的字典
# URL_FUNC_DICT = {
#       "/index.py":index,
#        "/center.py":center,
#        "/login.py":login
#        }

def application(env, start_response):
    """主框架根据请求调用相应函数返回内容body以及返回HTTP响应头header"""
    # 设定http响应头信息，发回给浏览器的格式以及字符编码
    # 只写跟框架有关的响应头信息，不写服务器的
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])

    # 从传入的环境变量字典参数中 获取浏览器请求的文件名
    # 根据url不一样，返回的东西不一样
    # 缺点：有N个请求可能的话，有N个函数的话，就要写N个if语句来判断，代码太麻烦
    """
    file_name = env['PATH_INFO']
    if file_name == "/index.py":
        return index()
    elif file_name == "/login.py":
        return login()
    else:
        return 'Hello World 我爱你'
    """

    # 解决方式：事先将请求的对象名与对应的函数引用形成字典 保存在全局变量中：
    # 调用的时候通过键值获取函数引用来返回，可以避免使用繁多的if判断
    file_name = env['PATH_INFO']
    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        # return URL_FUNC_DICT[file_name]()
        for url, func in URL_FUNC_DICT.items():
            # print("url = %s, func = %s" % (url, func))
            ret = re.match(url, file_name)
            if ret:
                # 将正则匹配结果传入函数中，用不用由函数决定
                return func(ret)
        else:
            return "请求的url(%s)没有对应的函数..." % file_name

    except Exception as ret:
        return "产生了异常：%s" % str(ret)
