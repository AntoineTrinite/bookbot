with open("books/frankenstein.txt") as f:
    content = f.read()    


def word_counter(content):
    words = content.split()
    word_count = 0

    for word in words:
        word_count += 1
    print(f"number of words : {word_count}")

def character_count(content):
    lowered_content = content.lower()

    lowered_dic_content = {}

    for i in lowered_content:
        if i in lowered_dic_content and i.isalpha():
            lowered_dic_content[i] += 1
        elif i.isalpha():
            lowered_dic_content[i] = 1
    
    list_content = list(lowered_dic_content.items())
    sorted_list_content = sorted(list_content)

    for i in sorted_list_content:
        print(f"The '{i[0]}' character was found {i[1]} times")
        

# ///////////////////////
print('--- Begin report of books/frankenstein.txt ---')
word_counter(content)
print(' ')
character_count(content)
print('--- End report ---')