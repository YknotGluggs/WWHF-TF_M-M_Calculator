import numpy

class pillar:
    def __init__(self, color=-1, tile= None):
        self.color = color
        self.tile = tile
        self.allocated = 0

    def get_value(self):
        pass

class tile:
    def __init__(self, colors_front=[], colors_back = [], coordinates=[]):
        self.coordinates = coordinates
        self.colors_front = colors_front # Not Pillar Side
        self.colors_back = colors_back # Pillar Side
        self.allocated = 0
        self.pillar_color = -1 # -1 for unallocated, 0 for blue, 1 for green, 2 for red

    def assign(self, colors_front, colors_back):
        self.colors_front = colors_front
        self.colors_back = colors_back
        self.allocated = 1

    def get_sides(self,tiles):
        ret = []
        coords = self.coordinates
        end = -1
        if coords[0] == 0:
            if coords[1] == 1:
                end = 5
            else:
                end = 3
        else:
            if coords[1] == 0 or coords[1] == 3:
                end = 2
            else:
                end = 4
        
        if coords[2] == 0:
            ret.append(-1)
            ret.append(tiles[coords[0]][coords[1]][coords[2]+1])
        elif coords[2] == end:
            ret.append(tiles[coords[0]][coords[1]][coords[2]-1])
            ret.append(-1)
        else:
            ret.append(tiles[coords[0]][coords[1]][coords[2]-1])
            ret.append(tiles[coords[0]][coords[1]][coords[2]+1])
        return ret
    
    def get_above(self,tiles):
        ret = []
        coords = self.coordinates
        if coords[0] == 0:
            if coords[1] == 0:
                if coords[2]==0:
                    ret.append(-1)
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]])
                elif coords[2]==3:
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]-1])
                    ret.append(-1)
                else:
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]])
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]-1])
            elif coords[1] == 1:
                if coords[2]==0:
                    ret.append(-1)
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]])
                elif coords[2]==5:
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]-1])
                    ret.append(-1)
                else:
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]])
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]-1])
            else:
                ret.append(tiles[not coords[0]][coords[1]][coords[2]])
                ret.append(tiles[not coords[0]][coords[1]][coords[2]+1])
        else:
            if coords[1] == 0:
                ret = [-1,-1]
            elif coords[1] == 1:
                if coords[2]==0:
                    ret.append(-1)
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]])
                elif coords[2]==4:
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]-1])
                    ret.append(-1)
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
                    ret.append(-1)
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                elif coords[2] == 5:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
                    ret.append(-1)
                else:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
            else:
                if coords[2] == 0:
                    ret.append(-1)
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                elif coords[2] == 3:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
                    ret.append(-1)
                else:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
        else:
            if coords[1] == 0 or coords[1] == 1:
                ret.append(tiles[not coords[0]][coords[1]][coords[2]])
                ret.append(tiles[not coords[0]][coords[1]][coords[2]+1])
            elif coords[1] == 2:
                if coords[2] == 0:
                    ret.append(-1)
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]])
                elif coords[2] == 4:
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]-1])
                    ret.append(-1)
                else:
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]])
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]-1])
            else:
                ret = [-1,-1]
        return ret


    def get_surrounding(self,tiles):
        #print(self.get_above(tiles))
        #print(self.get_sides(tiles))
        #print(self.get_below(tiles))
        ret = self.get_above(tiles) + self.get_sides(tiles) + self.get_below(tiles)
        return ret

def test_get_surrounding(tiles):
    for i in range(2):
        for j in range(3 + i):
            rng = -1
            if i == 0:
                if j == 0 or j == 2:
                    rng = 4
                else:
                    rng = 6
            else:
                if j == 0 or j == 3:
                    rng = 3
                else:
                    rng = 5
            for k in range(rng):
                print(i,j,k)
                arr = []
                for x in tiles[i][j][k].get_surrounding(tiles):
                    if x != -1:
                        arr.append(x.coordinates)
                    else:
                        arr.append([-1])
                print(arr)


def gen_start(tiles, board_coordinates):
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
    tiles[0][1][2].assign([0,1,0,1,2,2],[0,1,2])
    tiles[0][1][3].assign([0,0,1,2,1,2],[0,1,2])


def get_pillar_scores(tiles):
    queue = []
    tested = []
    pil_b, pil_g, pil_r = 0,0,0

    for p in tiles:
        for x in p:
            for y in x:
                if y.coordinates not in tested and y.pillar_color != -1:
                    queue.append(y)
                    break
            else:
                continue
            break
        else:
            continue
        break
    temp_score = 0
    while len(queue) > 0:
        cur:tile = queue.pop(0)
        tested.append(cur.coordinates)
        temp_score += 1
        cur_sur = cur.get_surrounding(tiles)
        for x in cur_sur:
            if x != -1 and x.coordinates not in tested and x.pillar_color == cur.pillar_color:
                queue.append(x)

        if len(queue) == 0:
            match cur.pillar_color:
                case 0:
                    pil_b = max(pil_b, temp_score)
                case 1:
                    pil_g = max(pil_g, temp_score)
                case 2:
                    pil_r = max(pil_r, temp_score)
            temp_score = 0
            for p in tiles:
                for x in p:
                    for y in x:
                        if y.coordinates not in tested and y.pillar_color != -1:
                            queue.append(y)
                            break
                    else:
                        continue
                    break
                else:
                    continue
                break
    return pil_b, pil_g, pil_r


def get_flow_score(tiles):
    flow_b, flow_g, flow_r = 0,0,0
    for current_tested_color in range(3):
        queue = []
        tested = []

        for p in tiles:
            for x in p:
                for y in x:
                    if y.coordinates not in tested and y.allocated == 1:
                        queue.append(y)
                        break
                else:
                    continue
                break
            else:
                continue
            break
        temp_score = 0
        while len(queue) > 0:
            cur:tile = queue.pop(0)
            tested.append(cur.coordinates)
            temp_score += 1
            cur_sur = cur.get_surrounding(tiles)
            for i,x in enumerate(cur_sur):
                if x != -1 and x.allocated == 1 and x.coordinates not in tested and cur.colors_front[i] == current_tested_color and x.colors_front[5-i] == cur.colors_front[i]:
                    queue.append(x)
            if len(queue) == 0:
                match current_tested_color:
                    case 0:
                        flow_b = max(flow_b, temp_score)
                    case 1:
                        flow_g = max(flow_g, temp_score)
                    case 2:
                        flow_r = max(flow_r, temp_score)
                temp_score = 0
                for p in tiles:
                    for x in p:
                        for y in x:
                            if y.coordinates not in tested and y.allocated == 1:
                                queue.append(y)
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
    return flow_b, flow_g, flow_r



def get_cur_score(tiles): # Might change to sim for pairs instead of score [(8,3), (6,4), (6,4)]
    pil_b, pil_g, pil_r = get_pillar_scores(tiles)
    flow_b, flow_g, flow_r = get_flow_score(tiles)
    print(pil_b, pil_g, pil_r)
    print(flow_b, flow_g, flow_r)
    return min(pil_b * flow_b, 24), min(pil_g * flow_g, 24), min(pil_r * flow_r, 24)
    
def percentage_increase(cur_score, sim_score): # Currently prioritizing closeness to 24 rather than balance
    tot_percentage_diff = 0
    for i in range(3):
        sim_score[i] = min(24, sim_score[i])
        tot_percentage_diff += ((sim_score[i] - cur_score[i]) * 100) // 24
    return tot_percentage_diff

    


def simulate_tile_pair(tiles, cur_score, tile:tile, pillar:pillar):
    delta = [0,0,0]
    sim_tile = []
    for p in tiles:
        for x in p:
            for y in x:
                if y.allocated == 0:
                    sim_tile.append(y.coordinates)
    
    placements = [-1,-1]
    mx_inc = -1
    found = False
    for x in sim_tile:
        sim_tiles = tiles.copy()
        sim_tiles[x[0]][x[1]][x[2]] = tile
        for p in sim_tiles:
            for l in p:
                for y in l:
                    if y.allocated == 1 and pillar.color in y.colors_back:
                        found = True
                        y.pillar_color = pillar.color
                        sim_b, sim_g, sim_r = get_cur_score(sim_tiles)
                        sim_inc = percentage_increase(cur_score, [sim_b, sim_g, sim_r])
                        if sim_inc > mx_inc:
                            mx_inc = sim_inc
                            placements = [x.coordinates, y.coordinates]
        if not found:
            sim_b, sim_g, sim_r = get_cur_score(sim_tiles)
            sim_inc = percentage_increase(cur_score, [sim_b, sim_g, sim_r])
            if sim_inc > mx_inc:
                mx_inc = sim_inc
                placements = [x.coordinates, y.coordinates]

    return placements


def game_loop():
    tiles = [[],[]]
    board_coordinates = [[],[]]
    gen_start(tiles, board_coordinates)
    score_r, score_b, score_g = get_cur_score(tiles)
    simulate_tile_pair()

    print(board_coordinates[0])
    print(board_coordinates[1])
    print()
    #print([x.coordinates for x in tiles[1][0][0].get_surrounding(tiles)])
    #test_get_surrounding(tiles)
    
    
    

game_loop()