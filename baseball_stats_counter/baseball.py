from asyncio import base_tasks
import re, sys, os

# extract player stats from each line
def regex_extract(line):
    stats = []
    pat = '(?P<name>[\w\s]*)batted[\s](?P<bats>[\d]) times with (?P<hits>[\d])'
    regex = re.match(pat, line)
    if regex:
        name = regex.group('name')
        bats = regex.group('bats')
        hits = regex.group('hits')
        stats = [name, bats, hits]
        return stats
    else:
        return False
      
 

class Player_Stats:
    names = []
    dict = {}
    printer = []
    


# input text file via commandline argument
# output error message when wrong command line arguments were input
if len(sys.argv) < 2:
    sys.exit(f'Usage: {sys.argv[0]} filename')

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

f = open(filename)

player_stat = Player_Stats()

# extract player stats from each line
for ln in f:
    
    stat = regex_extract(ln)
    if (stat == False):
        continue

    else:
        name = stat[0]
        bats = int(stat[1])
        hits = int(stat[2])

        if (name in player_stat.names): 
            i , j = player_stat.dict[name]
            i += bats
            j += hits
            # print (name, i, j)
            player_stat.dict.update({name: (i, j)})
        else:
            player_stat.names.append(name)
            player_stat.dict.update({name: (bats,hits)})

# take total bats and hits and calculate the batting average for each player
for player in player_stat.names:

    bats_total = player_stat.dict[player][0]
    hits_total = player_stat.dict[player][1]
    batting_average = hits_total / bats_total
    rounded = round(batting_average, 3)

    player_stat.printer.append([player, rounded])


# print(player_stat.printer)
# print (player_stat.printer)
    
player_stat.printer.sort(key=lambda x: x[1], reverse=True)

for player in player_stat.printer:
    print(player[0], ": ", player[1])
        
        




