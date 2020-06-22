#!/usr/bin/env python3
import os

print('''

         B O L L Y W O O D

        [Format of the Game]

               |
          HERO | HEROINE
        _______|________
               |
         MOVIE |  SONG
               |           ''')
def remove_boll(list):
    list.remove(list[0])
    print(list)

player1=input("Please enter the first player Name: (ask the question) ")
player2=input("Please enter the second player Name: (answerer) ")

question=input('''player 1 will ask the question to player 2.
                  PRESS 1 continue

                  Please enter here: ''')
if question=="1":
    print("OK! {} be carefull of the spellings. ".format(player1))
    movie=input("MOVIE NAME: ").upper()
    hero=input("NAME OF HERO: ").upper()
    heroine=input("NAME OF HEROINE: ").upper()
    song=input("NAME OF SONG: ").upper()
    os.system("clear")
    player_2_score=["B","O","L","L","Y","W","O","O","D"]
    player_2_win=["movie","hero","heroine","song"]
    print("BOLLYWOOD")
    print('''


                   |
               {}   |   {}
            _______|________
                   |
               {}   |   {}
                   |           '''.format(hero[0], heroine[0], movie[0], song[0]))
    print("now your turn {}, ALL THE BEST !".format(player2))
    while player_2_score!=[]:
        guess_coloum=input('''What would you like to guess:
                       PRESS "M" for movie
                       PRESS "H" for hero
                       PRESS "HR" for heroine
                       PRESS "S" for song
                       ENTER YOUR CHOICE HERE:    ''')
        if player_2_win==[]:
            print("YOU WON")
            break
        elif guess_coloum.upper()=="M":
            guess=input("Guess the movie name: ").upper()
            if guess==movie:
                print("correct !")
                player_2_win.remove("movie")

            else:
                print("not correct, try again")
                remove_boll(player_2_score)
        elif guess_coloum.upper()=="H":
            guess=input("Guess the name of hero: ").upper()
            if guess==hero:
                print("correct !")
                player_2_win.remove("hero")
            else:
                print("not correct, try again")
                remove_boll(player_2_score)
        elif guess_coloum.upper()=="HR":
            guess=input("Guess the name of heroine: ").upper()
            if guess==heroine:
                print("correct !")
                player_2_win.remove("heroine")
            else:
                print("not correct, try again")
                remove_boll(player_2_score)
        elif guess_coloum.upper()=="S":
            guess=input("Guess the song: ").upper()
            if guess==song:
                print("correct !")
                player_2_win.remove("song")
            else:
                print("not correct, try again")
                remove_boll(player_2_score)
        else:
            remove_boll(player_2_score)
    if player_2_win!=[]:
        print("YOU LOST")
