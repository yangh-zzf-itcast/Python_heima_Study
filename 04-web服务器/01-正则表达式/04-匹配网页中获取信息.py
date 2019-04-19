import re


def sub_space(temp):
    str_ori = temp.group()
    str_ret = ""
    return str_ret


def main():
    # 获取抓取到的html
    with open("HTML.txt", "r") as f:
        content = f.read()

    # print(content)

    # 正则匹配，使用sub将不需要的替换剔除
    ret = re.sub(r"<\w*>|</\w*>|<\w* \w*=\"\w*\">|<\w* \w*=\"\w*-\w*\""">|&nbsp", sub_space, content)
    print(ret)

if __name__ == "__main__":
    main()
