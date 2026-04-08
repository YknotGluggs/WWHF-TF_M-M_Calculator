import numpy


class tile:
    def __init__(self, colors_front=[], colors_back = [], coordinates=[]):
        self.coordinates = coordinates
        self.colors_front = colors_front
        self.colors_back = colors_back
        self.allocated = 0

    def get_sides(self,tiles):
        ret = []
        coords = self.coordinates
        off = 3-coords%2
        if coords[2] == 0:
            ret.append(tiles[coords[0]][coords[2]+1])
        elif coords[2] == coords[1] + off:
            ret.append(tiles[coords[0]][coords[2]-1])
        else:
            ret.append(tiles[coords[0]][coords[2]-1])
            ret.append(tiles[coords[0]][coords[2]+1])
        return ret
    
    def get_above(self,tiles):
        ret = []
        coords = self.coordinates
        if coords[0] == 0:
            if coords[1] == 0:
                if coords[2]==0:
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]])
                elif coords[2]==3:
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]+1])
                else:
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]])
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]+1])
            elif coords[1] == 1:
                if coords[2]==0:
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]])
                elif coords[2]==5:
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]]-1)
                else:
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]])
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]-1])
            else:
                ret.append(tiles[not coords[0]][coords[1]-1][coords[2]])
                ret.append(tiles[not coords[0]][coords[1]-1][coords[2]+1])
        else:
            if coords[1] == 0:
                ret = []
            elif coords[1] == 1:
                if coords[2]==0:
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]])
                elif coords[2]==4:
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]-1])
                else:
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]])
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]-1])
            elif coords[1] == 2 or coords[1] == 3:
                ret.append(tiles[not coords[0]][coords[1]-1][coords[2]])
                ret.append(tiles[not coords[0]][coords[1]-1][coords[2]+1])
        return ret
    
    def get_below(self,tiles):
        ret = []
        coords = self.coordinates
        if coords[0] == 0:
            if coords[1] == 0:
                ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                ret.append(tiles[not coords[0]][coords[1]+1][coords[2]+1])
            elif coords[1] == 1:
                if coords[2] == 0:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                elif coords[2] == 5:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
                else:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
            else:
                if coords[2] == 0:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                elif coords[2] == 5:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
                else:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
        else:
            if coords[1] == 0 or coords[1] == 1:
                ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                ret.append(tiles[not coords[0]][coords[1]+1][coords[2]+1])
            elif coords[1] == 2:
                if coords[2] == 0:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                elif coords[2] == 4:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
                else:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
            else:
                ret = []





    def get_surrounding(self,tiles):
        ret = self.get_sides(tiles)
        coords = self.coordinates
        
        return ret

    

class pillar:
    def __init__(self, color=-1, tile= None):
        self.color = color
        self.tile = tile
        self.allocated = 0

    def get_value(self):
        pass
    


def game_loop():
    tiles = [[],[]]
    pillars = [[],[]]
    score_r, score_b, score_g = 0,0,0
    board_coordinates = [[],[]]
    for i in range(7):
        board_coordinates[(i+1)%2].append([])
        tiles[(i+1)%2].append([])
        if i < 4:
            for j in range(i+3):
                board_coordinates[(i+1)%2][i//2].append(j)
                tiles[(i+1)%2][i//2].append(tile(coordinates=[(i+1)%2,i//2,j]))
        else:
            for j in range(9-i):
                board_coordinates[(i+1)%2][i//2].append(j)
                tiles[(i+1)%2][i//2].append(tile(coordinates=[(i+1)%2,i//2,j]))

    print(board_coordinates[0])
    print(board_coordinates[1])

    
    

game_loop()