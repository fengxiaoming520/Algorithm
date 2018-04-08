import PIL.Image, PIL.ImageDraw


def Dcircle(R):
    points = set()
    x, y = 0, R
    d = 1.25-R
    while (x<=y):
        #将对称点加入
        points.add((x,y))
        points.add((x,-y))
        points.add((-x,y))
        points.add((-x,-y))
        points.add((y,x))
        points.add((y,-x))
        points.add((-y,x))
        points.add((-y,-x))
        x +=1
        y = y if d < 0 else y - 1
        d = d + 2*x+3 if d < 0 else d+2*(x-y)+5
        
    return points


R = 70 #半径
size = 400 #画布尺寸
circle=PIL.Image.new("RGB",(size,size),(0,0,0))#创建图像
draw = PIL.ImageDraw.Draw(circle)

p=Dcircle(R)
print(p)
for point in p:
    draw.point((size/2+point[0],size/2+point[1]))#将点移到画布中央
circle.show()
    
