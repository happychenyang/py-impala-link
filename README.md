# py-impala-link

#需要安装 python 扩展 impala.dbapi

#其余扩展上网查找安装即可

#可自行调配监听端口 默认设置 8002

#cd 当前文件夹

#执行命令 python ./webService.py

#该命令做为服务启动，访问端口带端口号可执行命令信息

# 参数：
'{
  "hostip":"impala的ip地址",
	
  "portnum":"端口号",
	
  "sqlstrs":"执行的SQL",
	
  "actions":"（add / query / delete / upload / execute / queryone）",
	
  }'

#把python作为服务启动

vim  /etc/systemd/system/impala.service

内容如下：

[Unit]

Description=The python script used for release

After=syslog.target network.target remote-fs.target nss-lookup.target

[Service]

Type=simple

ExecStart=/usr/bin/python2.7 /data/test/services.py

Restart=on-failure

[Install]

WantedBy=multi-user.target



//可以执行内容纯输出

ExecStart=/data/test/services.py > /data/test/services.log 2>&1

给上执行权限 chmod +x /etc/systemd/system/impala.service

 sudo chmod 644 /etc/systemd/system/impala.service
 

#3 使配置文件生效

sudo systemctl daemon-reload

sudo systemctl enable impala.service


设置开机自启动

systemctl enable impala.service


执行命令:

sudo systemctl start impala.service

sudo systemctl restart impala.service

sudo systemctl stop impala.service

sudo systemctl status impala.service

