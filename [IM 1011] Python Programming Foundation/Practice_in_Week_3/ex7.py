# Write a program that allows the user to input 3 movies’ names
# and their ratings (separated by ,)
# and then print the movies’ names
# and their ratings in descending order,
# as well as print out the highest and lowest ratings. (rate:0-10)
#
# IMDb example:
# input
# Top Gun maverick, 8.4
# Nope, 7.0
# Bullet Train, 7.5
#
# output
# Top Gun maverick, 8.4
# Bullet Train, 7.5
# Nope, 7.0
#
# highest: Top Gun maverick, 8.4
# lowest: Nope, 7.0
first_movie_name = input()
first_rate = float(input())
second_movie_name = input()
second_rate = float(input())
third_movie_name = input()
third_rate = float(input())

a = dict(first_movie=[first_movie_name, first_rate],
         second_movie=[second_movie_name, second_rate],
         third_movie=[third_movie_name, third_rate])

# key=lambda movies: movies[1] means name the elements in a.values() 'movies', and then sort 'movies' with movies[1].
sorted_movie_list = sorted(a.values(), key=lambda movies: movies[1], reverse=True)
print(f'The highest rated movie is {sorted_movie_list[0][0]}, whose rate is {sorted_movie_list[0][1]}.', sep='', end='\n')
print(f'The highest rated movie is {sorted_movie_list[2][0]}, whose rate is {sorted_movie_list[2][1]}.', sep='', end='\n')
print(f'{sorted_movie_list[0][0]}, {sorted_movie_list[0][1]}',
      f'{sorted_movie_list[1][0]}, {sorted_movie_list[1][1]}',
      f'{sorted_movie_list[2][0]}, {sorted_movie_list[2][1]}', sep='\n', end='')
