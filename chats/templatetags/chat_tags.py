from django import template
from accounts.models import User

register = template.Library()

@register.simple_tag
def profile_picture(user):
    if user.profile_picture:
        return user.profile_picture.url
    else:
        return '/static/images/default.png'


@register.simple_tag
def user_role(user):
    return user.role.name