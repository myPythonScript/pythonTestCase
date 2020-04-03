'''发送邮件'''
import os
import re
import smtplib
#发送多种形态的邮件，可带附件
from email.mime.multipart import MIMEMultipart
#发送字符串的邮件
from email.mime.text import MIMEText
#发送图片邮件
from email.mime.image import MIMEImage
#邮件中带附件
from email.mime.application import MIMEApplication

class send_email(object):

    def sendeml(self,sender,receiver,content,report_path):

        # 邮件头，From,To，邮件主题，
        msg = MIMEMultipart()
        msg['From'] = 'Daisy <'+ sender +'>'
        msg['To'] = '接收人 <'+ receiver +'>'
        msg['Subject'] = '发送邮件测试'

        #组装邮件发送的内容
        # 添加附件
        attachment = MIMEText(open(report_path, 'rb').read(), 'base64', 'utf-8')
        attachment['Content-Type'] = 'application/octet-stream'
        attachment["Content-Disposition"] = f'attachment; filename={os.path.basename(report_path)} '
        msg.attach(attachment)
        #正文是纯文本内容
        msg.attach(MIMEText(content,'plain','utf-8'))
        #正文是html格式的
        # msg.attach(MIMEText(content_html,'html','utf-8'))
        #发送图片
        # image = MIMEImage(open('C:/Users/Administrator/Desktop/9.jpg','rb').read())
        # image['Content-Type'] = 'application/octet-stream'
        # image['Content-Disposition'] = f'attachment; filename={os.path.basename("C:/Users/Administrator/Desktop/9.jpg")}'
        # msg.attach(image)


        #登录smtp服务，并发送邮件
        smtp = smtplib.SMTP('smtp.qq.com')
        smtp.ehlo()
        smtp.starttls()
        smtp.login('540224203@qq.com','acpkkzfdsdbdbcgc') #发送邮箱地址及授权码
        #收件人邮箱地址，可同时发多人
        smtp.sendmail(sender, receiver, msg.as_string())
        print("邮件发送成功")


# if __name__ == '__main__':
#     fromaddr = '540224203@qq.com'
#     toaddrs = '1584903008@qq.com'
#     content = '''发送邮件正文'''
#     Autho_code = 'acpkkzfdsdbdbcgc'
#     send_eml = send_email()
#     send_eml.sendeml(fromaddr, toaddrs,content,Autho_code)

