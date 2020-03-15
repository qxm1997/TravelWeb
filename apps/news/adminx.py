import xadmin
from xadmin import views

from news.models import *


class NewsAdmin:
    """
    新闻后台管理
    """
    list_display = ['title', 'checknum', 'classification', 'add_times']
    list_filter = ['checknum', 'classification', 'add_times']
    search_fields = ['title', 'checknum', 'classification', 'add_times']
    fields = ['title', 'content', 'image', 'checknum', 'classification', 'add_times']
    readonly_fields = ['checknum']
    model_icon = 'fa newspaper-o'
    style_fields = {"content": "ueditor"}


class GlobalSettings:
    site_title = '后台管理系统'
    site_footer = 'TravelWeb'
    menu_style = 'accordion'


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(News, NewsAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
