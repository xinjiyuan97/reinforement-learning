import numpy as np
from typing import Sequence, Tuple
class Grid:

    width: int
    height: int
    grid: np.ndarray # 2D array of int, 0 = empty, 1 = obstacle, 2 = goal
    actions: Sequence[str] = ["up", "down", "left", "right", "stay"]
    action_space: int = len(actions)
    state_space: int = 3 # 0 = empty, 1 = obstacle, 2 = goal
    border_punishment: int = -1
    obstacle_punishment: int = -1
    goal_reward: int = 1

    def init_grid(self) -> np.ndarray:
        # generate random grid
        grid = np.random.randint(0, 2, (self.height, self.width))
        return grid
    
    def __init__(self, width: int = None, height: int = None, grid: np.ndarray = None):
        if width is None and height is None and grid is None:
            raise ValueError("Must provide either width and height or grid")
        
        if width is not None and height is not None and grid is not None:
            raise ValueError("Must provide either width and height or grid, not both")
        
        if grid is not None:
            self.width = len(grid[0])
            self.height = len(grid)
            self.grid = grid
        else:
            self.width = width
            self.height = height
            self.grid = self.init_grid()

    def render(self, grid: np.ndarray = None, 
               border_punishment: int = -1,
               obstacle_punishment: int = -1, 
               goal_reward: int = 1) -> None:
        if grid is None:
            grid = self.grid
        else:
            grid = self.init_grid()
    
    def step(self, action: str) -> Tuple[Tuple[int, int], int, bool]:
        # return new state, reward, done
        if action not in self.actions:
            raise ValueError("Invalid action")
        
        if action == "up":
            pass
        elif action == "down":
            pass
        elif action == "left":
            pass
        elif action == "right":
            pass
        elif action == "stay":
            pass
        else:
            raise ValueError("Invalid action")
        
        return (0, 0), 0, False

       