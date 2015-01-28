#coding: utf8
from django.shortcuts import render_to_response,Http404,get_object_or_404
from django.http import HttpResponse
from poll.models import Poll,Choice
from django.template import Context,loader

# Create your views he
def index(req):
	poll_list=Poll.objects.order_by('-pub_date')[:5]
	output = ','.join([p.question for p in poll_list])
	
	'''
	template = loader.get_template('index.html')
	context=Context({'poll_list':poll_list})
	return HttpResponse(template.render(context))
	'''
	return render_to_response('index.html',{'poll_list':poll_list})


def vote(req,poll_id):
	return render_to_response('vote.html',{'poll_id':poll_id})

def result(req,poll_id):
	return render_to_response('result.html',{'poll_id':poll_id})

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
	return render_to_response('detail.html',{'poll':poll})


def error_404(req):
	return render_to_response('404.html')