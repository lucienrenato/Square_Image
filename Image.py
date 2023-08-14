from PIL import Image

# 打开图片
im = Image.open("2.jpg")

# 获取图片的宽度和高度
width, height = im.size

# 取宽度和高度中较小的值
size = min(width, height)

# 计算左上角的坐标
x = (width - size) // 2
y = (height - size) // 2

# 裁剪图片
im = im.crop((x, y, x + size, y + size))

# 保存图片
im.save("output.jpg")
