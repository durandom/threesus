import numpy as np
from enum import Enum
from .card import Card

class ShiftDirection( Enum ):
    left = 1
    right = 2
    up = 3
    down = 4

class Board():

    width = 4
    height = 4

    def __init__(self, board = None):
        if board:
            self._board = np.copy(board)
        else:
            self._board = np.empty([self.height, self.width], dtype=Card)
    
    def copy_from(self, board):
        self._board = np.copy(board)

    def get_max_card_value(self):
        ret = 0
        for x in range(self.width):
            for y in range(self.height):
                card = self._board[(x, y)]
                if card:
                    if card.value > ret:
                        ret = card.value
        return ret

        
    def all_shift_directions(self):
        return list(ShiftDirection)

    def shift(self, dir, new_card_cells):
        ret = False
        increment = self.get_shift_increment(dir)
        width_or_height = self.get_shift_width_or_height(dir)

        for start_cell in self.get_shift_start_cells(dir):
            shifted = self.shift_row_or_column(start_cell, increment, width_or_height) 
            if (shifted and new_card_cells):
                new_card_cells.append(start_cell - increment * (width_or_height -1))
            print(start_cell)
        
        return ret
    # public bool Shift(ShiftDirection dir, IList<IntVector2D> newCardCells)
    # {
    # 	bool ret = false;
    # 	IntVector2D increment = GetShiftIncrement(dir);
    # 	int widthOrHeight = GetShiftWidthOrHeight(dir);
    # 	foreach(IntVector2D startCell in GetShiftStartCells(dir))
    # 	{
    # 		bool shifted = ShiftRowOrColumn(startCell, increment, widthOrHeight);
    # 		if(shifted && newCardCells != null)
    # 			newCardCells.Add(startCell - increment * (widthOrHeight - 1));
    # 		ret = ret || shifted;
    # 	}
    # 	return ret;
    # }

    def shift_row_or_column(self, start_cell, increment, width_or_height):
        ret = False

        # Impossible to shift the start cell, so just skip it.
        prev_cell = start_cell
        cur_cell = start_cell - increment

        # Try to shift each cell one-by-one.
        for i in range(1, width_or_height):
            cur_card = self[cur_cell]
            print(f'The card at {cur_cell} is {cur_card}')
    #     for(int i = 1; i < widthOrHeight; i++)
    #     {
    #         Card curCard = this[curCell];
    #         if(curCard != null)
    #         {
    #             Card prevCard = this[prevCell];
    #             if(prevCard == null)
    #             {
    #                 this[prevCell] = curCard;
    #                 this[curCell] = null;
    #                 ret = true;
    #             }
    #             else
    #             {
    #                 // Try to merge on top of the previous card.
    #                 Card merged = curCard.GetMergedWith(prevCard);
    #                 if(merged != null)
    #                 {
    #                     this[prevCell] = merged;
    #                     this[curCell] = null;
    #                     ret = true;
    #                 }
    #             }
    #         }

    #         prevCell = curCell;
    #         curCell -= increment;
    #     }

    #     return ret;
    # }
        return ret

    def get_shift_start_cells(self, dir):
        r = []
        if dir is ShiftDirection.left:
            for y in range(self.height):
                r.append(np.array([0, y]))
        return r
        
        # public static IEnumerable<IntVector2D> GetShiftStartCells(ShiftDirection dir)
        # {
        # 	switch(dir)
        # 	{
        # 		case ShiftDirection.Left:
        # 		{
        # 			for(int y = 0; y < BOARD_HEIGHT; y++)
        # 				yield return new IntVector2D(0, y);
        # 			break;
        # 		}
        # 		case ShiftDirection.Right:
        # 		{
        # 			for(int y = 0; y < BOARD_HEIGHT; y++)
        # 				yield return new IntVector2D(BOARD_WIDTH - 1, y);
        # 			break;
        # 		}
        # 		case ShiftDirection.Up:
        # 		{
        # 			for(int x = 0; x < BOARD_WIDTH; x++)
        # 				yield return new IntVector2D(x, 0);
        # 			break;
        # 		}
        # 		case ShiftDirection.Down:
        # 		{
        # 			for(int x = 0; x < BOARD_WIDTH; x++)
        # 				yield return new IntVector2D(x, BOARD_HEIGHT - 1);
        # 			break;
        # 		}
        # 		default:
        # 		{
        # 			throw new NotSupportedException("Unknown ShiftDirection '" + dir + "'.");
        # 		}
        # 	}
        # }

    def get_shift_width_or_height(self, dir):
        if dir is ShiftDirection.left:
            return self.width
        elif dir is ShiftDirection.right:
            return self.width
        elif dir is ShiftDirection.up:
            return self.height
        elif dir is ShiftDirection.down:
            return self.height

    def get_shift_increment(self, dir):
        if dir is ShiftDirection.left:
            return np.array([-1, 0])
        elif dir is ShiftDirection.right:
            return np.array([1, 0])
        elif dir is ShiftDirection.up:
            return np.array([0, -1])
        elif dir is ShiftDirection.down:
            return np.array([0, 1])

    def __getitem__(self, position):
        return self._board[tuple(position)]
    
    def __setitem__(self, position, value):
        self._board[tuple(position)] = value

    def __str__(self):
        return str(self._board)