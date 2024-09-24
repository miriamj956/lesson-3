import pygame
pygame.init()

screen = pygame.display.set_mode([500,500])

red = (255, 0, 0)
green = (0,255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

screen.fill(white)

position = (300, 300)
radius = 50
wid = 2

pygame.draw.circle(screen, red, position, radius, wid)

class Circle():
    def __init__(self, color, position, radius, width = 0):
        self.color = color
        self.position = position
        self.radius = radius
        self.width = width
        self.screen = screen

    def drawCircle(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius, self.width)

    def expandCircle(self, r):
        self.radius += r
        pygame.draw.circle(self.screen, self.color, self.position, self.radius, self.width)

blueCircle = Circle(blue, position, radius+60)
greenCircle = Circle(green, position, radius+100)
yellowCircle = Circle(yellow, position, radius+150, 2)
purpleCircle = Circle("purple", position, radius+200, 5)

while True:
    for event in pygame.event.get():
        #mousedown = clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            blueCircle.drawCircle()
            greenCircle.drawCircle()
            yellowCircle.drawCircle()
            purpleCircle.drawCircle()

        #mouseup = realeased
        if event.type == pygame.MOUSEBUTTONUP:
            blueCircle.expandCircle(2)
            greenCircle.expandCircle(3)
            yellowCircle.expandCircle(4)
            purpleCircle.expandCircle(5)

        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            blackCircle = Circle(black, pos, 5)
            blackCircle.drawCircle()



        
        
    
    pygame.display.update()