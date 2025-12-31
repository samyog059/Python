import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Line Chart in Pygame")
clock = pygame.time.Clock()

# Data for chart
x_data = [1, 2, 3, 4, 6, 20, 24]
y_data = [3, 5, 7, 2, 7, 9, 1]

# Chart area
chart_rect = pygame.Rect(50, 50, 700, 500)

def draw_chart(surface, rect, x_vals, y_vals):
    # Draw border
    pygame.draw.rect(surface, (0, 0, 0), rect, 2)

    # Normalize values
    max_x = max(x_vals)
    max_y = max(y_vals)

    points = []
    for i in range(len(x_vals)):
        px = rect.x + (x_vals[i] / max_x) * rect.width
        py = rect.y + rect.height - (y_vals[i] / max_y) * rect.height
        points.append((px, py))

    # Draw line
    if len(points) > 1:
        pygame.draw.lines(surface, (0, 0, 255), False, points, 3)

    # Draw points
    for p in points:
        pygame.draw.circle(surface, (255, 0, 0), (int(p[0]), int(p[1])), 5)

    # Title
    font = pygame.font.SysFont(None, 36)
    title = font.render("Dynamic Data Plot", True, (0, 0, 0))
    surface.blit(title, (rect.x, rect.y - 40))


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    draw_chart(screen, chart_rect, x_data, y_data)

    pygame.display.update()
    clock.tick(60)
