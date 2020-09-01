import os
import hashlib
"""
修改视频文件md5,防止百度云和谐
"""

def get_md5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


def change(filename,content='0000000000000000'):
    old_md5 = get_md5(filename)
    f = open(filename,'a')
    f.write(content)
    f.close()
    print(f"change md5 {old_md5} to {get_md5(filename)}")

def change_dir_files(dir):
    files = os.listdir(dir)
    for index,file in enumerate(files):
        filename = os.path.join(dir,file)
        change(filename)
        print(f"{index+1} {filename}")


if __name__ == "__main__":
    # dirs = ['/Users/apple/Downloads/mooc_download-master/file/Python3入门机器学习 经典算法与应用 轻松入行人工智能_课程/mp4',
    #         '/Users/apple/Downloads/mooc_download-master/file/Python3数据分析与挖掘建模实战_课程/mp4',
    #         '/Users/apple/Downloads/mooc_download-master/file/Python3数据分析与挖掘建模实战_课程/pdf']
    # for dir in dirs:
    #     change_dir_files(dir)
    print(get_md5('/Users/apple/Downloads/mooc_download-master/file/Python3数据分析与挖掘建模实战_课程/mp4/2-2.监测与抓取_(02:53).mp4'))