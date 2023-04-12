import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 登录
smtpd_obj = smtplib.SMTP_SSL("smtp.email.163.com", 465)
# 用户名密码
smtpd_obj.login("aloysli@163.com", "1216@0913")
# 设置邮箱内容
msg = MIMEText("hello, 小哥哥约嘛", "plain", "utf-8")
msg["From"] = Header("来自小妹妹的问候", "utf-8")
msg["To"] = Header("幽暗人", "utf-8")
msg["subject"] = Header("小妹的信", "utf-8")

# 发邮件
smtpd_obj.sendmail("702251811@qq.com", msg.as_string())