import numpy
import copy
import random as rd


class pillar:
    def __init__(self, color=-1, tile=None):
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
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]-1])
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]])
            elif coords[1] == 1:
                if coords[2]==0:
                    ret.append(-1)
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]])
                elif coords[2]==5:
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]-1])
                    ret.append(-1)
                else:
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]-1])
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]])
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
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]-1])
                    ret.append(tiles[not coords[0]][coords[1]-1][coords[2]])
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
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
            else:
                if coords[2] == 0:
                    ret.append(-1)
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
                elif coords[2] == 3:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
                    ret.append(-1)
                else:
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]-1])
                    ret.append(tiles[not coords[0]][coords[1]+1][coords[2]])
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
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]-1])
                    ret.append(tiles[not coords[0]][coords[1]][coords[2]])
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
                    #print(x.coordinates, cur.coordinates)
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
    #print('pillar:', pil_b, pil_g, pil_r)
    #print('flow:', flow_b, flow_g, flow_r)
    return [min(pil_b * flow_b, 21), min(pil_g * flow_g, 21), min(pil_r * flow_r, 21)]
    
def percentage_increase(cur_score, sim_score): # Currently prioritizing closeness to 21 rather than balance
    tot_percentage_diff = 0
    #print(sim_score)
    for i in range(3):
        sim_score[i] = min(21, sim_score[i])
        tot_percentage_diff += ((sim_score[i] - cur_score[i]) * 100) // 21
    return tot_percentage_diff

    


def simulate_tile_pair(tiles, cur_score, tile:tile, pillar:pillar):
    sim_tile = []
    for p in tiles:
        for x in p:
            for y in x:
                #print(y.coordinates, y.get_surrounding(tiles))
                if y.allocated == 0 and any(x.allocated == 1 for x in [x for x in y.get_surrounding(tiles) if x != -1]):
                    #print(y.coordinates, y.get_surrounding(tiles))
                    sim_tile.append(y.coordinates)
    placements = [-1,-1]
    mx_inc = -1
    found = False
    tot_no_pillar = 0
    no_pillar_mx_inc = -1
    no_pillar_placements = [-1,-1]
    #print(len(sim_tile))
    for x in sim_tile:
        sim_tiles = copy.deepcopy(tiles)
        tile.coordinates = x
        sim_tiles[x[0]][x[1]][x[2]] = tile
        for p in sim_tiles:
            for l in p:
                for y in l:
                    #print(y.allocated)
                    if y.allocated == 1 and pillar.color in y.colors_back and y.pillar_color == -1:
                        #print(y.coordinates)
                        found = True
                        sim_sim_tiles = copy.deepcopy(sim_tiles)
                        temp_coords = y.coordinates
                        sim_sim_tiles[temp_coords[0]][temp_coords[1]][temp_coords[2]].pillar_color = pillar.color
                        sim_score = get_cur_score(sim_sim_tiles)
                        sim_inc = percentage_increase(cur_score, sim_score)
                        if sim_inc > mx_inc: # might need to implemnent system that prioritizes closeness to other colors and amount of color pillars it supports
                            mx_inc = sim_inc
                            placements = [x, y.coordinates]
                        if sim_inc > no_pillar_mx_inc:
                            no_pillar_mx_inc = sim_inc
                            no_pillar_placements = [x, -1]
        if not found:
            tot_no_pillar += 1
            sim_score = get_cur_score(sim_tiles)
            sim_inc = percentage_increase(cur_score, sim_score)
            if sim_inc > no_pillar_mx_inc:
                no_pillar_mx_inc = sim_inc
                no_pillar_placements = [x, -1]
    if tot_no_pillar == len(sim_tile):
        placements = no_pillar_placements
        mx_inc = no_pillar_mx_inc

    return placements, mx_inc

def get_pairs():
    if rand_gen:
        inp1 = ""
        inp2 = ""
        inp3 = ""

        for _ in range(rd.randint(8,10)):
            inp1 += str(rd.randint(0,2))

        for _ in range(rd.randint(8,10)):
            inp2 += str(rd.randint(0,2))

        for _ in range(rd.randint(8,10)):
            inp3 += str(rd.randint(0,2))
    else:
        inp1 = input()
        inp2 = input()
        inp3 = input()
    pair1 = [inp1[0:6],inp1[6:-1], inp1[-1]]
    pair2 = [inp2[0:6],inp2[6:-1], inp2[-1]]
    pair3 = [inp3[0:6],inp3[6:-1], inp3[-1]]
    #print(pair1)
    ret = []
    tile1 = tile()
    tile2 = tile()
    tile3 = tile()

    tile1.assign([int(x) for x in pair1[0]], [int(x) for x in pair1[1]])
    tile2.assign([int(x) for x in pair2[0]], [int(x) for x in pair2[1]])
    tile3.assign([int(x) for x in pair3[0]], [int(x) for x in pair3[1]])

    ret.append([tile1, pillar(int(pair1[2]))])
    ret.append([tile2, pillar(int(pair2[2]))])
    ret.append([tile3, pillar(int(pair3[2]))])
    #print(ret)
    return ret
    
def simulate_mult_pairs(tiles, score, pairs):
    place = []
    best_score = -1
    index = -1
    for i,x in enumerate(pairs):
        temp_place, sim_score = simulate_tile_pair(tiles, score, x[0], x[1])
        if sim_score > best_score:
            place = temp_place
            best_score = sim_score
            index = i
    return place[0], place[1], index

def get_allocated(tiles):
    ret = []
    for x in tiles:
        for y in x:
            for z in y:
                if z.allocated:
                    if z.coordinates in ret:
                        print('hi there', z.coordinates)
                    else:
                        ret.append(z.coordinates)
    return ret

def game_loop():
    tiles = [[],[]]
    board_coordinates = [[],[]]
    gen_start(tiles, board_coordinates)
    score = get_cur_score(tiles)
    #print(score)
    coordinates_pillar = []
    coordinates_tile = [[0,1,2],[0,1,3]]
    for _ in range(10):
        pairs = get_pairs()
        new_tile, new_pillar, index = simulate_mult_pairs(tiles, score, pairs)

        #print(new_tile, new_pillar)
        #print(pairs[index][0].colors_front, pairs[index][0].colors_back, pairs[index][1].color)
        if new_tile not in coordinates_tile:
            coordinates_tile.append(new_tile)
        else:
            print('overlap')
        pairs[index][0].coordinates = new_tile
        tiles[new_tile[0]][new_tile[1]][new_tile[2]] = pairs[index][0]
        alloc = get_allocated(tiles)
        """for x in alloc:
            if x not in coordinates_tile:
                print(x)
        print()"""
        if new_pillar != -1:
            tiles[new_pillar[0]][new_pillar[1]][new_pillar[2]].pillar_color = pairs[index][1].color
            if new_pillar not in coordinates_pillar:
                coordinates_pillar.append(new_pillar)
            """
            else:
                print("Overlap")
            if new_pillar not in coordinates_tile:
                print("No Tile")
            """
        """
        else:
            print("No pillar")
        """
        score = get_cur_score(tiles)
        #print(score)


    #print(board_coordinates[0])
    #print(board_coordinates[1])
    #print()
    #print([x.coordinates for x in tiles[1][0][0].get_surrounding(tiles)])
    #test_get_surrounding(tiles)
    score = get_cur_score(tiles)
    #print(score)
    return coordinates_tile, coordinates_pillar
    
    
rand_gen = True
tot = 0
for _ in range(100):
    cur = game_loop()
    if cur == [21,21,21]:
        tot += 1
print(tot)