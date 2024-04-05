from get_links import get_links
from get_pics import get_pics

SEASON = "springsummer2024"

def main():
    # 目标网站的URL
    url = "https://supreme.com/previews/{}/".format(SEASON)

    # 获取所有链接
    links = get_links(url)

    if links:
        # 遍历链接并运行get_pics方法
        for link in links:
            print("当前链接：", link)
            get_pics(link,SEASON)

if __name__ == "__main__":
    main()
