from django.contrib import admin

# Register your models here.
from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'desc','source','link','author', 'ctime','mtime')

    #搜索字段
    # search_fields = ('id', 'user_id', 'title','label','content')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('id',)

    # list_editable 设置默认可编辑字段
    # list_editable = ['username']

    # 设置哪些字段可以点击进入编辑界面
    # list_display_links = ('id', 'caption')