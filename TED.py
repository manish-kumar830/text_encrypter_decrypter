MCD={
'A':'199',
'B':'55',
'C':'44',
'D':'66',
'E':'e',
'F':'w',
'G':'33',
'H':'34',
'I':'j',
'J':'23',
'K':'00',
'L':'2',
'M':'q',
'N':'3',
'O':'P',
'P':'898',
'Q':'2323',
'R':'545',
'S':'@',
'T':'**',
'U':'___',
'V':'8be',
'W':'@#$',
'X':'&#^',
'Y':'fjdl',
'Z':'298fdj',
'a':'ue98',
'b':'87jf',
'c':'9ee',
'd':'kk',
'e':'2#',
'f':'*%%',
'g':'0u',
'h':'aaa',
'i':'dd',
'j':'@@@',
'k':'+++',
'l':'man',
'm':'uy77',
'n':'88u8',
'o':'2@2@',
'p':'0807',
'q':'hihi',
'r':'nust',
's':'uyy',
't':'ma090',
'u':'rr',
'v':'opo',
'w':'123',
'x':'cvc',
'y':'weu',
'z':'kdk',
'1':'zxzx',
'2':'0k00',
'3':'jmjm',
'4':'~~',
'5':'676',
'6':'&#*#',
'7':'===',
'8':'opop',
'9':'asdf',
'0':'bvb',
'`':'popiu',
'~':'0789',
'!':'he8',
'@':'jfj',
'#':'7y7y',
'$':'b88b',
'%':'9h9h',
'^':'iei',
'&':'9--',
'*':'**8',
'(':'5%%5',
')':'8*#3',
'-':'p0p-',
'_':'u`j`',
'=':'AD',
'+':'QoE',
'\\':'IEIo',
'|':'H8Dj',
'[':'JJj',
'{':'nano',
']':'HHHE',
'}':'URD',
':':'kK(',
';':'JdKl',
'"':'U873',
"'":"JF12@",
',':'www',
'<':'87jfk',
'.':'WWIEe',
'>':'p2p',
'?':'ueueei',
'/':'hiod',
}

def encrypter(t):
    encrypted_text=""
    for l in t:
        if l != " ":
            encrypted_text += MCD.get(l)+" "
        else:
            encrypted_text += " "
    print(encrypted_text)

def decrypter(t):
    k_l=list(MCD.keys())
    v_l=list(MCD.values())
    t += " "
    morse=""
    normal=""
    for l in t:
        if l!=" ":
            morse += l
            space=0
        else:
            space+=1
            if space==2:
                normal+=" "
            else:
                normal+=k_l[v_l.index(morse)]
                morse=""
    print('\t\t',normal)
print('\n\n\n\t\t\t***This Tool Is Made By MANISH***')
print("\n\n\t\t\t***Text Encrypter And Decrypter***")
while True:
    c=input("\n\tChose 'e' or 'E' for Encrypt Text And 'd' or 'D' For Decrypt Code : ")
    if c=='E'  or c=='e':
        t_e=input("\n\t\t\tEnter Word for Encrypt : ")
        encrypter(t_e)
        continue

    elif  c=='d' or c=='D':
        t_d=input('\n\t\t\tEnter Code For Decrypt : ')
        decrypter(t_d)
        continue

    else:
        print('\n\t\t\t+++You Enter Wrong Choice+++')
        continue
