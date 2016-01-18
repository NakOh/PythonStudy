import random


# 타일은 자신이 지뢰 인지 아닌지 정보를 가지고 있으며 자신 주변을 체크해서 숫자가 몇인지 가지고 있는다.
class Tile:
    isMine = False
    number = 0

    def __init__(self):
        mine = [True, False, False, False]
        self.isMine = random.choice(mine)


def find_mine(tile):
    if tile.isMine:
        pass
    else:
        pass


# 기본 맵 크기는 숫자 하나를 받아서 그 숫자 길이만큼의 정사각형 행렬로 진행합니다.
def make_map():
    print('맵을 만드는 중 입니다')
    # 입력 받은 크기 보다 2개 크게 만듭니다. 검사할때 편하도록
    tile = [[0] * (index+2) for x in range(index+2)]

    for i in range(len(tile)):
        for j in range(len(tile[i])):
            if i is 0 or j is 0 or i is (index + 1) or j is (index + 1):
                print("통과")
            else:
                tile[i][j] = Tile()

    for i in range(len(tile)):
        for j in range(len(tile[i])):
            if i is 0 or j is 0 or i is (index + 1) or j is (index + 1):
                print("통과")
            else:
                set_number(tile, i, j)

    for row in tile:
        print(row)


def set_number(tile, x, y):
    if tile[x][y].isMine is False:
        find_around_mine(tile, x, y)


def find_around_mine(tile, x, y):
    count = 0
    if tile[x-1][y].isMine or tile[x-1][y+1].isMine or tile[x][y+1].isMine or \
        tile[x+1][y+1].isMine or tile[x+1][y].isMine or tile[x+1][y-1].isMine or\
            tile[x][y-1].isMine or tile[x-1][y-1].isMine:
        count += 1


# 기본 크기 5
index = 5
index = int(input('맵 크기를 입력해 주세요 (5 이상)'))
if index < 5:
    index = 5
print('맵은 %d * %d 로 만들어집니다' % (index, index))
make_map()

# 기본 로직
# 처음 시작하면 타일 인스턴스를 맵 크기만큼 만든다.
# 타일 인스턴스를 하나씩 거치면서 랜덤으로 지뢰를 배치한다.
# 다시 한 번 타일을 돌면서 지뢰가 아닌 타일은 주변의 타일 지뢰 갯수를 샌 뒤 그 숫자를 할당 받는다.
# 맵 크기 만큼 콘솔에 별을 출력한다. (행렬 모양으로)
# 사용자가 (x,y)를 입력할 경우 해당 타일을 체크하여 지뢰일 경우 게임 끝 숫자일 경우 계속 진행한다.

# 추가 기능
# 만약 0일 경우 연결된 숫자 타일들을 전부 연다. 0일 경우 계속 반복한다.
