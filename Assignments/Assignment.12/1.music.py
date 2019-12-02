def music_func(music="Classic Rock", group="The Beatles", singer="Freddie Mercury"):
    print("The best type of music is", music)
    print("The best music group is", group)
    print("The best lead vocalist is", singer)



#definition for music_func goes here

def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()

main()







''' Write a function 'music_func' that takes 3 parameters -- music type, 
music group, vocalist -- and prints them all out as shown in the example below. 
In case no input is provided by the user, the function should assume these default 
values for the parameters: "Classic Rock", "The Beatles", "Freddie Mercury".'''