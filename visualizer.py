import pygame
import time

class SudokuVisualizer:
    def __init__(self, width=540, height=540):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sudoku Solver Visualizer")
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (128, 128, 128)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        
        # Grid settings
        self.cell_size = width // 9
        self.font = pygame.font.Font(None, 36)

    def draw_grid(self, board, highlight_cell=None, highlight_color=None):
        self.screen.fill(self.WHITE)
        
        # Draw cells
        for i in range(9):
            for j in range(9):
                x = j * self.cell_size
                y = i * self.cell_size
                
                # Highlight cell if specified
                if highlight_cell and (i, j) == highlight_cell:
                    pygame.draw.rect(self.screen, highlight_color or self.GREEN,
                                  (x, y, self.cell_size, self.cell_size))
                
                # Draw cell borders
                pygame.draw.rect(self.screen, self.GRAY,
                               (x, y, self.cell_size, self.cell_size), 1)
                
                # Draw number
                if board[i][j] != 0:
                    number = self.font.render(str(board[i][j]), True, self.BLACK)
                    number_rect = number.get_rect(center=(x + self.cell_size // 2,
                                                        y + self.cell_size // 2))
                    self.screen.blit(number, number_rect)
        
        # Draw thick lines for 3x3 boxes
        for i in range(10):
            line_width = 4 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, self.BLACK,
                           (i * self.cell_size, 0),
                           (i * self.cell_size, self.height), line_width)
            pygame.draw.line(self.screen, self.BLACK,
                           (0, i * self.cell_size),
                           (self.width, i * self.cell_size), line_width)
        
        pygame.display.flip()

    def update(self, board, pos=None, value=None, delay=0.1):
        """Update the visualization with new board state"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        if pos:
            # First show the cell being considered
            self.draw_grid(board, pos, self.GREEN)
            time.sleep(delay)
            
            if value:
                board[pos[0]][pos[1]] = value
                # Then show the number being placed
                self.draw_grid(board, pos, self.GREEN)
                time.sleep(delay)
        else:
            self.draw_grid(board)
            time.sleep(delay)
        
        return True 