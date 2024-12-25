import pandas as pd
from enum import Enum
import platform
import os

FILE_NAME = 'diamonds.csv'
df = pd.read_csv(FILE_NAME)



class Actions(Enum):
    HIGHEST_PRICE = 1
    AVERAGE_PRICE = 2
    IDEAL_COUNT = 3
    DIFFERENT_COLORS = 4
    PREMIUM_MEDIAN = 5
    AVERAGE_CARAT_PER_CUT = 6
    AVERAGE_PRICE_PER_COLOR = 7
    EXIT = 8

def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    for act in Actions: 
        print(f"{act.value} - {act.name}" )
    while True:
        try:
            user_select = int(input("What would you like to do? "))
            return int(user_select)
        except ValueError:
            print("Invalid input. Please enter a number.")


def highest_price():
    most_expensive_row = df['price'].max()
    print(f"The most diamond's price is {most_expensive_row}")

def average_price():
    average_price = df['price'].mean()
    print(f'The average price is {average_price}')


def ideal_count():
    cut_row = df['cut'].to_list()
    count = 0
    cut_level = 'Ideal'
    for cut in cut_row:
        if cut == cut_level:
            count += 1
    print(f'There are {count} {cut_level} diamonds in the list')

def different_colors():
    colors = set()
    colors_row = df['color'].to_list()
    for color in colors_row:
        colors.add(color)
    print(f'There are {len(colors)} colors, and the colors are {colors}')

def premium_median():
    specific_cut = 'Premium'  
    filtered_df = df[df['cut'] == specific_cut]
    median_carat = filtered_df['carat'].median()
    print(f"The median carat for {specific_cut} cut is: {median_carat}")


def average_carat_per_cut():
        cuts = set()
        all_cuts = df['cut'].to_list()
        for cut in all_cuts:
            cuts.add(cut)
        for cut in cuts:
            carat_average = df[df['cut'] == cut]
            average = carat_average['carat'].mean()        
            print(f"For {cut}, the average carat is {average}") 
    


def average_price_per_color():
    colors = set()
    all_colors = df['color'].to_list()
    for color in all_colors:
        colors.add(color)
    for color in colors:
        color_average = df[df['color'] == color]
        average = color_average['price'].mean()
        print(f'For {color}, the average price is {average}')


if __name__ == "__main__":
    while True:
        user_select = menu()
        clear_terminal()
        if user_select == Actions.HIGHEST_PRICE.value:
            highest_price()
        elif user_select == Actions.AVERAGE_PRICE.value:
            average_price()
        elif user_select == Actions.IDEAL_COUNT.value:
            ideal_count()
        elif user_select == Actions.DIFFERENT_COLORS.value:
            different_colors()
        elif user_select == Actions.PREMIUM_MEDIAN.value:
            premium_median()
        elif user_select == Actions.AVERAGE_CARAT_PER_CUT.value:
            average_carat_per_cut()
        elif user_select == Actions.AVERAGE_PRICE_PER_COLOR.value:
            average_price_per_color()
        elif user_select == Actions.EXIT.value:
            exit()
        else:
            print("Please selecet a proper action ")



