from django import template
register = template.Library() #регистрация для работы моих фильтров

@register.filter(name='cut_me') #регистрация самого фильтра
def cut_me(arg):
    print(arg.split('/')[-1])
    return arg.split('/')[-1]