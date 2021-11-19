'''

pg.draw.circle(screen, color.YELLOW, (250, 250), 75)

pg.draw.rect(sc, color.YELLOW, (20, 20, 100, 75))
pg.draw.rect(sc, color.YELLOW, (20, 20, 100, 75), 8)

pygame.draw.line(sc, color.YELLOW, [10, 30], [290, 15], 3)
pygame.draw.line(sc, color.YELLOW, [10, 50], [290, 35])
pygame.draw.aaline(sc, color.YELLOW, [10, 70], [290, 55])

pygame.draw.lines(sc, color.YELLOW, True, [[10, 10], [140, 70], [280, 20]], 2)
pygame.draw.aalines(sc, color.YELLOW, False, [[10, 100], [140, 170], [280, 110]])

pygame.draw.polygon(sc, color.YELLOW, [[150, 10], [180, 50], [90, 90], [30, 30]])
pygame.draw.polygon(sc, color.YELLOW, [[250, 110], [280, 150], [190, 190], [130, 130]])
pygame.draw.aalines(sc, color.YELLOW, True, [[250, 110], [280, 150], [190, 190], [130, 130]])

pygame.draw.ellipse(sc, color.YELLOW, (10, 50, 280, 100))

pi = 3.14
pygame.draw.arc(sc, WHITE, (10, 50, 280, 100), 0, pi)
pygame.draw.arc(sc, PINK, (50, 30, 200, 150), pi, 2*pi, 3)

'''