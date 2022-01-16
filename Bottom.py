class Bottom:

    #思考如何初始化
    #bottom = Bottom.Bottom(x,y,w,h)
    #bottom = Bottom.Bottom(400,550,100,50)
    #建構方法
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    #思考底版的移動方法
    #bottom.move(x)
    def move(self, x):
        self.x = x
    
