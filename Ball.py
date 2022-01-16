class Ball:

    def __init__(self, Bottom):
        self.x = Bottom.x + Bottom.w/2
        self.r = 20
        self.y = Bottom.y - self.r
        self.status = 0 #0:wait 1:run
        self.dx = 5
        self.dy = -5
    #參數中的x代表著滑鼠的x座標      
    def move(self, x):
        if self.status == 0:
            self.x = x

            if self.x <= self.r:
                self.x = self.r
            if self.x > 800 - self.r:
                self.x = 800 - self.r
                
        elif self.status == 1:
            self.x = self.x + self.dx
            self.y = self.y + self.dy

            if self.x >= 800 - self.r: #右邊界
                self.dx = -self.dx
                
            if self.x <= self.r: #左邊界
                self.dx = -self.dx

            if self.y <= self.r: #上邊界:
                self.dy = -self.dy

            if self.y >= 600 - self.r: #下邊界
                pass
                #game over
