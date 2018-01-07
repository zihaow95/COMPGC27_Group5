import numpy as np
from itertools import combinations, permutations
import matplotlib.pyplot as plt


bias = [np.asarray([-0.41672516, -0.08315316, -2.1361076, 1.6402711, -1.79720985,
                    -0.82247295, 0.50268592, -1.24528809, -1.06030302, -0.90919977]),
        np.asarray([0.84780166, 1.82571246, 0.36449871, -1.011711, 0.74495357,
                    -0.60988426, -0.09355117, 1.20129206, -0.49430521, 0.11425103]),
        np.asarray([-1.05433495, -0.2732333, -0.17596661, -0.95781359, -0.29816053,
                    -0.23611451, -0.56536253, -1.27882702, -1.29263377, -0.23341424]),
        np.asarray([-1.1301799, 2.30144652])]

weights = [np.asarray([[-2.43472556e+00, 1.12437639e-01, 3.73061256e-01, 1.35921553e+00,
                        4.93958980e-01, -8.35508674e-01, 4.55115291e-03, 5.39244027e-01,
                        -3.13671001e-01, 7.70893296e-01, -1.85464939e+00, 1.74751072e+00,
                        1.47500798e+00, -3.20659425e-01, 6.18694754e-01, 6.66085833e-02],
                       [-7.89866360e-01, 1.22959271e-01, -7.53152772e-03, 1.12469602e-02,
                        -2.06399626e-02, -6.14371864e-03, 1.44193320e-02, 7.57429445e+00,
                        -6.52844828e-01, 4.67794629e-01, 4.88992564e-03, -3.49780896e-04,
                        1.33009283e-03, 1.06574124e-03, -1.87030925e-02, -7.57208495e+00],
                       [-2.04032754e+00, 4.62731992e-02, -6.69025494e-01, -1.43445528e+00,
                        5.31443570e-01, 7.40061841e-01, -6.52933049e-01, 8.49903643e-01,
                        -3.81169392e-01, 6.68360993e-02, -1.09570050e+00, 1.59503702e+00,
                        -2.65366550e+00, -8.77549499e-02, 7.03085032e-01, -2.03234560e+00],
                       [-1.89468969e-01, -7.72183701e-02, 8.24714718e-01, 1.24822460e+00,
                        -4.03880613e-01, -1.38449718e+00, 1.36724725e+00, 1.21789263e+00,
                        -4.62004782e-01, 3.50888657e-01, 3.81884277e-01, 5.66290764e-01,
                        2.04255743e-01, 1.40671127e+00, -1.73791763e+00, 1.04083343e+00],
                       [3.75702151e-01, -2.20875686e-01, 8.97638965e-01, -2.46701898e+00,
                        1.04759690e+00, 2.34698565e-01, -1.32151668e+00, 4.27488207e-01,
                        -3.07619607e-01, 2.58153184e+00, 1.44221664e+00, 9.79569316e-02,
                        -9.35983895e-01, -8.47363804e-01, -5.51527068e-01, -8.66922638e-01],
                       [-9.40411664e-01, -6.32431905e-01, 4.62387295e-02, -4.29526036e-02,
                        6.48180926e-02, -9.19492129e-04, -5.02925601e-03, -4.99471741e+00,
                        -1.00036572e+00, 4.71080583e-01, -4.09641564e-03, 4.61784952e-02,
                        -2.33128968e-02, 2.76640262e-02, 5.02376271e-02, 4.99301940e+00],
                       [1.10894595e+00, -1.76511472e+00, -1.29755247e-01, -5.18034904e-01,
                        -1.07327730e+00, 5.66383036e-01, -2.01127731e-01, 9.95935673e-01,
                        -1.48266098e+00, 8.46114565e-01, 4.79066186e-01, 1.19745556e-01,
                        -1.42208716e+00, -2.59805160e-01, -1.55087068e+00, -2.08588653e+00],
                       [3.27974540e+00, 9.70861320e-01, 1.79259285e+00, -4.29013319e-01,
                        6.96197980e-01, 6.97416272e-01, 6.01515814e-01, 3.65949071e-03,
                        -2.28247558e-01, -2.06961226e+00, 6.10144086e-01, 4.23496900e-01,
                        1.11788673e+00, -2.74242089e-01, 1.74181219e+00, -4.47500876e-01],
                       [-1.25999134e+00, 9.36684620e-01, -7.09765198e-01, -1.48514859e+00,
                        -5.90926701e-02, 5.03962871e-01, 1.81380522e-02, 2.75336355e-01,
                        4.10573042e+00, 8.17185051e-01, 1.52217291e+00, -1.96055810e+00,
                        2.73817932e-01, 5.47039911e-01, -3.86992672e-01, -9.55265611e-01],
                       [3.96324666e-01, -3.14580902e-01, -6.74996825e-01, 1.21290362e+00,
                        1.40458374e+00, 3.50946967e-01, -4.41599155e-01, 5.56639865e-01,
                        8.30072058e-01, 6.31191040e-01, -1.30282282e+00, -4.19213983e-01,
                        2.55865284e-01, 6.01437818e-01, 9.28982143e-01, 7.54593553e-01]]),
           np.asarray([[-0.86756043, -0.14669438, -1.23535239, 2.07106497, 0.1828606,
                        0.42243614, 1.03415871, -0.03265482, -1.07797081, -0.13027306],
                       [-0.68801174, 2.52730185, 0.85929802, -1.56795813, 0.54754679,
                        -0.27188271, -1.05255317, -0.57501238, -1.74265761, -0.09583257],
                       [-0.07086097, -0.89096448, -0.7095498, 0.54847843, -0.50481713,
                        0.22556009, 0.55472636, -0.5174837, -0.19956994, 2.46717724],
                       [0.26524038, -1.54723584, 0.07844344, -1.18323238, 1.26905436,
                        0.87643917, 1.08013912, 1.00839384, 0.35926678, 1.03674269],
                       [0.42910758, -1.88447137, -1.01504721, -0.16530596, -2.39896678,
                        2.5549646, -1.71434459, 0.12925568, -1.40540484, -1.8841886],
                       [-0.08523485, -1.20136003, -0.14254843, 0.56917451, -0.48912631,
                        0.92484478, 0.50949724, -0.34856868, -0.31829229, 0.48480116],
                       [-0.02983815, 0.28751982, -2.38749884, -0.02256075, 0.36964347,
                        -0.28282258, 0.33681179, 1.82995524, 0.10253788, 0.5971522],
                       [-0.83258486, -0.67446921, -0.4834168, -1.009903, -0.02519326,
                        -1.04699583, -0.17463629, -1.41085259, -1.64212731, -0.63605151],
                       [-0.74736523, -0.79335046, -0.61240326, -0.08834489, 1.05666269,
                        1.7040769, 0.72198106, -0.10590872, 1.39503645, -1.28550788],
                       [-1.89633545, 0.55299314, -0.0109908, -0.05095278, -0.06250685,
                        -1.7199084, -1.15414577, 1.33926046, 0.98712248, -0.60977316]]),
           np.asarray([[1.8609531, -1.29560288, -0.62935579, 0.34275597, -1.03925488,
                        -0.46326769, -0.34954288, -0.39659955, 0.8578759, 0.46500135],
                       [-0.91597677, -1.19333048, 0.36661748, 0.38702329, -0.03497859,
                        0.74648199, 0.66074053, -0.6273933, 0.89438666, -1.9053185],
                       [-1.87767154, 0.13534747, -1.08313454, -1.1327121, -0.2705376,
                        -0.81677215, -0.08137388, -1.4642558, -0.43814922, 3.00133058],
                       [0.30691574, -2.31425096, 0.80656583, 1.12420428, 2.04042744,
                        0.54290709, -0.66773456, 1.42265882, 0.88179071, -1.99529791],
                       [0.77952001, -0.22822874, 1.11599538, -0.31584715, 0.78985679,
                        0.21014268, 0.62224081, -0.01909552, -0.36158125, 0.10751637],
                       [0.63730302, 0.40737356, 1.60301432, 0.43640163, 0.63307585,
                        2.09601154, 0.06530595, 0.53568774, -0.58012846, 0.0613602],
                       [1.60771977, 0.62515448, 1.43956787, -1.34678859, -1.77865232,
                        0.12730941, -1.26939659, 2.6709809, 1.14339488, -1.09668249],
                       [-0.07778457, -0.96929706, 0.51089356, 0.31530677, 1.48567524,
                        1.728838, -0.3460907, -1.17013176, 0.66200566, -0.38263186],
                       [1.01711299, 0.39998883, 0.71722876, -0.16464814, -0.94203221,
                        -0.78560087, 0.89299323, 2.52822211, 0.67685333, 0.13787931],
                       [0.87527788, -0.34939532, -1.10947237, 0.80183665, 2.31692367,
                        0.04789603, -1.25550983, 0.49292569, 1.94067729, 0.63317945]]),
           np.asarray([[0.71146453, 2.27019374, 1.0006133, 1.98641845, -0.67047773,
                        -0.52500752, -0.75159139, 1.5595478, -1.40359444, 1.96757578],
                       [0.06330355, -0.63465465, 0.97536872, -3.07171229, -0.85686391,
                        -0.63432834, 1.17376393, -1.18634377, 1.50228957, -1.12547851]])
           ]


def sigmoid(z):
    g = 1 / (1 + np.exp(-z))
    return g


def feedforward(X):
    layer1 = sigmoid(weights[0] @ X + bias[0])
    layer2 = sigmoid(weights[1] @ layer1 + bias[1])
    layer3 = sigmoid(weights[2] @ layer2 + bias[2])
    output = sigmoid(weights[3] @ layer3 + bias[3])
    if output[0] >= output[1]:
        return 'lose'
    else:
        return 'win'


# battle1 = np.asarray([1, 0.5, 50, 64, 50, 45, 50, 41, 4, 1, 70, 70, 40, 60, 40, 60])
# battle2 = np.asarray([0.25, 1, 50, 47, 50, 57, 50, 65, 0.5, 1, 60, 50, 150, 50, 150, 60])
# battle3 = np.asarray([2, 2, 91, 90, 72, 90, 129, 108, 0.5, 1, 91, 129, 90, 72, 90, 108])
# battle4 = np.asarray([1, 1, 50, 20, 55, 25, 25, 30, 1, 0.5, 100, 110, 90, 85, 90, 60])
# battle5 = np.asarray([2, 2, 70, 60, 125, 115, 70, 55, 1, 1, 20, 10, 230, 10, 230, 5])
# print(feedforward(battle1))
# print(feedforward(battle2))
# print(feedforward(battle3))
# print(feedforward(battle4))
# print(feedforward(battle5))

type_list = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel',
             'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy']

counter_dict = {'Normal': [1, 1, 1, 1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                'Fighting': [2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5],
                'Flying': [1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 1],
                'Poison': [1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2],
                'Ground': [1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1, 1],
                'Rock': [1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1],
                'Bug': [1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2, 0.5],
                'Ghost': [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1],
                'Steel': [1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 1, 1, 2],
                'Fire': [1, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5, 0.5, 2, 1, 1, 2, 0.5, 1, 1],
                'Water': [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 0.5, 1, 1],
                'Grass': [1, 1, 0.5, 0.5, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 0.5, 1, 1],
                'Electric': [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1],
                'Psychic': [1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 0, 1],
                'Ice': [1, 1, 2, 1, 2, 1, 1, 1, 0.5, 0.5, 0.5, 2, 1, 1, 0.5, 2, 1, 1],
                'Dragon': [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 0],
                'Dark': [1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5],
                'Fairy': [1, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 2, 2, 1]
                }


def formFeatures(p1_info, p2_info):
    p1_type1 = p1_info['Type1']
    if p1_info['Type2'] not in type_list:
        p1_type2 = p1_type1
    else:
        p1_type2 = p1_info['Type2']

    p2_type1 = p2_info['Type1']
    if p2_info['Type2'] not in type_list:
        p2_type2 = p2_type1
    else:
        p2_type2 = p2_info['Type2']

    counter1 = counter_dict['{}'.format(p1_type1)][type_list.index('{}'.format(p2_type1))] * \
               counter_dict['{}'.format(p1_type1)][type_list.index('{}'.format(p2_type2))]
    counter2 = counter_dict['{}'.format(p1_type2)][type_list.index('{}'.format(p2_type2))] * \
               counter_dict['{}'.format(p1_type2)][type_list.index('{}'.format(p2_type2))]
    counter3 = counter_dict['{}'.format(p2_type1)][type_list.index('{}'.format(p1_type1))] * \
               counter_dict['{}'.format(p2_type1)][type_list.index('{}'.format(p1_type2))]
    counter4 = counter_dict['{}'.format(p2_type2)][type_list.index('{}'.format(p1_type1))] * \
               counter_dict['{}'.format(p2_type2)][type_list.index('{}'.format(p1_type2))]

    features = np.asarray([counter1, counter2, p1_info['{}'.format('HP')], p1_info['{}'.format('Attack')],
                           p1_info['{}'.format('Defense')], p1_info['{}'.format('Sp_Atk')],
                           p1_info['{}'.format('Sp_Def')], p1_info['{}'.format('Speed')],
                           counter3, counter4, p2_info['{}'.format('HP')], p2_info['{}'.format('Attack')],
                           p2_info['{}'.format('Defense')], p2_info['{}'.format('Sp_Atk')],
                           p2_info['{}'.format('Sp_Def')], p2_info['{}'.format('Speed')]
                           ])
    return features


# mega_x= {'ID': 8, 'Name': 'Mega Charizard X', 'rename': 'megacharizardx', 'Type1': 'Fire', 'Type2': 'Dragon', 'HP': 78, 'Attack': 130, 'Defense': 111, 'Sp_Atk': 130, 'Sp_Def': 85, 'Speed': 100, 'Generation': 1, 'Legendary': 'False'}
# Victreebel={'ID': 78, 'Name': 'Victreebel', 'rename': 'victreebel', 'Type1': 'Grass', 'Type2': 'Poison', 'HP': 80, 'Attack': 105, 'Defense': 65, 'Sp_Atk': 100, 'Sp_Def': 70, 'Speed': 70, 'Generation': 1, 'Legendary': 'False'}
# print(formFeatures(mega_x, Victreebel))

def prediction(info1, info2):
    features = formFeatures(info1, info2)
    return feedforward(features)

def soloResult(X):
    result = feedforward(X)
    if result == 'win':
        return 1
    else:
        return 0

def predict_wins(Team1Poke1, Team1Poke2, Team1Poke3, Team2Poke1, Team2Poke2, Team2Poke3):
    team1_list = [Team1Poke1, Team1Poke2, Team1Poke3]
    team2_list = [Team2Poke1, Team2Poke2, Team2Poke3]
    team1 = list(permutations(team1_list, 3))
    for i in range(len(team1)):
        team1[i] = list(team1[i])
    team2 = list(permutations(team2_list, 3))
    for i in range(len(team2)):
        team2[i] = list(team2[i])

    team = []
    for i in range(len(team1)):
        for j in range(len(team2)):
            team.append(team1[i] + team2[j])

    win_rates = []
    wins = []
    results = []
    teams = []
    w = [6, 6, 6, 6, 6, 6]  ########initial weights
    for k in range(6):
        test = team[6 * k:6 * (k + 1)]
        result = []
        win = []
        for i in range(len(test)):
            inputs = test[i][0:3]
            if inputs not in teams:
                teams.append(inputs)

            for j in range(3):
                example = formFeatures(test[i][j], test[i][j + 3])
                output = soloResult(example)
                result.append(output)
            results.append([result[0], result[1], result[2]])
            if np.sum(result) > 1:
                win.append(1)
                w[i] = w[i] - 1
            else:
                win.append(0)
                w[i] = w[i] + 1
        wins.append([win[0], win[1], win[2], win[3], win[4], win[5]])
        win_rate = np.sum(np.array(win) * np.array(w)) / np.sum(w)
        win_rates.append(win_rate)

    return teams, win_rates


def sorted_win_rate(order, output):
    orders = order.copy()
    order_with_win_rate = []
    for i in range(len(output)):
        order_with_win_rate.append([orders[i], output[i]])
    order_with_win_rate = sorted(order_with_win_rate, key = lambda x:x[1])

    for i in range(len(output)):
        orders[i] = order_with_win_rate[i][0]
        output[i] = order_with_win_rate[i][1]

    return orders, output


def plot_win_rate(sorted_win_rate):
    x = ['order 6', 'order 5', 'order 4', 'order 3', 'order2', 'order 1', ]
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.barh(np.arange(6), sorted_win_rate)
    ax.set_yticks(np.arange(6))
    ax.set_yticklabels(x)
    plt.savefig("static/images/win_rates_hist.png")
    return