import re


def main():
    names = ["age", "_age", "1age", "a_age", "age_1_", "age!", "a#123", "________", "--------"]

    for name in names:
        # ret = re.match(r"[a-zA-Z_]+[a-zA-Z0-9_]*", name)
        # 正确规范写法，^表示判断以什么开头
        # python中的match默认是判断开头
        # $表示判断以什么结尾
        ret = re.match(r"^[a-zA-Z_]+[a-zA-Z0-9_]*$", name)
        if ret:
            print("变量名：%s ---> 符合要求, 匹配到的字符 %s" % (name, ret.group()))
        else:
            print("变量名：%s ---> 非法" % name)


if __name__ == "__main__":
    main()
