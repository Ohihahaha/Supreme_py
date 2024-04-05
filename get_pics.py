import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def convert_webp_to_jpg(webp_data, jpg_path):
    try:
        # 使用BytesIO创建一个虚拟文件对象
        img_data = BytesIO(webp_data)

        # 打开WebP图像
        with Image.open(img_data) as img:
            # 保存为JPEG格式
            img.convert("RGB").save(jpg_path, "JPEG")

        print("转换成功：", jpg_path)
    except Exception as e:
        print("转换失败：", str(e))

def get_pics(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    }

    # 发送请求
    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找标题标签
        title_tag = soup.find('h1', {'data-component': 'title', 'class': 'font-bold'})
        if title_tag:
            # 提取标题文本作为文件名
            title_text = title_tag.get_text(strip=True)
            title_text = title_text.replace(' ', '_').lower()  # 替换空格为下划线并转为小写
            title_text = ''.join(e for e in title_text if (e.isalnum() or e in {'_', '-'}))  # 仅保留字母、数字、下划线和连字符
            print("标题文本：", title_text)

            # 创建保存图片的文件夹
            output_folder = "Supreme_images_News"
            os.makedirs(output_folder, exist_ok=True)

            # 查找所有图片标签
            img_tags = soup.find_all('img')

            # 提取并保存图片
            for index, img_tag in enumerate(img_tags):
                img_url = img_tag.get('src')
                if img_url:
                    try:
                        # 发送请求获取图片数据
                        img_response = requests.get(img_url)
                        img_data = img_response.content

                        # 创建JPEG文件路径
                        jpg_name = os.path.join(output_folder, "{}_{:03d}.jpg".format(title_text, index + 1))

                        # 转换并保存为JPEG格式
                        convert_webp_to_jpg(img_data, jpg_name)
                    except Exception as e:
                        print("保存图片失败：", str(e))

# 示例用法
# url = "https://supreme.com/previews/fallwinter2023/jackets/supreme-schott-shearling-bomber-jacket"
# get_pics(url)
