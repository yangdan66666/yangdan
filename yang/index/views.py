from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from .models import *
import os
# Create your views here.

def login_views(request):
	if request.method == 'GET':
		return render(request,'login.html')
	elif request.method == 'POST':
		uname = request.POST['uname']
		upwd = request.POST['upwd']
		uList = Users.objects.filter(uname=uname,upwd=upwd)
		if uList:
			#登陆失败
			if uList[0].isActive is False:
				c='该用户已被禁用!'
				return render(request,'login.html',locals())
			#登陆成功
			elif uList[0].isActive is True:
				#查询数据库wenjian表将用户名为uname的相关数据列表传输给浏览器
				L = wenjian.objects.filter(uname=uname)
				L1 = wenjian.objects.filter(gxname=uname)
				return render(request,'sym.html',locals())
		#登陆失败
		else:
			a='用户或密码错误!'
			return render(request,'login.html',locals())

def register_views(request):
	if request.method == 'GET':
		return render(request,'register.html')
	elif request.method == 'POST':
		uname = request.POST['uname']
		upwd = request.POST['upwd']
		uList = Users.objects.filter(uname=uname)
		#注册失败
		if uList:
			a='注册失败!!,用户名已存在!'
			return render(request,'register.html',locals())
		#注册成功
		else:
			#用户信息导入数据库
			dic={
				'uname':uname,
				'upwd':upwd
			}
			Users(**dic).save()
			#在服务器存储文件下创建注册用户名的文件夹用来存储用户上传文件以及区分
			LJ='./index/templates/文件'
			folder_name='%s'%str(uname)
			if os.path.isdir(LJ):
				os.mkdir(os.path.join(LJ,folder_name))
				b='注册成功！'
				return render(request,'login.html',locals())

def shangchuan_views(request):
	# 请求方法为POST时,进行处理;
	if request.method == "POST":
		# 获取上传的用户名称
		uname = request.POST['uname']
		#查询wenjian表中与用户为登陆用户的一直到文件数据
		L = wenjian.objects.filter(uname=uname)
		L1 = wenjian.objects.filter(gxname=uname)
		# 获取上传的文件,如果没有文件,则默认为None;
		File = request.FILES.get("myfile", None)
		if File is None:
			a='请选择上传文件!'
			return render(request,'sym.html',locals())
		else:
			#判断该用户上传文件目录下是否有本次上传文件
			lujing = "./index/templates/文件/"+"%s"%str(uname)+"/"+"%s"%File.name
			#用户已上传本次上传文件
			if File.name in os.listdir(r"./index/templates/文件/"+"%s"%str(uname)):
				a='你已上传%s,上传失败!'%File.name
				return render(request,'sym.html',locals())
			else:
				# 打开特定的文件进行二进制的写操作;
				with open(lujing,'wb+') as f:
					# 分块写入文件;
					for chunk in File.chunks():
						f.write(chunk)
				#文件信息存储到数据库
				dic={
					'wenjian':File.name,
					'lujing':lujing,
					'uname':uname,
				}
				wenjian(**dic).save()
				a='上传成功!!'
				return render(request,'sym.html',locals())


def gongxiang_views(request):
	if request.method == "POST":
		uname=request.POST['uname']
		wjm=request.POST['wjm']
		yonghu=request.POST['yonghu']
		uList = Users.objects.filter(uname=yonghu)
		#获取uname用户的文件信息数据返回页面
		L = wenjian.objects.filter(uname=uname)
		L1 = wenjian.objects.filter(gxname=uname)
		if uList:
			if wjm=='' or wjm=='已上传文件' or wjm=='共享给我的文件':
				b='请选择要共享的文件'
				return render(request,'sym.html',locals())
			else:
				s=wenjian.objects.get(uname=uname,wenjian=wjm)
				s.gxname=yonghu
				s.save()
				b='共享成功!'
				return render(request,'sym.html',locals())
		else:
			b='%s不存在此用户!'%yonghu
			return render(request,'sym.html',locals())


def dakai_views(request):
	if request.method=='POST':
		uname=request.POST['uname']
		wjm=request.POST['wjm']
		L = wenjian.objects.filter(uname=uname)
		L1 = wenjian.objects.filter(gxname=uname)
		if wjm=='' or wjm=='已上传文件' or wjm=='共享给我的文件':
			c='请选择要打开的文件'
			return render(request,'sym.html',locals())
		try:
			x=wenjian.objects.get(uname=uname,wenjian=wjm)
			f=open(x.lujing,'rb')
			if os.path.splitext(x.lujing)[1]=='.bmp' or os.path.splitext(x.lujing)[1]=='.jif'\
			 or os.path.splitext(x.lujing)[1]=='.jpg' or os.path.splitext(x.lujing)[1]=='.png':
				return StreamingHttpResponse(f,content_type="image/png")
			else:
				return StreamingHttpResponse(f)
		except:
			y=wenjian.objects.get(gxname=uname,wenjian=wjm)
			f00=open(y.lujing,'rb')
			if os.path.splitext(y.lujing)[1]=='.bmp' or os.path.splitext(y.lujing)[1]=='.jif' or\
			 os.path.splitext(y.lujing)[1]=='.jpg' or os.path.splitext(y.lujing)[1]=='.png':
				return StreamingHttpResponse(f00,content_type="image/png")
			else:
				return StreamingHttpResponse(f00)

def xiazai_views(request):
	if request.method=='POST':
		uname=request.POST['uname']
		wjm=request.POST['wjm']
		L = wenjian.objects.filter(uname=uname)
		L1 = wenjian.objects.filter(gxname=uname)
		if wjm=='' or wjm=='已上传文件' or wjm=='共享给我的文件':
			d='请选择要下载的文件'
			return render(request,'sym.html',locals())
		try:
			x=wenjian.objects.get(uname=uname,wenjian=wjm)
			file=open(x.lujing,'rb')
			response=StreamingHttpResponse(file)
			response['Content-Type']='application/octet-stream'
			response['Content-Disposition']='attachment;filename="%s"'%wjm
			return response
		except:
			y=wenjian.objects.get(gxname=uname,wenjian=wjm)
			file1=open(y.lujing,'rb')
			response=StreamingHttpResponse(file1)
			response['Content-Type']='application/octet-stream'
			response['Content-Disposition']='attachment;filename="%s"'%wjm
			return response