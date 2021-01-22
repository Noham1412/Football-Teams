import random
import math

# jsut a comment 2
# this too
class player:
    def __init__(self, name, attack, defence, shape, war, position):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.shape = shape
        self.war = war
        self.position = position
        self.team = None

class team:
    def __init__(self, number):
        self.number = number
        self.players = []

    def attack(self):
        total = 0
        for p in self.players:
            total += p.attack
        if total != 0:
            return total / len(self.players)
        else:
            return 0

    def defence(self):
        total = 0
        for p in self.players:
            total += p.defence
        if total != 0:
            return total / len(self.players)
        else:
            return 0

    def shape(self):
        total = 0
        for p in self.players:
            total += p.shape
        if total != 0:
            return total / len(self.players)
        else:
            return 0

    def war(self):
        total = 0
        for p in self.players:
            total += p.war
        if total != 0:
            return total / len(self.players)
        else:
            return 0

    def attackers(self):
        total = 0
        for p in self.players:
            if p.position == 'attack':
                total += 1
        return total

    def defencers(self):
        total = 0
        for p in self.players:
            if p.position == 'defence':
                total += 1
        return total

    def centers(self):
        total = 0
        for p in self.players:
            if p.position == 'center':
                total += 1
        return total

    def is_he_fit(self, attack_per_team, defence_per_team, shape_per_team, war_per_team, player):
        tot_att = 0
        tot_def = 0
        tot_shape = 0
        tot_war = 0
        for p in self.players:
            tot_att += p.attack
            tot_def += p.defence
            tot_shape += p.shape
            tot_war += p.war
        if (player.attack + tot_att) > attack_per_team or (player.defence + tot_def) > defence_per_team or (player.shape + tot_shape) > shape_per_team or (player.war + tot_war) > war_per_team:
            return False
        return True


def difference(teams):
    dif_attack = max(teams[0].attack(), teams[1].attack(), teams[2].attack()) - min(teams[0].attack(), teams[1].attack(), teams[2].attack())
    dif_defence = max(teams[0].defence(), teams[1].defence(), teams[2].defence()) - min(teams[0].defence(), teams[1].defence(), teams[2].defence())
    dif_shape = max(teams[0].shape(), teams[1].shape(), teams[2].shape()) - min(teams[0].shape(), teams[1].shape(), teams[2].shape())
    dif_war = max(teams[0].war(), teams[1].war(), teams[2].war()) - min(teams[0].war(), teams[1].war(), teams[2].war())
    end = 0.3 * (dif_attack + dif_defence) + 0.2 * (dif_shape + dif_war)
    return end

def difference_per_position(teams):
    dif_attack = max(teams[0].attack(), teams[1].attack(), teams[2].attack()) - min(teams[0].attack(), teams[1].attack(), teams[2].attack())
    dif_defence = max(teams[0].defence(), teams[1].defence(), teams[2].defence()) - min(teams[0].defence(), teams[1].defence(), teams[2].defence())
    dif_shape = max(teams[0].shape(), teams[1].shape(), teams[2].shape()) - min(teams[0].shape(), teams[1].shape(), teams[2].shape())
    dif_war = max(teams[0].war(), teams[1].war(), teams[2].war()) - min(teams[0].war(), teams[1].war(), teams[2].war())
    return dif_attack, dif_defence, dif_shape, dif_war

players_out_this_week = [['Didi', 8, 4, 5, 4, 'center'], ['Ostro', 9, 5, 6, 7, 'attack'], ['Nisim', 9, 10, 9, 9, 'center']]
players_old = [['Lavie', 9, 7, 9, 8, 'attack'], ['Menash', 8, 7, 7, 9, 'attack'],  ['Ostro', 8, 5, 5, 5, 'attack'], ['Lobel', 5, 10, 10, 10, 'defence'], ['Carmel', 7, 8, 8, 8, 'center'], ['Ayache', 8, 5, 9, 6, 'attack'],  ['Noam', 6, 6, 8, 8, 'center'], ['Nimrod', 6, 7, 9, 9, 'attack'],  ['Anis', 5, 8, 7, 6, 'defence'],  ['Omer', 5, 9, 8, 10, 'center'], ['Kobi', 2, 8, 9, 9, 'defence'], ['Aviad', 5, 6, 8, 5, 'center'], ['Tzuf', 3, 5, 6, 8, 'center'], ['Yosi', 4, 2, 3, 5, 'attack']]
total_attack = 0
total_defence = 0
total_shape = 0
total_war = 0


players = []
for p in players_old:
    players.append(player(p[0],p[1],p[2], p[3], p[4], p[5]))
    total_attack += p[1]
    total_defence += p[2]
    total_shape += p[3]
    total_war += p[4]

attack_per_team = total_attack/3
defence_per_team = total_defence/3
shape_per_team = total_shape/3
war_per_team = total_war/3

the_best = [None, math.inf]
for x in range(1,50000):
    counter = 0
    teams = [team(1), team(2), team(3)]
    players_to_put = players.copy()
 # print('len put:',len(players_to_put))
    while players_to_put != []:
        # print('the round number:', x+1)
        player = random.choice(players_to_put)
        who_fit = []
        for t in teams:
            if t.is_he_fit(attack_per_team, defence_per_team, shape_per_team, war_per_team, player) and len(t.players) < 5:
                who_fit.append(t)
            elif counter == 5 and len(t.players) < 5:
                who_fit.append(t)
        if who_fit != []:
            counter = 0
            which_team = random.choice(who_fit)
            which_team.players.append(player)
            player.team = which_team
            players_to_put.remove(player)
        else:
            counter += 1
    dif = difference(teams)

    check = False
    for ti in teams:
        check = True
        for pla in ti.players:
            if pla.attack >= 8:
                check = False
    for play in players:
        if play.name == 'Tzuf' or play.name == 'Yosi' or play.name == 'Ostro':
            if len(play.team.players) == 4:
                check = True

    if teams[0].defencers() == 0 or teams[1].defencers() == 0 or teams[2].defencers() == 0 or teams[0].centers() == 0 or teams[1].centers() == 0 or teams[2].centers() == 0 or teams[0].attackers() == 0 or teams[1].attackers() == 0 or teams[2].attackers() == 0:
        check = True
    elif check:
        check = True
    elif dif < the_best[1]:
        the_best = [teams, dif]
        # print('')
        # print(dif_attack + dif_defence)

att, defe, shapee, ware = difference_per_position(the_best[0])
print('The attack difference:', att)
print('The defence difference:', defe)
print('The shape difference:', shapee)
print('The war difference:', ware)
for team in the_best[0]:
    print('Team number: ', team.number)
    print('Attack:', team.attack())
    print('defence:', team.defence())
    print('shape:', team.shape())
    print('war:', team.war())
    for p in team.players:
        print(p.name)




