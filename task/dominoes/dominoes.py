# Write your code here
import random

domino = [[i, k] for k in range(7) for i in range(k + 1)]
def domino_start(lst):
	while True:
		random.shuffle(lst)
		p = lst[:7]
		c = lst[7:14]
		dom = lst[14:]
		p_max = max((filter(lambda x: x[0] == x[1], p)), key=sum, default=[-1, -1])
		c_max = max(filter(lambda x: x[0] == x[1], c), key=sum, default=[-1, -1])
		if p_max != c_max and p_max > c_max:
			s = p.pop(p.index(p_max))
			break
		elif p_max != c_max and p_max < c_max:
			s = c.pop(c.index(c_max))
			break
		else:
			continue
	if len(p) > len(c):
		status = "player"
	else:
		status = "computer"
	return p, c, s, dom, status #возвращает список, где p - костяшки player, c - костяшки computer, s - стартовая костяшка, dom - неизраскодованные костяшки

def draw(domino_snake_def):
	if domino_snake_def[0][0] == domino_snake_def[-1][1]:
		s = ''
		for i in domino_snake_def:
			for k in i:
				if k == domino_snake_def[0][0]:
					s += str(k)
	if len(s) >= 8:
		return 'draw'



def interface(stock_def, computer_def, domino_snake_def, player_def, status_def):
    print('=' * 70)
    print(f"Stock size: {len(stock_def)}")
    print(f'Computer pieces: {len(computer_def)}')
    print()
    if len(domino_snake_def) <= 6:
        print(*domino_snake_def, sep='')
    else:
        print(*domino_snake_def[:3], '...', *domino_snake_def[-3:], sep='')
    print()
    print("Your pieces:")
    for i in range(1, len(player_def) + 1):
        print(f'{i}:{player_def[i-1]}')
    print()


def is_win(player_def, computer_def, domino_snake_def, status, stok):
    if len(player_def) == 0:
        return 'player'
    elif len(computer_def) == 0:
        return 'computer'
    elif domino_snake_def[0][0] == domino_snake_def[-1][1]:
    	s = ''
    	for i in domino_snake_def:
    		for k in i:
    			if k == domino_snake_def[0][0]:
    				s += str(k)
    	if len(s) >= 8:
    		return 'draw'
    elif len(stok) == 0 and status == 'player':
        if len([s for s in player_def if domino_snake_def[0][0] in s or domino_snake_def[-1][1] in s]) < 1:
            return 'draw'
    elif len(stok) == 0 and status == 'computer':
        if len([s for s in computer_def if domino_snake_def[0][0] in s or domino_snake_def[-1][1] in s]) < 1:
            return 'draw'


def make_move(stock, character, domino_snake, choice):
    if choice > 0:
        temp = character.pop(choice - 1)
        domino_snake.append(temp)
    elif choice < 0:
        temp = character.pop(- choice - 1)
        domino_snake.insert(0, temp)
    else:
        if len(stock) > 0:
            character.append(stock.pop())

def command_num():
	 	while True:
	 	    try:
	 	    	num = int(input())
	 	    except ValueError:
	 	        print('Invalid input. Please try again.')
	 	        continue
	 	    else:
	 	         if -len(player) <= num <= len(player):
	 	         	return num
	 	         else:
	 	         	print('Invalid input. Please try again.')
	 	         	continue

def make_move1(stock, character, domino_snake):
    while True:
	 	    choice = input()
	 	    if 0 < len(choice) < 3 and choice.isdigit and -len(character) <= int(choice) <= len(character):
	 	        choice = int(choice)
	 	        if choice > 0:
	 	         	if domino_snake[-1][1] == character[choice-1][0]:
	 	         		temp = character.pop(choice - 1)
	 	         		domino_snake.append(temp)
	 	         		break
	 	         	elif domino_snake[-1][1] == character[choice-1][1]:
	 	         		temp = character.pop(choice - 1)[::-1]
	 	         		domino_snake.append(temp)
	 	         		break
	 	         	else:
	 	         		print('Illegal move. Please try again.')
	 	         		continue
	 	        elif choice < 0:
	 	         	if domino_snake[0][0] == character[-choice-1][1]:
	 	         		temp = character.pop(- choice - 1)
	 	         		domino_snake.insert(0, temp)
	 	         		break
	 	         	elif domino_snake[0][0] == character[-choice-1][0]:
	 	         		temp = character.pop(-choice -1)[::-1]
	 	         		domino_snake.insert(0, temp)
	 	         		break
	 	         	else:
	 	         		print('Illegal move. Please try again.')
	 	         		continue
	 	        else:
	 	         	if len(stock) > 0:
	 	         		character.append(stock.pop())
	 	         		break
	 	    else:
	 	      	print('Invalid input. Please try again.')

def make_move2(stock, computer, domino_snake):
    left = domino_snake[0][0]
    raight = domino_snake[-1][1]
    d = {}
    for i in domino_snake:
        for k in i:
           d[k] = d.get(k, 0) + 1
    for i in computer:
        for k in i:
            d[k] = d.get(k, 0) + 1
    score = {}
    count = 0
    count_l = 0
    for i in computer:
        score[count] = d[i[0]] + d[i[1]]
        count += 1
    l = sorted(score.items(), key=lambda x: x[1], reverse=True)
    for i, k in l:
        if left in computer[i]:
            temp = computer[i]
            if temp[1] == left:
                domino_snake.insert(0, temp)
                del computer[i]
                break
            else:
                domino_snake.insert(0, temp[::-1])
                del computer[i]
                break
        elif raight in computer[i]:
            temp = computer[i]
            if temp[0] == raight:
                domino_snake.append(temp)
                del computer[i]
                break
            else:
                domino_snake.append(temp[::-1])
                del computer[i]
                break
        else:
            count_l += 1
    if count_l == len(l):
        if len(stock) > 0:
            computer.append(stock.pop())


player, computer, start_snake, stock, status = domino_start(domino)
domino_snake= []
domino_snake.append(start_snake)

random.seed()


while True:
    left_num = domino_snake[0][0]
    raigt_num = domino_snake[-1][-1]
    interface(stock, computer, domino_snake, player, status)
    winner = is_win(player, computer, domino_snake, status, stock)
    if winner == 'player':
    	print('Status: The game is over. You won!')
    	break
    elif winner == 'computer':
    	print('Status: The game is over. The computer won!')
    	break
    elif winner == 'draw':
	    print("Status: The game is over. It's a draw!")
	    break
    else:
            if status == 'player':
            	print("\nIt's your turn to make a move. Enter your command.")
            	make_move1(stock, player, domino_snake)
            	status = 'computer'
            else:
            	command = input("\nStatus: Computer is about to make a move. Press Enter to continue...")
            	#command = random.randint(-len(computer), len(computer))
            	make_move2(stock, computer, domino_snake)
            	status = "player"




#print(f"Stock pieces: {stock}")
#print(f"Computer pieces: {computer}")
#print(f"Player pieces: {player}")
#print(f"Domino snake: {domino_snake}")
#print(f"Status: {status}")



