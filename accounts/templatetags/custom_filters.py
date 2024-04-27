from django import template
from django.contrib.auth.models import Group

register = template.Library()
 
@register.filter
def has_role(user, role):
    group = Group.objects.filter(name=role).first()
    return group in user.groups.all()