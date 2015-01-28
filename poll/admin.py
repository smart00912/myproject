#coding: utf8
from django.contrib import admin
from poll.models import Poll,Choice

# 设置Choice表的显示样式
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	''''
	 设置admin页面的布局(改变问题和日期输入框的上下顺序)
	fields = ['pub_date','question']
	'''''
	# 将日期和问题分成两个表格,并且折叠日期表格
	fieldsets = [(None,{'fields':['question']}),('date_info',{'fields':['pub_date'],'classes':['collapse']}),]
	# 设置与choice表的关联显示
	inlines = [ChoiceInline]
	#设置显示的列属性
	list_display = ('question','pub_date','was_published_recently')
	#在右侧显示过滤窗口
	list_filter = ['pub_date']
	#添加搜索窗口
	search_fields = ['question']
	#添加日期分层显示
	date_hierarchy = 'pub_date'
	
	
# Register your models here.


# 此种方式无法显示两个表的关联
#admin.site.register([Poll,Choice,],PollAdmin)

#指定Poll和类PollAdmin绑定确保在PollAdmin中定义的属性只体现在Poll的表中
admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)
