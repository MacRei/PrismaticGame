import pygame, sys, os, random, math, asyncio

async def main():
    global backgroundFrame, backgroundAnimationTimer, gameState, tutorial, highscore, traptimer, trapped
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((960, 480))
    pygame.display.set_caption("Prismatic Game")
    pygame.display.set_icon(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\Icon.png")))

    currentTime = 0
    score = 0
    highscore = 0
    speed = 1
    gameState = "Start"
    tutorial = True

    class Background(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground1.png")).convert_alpha(), (960, 480))
            self.rect = pygame.Rect(0, 0, 960, 480)
        def update(self):
            global backgroundAnimationTimer, backgroundFrame
            if speed == 1:
                self.image = backgroundFrames[backgroundFrame]
                if (currentTime - backgroundAnimationTimer) > 25:
                    backgroundFrame += 1
                    if backgroundFrame == 18:
                        backgroundFrame = 0
                    backgroundAnimationTimer = pygame.time.get_ticks()
            elif speed == 2:
                self.image = backgroundFrames[backgroundFrame]
                if (currentTime - backgroundAnimationTimer) > 5:
                    backgroundFrame += 1
                    if backgroundFrame == 18:
                        backgroundFrame = 0
                    backgroundAnimationTimer = pygame.time.get_ticks()
            elif speed == 3:
                self.image = backgroundFrames[backgroundFrame]
                if (currentTime - backgroundAnimationTimer) > 20:
                    backgroundFrame += 2
                    if backgroundFrame >= 18:
                        backgroundFrame = 0
                    backgroundAnimationTimer = pygame.time.get_ticks()
            elif speed == 4:
                self.image = backgroundFrames[backgroundFrame]
                if (currentTime - backgroundAnimationTimer) > 20:
                    backgroundFrame += 4
                    if backgroundFrame >= 18:
                        backgroundFrame = 0
                    backgroundAnimationTimer = pygame.time.get_ticks()
            else:
                self.image = backgroundFrames[backgroundFrame]
                if (currentTime - backgroundAnimationTimer) > 10:
                    backgroundFrame += 5
                    if backgroundFrame >= 18:
                        backgroundFrame = 0
                    backgroundAnimationTimer = pygame.time.get_ticks()
    background = Background()
    backgroundGroup = pygame.sprite.Group()
    backgroundGroup.add(background)
    backgroundAnimationTimer = 0
    backgroundFrames = [pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground1.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground2.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground3.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground4.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground5.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground6.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground7.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground8.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground9.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground10.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground11.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground12.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground13.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground14.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground15.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground16.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground17.png")).convert_alpha(), (960, 480)),
                    pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MovingBackground18.png")).convert_alpha(), (960, 480))]
    backgroundFrame = 0

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\PlayerRed.png")).convert_alpha(), (32, 32))
            self.rect = pygame.Rect(80, 224, 32, 32)
        def update(self):
            player.rect.y += playerYChange
            if player.rect.y < 0:
                player.rect.y = 0
            if player.rect.y > 448:
                player.rect.y = 448
            if playerColor == "Red":
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\PlayerRed.png")).convert_alpha(), (32, 32))
            elif playerColor == "Blue":
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\PlayerBlue.png")).convert_alpha(), (32, 32))
            else:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\PlayerYellow.png")).convert_alpha(), (32, 32))
    player = Player()
    playerGroup = pygame.sprite.Group()
    playerGroup.add(player)
    playerColor = "Red"
    playerYChange = 0
    movingDown = False
    movingUp = False

    class Barrier(pygame.sprite.Sprite):
        def __init__(self, posX, posY, color):
            super().__init__()
            if color == "Red":
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\ColorBarrierRed.png")).convert_alpha(), (32, 152))
            elif color == "Blue":
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\ColorBarrierBlue.png")).convert_alpha(), (32, 152))
            elif color == "Yellow":
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\ColorBarrierYellow.png")).convert_alpha(), (32, 152))
            else:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\ColorBarrierBlack.png")).convert_alpha(), (32, 152))
            self.rect = pygame.Rect(posX, posY, 32, 152)
            self.color = color
        def update(self):
            global colorGroup, gameState, highscore
            if gameState == "Play":
                if tutorial == False:
                    if speed == 1:
                        self.rect.x -= 3
                    elif speed == 2:
                        self.rect.x -= 4
                    elif speed == 3:
                        self.rect.x -= 5
                    elif speed == 4:
                        self.rect.x -= 7
                    else:
                        self.rect.x -= 9
                else:
                    self.rect.x -= 2
            if self.rect.x < -32:
                self.kill()
                if self.rect.y == 4 and tutorial == False:
                    colorGroup = [random.choice(colors),random.choice(colors),random.choice(colors)]
                    while colorGroup == ["Black", "Black", "Black"] or colorGroup == ["Yellow", "Yellow", "Yellow"] or colorGroup == ["Blue", "Blue", "Blue"] or colorGroup == ["Red", "Red", "Red"]:
                        colorGroup = [random.choice(colors),random.choice(colors),random.choice(colors)]
                    barrier = Barrier(960, 4, colorGroup[0])
                    barrierGroup.add(barrier)
                    barrier = Barrier(960, 164, colorGroup[1])
                    barrierGroup.add(barrier)
                    barrier = Barrier(960, 324, colorGroup[2])
                    barrierGroup.add(barrier)
            if self.rect.colliderect(player.rect) == True and playerColor != self.color:
                if score > highscore:
                    highscore = score
                gameState = "Dead"
            if gameState == "Dead":
                self.kill()
    barrierGroup = pygame.sprite.Group()

    def spawnBarriers():
        colors = ["Red", "Blue", "Yellow"]
        colorGroup = [random.choice(colors),random.choice(colors),random.choice(colors)]
        while colorGroup == ["Black", "Black", "Black"] or colorGroup == ["Yellow", "Yellow", "Yellow"] or colorGroup == ["Blue", "Blue", "Blue"] or colorGroup == ["Red", "Red", "Red"]:
            colorGroup = [random.choice(colors),random.choice(colors),random.choice(colors)]
        barrier = Barrier(800, 4, colorGroup[0])
        barrierGroup.add(barrier)
        barrier = Barrier(800, 164, colorGroup[1])
        barrierGroup.add(barrier)
        barrier = Barrier(800, 324, colorGroup[2])
        barrierGroup.add(barrier)
        colorGroup = [random.choice(colors),random.choice(colors),random.choice(colors)]
        while colorGroup == ["Black", "Black", "Black"] or colorGroup == ["Yellow", "Yellow", "Yellow"] or colorGroup == ["Blue", "Blue", "Blue"] or colorGroup == ["Red", "Red", "Red"]:
            colorGroup = [random.choice(colors),random.choice(colors),random.choice(colors)]
        barrier = Barrier(1280, 4, colorGroup[0])
        barrierGroup.add(barrier)
        barrier = Barrier(1280, 164, colorGroup[1])
        barrierGroup.add(barrier)
        barrier = Barrier(1280, 324, colorGroup[2])
        barrierGroup.add(barrier)

    def spawnTutorialBarriers():
        barrier = Barrier(960, 4, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(960, 164, "Red")
        barrierGroup.add(barrier)
        barrier = Barrier(960, 324, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(1440, 4, "Red")
        barrierGroup.add(barrier)
        barrier = Barrier(1440, 164, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(1440, 324, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(1920, 4, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(1920, 164, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(1920, 324, "Red")
        barrierGroup.add(barrier)
        barrier = Barrier(2400, 4, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(2400, 164, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(2400, 324, "Blue")
        barrierGroup.add(barrier)
        barrier = Barrier(2880, 4, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(2880, 164, "Yellow")
        barrierGroup.add(barrier)
        barrier = Barrier(2880, 324, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(3360, 4, "Yellow")
        barrierGroup.add(barrier)
        barrier = Barrier(3360, 164, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(3360, 324, "Red")
        barrierGroup.add(barrier)
        barrier = Barrier(3840, 4, "Red")
        barrierGroup.add(barrier)
        barrier = Barrier(3840, 164, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(3840, 324, "Blue")
        barrierGroup.add(barrier)
        barrier = Barrier(4320, 4, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(4320, 164, "Yellow")
        barrierGroup.add(barrier)
        barrier = Barrier(4320, 324, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(4800, 4, "Black")
        barrierGroup.add(barrier)
        barrier = Barrier(4800, 164, "Blue")
        barrierGroup.add(barrier)
        barrier = Barrier(4800, 324, "Red")
        barrierGroup.add(barrier)

    class SwitchParticles(pygame.sprite.Sprite):
        def __init__(self, posY, color):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\RedParticleEffect1.png")).convert_alpha(), (50, 52))
            self.rect = pygame.Rect(72, (posY - 10), 50, 52)
            self.timer = pygame.time.get_ticks()
            if color == "Red":
                self.frames = [pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\RedParticleEffect1.png")).convert_alpha(), (50, 52)),
                               pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\RedParticleEffect2.png")).convert_alpha(), (50, 52)),
                               pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\RedParticleEffect3.png")).convert_alpha(), (50, 52)),
                               pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\RedParticleEffect4.png")).convert_alpha(), (50, 52)),
                               pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\RedParticleEffect5.png")).convert_alpha(), (50, 52))]
            elif color == "Blue":
                self.frames = [pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\BlueParticleEffect1.png")).convert_alpha(), (50, 52)),
                               pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\BlueParticleEffect2.png")).convert_alpha(), (50, 52)),
                               pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\BlueParticleEffect3.png")).convert_alpha(), (50, 52)),
                               pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\BlueParticleEffect4.png")).convert_alpha(), (50, 52)),
                               pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\BlueParticleEffect5.png")).convert_alpha(), (50, 52))]
            else:
                self.frames = [pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\YellowParticleEffect1.png")).convert_alpha(), (50, 52)),
                               pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\YellowParticleEffect2.png")).convert_alpha(), (50, 52)),
                               pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\YellowParticleEffect3.png")).convert_alpha(), (50, 52)),
                               pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\YellowParticleEffect4.png")).convert_alpha(), (50, 52)),
                               pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\YellowParticleEffect5.png")).convert_alpha(), (50, 52))]
        def update(self):
            if currentTime - self.timer < 50:
                self.image = self.frames[0]
            elif currentTime - self.timer < 100:
                self.image = self.frames[1]
            elif currentTime - self.timer < 150:
                self.image = self.frames[2]
            elif currentTime - self.timer < 200:
                self.image = self.frames[3]
            elif currentTime - self.timer < 250:
                self.image = self.frames[4]
            else:
                self.kill()
            if gameState == "Dead":
                self.kill()
    switchParticlesGroup = pygame.sprite.Group()

    class Orb(pygame.sprite.Sprite):
        def __init__(self, ypos):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\MetallicOrb2.png")).convert_alpha(), (32, 32))
            self.rect = pygame.Rect(960, ypos, 32, 32)
            self.particleTracker = 0
            self.particleColors = ["Red", "Red", "Red", "Blue", "Blue", "Blue", "Yellow", "Yellow", "Yellow"]
            self.timer = pygame.time.get_ticks()
        def update(self):
            global trapped, traptimer
            self.rect.x -= 2
            self.rect.y += math.sin(self.rect.x / 40) * 2
            if self.rect.x < -32:
                self.kill()
            if self.rect.colliderect(player.rect):
                trapped = True
                traptimer = pygame.time.get_ticks()
                self.kill()
            if currentTime - self.timer > 100:
                orbParticle = OrbParticle(self.rect.x, self.rect.y, self.particleColors[self.particleTracker])
                self.particleTracker += 1
                if self.particleTracker == 9:
                    self.particleTracker = 0
                orbParticleGroup.add(orbParticle)
                self.timer = pygame.time.get_ticks()
            if gameState == "Dead":
                self.kill()
    orbGroup = pygame.sprite.Group()
    orbSpawnTimer = 0
    trapped = False
    traptimer = 0

    class OrbParticle(pygame.sprite.Sprite):
        def __init__(self, xpos, ypos, color):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\OrbParticleEffectRed.png")).convert_alpha(), (16, 16))
            self.rect = pygame.Rect(xpos + 8, ypos + 8, 16, 16)
            self.timer = pygame.time.get_ticks()
            self.color = color
        def update(self):
            if self.color == "Red":
                if currentTime - self.timer < 300:
                    self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\OrbParticleEffectRed.png")).convert_alpha(), (16, 16))
                elif currentTime - self.timer < 600:
                    self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\OrbParticleEffectRed2.png")).convert_alpha(), (16, 16))
                elif currentTime - self.timer < 900:
                    self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\OrbParticleEffectRed3.png")).convert_alpha(), (16, 16))
                else:
                    self.kill()
            elif self.color == "Blue":
                if currentTime - self.timer < 300:
                    self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\OrbParticleEffectBlue.png")).convert_alpha(), (16, 16))
                elif currentTime - self.timer < 600:
                    self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\OrbParticleEffectBlue2.png")).convert_alpha(), (16, 16))
                elif currentTime - self.timer < 900:
                    self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\OrbParticleEffectBlue3.png")).convert_alpha(), (16, 16))
                else:
                    self.kill()
            else:
                if currentTime - self.timer < 300:
                    self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\OrbParticleEffectYellow.png")).convert_alpha(), (16, 16))
                elif currentTime - self.timer < 600:
                    self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\OrbParticleEffectYellow2.png")).convert_alpha(), (16, 16))
                elif currentTime - self.timer < 900:
                    self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\OrbParticleEffectYellow3.png")).convert_alpha(), (16, 16))
                else:
                    self.kill()
            if gameState == "Dead":
                self.kill()
    orbParticleGroup = pygame.sprite.Group()

    class Trap(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\trap.png")).convert_alpha(), (40, 36))
            self.rect = pygame.Rect(0, 0, 40, 36)
        def update(self):
            self.rect.x = player.rect.x - 4
            self.rect.y = player.rect.y - 2
    trapGroup = pygame.sprite.Group()
    trap = Trap()
    trapGroup.add(trap)

    class StartScreen(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\StartLogo1.png")).convert_alpha(), (960, 480))
            self.rect = pygame.Rect(0, 0, 960, 480)
        def update(self):
            if tutorial == True:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\StartLogo1.png")).convert_alpha(), (960, 480))
            else:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\StartLogo2.png")).convert_alpha(), (960, 480))
    startScreenGroup = pygame.sprite.Group()
    startScreen = StartScreen()
    startScreenGroup.add(startScreen)

    class TutorialText(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\TutorialText1.png")).convert_alpha(), (960, 480))
            self.rect = pygame.Rect(0, 0, 960, 480)
            self.orbSpawned = False
        def update(self):
            global tutorial
            if (currentTime - tutorialTimer) < 15000:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\TutorialText1.png")).convert_alpha(), (960, 480))
            elif (currentTime - tutorialTimer) < 27200:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\TutorialText2.png")).convert_alpha(), (960, 480))
            elif (currentTime - tutorialTimer) < 35000:
                if self.orbSpawned == False and tutorial == True:
                    orb = Orb(230)
                    orbGroup.add(orb)
                    self.orbSpawned = True
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Owner\Documents\Code\ColorPygame\Color Game Art\TutorialText3.png")).convert_alpha(), (960, 480))
            else:
                tutorial = False
    tutorialTextGroup = pygame.sprite.Group()
    tutorialText = TutorialText()
    tutorialTextGroup.add(tutorialText)
    tutorialTimer = 0

    font = pygame.font.Font("freesansbold.ttf", 32)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and gameState == "Dead" and mouseX > 400 and mouseX < 540 and mouseY > 300 and mouseY < 335:
                gameState = "Play"
                score = 0
                speed = 0
                if tutorial == False:
                    spawnBarriers()
                else:
                    spawnTutorialBarriers()
                    playerColor = "Red"
                    tutorialTimer = pygame.time.get_ticks()
            if event.type == pygame.MOUSEBUTTONDOWN and gameState == "Start" and mouseX > 660 and mouseX < 755 and mouseY > 250 and mouseY < 275:
                gameState = "Play"
                score = 0
                speed = 0
                if tutorial == False:
                    spawnBarriers()
                if tutorial == True:
                    spawnTutorialBarriers()
                    tutorialTimer = pygame.time.get_ticks()
            if event.type == pygame.MOUSEBUTTONDOWN and gameState == "Start" and mouseX > 655 and mouseX < 755 and mouseY > 200 and mouseY < 220:
                if tutorial == True:
                    tutorial = False
                else:
                    tutorial = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and trapped == False and gameState == "Play":
                    if playerColor == "Red":
                        playerColor = "Blue"
                        switchParticles = SwitchParticles(player.rect.y, "Blue")
                        switchParticlesGroup.add(switchParticles)
                    elif playerColor == "Blue":
                        playerColor = "Yellow"
                        switchParticles = SwitchParticles(player.rect.y, "Yellow")
                        switchParticlesGroup.add(switchParticles)
                    else:
                        playerColor = "Red"
                        switchParticles = SwitchParticles(player.rect.y, "Red")
                        switchParticlesGroup.add(switchParticles)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    movingUp = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    movingDown = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    movingUp = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    movingDown = False

        if gameState == "Start": #This makes sure that the tutorial timer will not start until the tutorial starts.
            tutorialTimer = pygame.time.get_ticks()

        mouseX, mouseY = pygame.mouse.get_pos()

        if movingUp == True and playerYChange >= -6:
            playerYChange -= 0.3
        elif movingDown == True and playerYChange <= 6:
            playerYChange += 0.3
        elif movingUp == False and movingDown == False:
            if playerYChange > 0:
                playerYChange -= 0.05
            elif playerYChange <0:
                playerYChange += 0.05

        if gameState == "Play" and tutorial == False:
            if score < 400:
                speed = 1
                score += 1
                colors = ["Red", "Blue", "Yellow"]
            elif score < 1500:
                speed = 2
                score += 2
                colors = ["Red", "Red", "Blue", "Blue", "Yellow", "Yellow", "Black"]
            elif score < 5000:
                speed = 3
                score += 3
                colors = ["Red", "Blue", "Yellow", "Black"]
            elif score < 10000:
                speed = 4
                score += 4
                colors = ["Red", "Blue", "Yellow", "Black", "Black"]
            else:
                speed = 5
                score += 5
                colors = ["Red", "Blue", "Yellow", "Black", "Black", "Black"]
        elif gameState == "Play" and tutorial == True:
            speed = 1

        if speed >= 3:
            if currentTime - orbSpawnTimer > 5000:
                orb = Orb(random.randint(40, 460))
                orbGroup.add(orb)
                orbSpawnTimer = pygame.time.get_ticks()

        if trapped == True and (currentTime - traptimer > 1000):
            trapped = False

        backgroundGroup.draw(screen)
        orbParticleGroup.draw(screen)
        orbGroup.draw(screen)
        if gameState == "Play" or gameState == "Start":
            playerGroup.draw(screen)
        if trapped == True and gameState == "Play":
            trapGroup.draw(screen)
        switchParticlesGroup.draw(screen)
        barrierGroup.draw(screen)

        if gameState == "Dead":
            scoreTextDisplay = font.render(str("Score:"), True, (180, 0, 0))
            screen.blit(scoreTextDisplay, (425, 110))
            scoreDisplay = font.render(str(score // 100), True, (180, 0, 0))
            screen.blit(scoreDisplay, (450, 140))
            highscoreTextDisplay = font.render(str("High Score:"), True, (180, 180, 0))
            screen.blit(highscoreTextDisplay, (386, 210))
            highscoreDisplay = font.render(str(highscore // 100), True, (180, 180, 0))
            screen.blit(highscoreDisplay, (450, 240))
            replayTextDisplay = font.render(str("Replay?"), True, (0, 0, 180))
            screen.blit(replayTextDisplay, (410, 310))
            player.rect.y = 224
            playerColor = "Red"

        if gameState == "Start":
            startScreenGroup.draw(screen)

        if gameState == "Play" and tutorial == True:
            tutorialTextGroup.draw(screen)

        if gameState == "Play" or gameState == "Start":
            playerGroup.update()
        if gameState == "Play":
            if (score // 100) % 3 == 0:
                scoreColor = (218, 54, 54)
            elif (score // 100) % 3 == 1:
                scoreColor = (56, 69, 213)
            else:
                scoreColor = (204, 218, 54)
            scoreDisplay = font.render(str(score // 100), True, scoreColor)
            if tutorial == False:
                screen.blit(scoreDisplay, (440, 12))
            backgroundGroup.update()
            trapGroup.update()
        switchParticlesGroup.update()
        orbGroup.update()
        orbParticleGroup.update()
        barrierGroup.update()
        startScreenGroup.update()
        tutorialTextGroup.update()

        currentTime = pygame.time.get_ticks()
        pygame.display.flip()
        await asyncio.sleep(0)
        clock.tick(60)

asyncio.run(main())
