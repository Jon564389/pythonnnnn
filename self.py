        self.rad = rad
        self.wid = wid
        self.scrn = screen

    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid )

    def grow(self,x):
        self.rad += x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid )

#how to draw a circle
position = (300,300)
radius = 50
wid = 2
pygame.draw.circle(screen, red, position, radius, wid )
pygame.display.update()

#creating instances
blueCircle = myCircle(blue, position, radius+60)
redCircle = myCircle(red, position, radius+40)
yellowCircle = myCircle(yellow, position, radius, 5)
greenCircle = myCircle(green, position, 20)

while(1):
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            blueCircle.draw()
            redCircle.draw()
            yellowCircle.draw()
            greenCircle.draw()
