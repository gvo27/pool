from classes import *
import sys

def game():

    pygame.init()

    walls = Walls()
    pockets = []
    
    p1 = Pocket(margin, margin, black)
    p2 = Pocket(width/2, margin, black)
    p3 = Pocket(width-margin, margin, black)
    p4 = Pocket(margin, height-margin, black)
    p5 = Pocket(width/2, height-margin, black)
    p6 = Pocket(width-margin, height-margin, black)

    pockets.append(p1)
    pockets.append(p2)
    pockets.append(p3)
    pockets.append(p4)
    pockets.append(p5)
    pockets.append(p6)

    loop = True
    reset = True

    while loop:
        if reset:
            rack = Rack() 
            reset = False
            cueStick = CueStick()

        display.fill(background)
        walls.draw()
        for p in pockets:
            p.draw()

        for i in range(len(rack.ball_array)):
            b1 = rack.ball_array[i]
            
            if b1.on:
                for n in range(i, len(rack.ball_array)):
                    b2 = rack.ball_array[n]
                    if b2.on:
                        b1.collision(b2)

                for p in pockets:
                    p.collision(b1)
                walls.collision(b1)

                b1.vel *= .991
                b1.update()
                b1.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == 'r':
                    reset = True
            if event.type == pygame.MOUSEBUTTONUP:
                cueStick.hit()
        
        cueStick.update(rack.cueBall)
        cueStick.on = rack.cueBall.vel.magnitude() == 0
        if pygame.mouse.get_pressed()[0]:
            cueStick.update_force(.2)
        cueStick.draw()

        pygame.display.update()
        clock.tick(RATE)

game()

