class score():
    def __init__(self):
        self.score = 1
    def showscore(self):
        print(self.score)
    def updatescore(self):
        self.score = self.score + 1
        print(self.score)
        
player = score()
player.updatescore()
player.updatescore()