import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_links(page_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    }

    # 发送请求
    response = requests.get(page_url, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找包含在 <main> 中的所有链接
        main_tag = soup.find('main')
        if main_tag:
            links = main_tag.find_all('a', href=True)

            # 提取链接并拼接域名
            full_urls = [urljoin(page_url, link.get('href')) for link in links]
            return full_urls
        else:
            print('未找到 <main> 标签')
            return None
    else:
        print('请求失败，状态码:', response.status_code)
        return None

# 示例用法
# url = "https://supreme.com/previews/fallwinter2023/"
# result = get_links(url)
#
# if result:
#     for link in result:
#         print(link)
