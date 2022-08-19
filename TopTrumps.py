import random
import requests
import openpyxl
from PIL import Image
from termcolor import colored


def choice():
    multiple_choice = []
    for i in range(3):
        random_nos = str(random.randint(1, 151))
        multiple_choice.append(random_nos)
    return multiple_choice


def random_pokemon(id):
    url = f'https://pokeapi.co/api/v2/pokemon/{id}/'
    response = requests.get(url)
    r = response.json()
    return {'name': r['name'],
                'id': r['id'],
                'height': r['height'],
                'weight': r['weight'],
                'b_experience': r['base_experience'],
                'order': r['order']}


def choose_num_from_list():
    a = choice()
    print(a)
    num = ""
    while True:
        num = input(colored("choose a Pokemon number from the above list: ",'magenta',attrs=['bold']))
        if num in a:
            break
        else:
            print(colored("Please a number from the list: ",'red'))

    return num

def run():

    s = ['id', 'height', 'weight', 'b_experience', 'order']
    round = 1
    player_score = 0
    opponent_score = 0
    high_score = 0
    turn = True
    for i in range(2):
           my_num = choose_num_from_list()
           my_pokemon_card = random_pokemon(my_num)
           print ('My Pokemon card is : ', my_pokemon_card['name'])
           opp_num = choose_num_from_list()
           opp_pokemon_card  = random_pokemon(opp_num)
           print('Opponent Pokemon card is : ', opp_pokemon_card['name'])
           stat_choice=''
           while True:
                if turn:
                   stat_choice = input(colored("My stat choice from (id/height/weight/b_experience/order): ",'yellow')).lower()
                   if stat_choice in s:
                       break

                   else:
                        print(colored("Enter an option from the list: ",'red'))

                else:
                   stat_choice = random.choice((s))
                   break
           my_stat = my_pokemon_card[stat_choice]
           print('The stat choice is: ', stat_choice)
           opp_stat = opp_pokemon_card[stat_choice]
           if my_stat > opp_stat:
               print(colored("You won this round. ",'cyan',attrs=['bold']))
               player_score += 1
               turn = True
           elif my_stat < opp_stat:
               print(colored("Opponent won this round. ",'cyan',attrs=['bold']))
               turn = False
               opponent_score += 1
           else:
               print(colored("This game is draw. ", 'yellow'))
    round += 1
    if player_score > opponent_score:
        print(colored("Player won the Game",'red',attrs=['bold']))
        high_score = player_score
    elif player_score < opponent_score:
        print(colored("Opponent won the Game",'red',attrs=['bold']))
        high_score = opponent_score
    else:
        print(colored('Its a tie. ','red',attrs=['bold']))
        high_score = opponent_score = player_score

    print('Player Score: ', player_score)
    print('Opponent Score: ', opponent_score)
    print('High score: ', high_score)
    print("Number of rounds: ", round)
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = 'Player Score'
    sheet['B1'] = 'Opponent Score'
    sheet['A2'] = player_score
    sheet['B2'] = opponent_score
    sheet['A4'] = "Total number of rounds: " + str(round)
    sheet['A5'] = "High score : " + str(high_score)
    wb.save('score.xlsx')

    return

print(colored("Welcome to the Pokemon Trump card game. ",'blue'))
run()

while True:
    game = input(colored("Do you want to play again ? (Y/N): ",'green'))
    if game.upper() == 'Y':
        run()
    elif game.upper() == 'N':
        img = Image.open('pokemon.jpg')
        img.show()
        break
    else:
        print(colored("Please select between Y or N",'red'))