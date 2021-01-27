import pygame

pygame.init()

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 0.01
RAIO = 30
x = 10
y = 10
vel_x = VELOCIDADE
vel_y = VELOCIDADE

tela = pygame.display.set_mode((640, 480), 0)

class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 100
        self.raio = self.tamanho//2

    def calcular_regras(self):
        self.centro_x += 1

    def pintar(self, tela):
        #Desenhar o corpo do Pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        #Desenho da boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        #Olho do Pacman
        olho_x = int(self.centro_x + self.raio/4)
        olho_y = int(self.centro_y - self.raio*0.75)
        olho_raio = int(self.raio/10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

if __name__ == '__main__':
    pacman = Pacman()

    while True:
        # Calcular as regras
        pacman.calcular_regras()



        # Pintar a tela
        pacman.pintar(tela)
        pygame.display.update()




        # Captura os eventos
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()





"""while True:
    #Calcula as regras
    x += vel_x
    y += vel_y
    if x + RAIO > 640:
        vel_x = -VELOCIDADE
    elif x - RAIO< 0:
        vel_x = VELOCIDADE
    if y + RAIO> 480:
        vel_y = -VELOCIDADE
    elif y - RAIO< 0:
        vel_y = VELOCIDADE

    #Pinta
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (int(x), int(y)), RAIO, 0)
    pygame.display.update()

    #Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()"""