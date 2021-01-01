from django import template
from ..models import Post, SocialShares
import re

register = template.Library()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts }

@register.inclusion_tag('blog/post/social_share.html')
def social_sharing(url, title):
    share_objects = SocialShares.objects.all()
    url_reg = re.compile('<SITE>')
    title_reg = re.compile('<TITLE>')
    tag_reg = re.compile('<TAG>')
    for i in share_objects:
        i.share_source = re.sub(url_reg, '{url}'.format(url=url), i.share_source)
        i.share_source = re.sub(title_reg, '{title}'.format(title=title), i.share_source)
        i.share_source = re.sub(tag_reg, '{tag}'.format(tag=title), i.share_source)
        
    return {'social_share': share_objects }