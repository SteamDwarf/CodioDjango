from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html
from blog.models import Post

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

@register.simple_tag(takes_context=True)
def author_details_tag(context):
  request = context['request']
  current_user = request.user
  post = context['post']
  author = post.author

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

@register.simple_tag
def row(extra_classes=""):
  return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def col(extra_classes=""):
  return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def enddiv():
  return format_html('</div>')

@register.inclusion_tag('blog/post-list.html', takes_context=True)
def recent_posts(context):
  post = context['post']
  posts = Post.objects.exclude(pk=post.pk)[:5]
  return {'posts': posts, 'title': 'Recent Posts'}