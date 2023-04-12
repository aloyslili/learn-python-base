import re
import os
import time
import random
import requests
from lxml import etree

headers = {

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    'Cookie': '__yjs_duid=1_002635c9cb0c21fbc537616375b78db01667376111485; Hm_lvt_c59f2e992a863c2744e1ba985abaea6c=1667376112,1667385958; zkhanecookieclassrecord=%2C66%2C54%2C; PHPSESSID=s5s8d9ee48npdjomni82pogi66; zkhanmlusername=qq_ikaros128; zkhanmluserid=6586793; zkhanmlgroupid=1; zkhanmlrnd=0Ld2FgVl5wk8Et6zPhjh; zkhanmlauth=266906104831f663901fcc48fbb2f865; Hm_lpvt_c59f2e992a863c2744e1ba985abaea6c=1667386383',
    'Referer': 'http://pic.netbian.com/e/memberconnect/qq/loginend.php?code=0420B576386DDEE9D97C44193121538B&state=2ed7f38385c32d9116b8cf23d45c3653',
}
path = '../4K高清美女大图'
if not os.path.exists(path):
    os.mkdir(path)
for i in range(1, 62):
    if i == 1:
        url = 'http://pic.netbian.com/4kmeinv/'
    else:
        url = f'https://pic.netbian.com/4kmeinv/index_{i}.html'

    res = requests.get(url=url, headers=headers)
    data = res.content.decode("gbk")
    tree = etree.HTML(data)
    li_list = tree.xpath('//ul[@class="clearfix"]/li')
    for li in li_list:
        a_url = "http://pic.netbian.com"+li.xpath('./a/@href')[0]
        img_res = requests.get(url=a_url).content.decode("gbk")
        tree = etree.HTML(img_res)
        img_src = "http://pic.netbian.com"+tree.xpath('//a[@id="img"]/img/@src')[0]
        title = tree.xpath('//a[@id="img"]/img/@alt')[0]
        img_data = requests.get(url=img_src).content
        with open(os.path.join(path, title+".jpg"), "wb") as f:
            f.write(img_data)
    print("下载第"+str(i)+"页图片完成")
    time.sleep(random.randint(1, 5))