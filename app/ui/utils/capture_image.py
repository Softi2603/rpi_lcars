# Python program to capture a single image
# using pygame library
  
# importing the pygame library
import pygame
import pygame.camera
  
class webcam():
    def __init__(self, cam_port, size):
        # initializing  the camera
        pygame.camera.init()
        
        # make the list of all available cameras
        self.camlist = pygame.camera.list_cameras()
        
        # if camera is detected or not
        if self.camlist:
        
            # initializing the cam variable with default camera
            self.cam = pygame.camera.Camera(self.camlist[cam_port], size)

    def get_image(self):
        if self.camlist:
            # opening the camera
            self.cam.start()
        
            # capturing the single image
            image = self.cam.get_image()
        else:
            image = None
            
        return image
    
if __name__ == '__main__':
    image = webcam(0, (640, 480)).get_image()
    
    if image != None:
        # saving the image
        pygame.image.save(image, "filename.png")
  
    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")