from django import template
import time
from urllib.parse import quote,unquote
#创建模板库的实例
register = template.Library()

#注册过滤器
@register.filter
def dealwithtime(t1):
    x = time.localtime(int(t1))
    t2 = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return t2

@register.filter
def dealwithkeyword(t1):
    t2=unquote(t1)
    return t2