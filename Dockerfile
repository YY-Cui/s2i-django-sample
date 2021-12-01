# 导入基础镜像
FROM python:3.9

USER 1001

# 复制代码文件
COPY . /django-sample

# 切换工作目录
WORKDIR /django-sample

USER root

# 构建镜像时需要执行的命令
RUN pip install -i https://pypi.douban.com/simple -r requirements.txt

USER 1001

# 每次启动镜像时需要执行的命令
CMD python manage.py runserver 0:8000

# 公开一个端口
EXPOSE 8000