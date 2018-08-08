from PIL import Image
import numpy as np
a = np.asarray(Image.open(
    r"C:/Users/MF/Desktop/n.jpg").convert('L')).astype('float')
# 压缩度
depth = 10.
# 梯度
grad = np.gradient(a)
# 取纵横坐标梯度值
grad_x, grad_y = grad
# 压缩梯度，改变画笔深度
grad_x = grad_x * depth / 100.
grad_y = grad_y * depth / 100.
# 图像平面的单位法向量
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A
# 光源极坐标
vec_el = np.pi / 2.2
vec_az = np.pi / 4.
# 光源单位坐标
dx = np.cos(vec_el) * np.cos(vec_az)
dy = np.cos(vec_el) * np.sin(vec_az)
dz = np.sin(vec_el)
# 裁剪溢出
b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
b = b.clip(0, 255)
im = Image.fromarray(b.astype('uint8'))
im.save(r"C:/Users/MF/Desktop/m.jpg")
