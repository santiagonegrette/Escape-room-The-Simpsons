import pygame
import sys

class Juego:
    def __init__(self):
        # Inicializar Pygame
        pygame.init()

        # Obtener la resolución del monitor
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

        # Inicializar la pantalla en modo pantalla completa
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)

        # Cargar imágenes
        self.imagen_actual = pygame.image.load('barrio los simpson.png')
        self.imagen_siguiente = pygame.image.load('casa.png')

        # Escalar las imágenes para que se ajusten a la pantalla
        self.imagen_actual = pygame.transform.scale(self.imagen_actual, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.imagen_siguiente = pygame.transform.scale(self.imagen_siguiente, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Definir variables para la transición
        self.transicion_duración = 6000  # Duración en milisegundos
        self.tiempo_inicio_transicion = pygame.time.get_ticks()

        # Bandera para indicar si se ha completado la transición
        self.transicion_terminada = False

        # Cargar imagen del botón y definir su tamaño
        self.boton_play = pygame.image.load('play.png')
        self.boton_ancho = 200  # Nuevo ancho del botón
        self.boton_alto = 200   # Nuevo alto del botón
        self.boton_play = pygame.transform.scale(self.boton_play, (self.boton_ancho, self.boton_alto))

        self.boton_ranking = pygame.image.load("ranking.png")
        self.boton_ranking = pygame.transform.scale(self.boton_ranking, (self.boton_ancho, self.boton_alto))

        # Definir la posición inicial del botón play
        self.boton_play_x = 100  # Posición X del botón play
        self.boton_play_y = 50  # Posición Y del botón play

        # Definir la posición inicial del botón ranking
        self.boton_ranking_x = 100  # Posición X del botón ranking
        self.boton_ranking_y = 400  # Posición Y del botón ranking

        # Crear los rectángulos de los botones con las nuevas posiciones
        self.boton_play_rect = self.boton_play.get_rect(topleft=(self.boton_play_x, self.boton_play_y))
        self.boton_ranking_rect = self.boton_ranking.get_rect(topleft=(self.boton_ranking_x, self.boton_ranking_y))

        # Lista de botones
        self.botones = [(self.boton_play, self.boton_play_rect), (self.boton_ranking, self.boton_ranking_rect)]

    def centrar_botones(self):
        total_altura = sum(boton.get_height() for boton, _ in self.botones)
        y_offset = (self.SCREEN_HEIGHT - total_altura) // 2

        for boton, rect in self.botones:
            x_offset = (self.SCREEN_WIDTH - boton.get_width()) // 2
            self.screen.blit(boton, (x_offset, y_offset))
            y_offset += boton.get_height()

    def bucle_principal(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for boton, rect in self.botones:
                        if rect.collidepoint(event.pos):
                            if boton == self.boton_play:
                                print("El botón de Play fue presionado")
                            elif boton == self.boton_ranking:
                                print("El botón de Ranking fue presionado")

            # Si la transición aún no ha terminado, realizar la transición
            if not self.transicion_terminada:
                # Calcular la fracción de tiempo transcurrido
                tiempo_transcurrido = pygame.time.get_ticks() - self.tiempo_inicio_transicion
                fraccion_tiempo = min(tiempo_transcurrido / self.transicion_duración, 1)

                # Combinar las dos imágenes con una interpolación lineal
                self.screen.blit(self.imagen_actual, (0, 0))
                surface_siguiente = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
                surface_siguiente.set_alpha(fraccion_tiempo * 255)
                surface_siguiente.blit(self.imagen_siguiente, (0, 0))
                self.screen.blit(surface_siguiente, (0, 0))

                # Si la transición ha terminado (fracción de tiempo igual a 1), actualizar la bandera
                if fraccion_tiempo >= 1:
                    self.transicion_terminada = True
            else:
                # Centrar los botones en la pantalla
                self.centrar_botones()

            # Actualizar la pantalla en cada iteración del bucle
            pygame.display.flip()

# Crear una instancia del juego y ejecutar el bucle principal
if __name__ == "__main__":
    juego = Juego()
    juego.bucle_principal()
