import random  
import numpy as np

class Chinese_poker:
    def __init__(self, total_num_of_cards, num_ofcards_per_person, num_of_players):
        
        '''
        total_num_of_cards     : total number of poker cards.
        num_ofcards_per_person : number of cards per person
        num_of_players         : number of players.
        pot_card               : 彩金
        self.hand_cards      : 玩家手上的牌
        card_list              : [1 ~ 52] or [1 ~ 52+13].

        '''

        self.total_num_of_cards     = int(total_num_of_cards)
        self.num_ofcards_per_person = int(num_ofcards_per_person)
        self.num_of_players         = int(num_of_players)
        self.pot_card               = None
        self.hand_cards             = None
        self.ranks_index            = []
        self.suits_index            = []
        
        if self.total_num_of_cards % 13 == 0:
            self.card_list  = [i for i in range(1, 1 + self.total_num_of_cards)]
        else:
            print('Error! Incorrect number of cards!')
    
    def shuffle(self, pot=None):

        if pot == None:
            random.shuffle(self.card_list)                 # 洗牌
        elif pot == 'choose':
            random.shuffle(self.card_list)                 # 洗牌
            self.pot_card = random.choice(self.card_list)  # 選出彩金鋪克牌
        elif pot == 'take':
            random.shuffle(self.card_list)                 # 洗牌
            self.pot_card = random.choice(self.card_list)  # 選出彩金鋪克牌
            self.card_list.remove(self.pot_card)           # 且將彩金鋪克牌「抽出」
        else:
            print('pot only equal string choose or take')

    def dealing_cards(self, pot=None):
        '''
        pot = "None, choose, take" only.
        '''
        num_of_players = self.num_of_players
        cards_per      = self.num_ofcards_per_person
        a              = []

        self.shuffle(pot)

        if self.num_of_players * self.num_ofcards_per_person > len(self.card_list):
            print('Error! Incorrect number of cards!')
        else:
            for i in range(self.num_of_players):
                a.append(self.card_list[0 + i * cards_per: cards_per * (i+1)])
            # print(a)
            self.hand_cards= np.array(a)
            # print(self.hand_cards)
            self.hand_cards.sort()                        # 將牌由小到大排列。


    def analysis_cards(self):
        '''
        find ranks numbers.
        鐵支, 三條, 對子.
        '''
        ranks = self.hand_cards % 13

        for i in range(self.num_of_players):

            self.ranks_index.append([])
            for j in range(0, 13):
                self.ranks_index[i].append(j)
                self.ranks_index[i].append(list(ranks[i]).count(j))


        '''
        找出花色
        同花順, 同花.
        '''
        suits = self.hand_cards // 13

        for i in range(self.num_of_players):
            self.suits_index.append([])
            # [1, 2, 3, 4] = ['♠', '♦', '♥', '♣']
            for j in range(1, 5):
                self.suits_index[i].append(j)
                self.suits_index[i].append(list(suits[i]).count(j))



    def straight_flush(self):

        print(self.suits_index)
        for i in range(self.num_of_players):
            for j in range(1,8,2):
                if self.suits_index[i][j] > 4:
                    print(f'player{i+1}: {self.suits_index[i][j-1]}')







C = Chinese_poker(52, 13, 4)
C.dealing_cards(pot=None)
C.analysis_cards()
C.straight_flush()



