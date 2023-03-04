from django import template


register = template.Library()

CENSOR_SYMBOL = {
   'редиска': '***',
}


@register.filter()
def censor(value, code='редиска'):

   value = value.replace(code, '*' * len(code))


   if type(value) == str:
      return f'{value}'
   else:
      print('ошибка')