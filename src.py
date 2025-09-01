import pygame

pygame.init()  # Initialize Pygame


            
#Ustawienia okna gry

szerokosc_okna = 1024
wysokosc_okna = 1024

#kolory
green = (25,100,25)

background_image = pygame.image.load("trace.jpg") #ładowanie obrazka tło
car_image = "Car.png" #scieżka do obrazka samochodu

class Auto(pygame.sprite.Sprite):           #class tworząca samochód
    def __init__(self, obrazek, x, y):
        super().__init__()
        self.image = pygame.image.load(obrazek).convert_alpha()  # Wczytaj obrazek samochodu z przezroczystością
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.predkosc = 0
    
        def aktualizuj(self):   #logika poruszania się
            pass



ekran = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
player = Auto(car_image,256,256)

pygame.display.set_caption("Wyścig 2D")

# Grupa sprite'ów
wszystkie_spritey = pygame.sprite.Group()
wszystkie_spritey.add(player)


uruchomiona = True #flaga 

while uruchomiona: # uruchomiona główna pętla

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            uruchomiona = False

        wszystkie_spritey.update()

        ekran.blit(background_image, (0, 0)) # Narysuj tor jako tło

        wszystkie_spritey.draw(ekran) # Narysuj wszystkie sprite'y na ekranie
    pygame.display.flip() # Odśwież ekran
    
pygame.quit()
    
