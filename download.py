import os
import re
import execjs
import ffmpeg
import requests
from Crypto.Cipher import AES
from lxml.html import fromstring


# 解密ts视频流
IV = b'0000000000000000'
def aes_decrypt(bytes_,key_array):
    key = bytes(key_array)
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, IV)
    decrypt_bytes = cryptos.decrypt(bytes_)
    return decrypt_bytes


# 解密文本内容
JS_FILE = open("decrypt.js")
CTX = execjs.compile(JS_FILE.read())
JS_FILE.close()
def destm_decrypt(content,mode=None):
    return  CTX.call("Destm", content, mode)


# 单个ts下载切换cdn
# 通过抓包测试获取的cnd域名
CDN = ["v3.mukewang.com","video3.sycdn.imooc.com","video1.sycdn.imooc.com"]
def ts_download(url):
    # cdn域名排序
    host_cdn = url.split('//')[-1].split('/')[0]
    cdn_list = CDN.copy()
    if host_cdn in cdn_list:
        cdn_list.remove(host_cdn)
    cdn_list.insert(0,host_cdn)
    # 切换cdn
    for cdn in cdn_list:
        host_cdn = url.split('//')[-1].split('/')[0]
        new_url = url.replace(host_cdn,cdn)
        try:
            resp = requests.get(new_url, timeout=5)
            if resp.status_code == 200:
                return resp
        except:
            pass
        print(f"切换cdn {cdn}")


# 单集视频下载
def moc_m3u8_download(url,ts_dir_name,output_filename,word=''):
    resp = requests.get(url)
    m3u8_ = resp.json()['data']['info']
    m3u8 = destm_decrypt(m3u8_)
    key_url = re.search('METHOD=AES-128,URI="(.*?)"',m3u8).group(1)
    key_resp = requests.get(key_url)
    key_ = key_resp.json()['data']['info']
    key_dict = destm_decrypt(key_,1)
    key_array = list(key_dict.values())
    ts_url_list = re.findall("https?://.*?\.ts",m3u8)
    concat_filename = os.path.join(ts_dir_name,'concat_file.txt')
    f_concat_filename = open(concat_filename,'w')
    for index,ts_url in enumerate(ts_url_list):
        print(f"{ts_dir_name} {word} ts:{index+1}/{len(ts_url_list)} {ts_url}")
        f_concat_filename.write(f"file {index}.ts\n")
        ts_filename = os.path.join(ts_dir_name,f"{index}.ts")
        if os.path.exists(ts_filename):
            continue
        ts_resp = ts_download(ts_url)
        ts_content_ = ts_resp.content
        ts_content = aes_decrypt(ts_content_,key_array)
        with open(ts_filename,'wb') as f:
             f.write(ts_content)
    f_concat_filename.close()
    ffmpeg.input(concat_filename, format='concat', safe=1).output(output_filename, codec='copy').run()


# 通过视频url获取视频播放信息
# 购买视频需要登录后的cookie，把登录后的cookie保存到cookie.txt
with open('cookie.txt') as f:
    COOKIES = eval(f.read())
def get_play_url(url):
    resp = requests.get(url,cookies=COOKIES)
    info_ = resp.json()['data']['info']
    info = destm_decrypt(info_)
    play_urls = re.findall("http.*",info)
    return play_urls[0]


# 通过专辑页面下载课程专辑
# 购买视频页面登录后才能获取，把浏览器登录后的页面保存下来到album.html
def main(html=None):
    if not html:
        with open("album.html") as f:
            html = f.read()
    xml = fromstring(html)
    lis = xml.xpath(".//div[@class='list-item']//li")
    album_name = xml.xpath(".//title/text()")[0].replace('(','').replace(' ','').replace(')','').replace('（','').replace('）','')
    mp4_dir_name = os.path.join('file', album_name, 'mp4')
    if not os.path.exists(mp4_dir_name):
        os.makedirs(mp4_dir_name)
    for index, li in enumerate(lis):
        # 跳过不是视频的课程
        if index in [56]:
            continue
        cid,mid = re.search("/lesson/(\d+).html#mid=(\d+)",li.xpath("./a/@href")[0]).groups()
        name = li.xpath("./a/span/text()")[0].replace('.mp4','').strip().replace(' ','.') +'_'+ li.xpath("./a/text()")[1].strip()
        name = name.replace('(','').replace(' ','').replace(')','').replace('（','').replace('）','')
        output_filename = os.path.join(mp4_dir_name, f"{name}.mp4")
        if not os.path.exists(output_filename):
            lesson_url = f"https://coding.imooc.com/lesson/m3u8h5?mid={mid}&cid={cid}&ssl=1&cdn=aliyun1"
            print(lesson_url)
            play_url = get_play_url(lesson_url)
            ts_dir_name = os.path.join('file', album_name, 'ts', name)
            if not os.path.exists(ts_dir_name):
                os.makedirs(ts_dir_name)
            moc_m3u8_download(play_url,ts_dir_name,output_filename,f"episode:{index+1}/{len(lis)}")
        else:
            print(output_filename,'exists !!!')


if __name__ == "__main__":
    main()
