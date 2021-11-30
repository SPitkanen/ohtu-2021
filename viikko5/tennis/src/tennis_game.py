class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            score = self.equal_points(self.m_score1)
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.minus_score(self.m_score1 - self. m_score2)
        else:
            score = self.other_score(score)

        return score

    def equal_points(self, points):
        score_prints = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All"
        }

        score = "Deuce"
        if 0 <= points <= 3:
            score = score_prints.get(points)

        return score

    def minus_score(self, points):
        score_prints = {
            1: "Advantage player1",
            -1: "Advantage player2",
            2: "Win for player1"
        }

        score = "Win for player2"
        if points >= -1:
            if points > 2: points = 2
            score = score_prints.get(points)

        return score

    def other_score(self, score):
        score = score
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                score = score + "-"
                temp_score = self.m_score2

            score_prints = {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty"
            }

            score = score + score_prints.get(temp_score)
        
        return score
