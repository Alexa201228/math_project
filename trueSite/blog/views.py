from django.shortcuts import render, get_object_or_404
from .models import Post, PostImages
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.db.models import Count

def post_list(request, tag_slug=None):
    posts = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')

        posts = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request, 'blog/post/list_ajax.html', context={'posts': posts,
                                                                    'tag': tag})
    
    return render(request, 'blog/post/list.html', context={'posts': posts,
                                                            'tag': tag})

def post_detail(request, year, month, day, post):
    post_all = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    images = PostImages.objects.filter(post=post_all)
    str_images_pathes = "~^"
    for i in images:
        str_images_pathes += str(i.images.url) + ","

    post_tags_ids = post_all.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post_all.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    return render(request, 'blog/post/detail.html', context={'post': post_all,
                                                    'images': str_images_pathes,
                                                    'similar_posts':similar_posts,})
