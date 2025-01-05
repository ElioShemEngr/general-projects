import pygame
import random
import sys

# Inicialización
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Tao Pai Pai")
clock = pygame.time.Clock()

# Cargar las imágenes
cielo = pygame.image.load(r"D:\Projects-git\general-projects\taopaipai-game\images\cielo.png").convert()
montanas = pygame.image.load(r"D:\Projects-git\general-projects\taopaipai-game\images\montanas.png").convert_alpha()
viento = pygame.image.load(r"D:\Projects-git\general-projects\taopaipai-game\images\viento.png").convert_alpha()
tao = pygame.image.load(r"D:\Projects-git\general-projects\taopaipai-game\images\tao.png").convert_alpha()
fuego = pygame.image.load(r"D:\Projects-git\general-projects\taopaipai-game\images\fuego.png").convert_alpha()

# Cargar la Música
pygame.mixer.music.load(r"D:\Projects-git\general-projects\taopaipai-game\music\sonundtrack-tao.mp3")
pygame.mixer.music.play(-1)

# Obtener anchos de las imágenes
ancho_cielo = cielo.get_width()
ancho_montanas = montanas.get_width()
ancho_viento = viento.get_width()

# Posiciones iniciales
pos_x_cielo = pos_x_montanas = pos_x_viento = 0

# Velocidades del parallax
velocidad_cielo = 1
velocidad_montanas = 2
velocidad_viento = 4

# Posición inicial y velocidad de Tao
pos_tao_x = 100
pos_tao_y = 300
velocidad_tao_y = 7
velocidad_tao_x = 8
rango_movimiento_y = (50, 500)
rango_movimiento_x = (20, 480 - tao.get_width())

amplitud_temblor = 1

# Configurar la fuente para el contador de distancia y mensaje de Game Over
font = pygame.font.SysFont("comicsans", 36)
game_over_font = pygame.font.SysFont("saiyan sans regular", 92)  

# Inicializar la distancia recorrida
distancia_recorrida = 0
ultimo_tiempo = pygame.time.get_ticks()

# Lista de bolas de fuego
fuegos = []
velocidad_fuegos = 7
tiempo_crear_fuego = 1000
ultimo_tiempo_fuego = pygame.time.get_ticks()

def game_over():
    # Detener la música
    pygame.mixer.music.stop()
    
    # Renderizar el mensaje "Game Over"
    game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2 - game_over_text.get_height() // 2))
    
    # Actualizar la pantalla para mostrar el mensaje
    pygame.display.flip()
    
    # Esperar unos segundos antes de cerrar
    pygame.time.delay(2000)
    
    # Cerrar el juego
    pygame.quit()
    sys.exit()


# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Movimiento de Tao
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and pos_tao_y > rango_movimiento_y[0]:
        pos_tao_y -= velocidad_tao_y
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and pos_tao_y < rango_movimiento_y[1]:
        pos_tao_y += velocidad_tao_y
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and pos_tao_x < rango_movimiento_x[1]:
        pos_tao_x += velocidad_tao_x
        distancia_recorrida += 1
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and pos_tao_x > rango_movimiento_x[0]:
        pos_tao_x -= velocidad_tao_x

    # Actualizar contador de distancia cada segundo
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_tiempo >= 1000:
        distancia_recorrida += 1
        ultimo_tiempo = tiempo_actual

    # Generar nuevas bolas de fuego
    if tiempo_actual - ultimo_tiempo_fuego >= tiempo_crear_fuego:
        nuevo_fuego_y = random.randint(50, 500)
        fuegos.append(pygame.Rect(500, nuevo_fuego_y, fuego.get_width(), fuego.get_height()))
        ultimo_tiempo_fuego = tiempo_actual

    # Mover las bolas de fuego y detectar colisiones
    fuegos_a_eliminar = []
    tao_rect = pygame.Rect(pos_tao_x, pos_tao_y, tao.get_width(), tao.get_height())

    for fuego_rect in fuegos:
        fuego_rect.x -= velocidad_fuegos
        if fuego_rect.x < -fuego.get_width():
            fuegos_a_eliminar.append(fuego_rect)
        if tao_rect.colliderect(fuego_rect):
            game_over()  # Llamar a la función game_over en caso de colisión

    for fuego_rect in fuegos_a_eliminar:
        fuegos.remove(fuego_rect)


    # Efecto de temblor para Tao
    temblor = random.randint(-amplitud_temblor, amplitud_temblor)

    # Mover el fondo de parallax
    pos_x_cielo -= velocidad_cielo
    pos_x_montanas -= velocidad_montanas
    pos_x_viento -= velocidad_viento

    if pos_x_cielo <= -ancho_cielo:
        pos_x_cielo = 0
    if pos_x_montanas <= -ancho_montanas:
        pos_x_montanas = 0
    if pos_x_viento <= -ancho_viento:
        pos_x_viento = 0

    # Dibujar el fondo
    screen.blit(cielo, (pos_x_cielo, 0))
    screen.blit(cielo, (pos_x_cielo + ancho_cielo, 0))
    screen.blit(montanas, (pos_x_montanas, 0))
    screen.blit(montanas, (pos_x_montanas + ancho_montanas, 0))
    screen.blit(viento, (pos_x_viento, 0))
    screen.blit(viento, (pos_x_viento + ancho_viento, 0))

    # Dibujar a Tao
    screen.blit(tao, (pos_tao_x + temblor, pos_tao_y + temblor))

    # Dibujar las bolas de fuego
    for fuego_rect in fuegos:
        screen.blit(fuego, fuego_rect)

    # Renderizar el contador de distancia
    texto_distancia = font.render(f"Distancia: {int(distancia_recorrida)}", True, (255, 255, 255))
    screen.blit(texto_distancia, (10, 10))

    pygame.display.flip()
    clock.tick(60)
