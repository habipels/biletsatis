from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def add(value, arg):
    return value + arg
@register.simple_tag
def oturma_duzeni():
    deger =[]
    for i in range(1,138):
        if i == 1:
            deger.append("-1") 
        
        elif i == 7:
            deger.append("-2") 
        elif i == 13:
           deger.append("-1") 
        elif i == 25:
           deger.append("-1")
        elif (i-25) % 15 == 0 and i >24  :
            print(1)
            deger.append("-1")
        
        deger.append(i)

    return deger