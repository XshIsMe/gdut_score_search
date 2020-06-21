#基于的基础镜像
FROM python

#代码添加到code文件夹
ADD ./app /usr/src/app

# 设置app文件夹是工作目录
WORKDIR /usr/src/app

# 安装支持
RUN pip install -i https://pypi.douban.com/simple --no-cache-dir -r requirements.txt

# 运行
CMD [ "python", "/usr/src/app/app.py" ]