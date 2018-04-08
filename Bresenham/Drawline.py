import PIL.Image, PIL.ImageDraw
from PIL import Image

def Dline(x0,y0,x1,y1):
    points = set()
    k = (y1-y0)/(x1-x0)
    x,y = x0, y0
    points.add((x,y))
    #斜率在0到1之间
    if 0<=k<=1:
        d = 0.5-k
        while x<=x1:
            x += 1
            d = d+1-k if d<0 else d-k
            y = y +1 if d<0 else y
            points.add((x,y))

    #斜率大于1
    if k>1:
        d = 1 - 0.5*k
        while y <= y1:
            y +=1
            d = d+1 if d<0 else d+1-k
            x = x  if d<0 else x+1
            points.add((x,y))

    #斜率在-1到0之间
    if -1<=k< 0:
        d = -0.5-k
        while x<=x1:
            x += 1
            d = d-1-k if d>0 else d-k
            y = y -1 if d>0 else y
            points.add((x,y))


    #斜率小于-1
    if k<-1:
        d = -1 - 0.5*k
        while y >= y1:
            y -=1
            d = d-1-k if d<0 else d-1
            x = x+1  if d<0 else x
            points.add((x,y))
    points.add((x1,y1))
    return points



x0,y0 = 1,60#起点坐标
x1,y1 = 100, 1#终点坐标
line=PIL.Image.new("RGB",(200,200),(0,0,0))#创建图像
draw = PIL.ImageDraw.Draw(line)
p = Dline(x0,y0,x1,y1)
print(p)
for point in p:
    draw.point((point[0],point[1]))
line1=line.transpose(Image.FLIP_TOP_BOTTOM)#将坐标轴进行上下对称变换
line1.show()
