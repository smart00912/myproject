#coding: utf8
from django.shortcuts import render_to_response,Http404,get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from poll.models import Poll,Choice
from django.template import Context,loader
from django.template import RequestContext
from django.core.urlresolvers import reverse,resolve
from django.views import generic




# 因为表单使用的是post方法，所以每个view 后都添加了 context_instance=RequestContext(request)
#否则可能会出现这个错误: {% csrf_token %} was used in a template, but the context did not provide the value. 
# Create your views he
def index(req):
	poll_list=Poll.objects.order_by('-pub_date')[:5]
	output = ','.join([p.question for p in poll_list])
	
	'''
	template = loader.get_template('index.html')
	context=Context({'poll_list':poll_list})
	return HttpResponse(template.render(context))
	'''
	return render_to_response('index.html',{'poll_list':poll_list},context_instance=RequestContext(req))

"""
def detail(req,poll_id):

	try:
		# 查看传入的poll_id是否有效,否则跳转404页面
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		#raise Http404
		return render_to_response('404.html')

	'''
	# 等价于上面备注是掉的代码
	poll = get_object_or_404(Poll,pk=poll_id)
	'''
	return render_to_response('detail.html',{'poll':poll},context_instance=RequestContext(req))
	
def result(req,poll_id):
	poll = get_object_or_404(Poll,pk=poll_id)
	return render_to_response('result.html',{'poll':poll},context_instance=RequestContext(req))

def vote(req,poll_id):
	p = get_object_or_404(Poll,pk=poll_id)
	try:
		selected_choice=p.choice_set.get(pk=req.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		return render(req,'poll/detail.html',{'error_message':'No Choice'})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		# reverse:通过传递给Reverse函数相应的url_name以及必要的参数，那么便会生成相应的url
		#此处的polls:result表示polls域名空间下的name=result的url
		return HttpResponseRedirect(reverse('polls:result',args=(p.id,)))
"""
#通用视图

class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'poll_list'
	def get_queryset(self):
		return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Poll
	template_name = 'detail.html'
	

class ResultView(generic.DetailView):
	model = Poll
	template_name = 'result.html'
	
def vote(req,poll_id):
	p = get_object_or_404(Poll,pk=poll_id)
	try:
		selected_choice=p.choice_set.get(pk=req.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		return render(req,'poll/detail.html',{'error_message':'No Choice'})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		# reverse:通过传递给Reverse函数相应的url_name以及必要的参数，那么便会生成相应的url
		#此处的polls:result表示polls域名空间下的name=result的url
		return HttpResponseRedirect(reverse('author-polls:result',args=(p.id,)))




