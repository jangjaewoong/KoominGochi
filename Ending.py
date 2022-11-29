

class ending:
    def __init__(self,x ,y):
        self.midScore = x
        self.endScore = y

    def calu(self):
        self.totalScroe = (self.midScore + self.endScore) / 2
        if self.totalScroe <= 4.5:
            return("대기업 입사")
            #return("스타트업 창업(정부지원)")
        elif self.totalScroe <4.2:
            return("중소기업 취업")
            #return("대학원 진학")
        elif self.totalScroe <3.5:
            return("취준생")
        else:
            return("백수")