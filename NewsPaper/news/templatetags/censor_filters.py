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


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()