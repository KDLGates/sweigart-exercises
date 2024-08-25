def rps_winner(player1: str, player2: str) -> str:
    """
    Simulates a rock paper scissors game for two players with input strings
    of 'rock', 'paper', or 'scissors'. Returns the winner as
    'player one', 'player two', or 'tie'.
    """
    match player1:
        case 'rock':
            if player2 == 'rock':
                return 'tie'
            elif player2 == 'paper':
                return 'player two'
            elif player2 == 'scissors':
                return 'player one'
        case 'paper':
            if player2 == 'rock':
                return 'player one'
            elif player2 == 'paper':
                return 'tie'
            elif player2 == 'scissors':
                return 'player two'
        case 'scissors':
            if player2 == 'rock':
                return 'player two'
            elif player2 == 'paper':
                return 'player one'
            elif player2 == 'scissors':
                return 'tie'
        case _:
            return ValueError("Input for each player must be 'rock', 'player' or 'scissors'.")

assert rps_winner('rock', 'paper') == 'player two'
assert rps_winner('rock', 'scissors') == 'player one'
assert rps_winner('paper', 'scissors') == 'player two'
assert rps_winner('paper', 'rock') == 'player one'
assert rps_winner('scissors', 'rock') == 'player two'
assert rps_winner('scissors', 'paper') == 'player one'
assert rps_winner('rock', 'rock') == 'tie'
assert rps_winner('paper', 'paper') == 'tie'
assert rps_winner('scissors', 'scissors') == 'tie'