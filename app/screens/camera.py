from datetime import datetime
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import *
from ui.widgets.screen import LcarsScreen
from datasources.network import get_ip_address_string

class ScreenCamera(LcarsScreen):
    def setup(self, all_sprites):
        all_sprites.add(LcarsBackgroundImage("assets/lcars_screen_3.png"), layer=0)
        # panel text
        all_sprites.add(LcarsText(colours.BLACK, (15, 44), "LCARS 105"), layer=1)

        all_sprites.add(LcarsText(colours.ORANGE, (0, 135), "WEBCAM", 2), layer=1)
        all_sprites.add(LcarsBlockSmall(colours.ORANGE, (211, 16), "LIGHTS"), layer=1)
        all_sprites.add(LcarsBlockSmall(colours.ORANGE, (249, 16), "CAMERAS"), layer=1)
        all_sprites.add(LcarsBlockSmall(colours.ORANGE, (287, 16), "ENERGY"), layer=1)

        self.ip_address = LcarsText(colours.BLACK, (444, 530), get_ip_address_string())
        all_sprites.add(self.ip_address, layer=1)

        # date display
        self.stardate = LcarsText(colours.BLUE, (12, 380), "STAR DATE 2311.05 17:54:32", 1.5)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)
        
        # camera display
        self.lastCameraUpdate = 0
        self.camera = LcarsImage("assets/weather.jpg", (188, 122))
        self.camera.visible = True
        all_sprites.add(self.camera, layer=2)

        # buttons
        all_sprites.add(LcarsButton(colours.RED_BROWN, (6, 662), "LOGOUT", self.logoutHandler), layer=4)
        all_sprites.add(LcarsButton(colours.PEACH, (106, 662), "HOME", self.homeHandler), layer=4)

        self.beep1 = Sound("assets/audio/panel/201.wav")
    
    def handleEvents(self, event, fpsClock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            return False
    
    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate >= 1000:
            self.stardate.setText("STAR DATE {}".format(datetime.now().strftime("%d%m.%y %H:%M:%S")))
            self.lastClockUpdate = pygame.time.get_ticks()
            
        if pygame.time.get_ticks() - self.lastCameraUpdate >= 10000:
            self.lastCameraUpdate = pygame.time.get_ticks()
            # update the picture from camera every 10 seconds
            #Sound("assets/audio/panel/207.wav").play()
        
        LcarsScreen.update(self, screenSurface, fpsClock)

    def homeHandler(self, item, event, clock):
        self.camera.visible = False
        from screens.main import ScreenMain
        self.loadScreen(ScreenMain())
        
    def logoutHandler(self, item, event, clock):
        from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenAuthorize())
