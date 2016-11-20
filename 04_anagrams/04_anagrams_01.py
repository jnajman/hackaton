try:
    f=open("words.txt",'r')
    dictionary = f.read().splitlines()
    # print(f.readlines())
    # print(dictionary)

    myword='tea'

    # print(len(dictionary[20]))
    # print(dictionary[12359])
    # alph_dict = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
    # print(alph_dict)


    # print(dictionary[0][3])

    myword_len=len(myword)
    # print(myword_len)

    myword_alph_dict=dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
    # print(myword_alph_dict.keys())

    for i in range(myword_len):
        myword_alph_dict[myword[i]] += 1

    # print(myword_alph_dict)


    dictionary_len=len(dictionary)

    for j in range(dictionary_len):
        if myword_len==len(dictionary[j]):
            newword_alph_dict = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
            for k in range(len(dictionary[j])):
                newword_alph_dict[dictionary[j][k]] += 1
            if myword_alph_dict==newword_alph_dict:
                print(dictionary[j])

finally:
    f.close()