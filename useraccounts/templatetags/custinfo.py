from django import template
from useraccounts.models import *

register = template.Library()

class FooNode(template.Node):
    def __init__(self,obj):
        self.object = template.Variable(obj)
    
    def render(self,context):
        obj = self.object.resolve(context)
        dietobj = obj
        cdetail = credittable.objects.get(messname = dietobj.messname, customer = dietobj.customer)
        context['credit'] = cdetail.credit
        return ''
    
@register.tag
def c2details(parser,token):
    try:
        tag_name, obj = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents.split()[0]
    return FooNode(obj)

