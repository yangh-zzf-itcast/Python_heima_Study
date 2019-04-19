# 自定义过滤器
# 过滤器的本质就是Python的函数
from django.template import Library

# 创建一个Library对象
register = Library()

# 自定义过滤器最少一个参数，最多两个参数
@register.filter
def mod(num):
    """判断是否为偶数"""
    return num%2 == 0

@register.filter
def mod_val(num, val):
    """判断num是否可以被val整除"""
    return num%val == 0
