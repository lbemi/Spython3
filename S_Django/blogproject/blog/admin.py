from django.contrib import admin
from .models import BlogArticles

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    list_filter =  ('publish', 'author') #过滤器（以日期，作者）
    search_fields = ('title', 'body') # 搜索框
    raw_id_fields = ('author', )
    date_hierarchy = "publish" #日期导航
    ordering = ['publish', 'author']  #排序

admin.site.register(BlogArticles,BlogArticlesAdmin)