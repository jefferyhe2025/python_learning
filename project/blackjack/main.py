from project.blackjack.models.player import Player,Dealer
from project.blackjack.models.deck import Deck
from project.blackjack.ui.console import ConsoleUI
from project.blackjack.game.blackjack import BlackJackGame

INITIAL_CHIPS = 1000

def main():
    player = Player('张三',chips=INITIAL_CHIPS)
    dealer = Dealer()
    deck = Deck()
    ui = ConsoleUI()

    game = BlackJackGame(deck,player,dealer,ui)
    game.run()

if __name__ == "__main__":
    main()