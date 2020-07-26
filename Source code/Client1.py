__author__ = 'fyt'

import socket
import random
import ClientBase
import collections

# IP address and port
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

# Agent
POKER_CLIENT_NAME = 'Abdul'
CURRENT_HAND = []


class pokerGames(object):
    def __init__(self):
        self.PlayerName = POKER_CLIENT_NAME
        self.Chips = 0
        self.CurrentHand = []
        self.Ante = 0
        self.playersCurrentBet = 0


'''
* Gets the name of the player.
* @return  The name of the player as a single word without space. <code>null</code> is not a valid answer.
'''


def queryPlayerName(_name):
    if _name is None:
        _name = POKER_CLIENT_NAME
    return _name


def infoCardsInHand(_hand):
    global hand
    hand = _hand[-5:]
    strength = strength_of_hand(hand)
    print(strength)


'''
* Modify queryOpenAction() and add your strategy here
* Called during the betting phases of the game when the player needs to decide what open
* action to choose.
* @param minimumPotAfterOpen   the total minimum amount of chips to put into the pot if the answer action is
*                              {@link BettingAnswer#ACTION_OPEN}.
* @param playersCurrentBet     the amount of chips the player has already put into the pot (dure to the forced bet).
* @param playersRemainingChips the number of chips the player has not yet put into the pot.
* @return                      An answer to the open query. The answer action must be one of
*                              {@link BettingAnswer#ACTION_OPEN}, {@link BettingAnswer#ACTION_ALLIN} or
*                              {@link BettingAnswer#ACTION_CHECK }. If the action is open, the answers
*                              amount of chips in the anser must be between <code>minimumPotAfterOpen</code>
*                              and the players total amount of chips (the amount of chips alrady put into
*                              pot plus the remaining amount of chips).
'''


def queryOpenAction(_minimumPotAfterOpen, _playersCurrentBet, _playersRemainingChips):
    print("Player requested to choose an opening action.")

    r = action()
    if r == 0:
        return ClientBase.BettingAnswer.ACTION_ALLIN
    elif r == 1:
        if _playersCurrentBet + _playersRemainingChips > _minimumPotAfterOpen:
            return ClientBase.BettingAnswer.ACTION_OPEN,  (10 + _minimumPotAfterOpen) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumPotAfterOpen else _minimumPotAfterOpen
    elif r == 2:
        if _playersCurrentBet + _playersRemainingChips > _minimumPotAfterOpen:
            return ClientBase.BettingAnswer.ACTION_OPEN,  (9 + _minimumPotAfterOpen) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumPotAfterOpen else _minimumPotAfterOpen
    elif r == 3:
        if _playersCurrentBet + _playersRemainingChips > _minimumPotAfterOpen:
            return ClientBase.BettingAnswer.ACTION_OPEN,  (7 + _minimumPotAfterOpen) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumPotAfterOpen else _minimumPotAfterOpen
    elif r == 4:
        if _playersCurrentBet + _playersRemainingChips > _minimumPotAfterOpen:
            return ClientBase.BettingAnswer.ACTION_OPEN,  (12+ _minimumPotAfterOpen) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumPotAfterOpen else _minimumPotAfterOpen
    elif r == 5:
        if _playersCurrentBet + _playersRemainingChips > _minimumPotAfterOpen:
            return ClientBase.BettingAnswer.ACTION_OPEN,  (8+ _minimumPotAfterOpen) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumPotAfterOpen else _minimumPotAfterOpen
    elif r == 6:
        return ClientBase.BettingAnswer.ACTION_CHECK
    else:
        if _playersCurrentBet + _playersRemainingChips > _minimumPotAfterOpen:
            return ClientBase.BettingAnswer.ACTION_OPEN, (2 + _minimumPotAfterOpen) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumPotAfterOpen else _minimumPotAfterOpen
        else:
            return ClientBase.BettingAnswer.ACTION_CHECK


'''
* Modify queryCallRaiseAction() and add your strategy here
* Called during the betting phases of the game when the player needs to decide what call/raise
* action to choose.
* @param maximumBet                the maximum number of chips one player has already put into the pot.
* @param minimumAmountToRaiseTo    the minimum amount of chips to bet if the returned answer is {@link BettingAnswer#ACTION_RAISE}.
* @param playersCurrentBet         the number of chips the player has already put into the pot.
* @param playersRemainingChips     the number of chips the player has not yet put into the pot.
* @return                          An answer to the call or raise query. The answer action must be one of
*                                  {@link BettingAnswer#ACTION_FOLD}, {@link BettingAnswer#ACTION_CALL},
*                                  {@link BettingAnswer#ACTION_RAISE} or {@link BettingAnswer#ACTION_ALLIN }.
*                                  If the players number of remaining chips is less than the maximum bet and
*                                  the players current bet, the call action is not available. If the players
*                                  number of remaining chips plus the players current bet is less than the minimum
*                                  amount of chips to raise to, the raise action is not available. If the action
*                                  is raise, the answers amount of chips is the total amount of chips the player
*                                  puts into the pot and must be between <code>minimumAmountToRaiseTo</code> and
*                                  <code>playersCurrentBet+playersRemainingChips</code>.
'''


def queryCallRaiseAction(_maximumBet, _minimumAmountToRaiseTo, _playersCurrentBet, _playersRemainingChips):
    print("Player requested to choose a call/raise action.")

    r = action()
    if r == 0:
        return ClientBase.BettingAnswer.ACTION_ALLIN
    elif r == 1:
        if _playersCurrentBet + _playersRemainingChips > _minimumAmountToRaiseTo:
            return ClientBase.BettingAnswer.ACTION_RAISE,  (10 + _minimumAmountToRaiseTo) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumAmountToRaiseTo else _minimumAmountToRaiseTo
    elif r == 2:
        if _playersCurrentBet + _playersRemainingChips > _minimumAmountToRaiseTo:
            return ClientBase.BettingAnswer.ACTION_RAISE,  (9 + _minimumAmountToRaiseTo) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumAmountToRaiseTo else _minimumAmountToRaiseTo
    elif r == 3:
        if _playersCurrentBet + _playersRemainingChips > _minimumAmountToRaiseTo:
            return ClientBase.BettingAnswer.ACTION_RAISE,  (7 + _minimumAmountToRaiseTo) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumAmountToRaiseTo else _minimumAmountToRaiseTo
    elif r == 4:
        if _playersCurrentBet + _playersRemainingChips > _minimumAmountToRaiseTo:
            return ClientBase.BettingAnswer.ACTION_RAISE,  (12 + _minimumAmountToRaiseTo) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumAmountToRaiseTo else _minimumAmountToRaiseTo
    elif r == 5:
        if _playersCurrentBet + _playersRemainingChips > _minimumAmountToRaiseTo:
            return ClientBase.BettingAnswer.ACTION_RAISE,  (8 + _minimumAmountToRaiseTo) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumAmountToRaiseTo else _minimumAmountToRaiseTo
    elif r == 6:
        return ClientBase.BettingAnswer.ACTION_FOLD

    else:
        return ClientBase.BettingAnswer.ACTION_CALL if _playersCurrentBet + _playersRemainingChips > _maximumBet else ClientBase.BettingAnswer.ACTION_FOLD


def strength_of_hand(current_hand):
    print (current_hand)
    hand_string = ''.join(current_hand)
    element_list = list(hand_string)
    suits = element_list[1::2]
    card_rank = element_list[0::2]
    #print (suits)
    #print (card_rank)
    for i, num in enumerate(card_rank):
        if num == "A":
            card_rank[i] = '14'
        elif num == "K":
            card_rank[i] = '13'
        elif num == "Q":
            card_rank[i] = '12'
        elif num == "J":
            card_rank[i] = '11'
        elif num == "T":
            card_rank[i] = '10'

    number_of_distinct_cards = collections.defaultdict(int)
    number_of_distinct_suits = collections.defaultdict(int)
    for i in card_rank:
        number_of_distinct_cards[i] += 1
    for j in suits:
        number_of_distinct_suits[j] += 1

    print (number_of_distinct_cards)
    print (number_of_distinct_suits)

    # print(max(card_rank))
    # print(min(card_rank))

    # 4-of-a-kind

    if len(number_of_distinct_cards) == 2:
        if 4 in number_of_distinct_cards.values():
            rank = "Four-of-a-kind"
            print(rank)
            return rank

    # Full house

    elif len(number_of_distinct_cards) == 2:
        if 3 in number_of_distinct_cards.values() and 2 in number_of_distinct_cards.values():
            rank = "Full-House"
            print(rank)
            return rank

    # flush

    elif len(number_of_distinct_suits) == 1:
        if 5 in number_of_distinct_suits.values():
            rank = "Flush"
            print(rank)
            return rank

    # 3-of-a-kind

    elif len(number_of_distinct_cards) == 3:
        if 3 in number_of_distinct_cards.values():
            rank = "Three-of-a-kind"
            print(rank)
            return rank

    # 2 Pair

    elif len(number_of_distinct_cards) == 3:
        if 2 in number_of_distinct_cards.values():
            rank = "Two-Pair"
            print(rank)
            return rank


    # 1 Pair

    elif len(number_of_distinct_cards) == 4:
        if 2 in number_of_distinct_cards.values():
            rank = "One-Pair"
            print(rank)
            return rank

    # High Card

    elif len(number_of_distinct_cards) == 5:
        my_cards = number_of_distinct_cards.keys()
        for i in my_cards:
            if i == '14':
                rank = "High Card"
                print (rank)
                return rank
            elif i == '13':
                rank = "High Card"
                print (rank)
                return rank

    # straight

    elif len(number_of_distinct_cards) == 5:

        max_val = max(card_rank)
        min_val = min(card_rank)
        if int(max_val) - int(min_val) == 4:
            rank = "Straight"
            print(rank)
            return rank
    else:
        rank = "Nothing"
        print (rank)
        return rank

def action():
    r = strength_of_hand(hand)
    if r == "Four-of-a-kind":
        return 0
    elif r == "Full-House" or r == "Flush":
        return 1
    elif r == "Straight":
        return 2
    elif r == "Three-of-a-kind" or r == "Two-Pair":
        return 3
    elif r == "One-Pair":
        return 4
    elif r == "High Card":
        return 5
    else:
        return 6

'''
* Modify queryCardsToThrow() and add your strategy to throw cards
* Called during the draw phase of the game when the player is offered to throw away some
* (possibly all) of the cards on hand in exchange for new.
* @return  An array of the cards on hand that should be thrown away in exchange for new,
*          or <code>null</code> or an empty array to keep all cards.
* @see     #infoCardsInHand(ca.ualberta.cs.poker.Hand)
'''


def queryCardsToThrow(_hand):
    print("Requested information about what cards to throw")
    print(_hand)
    global new_hand
    x = action()
    if x == 0 or x == 1 or x == 2:
        return ' '
    elif x == 6:
        new_hand.append(_hand)
        return new_hand
    else:
        return _hand[random.randint(0, 4)] + ' '

# InfoFunction:

'''
* Called when a new round begins.
* @param round the round number (increased for each new round).
'''
def infoNewRound(_round):
    #_nrTimeRaised = 0
    print('Starting Round: ' + _round )

'''
* Called when the poker server informs that the game is completed.
'''
def infoGameOver():
    print('The game is over.')

'''
* Called when the server informs the players how many chips a player has.
* @param playerName    the name of a player.
* @param chips         the amount of chips the player has.
'''
def infoPlayerChips(_playerName, _chips):
    print('The player ' + _playerName + ' has ' + _chips + 'chips')

'''
* Called when the ante has changed.
* @param ante  the new value of the ante.
'''
def infoAnteChanged(_ante):
    print('The ante is: ' + _ante)

'''
* Called when a player had to do a forced bet (putting the ante in the pot).
* @param playerName    the name of the player forced to do the bet.
* @param forcedBet     the number of chips forced to bet.
'''
def infoForcedBet(_playerName, _forcedBet):
    print("Player "+ _playerName +" made a forced bet of "+ _forcedBet + " chips.")


'''
* Called when a player opens a betting round.
* @param playerName        the name of the player that opens.
* @param openBet           the amount of chips the player has put into the pot.
'''
def infoPlayerOpen(_playerName, _openBet):
    print("Player "+ _playerName + " opened, has put "+ _openBet +" chips into the pot.")

'''
* Called when a player checks.
* @param playerName        the name of the player that checks.
'''
def infoPlayerCheck(_playerName):
    print("Player "+ _playerName +" checked.")

'''
* Called when a player raises.
* @param playerName        the name of the player that raises.
* @param amountRaisedTo    the amount of chips the player raised to.
'''
def infoPlayerRise(_playerName, _amountRaisedTo):
    print("Player "+_playerName +" raised to "+ _amountRaisedTo+ " chips.")

'''
* Called when a player calls.
* @param playerName        the name of the player that calls.
'''
def infoPlayerCall(_playerName):
    print("Player "+_playerName +" called.")

'''
* Called when a player folds.
* @param playerName        the name of the player that folds.
'''
def infoPlayerFold(_playerName):
    print("Player "+ _playerName +" folded.")

'''
* Called when a player goes all-in.
* @param playerName        the name of the player that goes all-in.
* @param allInChipCount    the amount of chips the player has in the pot and goes all-in with.
'''
def infoPlayerAllIn(_playerName, _allInChipCount):
    print("Player "+_playerName +" goes all-in with a pot of "+_allInChipCount+" chips.")

'''
* Called when a player has exchanged (thrown away and drawn new) cards.
* @param playerName        the name of the player that has exchanged cards.
* @param cardCount         the number of cards exchanged.
'''
def infoPlayerDraw(_playerName, _cardCount):
    print("Player "+ _playerName + " exchanged "+ _cardCount +" cards.")

'''
* Called during the showdown when a player shows his hand.
* @param playerName        the name of the player whose hand is shown.
* @param hand              the players hand.
'''
def infoPlayerHand(_playerName, _hand):
    print("Player "+ _playerName +" hand " + str(_hand))

'''
* Called during the showdown when a players undisputed win is reported.
* @param playerName    the name of the player whose undisputed win is anounced.
* @param winAmount     the amount of chips the player won.
'''
def infoRoundUndisputedWin(_playerName, _winAmount):
    print("Player "+ _playerName +" won "+ _winAmount +" chips undisputed.")

'''
* Called during the showdown when a players win is reported. If a player does not win anything,
* this method is not called.
* @param playerName    the name of the player whose win is anounced.
* @param winAmount     the amount of chips the player won.
'''
def infoRoundResult(_playerName, _winAmount):
    print("Player "+ _playerName +" won " + _winAmount + " chips.")

