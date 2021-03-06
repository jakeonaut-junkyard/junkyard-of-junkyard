import os,sys
import pygame
from pygame.locals import *

def load_image(name,colorkey=None):
  fullname = os.path.join("resources/images",name)
  try:
    image = pygame.image.load(fullname)
  except pygame.error, message:
    print"Cannot load image:",name
    raise SystemExit, message
  image = image.convert()
  if colorkey is -1:
    if colorkey is -1:
      colorkey = image.get_at((0,0))
    image.set_colorkey(colorkey, RLEACCEL)
  return image

def load_sound(name):
  class NoneSound:
    def play(self): pass
  if not pygame.mixer:
    return NoneSound()
  fullname = os.path.join("resources",name)
  try:
    sound = pygame.mixer.Sound(fullname)
  except pygame.error, message:
    print "Cannot load sound:",wav
    raise SystemExit, message
  return sound
