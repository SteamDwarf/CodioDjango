from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html

user_model = get_user_model()
register = template.Library()

@register.filter
def author_details(author, current_user):
  if not isinstance(author, user_model): return ""

  if author.id == current_user.id:
    return format_html('<strong>me</strong>')

  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  else: 
    name = author.username

  
  if author.email:
    return format_html(
      '<a href="mailto:{}">{}</a>',
      author.email,
      name
    )
    

  return name