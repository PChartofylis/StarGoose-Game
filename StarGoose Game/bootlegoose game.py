"""
author: Παναγιώτης Χαρτοφύλης 4090
"""

from pygame.locals import *
import pygame as pg
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class game(pg.sprite.Sprite):
    def __init__(self, name, x, y):
       
        super().__init__()
 
        self.image = pg.image.load(name).convert()
        self.image.set_colorkey(BLACK)
      
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        
        self.help_x = 0
        self.help_y = 0
        
        self.x_speed = 0
        self.y_speed = 0        
        
    def speed(self, x, y):
        self.x_speed += x
        self.y_speed += y
        
    def updatepl(self):
        if self.rect.x >=0 and self.rect.x <=480:
            self.help_x = self.rect.x
            self.rect.x += self.x_speed   
            
        else:
            self.rect.x = self.help_x
            
        if self.rect.y >= 0 and self.rect.y <= 420:
            self.help_y = self.rect.y  
            self.rect.y += self.y_speed   
            
        else:
            self.rect.y = self.help_y

    def update(self):
        self.rect.y += level
 
        if self.rect.y > 430:
            self.reset_pos()
        
        if self.rect.x > 400 or self.rect.x < 50:
            self.reset_pos()
            
    def reset_pos(self):
        self.rect.y = random.randint(-500, 0)
        self.rect.x = random.randint(0, w-50)    
    
    def reset_playpos(self):
        self.rect.x = 234
        self.rect.y = 358
        
        for shooter in shooterlist:
            shooter.reset_pos()
            
        for collider in colliderlist:
            collider.reset_pos()
    
    def reset_gatepos(self):
        self.rect.x = 229
        self.rect.y = random.randrange(-1500, -500)
    
    def reset_returngatepos(self):
        self.rect.x = 229
        self.rect.y = -650
        
class bullets(pg.sprite.Sprite):
    def __init__(self, name, x, y):
       
        super().__init__()
        
        self.image = pg.image.load(name).convert()
        self.image.set_colorkey(BLACK)
              
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        
        self.y_speed = 0
        
    def update(self):
        self.rect.y -= 3
        
        if self.rect.y <= -10:
            self.kill()
    
class enemiesbullets(pg.sprite.Sprite):
    def __init__(self, name, x, y):
        
        super().__init__()
        
        self.image = pg.image.load(name).convert()
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        
        self.y_speed = 0
        
    def update(self):
        self.rect.y += 3

        if self.rect.y >= 450:
            self.kill()

class fills(pg.sprite.Sprite):
    def __init__(self, name, x, y):
        
        super().__init__()
        
        self.image = pg.image.load(name).convert()
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.rect.y += level
        
        if self.rect.y >= 420:
            self.kill_pos()
    
    def kill_pos(self):
        self.kill()
        
    def reset_pos(self):
        self.rect.x += ratiox
        self.rect.y += ratioy
        
pg.init()

#sprite groups
playerlist = pg.sprite.Group()
maxlifelist = pg.sprite.Group()
shooterlist = pg.sprite.Group()
colliderlist = pg.sprite.Group()
bulletlist = pg.sprite.Group()
enemiesbulletlist = pg.sprite.Group()
shieldgatelist = pg.sprite.Group()
returnslist = pg.sprite.Group()
shieldlist = pg.sprite.Group()
ammogatelist = pg.sprite.Group()
returnalist = pg.sprite.Group()
ammolist = pg.sprite.Group()
fuelgatelist = pg.sprite.Group()
returnflist = pg.sprite.Group()
fuellist = pg.sprite.Group()

#all sprites group
asl = pg.sprite.Group()

#screen
w, h = 505, 503
screen = pg.display.set_mode((w, h), pg.FULLSCREEN)
bg = pg.image.load("background.png").convert()

#variables
banderange = 4
bgy = 0
level = 1
damage = 10
enemydamage = 5 
score = 0
ammo = 100
fuel = 100
shield = 100
timer = 0
shooting = 0
time = 0
hs = 0
maxlifenum = 3
frames = 60
pausenum = 0
ratiox = 0
ratioy = 0

#lists
shooterhealth = [70 for i in range(banderange)]
colliderhealth = [150 for i in range(banderange)]
cd = [1000 for i in range(banderange)]
last = [pg.time.get_ticks() for i in range(banderange)]

#sounds
bulplaysound = pg.mixer.Sound("honk.ogg")
lostsound = pg.mixer.Sound("lost.ogg")

#booleans
screen1 = True
screen2 = False
screen3 = False
screen4 = False
pause = False
lost = False
done = False

#player generation
player = game("player2.png", 234, 358)
playerlist.add(player)

#gates generation
shieldgate = game("shieldgate.png", 229, -500)
shieldgatelist.add(shieldgate)
asl.add(shieldgate)
shieldgatereturn = game("shieldgate.png", 229, -650)
returnslist.add(shieldgatereturn)
ammogate = game("ammogate.png", 229, -1000)
ammogatelist.add(ammogate)
asl.add(ammogate)
ammogatereturn = game("ammogate.png", 229, -650)
returnalist.add(ammogatereturn)
fuelgate = game("fuelgate.png", 229, -1500)
fuelgatelist.add(fuelgate)
asl.add(fuelgate)
fuelgatereturn = game("fuelgate.png", 229, -650)
returnflist.add(fuelgatereturn)

#lives generation
maxlife1=game("life1.png", 170, 458)
maxlifelist.add(maxlife1)
maxlife2=game("life1.png", 190, 458)
maxlifelist.add(maxlife2)
maxlife3=game("life1.png", 210, 458)
maxlifelist.add(maxlife3)

#enemy generation
for i in range(banderange):
    shooter = game("shooter.png", 15, 15)
    collider = game("collider.png", 15, 15)
    
    shooter.rect.x = random.randint(0, w-50)
    shooter.rect.y = random.randint(0, h)
    
    collider.rect.x = random.randint(0, w-50)
    collider.rect.y = random.randint(0, h)
    
    shooterlist.add(shooter)
    asl.add(shooter)
    
    colliderlist.add(collider)
    asl.add(collider)
    
    shooter.reset_pos()
    collider.reset_pos()

#fonts
font1 = pg.font.SysFont('Calibri', 30, True, False)
font2 = pg.font.SysFont('Calibri', 15, True, False)

#name and clock
pg.display.set_caption("BootleGoose Warrior")
clock = pg.time.Clock()

'''
========== main program loop ==========
'''

while not done:
    #user inputs, player fuel, ammo and bullets behaviour
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                done = True
                
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p and pausenum == 0:
                pausenum = 1
                frames = 0.5
                break
            
            elif event.key == pg.K_p and pausenum == 1:
                pausenum = 0
                frames = 60
                break
    
        if fuel > 0:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    player.speed(-3, 0)
                    fuel -= 1
                    
                    if fuel == 0:
                        player.speed(3, 0)
                        
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    player.speed(3, 0)
                    fuel -= 1
                    
                    if fuel == 0:
                        player.speed(-3, 0)
                        
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    player.speed(0, -3)
                    fuel -= 1
                    
                    if fuel == 0:
                        player.speed(0, 3)
                        
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    player.speed(0, 3)
                    fuel -= 1
                    
                    if fuel == 0:
                        player.speed(0, -3)
                        
                elif event.key == pg.K_z:
                    if ammo > 0:
                        bullet = bullets("bullet1.png", 600, 600)
                        bullet.rect.x = player.rect.x+15
                        bullet.rect.y = player.rect.y
                        asl.add(bullet)
                        bulletlist.add(bullet)
                        bulplaysound.set_volume(0.5)
                        bulplaysound.play()
                        ammo -= 1
                        
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    player.speed(3, 0)
                    
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    player.speed(-3, 0)
                    
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    player.speed(0, 3)
                    
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    player.speed(0, -3)
                    
    #screen behaviour
    screen.fill(BLACK)
    pg.mouse.set_visible(False)
    if lost == False:
        bgy2 = bgy % bg.get_rect().height
        screen.blit(bg, (0, bgy2-bg.get_rect().height))
        
        if bgy2 < h:
            screen.blit(bg, (0, bgy2))
            
        bgy += 1
    pg.draw.rect(screen, BLACK, [0, 450, 550, 550])
    
    #score behaviour
    time += 1
    if lost == False:
        if time >= 5:
            score += 1
            time = 0 
    
    '''
    ====== screen 1 ======
    '''
    
    enemiescollidelist1 = pg.sprite.spritecollide(shooter, 
                                                  colliderlist, 
                                                  False)
    for collider in enemiescollidelist1:
        shooter.reset_pos()
        
    enemiescollidelist2 = pg.sprite.spritecollide(collider, 
                                                  shooterlist, 
                                                  False)
    for shooter in enemiescollidelist2:
        collider.reset_pos()
    
    #player shooting and player bullets behaviour
    for bullet in bulletlist:
        bullethitlist1 = pg.sprite.spritecollide(bullet, 
                                                 shooterlist, 
                                                 False)
        bullethitlist2 = pg.sprite.spritecollide(bullet, 
                                                 colliderlist, 
                                                 False)
        
        for shooter, i in zip(bullethitlist1, range(banderange)):
            shooterhealth[i] -= damage
            
            if shooterhealth[i] <= 0:
                score += 50
                shooterhealth[i] = 70
                shooter.reset_pos()
                
            bulletlist.remove(bullet)
            asl.remove(bullet)

        for collider, i in zip(bullethitlist2, range(banderange)):
            colliderhealth[i] -= damage
            
            if colliderhealth[i] <= 0:
                score += 100
                colliderhealth[i] = 150
                collider.reset_pos()
                
            bulletlist.remove(bullet)
            asl.remove(bullet)
            
        if bullet.rect.y <= 0:
            bulletlist.remove(bullet)
            asl.remove(bullet)
    
    #enemies shooting behaviour
    for shooter, i in zip(shooterlist, range(banderange)):
        now = pg.time.get_ticks()
        
        if now - last[i] >= cd[i]:
            last[i] = now
            
            if shooter.rect.y >= -30:
                bullet1 = enemiesbullets("bullet2.png", 700, 700)
                enemiesbulletlist.add(bullet1)
                bullet1.rect.x = shooter.rect.x+13
                bullet1.rect.y = shooter.rect.y+13
    
    #enemy bullets and player shield behaviour
    ebullethitlist = pg.sprite.spritecollide(player, 
                                             enemiesbulletlist, 
                                             False)
    for bullet1 in ebullethitlist:
        shield -= 5
        enemiesbulletlist.remove(bullet1)                   
            
    for bullet1 in enemiesbulletlist:
        if bullet1.rect.y >= 430:
            enemiesbulletlist.remove(bullet1)
    
    if frames == 0.5:
        for bullet1 in enemiesbulletlist:
            bullet1.kill()
            
    '''
    gates behaviour
    '''
    
    #shieldgate behaviour
    playershieldgatecollidinglist = pg.sprite.spritecollide(player, 
                                                            shieldgatelist, 
                                                            False)
    for shieldgate in playershieldgatecollidinglist:
        for i in range(0, 10):
            shieldfill = fills("shieldfill.png", 67, -50)
            
            if i == 0:
                ratiox = 0
                ratioy = 0
                
            elif i <= 2:
                ratiox += 168
        
            elif i <= 4:
                ratiox -= 168
            
            elif i <= 6:
                ratiox += 168
            
            elif i <= 8:
                ratiox -= 168
            
            elif i <= 9:
                ratiox += 168
            
            if i >= 1:
                ratioy -= 50
                
            shieldlist.add(shieldfill)
            shieldfill.reset_pos()
        
        ratiox = 0
        ratioy = 0
        screen1 = False
        screen2 = True
        player.reset_playpos()
        shieldgatereturn.reset_returngatepos()
        
    shieldgatehitlist1 = pg.sprite.spritecollide(shieldgate, 
                                                 shooterlist, 
                                                 False)
    for shooter in shieldgatehitlist1:
        shooter.reset_pos()
        
    shieldgatehitlist2 = pg.sprite.spritecollide(shieldgate, 
                                                 colliderlist, 
                                                 False)
    for collider in shieldgatehitlist2:
        collider.reset_pos()
        
    for shieldgate in shieldgatelist:
        if shieldgate.rect.y >= 400:
            shieldgate.reset_gatepos()
    
    gatescollision1 = pg.sprite.spritecollide(shieldgate,
                                              ammogatelist,
                                              False)
    for ammogate in gatescollision1:
        ammogate.reset_gatepos()
    
    gatescollision2 = pg.sprite.spritecollide(shieldgate,
                                              fuelgatelist,
                                              False)
    for fuelgate in gatescollision2:
        fuelgate.reset_gatepos()
        
    if screen2 == True:
        for shooter in shooterlist:
            shooter.reset_pos()
        
        for collider in colliderlist:
            collider.reset_pos()
            
        for shieldgate in shieldgatelist:
            shieldgate.reset_gatepos()
            
        for bullet1 in enemiesbulletlist:
            bullet1.kill()
    
    #ammogate behaviour
    playerammogatecollidinglist = pg.sprite.spritecollide(player, 
                                                          ammogatelist, 
                                                          False)
    for ammogate in playerammogatecollidinglist:
        for i in range(0, 10):
            ammofill = fills("ammofill.png", 67, -50)
            
            if i == 0:
                ratiox = 0
                ratioy = 0
                
            elif i <= 2:
                ratiox += 168
        
            elif i <= 4:
                ratiox -= 168
            
            elif i <= 6:
                ratiox += 168
            
            elif i <= 8:
                ratiox -= 168
            
            elif i <= 9:
                ratiox += 168
            
            if i >= 1:
                ratioy -= 50
                
            ammolist.add(ammofill)
            ammofill.reset_pos()
        
        ratiox = 0
        ratioy = 0
        screen1 = False
        screen3 = True
        player.reset_playpos()
        ammogatereturn.reset_returngatepos()
        
    ammogatehitlist1 = pg.sprite.spritecollide(ammogate, 
                                               shooterlist, 
                                               False)
    for shooter in ammogatehitlist1:
        shooter.reset_pos()
        
    ammogatehitlist2 = pg.sprite.spritecollide(ammogate, 
                                               colliderlist, 
                                               False)
    for collider in ammogatehitlist2:
        collider.reset_pos()
        
    for ammogate in ammogatelist:
        if ammogate.rect.y >= 400:
            ammogate.reset_gatepos()
    
    gatescollision3 = pg.sprite.spritecollide(ammogate,
                                              shieldgatelist,
                                              False)
    for shieldgate in gatescollision3:
        shieldgate.reset_gatepos()
    
    gatescollision4 = pg.sprite.spritecollide(ammogate,
                                              fuelgatelist,
                                              False)
    for fuelgate in gatescollision4:
        fuelgate.reset_gatepos()
        
    if screen3 == True:
        for shooter in shooterlist:
            shooter.reset_pos()
        
        for collider in colliderlist:
            collider.reset_pos()

        for ammogate in ammogatelist:
            ammogate.reset_gatepos()
            
        for bullet1 in enemiesbulletlist:
            bullet1.kill()
    
    #fuelgate behaviour
    playerfuelgatecollidinglist = pg.sprite.spritecollide(player, 
                                                          fuelgatelist, 
                                                          False)
    for fuelgate in playerfuelgatecollidinglist:
        for i in range(0, 10):
            fuelfill = fills("fuelfill.png", 67, -50)
            
            if i == 0:
                ratiox = 0
                ratioy = 0
                
            elif i <= 2:
                ratiox += 168
        
            elif i <= 4:
                ratiox -= 168
            
            elif i <= 6:
                ratiox += 168
            
            elif i <= 8:
                ratiox -= 168
            
            elif i <= 9:
                ratiox += 168
            
            if i >= 1:
                ratioy -= 50
                
            fuellist.add(fuelfill)
            fuelfill.reset_pos()
        
        ratiox = 0
        ratioy = 0
        screen1 = False
        screen4 = True
        player.reset_playpos()
        fuelgatereturn.reset_returngatepos()
        
    fuelgatehitlist1 = pg.sprite.spritecollide(fuelgate, 
                                               shooterlist, 
                                               False)
    for shooter in fuelgatehitlist1:
        shooter.reset_pos()
        
    fuelgatehitlist2 = pg.sprite.spritecollide(fuelgate, 
                                               colliderlist, 
                                               False)
    for collider in fuelgatehitlist2:
        collider.reset_pos()
        
    for fuelgate in fuelgatelist:
        if fuelgate.rect.y >= 400:
            fuelgate.reset_gatepos()
    
    gatescollision5 = pg.sprite.spritecollide(fuelgate,
                                              ammogatelist,
                                              False)
    for ammogate in gatescollision5:
        ammogate.reset_gatepos()
    
    gatescollision6 = pg.sprite.spritecollide(fuelgate,
                                              shieldgatelist,
                                              False)
    for shieldgate in gatescollision6:
        shieldgate.reset_gatepos()
        
    if screen4 == True:
        for shooter in shooterlist:
            shooter.reset_pos()
        
        for collider in colliderlist:
            collider.reset_pos()

        for fuelgate in fuelgatelist:
            fuelgate.reset_gatepos()
            
        for bullet1 in enemiesbulletlist:
            bullet1.kill()
            
    #player lives behaviour
    shooterhitlist = pg.sprite.spritecollide(player, 
                                             shooterlist, 
                                             False)
    colliderhitlist = pg.sprite.spritecollide(player, 
                                              colliderlist, 
                                              False)
    for shooter in shooterhitlist:
        if maxlifenum == 3:
            maxlifelist.remove(maxlife3)
            maxlifenum -= 1
            player.reset_playpos()
            ammo = 100
            fuel = 100
            shield = 100
            
            for shieldgate in shieldgatelist:
                shieldgate.reset_gatepos()
            
            for ammogate in ammogatelist:
                ammogate.reset_gatepos()
            
            for fuelgate in fuelgatelist:
                fuelgate.reset_gatepos()
            
        elif maxlifenum == 2:
            maxlifelist.remove(maxlife2)
            maxlifenum -= 1
            player.reset_playpos()
            ammo = 100
            fuel = 100
            shield = 100
            
            for shieldgate in shieldgatelist:
                shieldgate.reset_gatepos()
            
            for ammogate in ammogatelist:
                ammogate.reset_gatepos()
            
            for fuelgate in fuelgatelist:
                fuelgate.reset_gatepos()
            
        elif maxlifenum == 1:
            maxlifelist.remove(maxlife1)
            maxlifenum -= 1
            player.reset_playpos()
            ammo = 100
            fuel = 100
            shield = 100
            
            for shieldgate in shieldgatelist:
                shieldgate.reset_gatepos()
            
            for ammogate in ammogatelist:
                ammogate.reset_gatepos()
            
            for fuelgate in fuelgatelist:
                fuelgate.reset_gatepos()
            
        elif maxlifenum == 0:
            maxlifenum -= 1
            
        if maxlifenum == -1:
            lost = True
        
        for shieldgate in shieldgatelist:
            shieldgate.reset_gatepos()
            
        for ammogate in ammogatelist:
            ammogate.reset_gatepos()
            
        for fuelgate in fuelgatelist:
            fuelgate.reset_gatepos()
            
        shooter.reset_pos()
        ammo = 100
        fuel = 100
        shield = 100
        
    for collider in colliderhitlist:
        if maxlifenum == 3:
            maxlifelist.remove(maxlife3)
            maxlifenum -= 1
            player.reset_playpos()
            ammo = 100
            fuel = 100
            shield = 100
            
            for shieldgate in shieldgatelist:
                shieldgate.reset_gatepos()
            
            for ammogate in ammogatelist:
                ammogate.reset_gatepos()
            
            for fuelgate in fuelgatelist:
                fuelgate.reset_gatepos()
            
        elif maxlifenum == 2:
            maxlifelist.remove(maxlife2)
            maxlifenum -= 1
            player.reset_playpos()
            ammo = 100
            fuel = 100
            shield = 100
            
            for shieldgate in shieldgatelist:
                shieldgate.reset_gatepos()
            
            for ammogate in ammogatelist:
                ammogate.reset_gatepos()
            
            for fuelgate in fuelgatelist:
                fuelgate.reset_gatepos()
            
        elif maxlifenum == 1:
            maxlifelist.remove(maxlife1)
            maxlifenum -= 1
            player.reset_playpos()
            ammo = 100
            fuel = 100
            shield = 100
            
            for shieldgate in shieldgatelist:
                shieldgate.reset_gatepos()
            
            for ammogate in ammogatelist:
                ammogate.reset_gatepos()
            
            for fuelgate in fuelgatelist:
                fuelgate.reset_gatepos()
            
        elif maxlifenum == 0:
            maxlifenum -= 1
            
        if maxlifenum == -1:
            lost = True
        
        for shieldgate in shieldgatelist:
            shieldgate.reset_gatepos()
            
        for ammogate in ammogatelist:
            ammogate.reset_gatepos()
            
        for fuelgate in fuelgatelist:
            fuelgate.reset_gatepos()
            
        collider.reset_pos()
        ammo = 100
        fuel = 100
        shield = 100
        
    if shield == 0:
        if maxlifenum == 3:
            maxlifelist.remove(maxlife3)
            maxlifenum -= 1
            player.reset_playpos()
            ammo = 100
            fuel = 100
            shield = 100
            
            for shieldgate in shieldgatelist:
                shieldgate.reset_gatepos()
            
            for ammogate in ammogatelist:
                ammogate.reset_gatepos()
            
            for fuelgate in fuelgatelist:
                fuelgate.reset_gatepos()
                    
        elif maxlifenum == 2:
            maxlifelist.remove(maxlife2)
            maxlifenum -= 1
            player.reset_playpos()
            ammo = 100
            fuel = 100
            shield = 100
            
            for shieldgate in shieldgatelist:
                shieldgate.reset_gatepos()
            
            for ammogate in ammogatelist:
                ammogate.reset_gatepos()
            
            for fuelgate in fuelgatelist:
                fuelgate.reset_gatepos()
                    
        elif maxlifenum == 1:
            maxlifelist.remove(maxlife1)
            maxlifenum -= 1
            player.reset_playpos()
            ammo = 100
            fuel = 100
            shield = 100
            
            for shieldgate in shieldgatelist:
                shieldgate.reset_gatepos()
            
            for ammogate in ammogatelist:
                ammogate.reset_gatepos()
            
            for fuelgate in fuelgatelist:
                fuelgate.reset_gatepos()
                    
        elif maxlifenum == 0:
            maxlifenum -= 1
                    
        if maxlifenum == -1:
            lost = True
        
        for shieldgate in shieldgatelist:
            shieldgate.reset_gatepos()
            
        for ammogate in ammogatelist:
            ammogate.reset_gatepos()
            
        for fuelgate in fuelgatelist:
            fuelgate.reset_gatepos()
                
        shooter.reset_pos()
        ammo = 100
        fuel = 100
        shield = 100
    
    '''
    ====== screen 2 ======
    '''
    
    #shield fills behaviour
    shieldfillhitlist = pg.sprite.spritecollide(player, 
                                                shieldlist, 
                                                False)
    for shieldfill in shieldfillhitlist:
        shieldfill.kill_pos()
        if shield < 100:
            shield += 5
            if shield >= 100:
                shield = 100
    
    #return gate behaviour
    shieldgatehitlist = pg.sprite.spritecollide(player, 
                                                returnslist, 
                                                False)
    for shieldgatereturn in shieldgatehitlist:
        screen2 = False
        screen1 = True
        player.reset_playpos()
        shieldgatereturn.reset_returngatepos()
        
    for shieldgatereturn in returnslist:
        if shieldgatereturn.rect.y == 400:
            shieldgatereturn.reset_returngatepos()
    
    '''
    ====== screen 3 ======
    '''
    
    #ammo fills behaviour
    ammofillhitlist = pg.sprite.spritecollide(player, 
                                              ammolist, 
                                              False)
    for ammofill in ammofillhitlist:
        ammofill.kill_pos()
        if ammo < 100:
            ammo += 3
            if ammo >= 100:
                ammo = 100
    
    #return gate behaviour
    ammogatehitlist = pg.sprite.spritecollide(player, 
                                              returnalist, 
                                              False)
    for ammogatereturn in ammogatehitlist:
        screen3 = False
        screen1 = True
        player.reset_playpos()
        ammogatereturn.reset_returngatepos()
        
    for ammogatereturn in returnalist:
        if ammogatereturn.rect.y == 400:
            ammogatereturn.reset_returngatepos()
            
    '''
    ====== screen 4 ======
    '''
    
    #fuel fills behaviour
    fuelfillhitlist = pg.sprite.spritecollide(player, 
                                              fuellist, 
                                              False)
    for fuelfill in fuelfillhitlist:
        fuelfill.kill_pos()
        if fuel < 100:
            fuel += 10
            if fuel >= 100:
                fuel = 100
    
    #return gate behaviour
    fuelgatehitlist = pg.sprite.spritecollide(player, 
                                              returnflist, 
                                              False)
    for fuelgatereturn in fuelgatehitlist:
        screen4 = False
        screen1 = True
        player.reset_playpos()
        fuelgatereturn.reset_returngatepos()
        
    for fuelgatereturn in returnflist:
        if fuelgatereturn.rect.y == 400:
            fuelgatereturn.reset_returngatepos()
            
    '''
    if lost == false update and draw objects
    '''
    
    #global objects
    if lost == False:
        player.updatepl()

        playerlist.draw(screen)
        maxlifelist.draw(screen)
    
    #screen1 objects
    if lost == False and screen1 == True:
        enemiesbulletlist.update()
        asl.update()
    
        enemiesbulletlist.draw(screen)
        asl.draw(screen)
    
    #screen2 objects
    if lost == False and screen2 == True:
        shieldlist.update()
        returnslist.update()
    
        shieldlist.draw(screen)
        returnslist.draw(screen)
        
    #screen 3 objects
    if lost == False and screen3 == True:
        ammolist.update()
        returnalist.update()
        
        ammolist.draw(screen)
        returnalist.draw(screen)
    
    #screen 4 objects
    if lost == False and screen4 == True:
        fuellist.update()
        returnflist.update()
        
        fuellist.draw(screen)
        returnflist.draw(screen)
        
    #if lost == true show finale score
    if lost == True:
        lostsound.set_volume(0.1)
        lostsound.play()
        
        text = font1.render("You Lost !!!", True, WHITE)
        screen.blit(text, [200, 250])
        
        text6 = font1.render("Final Score : " + str(score), True, WHITE)
        screen.blit(text6, [170, 300])
        
    #text renders
    if lost == False:
        text2 = font1.render("Score:"+str(score), True, WHITE)
        text2.set_colorkey(BLACK)
        screen.blit(text2, [170, 478])
            
        text3 = font2.render("Fuel:"+str(fuel), True, RED)
        text3.set_colorkey(BLACK)
        screen.blit(text3, [0, 455])
            
        text4 = font2.render("Ammo:"+str(ammo), True, GREEN)
        text4.set_colorkey(BLACK)
        screen.blit(text4, [0, 470])
            
        text5 = font2.render("Shield:"+str(shield), True, BLUE)
        text5.set_colorkey(BLACK)
        screen.blit(text5, [0, 485])
    
    #update screen
    pg.display.flip()
    
    #fps
    clock.tick(frames)

pg.quit()