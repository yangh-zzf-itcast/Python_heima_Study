import re
from pymysql import connect

URL_FUNC_DICT = dict()

# 函数列表
func_list = list()

# 应用装饰器自动添加字典
def route(url):
    def set_func(func):
        # func_list.append(func)  # 添加一个装饰器，列表中就会添加一个函数引用
        # 相当于 URL_FUNC_DICT["/index.py"] = index
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func

@route("/index.html")
def index():
    
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
                <input type="button" value="添加" id="toAdd" name="toAdd" systemidvalue="000007">   
            </td>
        </tr>
    """
    
    html = ""
    for line_info in goods_infos:
        html += tr_template % (line_info[0], line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6])
    # content = re.sub(r"\{%content%\}", str(goods_infos), content)
    content = re.sub(r"\{%content%\}", html, content)
    
    return content

@route("/login.html")
def login():
    return "这是登录页"

@route("/center.html")
def center():
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
                <input type="button" value="删除" id="toDel" name="toDel" systemidvalue="000007">   
            </td> 
        </tr>
    """
    
    html = ""
    for line_info in goods_infos:
        html += tr_template % (line_info[0], line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6])
    # content = re.sub(r"\{%content%\}", str(goods_infos), content)
    content = re.sub(r"\{%content%\}", html, content)
    
    return content

# 手动添加的字典
# URL_FUNC_DICT = {
#       "/index.py":index,
#        "/center.py":center,
#        "/login.py":login
#        }

def application(env, start_response):
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
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "产生了异常：%s" % str(ret)
