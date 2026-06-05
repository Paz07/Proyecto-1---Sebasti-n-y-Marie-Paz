import pygame
import lifelike_logica as lif
import easygui

tick = 10

def main():
    pygame.init()
    clock = pygame.time.Clock()
    filas = int(easygui.enterbox("Cantidad de filas"))
    columnas = int(easygui.enterbox("Cantidad de columnas"))
    tam = int(easygui.enterbox("Tamaño de las celdas"))
    texto = easygui.enterbox("Regla de nacimiento (B)")
    nacimiento = []
    for digito in texto:
        nacimiento.append(int(digito))
    texto = easygui.enterbox("Regla de supervivencia (S)")
    supervivencia = []
    for digito in texto:
        supervivencia.append(int(digito))
    M = lif.generar_matriz_aleatoria(filas, columnas)
    w, h = columnas * tam, filas * tam
    window = pygame.display.set_mode((w, h))
    loop = True
    pausa = False
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    pausa = not pausa
                elif keys[pygame.K_r]:
                    M = lif.generar_matriz_aleatoria(filas, columnas)
                elif keys[pygame.K_b]:
                    M = lif.generar_matriz_vacia(filas, columnas)
                elif keys[pygame.K_g]:
                    datos = {"M": M,"filas": filas,"columnas": columnas,"tam": tam,"nacimiento": nacimiento,"supervivencia": supervivencia}
                    lif.guardar("partida.dat", datos)
                elif keys[pygame.K_c]:
                    datos = lif.cargar("partida.dat")
                    M = datos["M"]
                    filas = datos["filas"]
                    columnas = datos["columnas"]
                    tam = datos["tam"]
                    nacimiento = datos["nacimiento"]
                    supervivencia = datos["supervivencia"]
                    w, h = columnas * tam, filas * tam
                    window = pygame.display.set_mode((w, h))
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                x, y = pygame.mouse.get_pos()
                if buttons[0]:
                    f = y // tam
                    c = x // tam
                    M[f][c] = (M[f][c] + 1) % 2
                    
        window.fill((0, 0, 0))
        for f in range(filas):
            for c in range(columnas):
                if M[f][c] == 1:
                    x = c * tam
                    y = f * tam
                    pygame.draw.rect(window, (0, 255, 128), (x, y, tam, tam))
        if not pausa:
            M = lif.transicion(M, nacimiento, supervivencia)
        pygame.display.update()
        clock.tick(tick)
    pygame.quit()

if __name__ == "__main__":
    main()
