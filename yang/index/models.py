from django.db import models

# Create your models here.
class Users(models.Model):
    # 密码 - CharField()
    upwd = models.CharField(max_length=18)
    # 用户名 - CharField()
    uname = models.CharField(max_length=14)
    # 启用/禁用 - BooleanField(),默认值为True
    isActive = models.BooleanField(default=True)

class wenjian(models.Model):
	#文件名
	wenjian = models.CharField(max_length=20)
	#文件路径
	lujing = models.CharField(max_length=60)
	#上传用户
	uname = models.CharField(max_length=14)
	#共享给的用户
	gxname = models.CharField(max_length=1)