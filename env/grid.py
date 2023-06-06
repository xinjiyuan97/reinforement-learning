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
    __current_state: Tuple[int, int] = (0, 0)

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
            if self.__current_state[0] == 0:
                return self.__current_state, self.border_punishment, False
            else:
                self.__current_state = (self.__current_state[0] - 1, self.__current_state[1])
        elif action == "down":
            if self.__current_state[0] == self.height - 1:
                return self.__current_state, self.border_punishment, False
            else:
                self.__current_state = (self.__current_state[0] + 1, self.__current_state[1])
        elif action == "left":
            if self.__current_state[1] == 0:
                return self.__current_state, self.border_punishment, False
            else:
                self.__current_state = (self.__current_state[0], self.__current_state[1] - 1)
        elif action == "right":
            if self.__current_state[1] == self.width - 1:
                return self.__current_state, self.border_punishment, False
            else:
                self.__current_state = (self.__current_state[0], self.__current_state[1] + 1)
        elif action == "stay":
            pass
        else:
            raise ValueError("Invalid action")
        if self.grid[self.__current_state[0]][self.__current_state[1]] == 1:
            return self.__current_state, self.obstacle_punishment, False
        elif self.grid[self.__current_state[0]][self.__current_state[1]] == 2:
            return self.__current_state, self.goal_reward, True
        return self.__current_state, 0, False

       