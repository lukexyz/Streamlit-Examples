import pandas as pd
import numpy as np
import random
import time


class QuickShot(): 
    """
    QuickShot Badminton Simulator 2k20®
        Calculates the win_rate of players based on their serving win_probablity
    """
    TARGET_SETS = 2
    TARGET_GAMES = 6
    TARGET_POINTS = 4
    
    def __init__(self, player1, player2, verbose=True, coin_toss=True):
        if verbose: print('QuickShot match initiated...')
        self.p1 = player1
        self.p2 = player2
        self.verbose = verbose
        self.match_length = 0

        # Throw shuttle to see who serves first:
        players = [self.p1, self.p2]
        if coin_toss: random.shuffle(players)
        self.server, self.reciever = players
        if verbose: 
            print(f"\n{' ' + self.server.name + ' to Serve First ':=^50}\n")
            print(f'Score format [points, games, sets, match]\n')
        
        self.display_score()

    def play_match(self):
        p1, p2 = self.p1, self.p2
        while (p1.score[2] < self.TARGET_SETS) and (p2.score[2] < self.TARGET_SETS) \
               or (abs(p1.score[2] - p2.score[2]) < 2):
            self.play_set()
        
        if p1.score[2] > p2.score[2]:
            p1.score[3] += 1
            winner, loser = p1, p2
        else:
            p2.score[3] += 1
            winner, loser = p2, p1

        if self.verbose: 
            print(f'Final ', end='')
            self.display_score(end='\n')
            print(f'\nMatch won by {winner.name}! ({winner.score[2]} sets to {loser.score[2]})')
            print(f'Match length: {self.match_length} points')
        if not self.verbose: return winner.name, self.match_length
        
    def play_set(self):
        p1, p2 = self.p1, self.p2
        p1.score[1], p2.score[1] = 0, 0
        while (p1.score[1] < self.TARGET_GAMES) and (p2.score[1] < self.TARGET_GAMES) \
               or (abs(p1.score[1] - p2.score[1]) < 2): 
            self.play_game()

        if p1.score[1] > p2.score[1]:
            p1.score[2] += 1
            winner = p1
        else:
            p2.score[2] += 1
            winner = p2
            
        self.display_score()
        if self.verbose: print(f'\n\n\t\t Set won by {winner.name}!\n\n')
        
    def play_game(self):
        p1, p2 = self.p1, self.p2
        p1.score[0], p2.score[0] = 0, 0
        
        while (p1.score[0] < self.TARGET_POINTS) and (p2.score[0] < self.TARGET_POINTS):
            self.play_point()
        
        if p1.score[0] > p2.score[0]:
            p1.score[1] += 1
        else:
            p2.score[1] += 1
            
        self.display_score()
        self.server, self.reciever = self.reciever, self.server
        
    def play_point(self):
        server_win = random.uniform(0, 1) < self.server.win_prob
        if server_win: 
            self.server.score[0] += 1
        else:
            self.reciever.score[0] += 1
        
        self.match_length += 1
        self.display_score()
            
    def display_score(self, end='\r'):
        if self.verbose:
            p1, p2 = self.p1, self.p2
            print(f'🏸 Score: {p1.name} {p1.score} - {p2.score} {p2.name}', end=end)
            time.sleep(0.05)


class Player():
    def __init__(self, name, serve_win):
        self.name = name
        self.win_prob = serve_win
        self.score = [0, 0, 0, 0]  # point, game, set, match


def simulator(p=0.65, q=0.55, n=100):
    """
    The simulator should take as input the probabilities (p ​and q)​ for each of the two players to win a
    point played when they are serving and return the probability for the first player to win the match
    and the average length of the match
    
    returns:  dict, {p1_win_rate, avg_match_length}
    """ 

    winner, match_length = [], []

    for _ in range(n):
        p1 = Player('Luke', p)
        p2 = Player('Lin Dan', q)
        match = QuickShot(p1, p2, verbose=False, coin_toss=False)

        w, l = match.play_match()
        winner.append(w)
        match_length.append(l)

    # Construct Results Dataframe
    df = pd.DataFrame()
    df['winner'] = winner
    df['match_length'] = match_length
    dx = df.groupby('winner').agg({'winner': "count"})
    dx['win_percentage'] = df.winner.value_counts(normalize=True)
    dx.columns = ['wins', 'win_rate']
    dx.index.name = None
    dx = dx.sort_values('wins', ascending=False)

    print(f'\nAverage match length for all games: {df.match_length.mean():.1f} points\n')
    print(dx)

    p1_win_rate = float(dx[dx.index == p1.name].win_rate)
    avg_match_length = df.match_length.mean()

    return {'p1_win_rate': p1_win_rate, 'avg_match_length': avg_match_length}


if __name__ == '__main__':

    res = simulator(p=0.65, q=0.55, n=10000)
    print('\n', res)
