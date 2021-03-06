
class PlayerStats:

    def __init__(self, reader):
        self.players = reader.get_players()
        
    def top_scorers_by_nationality(self, nationality):
        filtered = list(filter(lambda player: player.nationality == nationality, self.players))
        filtered.sort(key=lambda player: player.goals + player.assists, reverse=True)

        return filtered