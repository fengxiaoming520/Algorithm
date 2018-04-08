import PIL.Image, PIL.ImageDraw
from PIL import Image


def DEllipse(a,b):
    points = set()
    x,y=0,b
    points.add((x,y))#将点及其对称点全部加入集合
    points.add((x,-y))
    points.add((-x,-y))
    points.add((-x,y))
    d = b**2 + a**2 *(-b+0.25)
    #上半部分
    while b**2 * (x+1) < a**2 *(y-0.5) : #结束条件为当x方向法向量等于y方向法向量时
        x += 1
        y = y if d < 0 else y-1
        points.add((x,y))
        points.add((x,-y))
        points.add((-x,-y))
        points.add((-x,y))
        d = d + b**2 *(2*x+3) if d < 0 else d+b**2 *(2*x+3)+a**2 * (-2*y+2)

    #下半部分 
    d = b**2 * (x+0.5)**2 + a**2 * (y-1)**2 - (a*b)**2
   
    while y>0 : #结束条件y>=0时
        y -=1
        x = x+1 if d < 0 else x
        points.add((x,y))
        points.add((x,-y))
        points.add((-x,-y))
        points.add((-x,y))
        d = d + b**2 *(2*x+2)+a**2 *(-2*y+3) if d < 0 else d+a**2 * (-2*y+3)

    return points


a = 100 #长半轴
b = 60 #短半轴
size = 400 #画布大小
ellipse = PIL.Image.new("RGB", (size,size),(0,0,0)) #创建图像
draw = PIL.ImageDraw.Draw(ellipse)

p = DEllipse(a, b)
print(p)
for point in p:
    draw.point((size/2+point[0],size/2+point[1]))#将点移到画布中央
ellipse=ellipse.transpose(Image.FLIP_TOP_BOTTOM)#将坐标轴进行上下对称变换
ellipse.show()
