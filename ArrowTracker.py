import pygame
import win32api
import win32con
class ArrowTracker():
    def __init__(self):
        self.a = True
        self.b = True
        self.down = True
        self.left = True
        self.right = True             
        
    def getKey(self, code):        
        return (win32api.GetAsyncKeyState(code))
    
    def update(self):        
        self.down = self.getKey(win32con.VK_DOWN)
        self.left = self.getKey(win32con.VK_LEFT)
        self.right = self.getKey(win32con.VK_RIGHT)
        self.b = self.getKey(win32con.VK_UP)
        self.a = self.getKey(ord('Z'))
        
        
    
            