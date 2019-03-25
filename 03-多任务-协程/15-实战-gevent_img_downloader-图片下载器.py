import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

# 网络下载的过程就是一个耗时的过程，可以用gevent实现协程多任务
# 相当于一个小爬虫
def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    # 读取数据，以jpg图片的形式保存到当前文件夹
    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg", 'http://n.sinaimg.cn/eladies/360/w220h140/20190323/GVRj-huqrnap3104557.jpg'),
        gevent.spawn(downloader, "2.jpg", 'http://n.sinaimg.cn/eladies/360/w220h140/20190323/TKyV-huqrnap3102647.jpg'),
        gevent.spawn(downloader, "3.jpg", 'http://n.sinaimg.cn/eladies/360/w220h140/20190323/GVRj-huqrnap3104557.jpg'),
        gevent.spawn(downloader, "4.jpg", 'http://n.sinaimg.cn/eladies/360/w220h140/20190323/TKyV-huqrnap3102647.jpg')
        )    
    

if __name__ == "__main__":
    main()
