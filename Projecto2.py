
from parte1 import e_palavra
import itertools

def valid_letter (letter):
    """
    caracter --> logico
    """
    # verifica se um caracter e uma letra maiuscula ou uma string vazia 
    
    valid_letters = ["","A","B","C","D","E","F","G","H","I","J","L","M","N","O","P","Q","R","S","T","U","V","X","Z","K","W","Y"]
    return letter in valid_letters



def valid_letterSet(letterSet):
    """
    lista ou tuplo ou cadeia de caracteres --> logico  
    """
    # verifica se os elementos de uma lista, tuplo ou cadeia de caracteres sao uma letra maiuscula ou uma string vazia  
    
    letterSetLength = len(letterSet)
    if letterSetLength == 0:
        return True
    else:
        return  valid_letter(letterSet[0]) and valid_letterSet(letterSet[1:])



def validWord_inLetterSet (word,letterSet):
    """
    cadeia de caracteres x tuplo de letras --> logico
    """
    # verifica se uma cadeia de caracteres contem letras diferentes das que existem no tuplo de letras sendo que se existem letras repetidas
    # na cadeia de caracteres devem existir pelo menos as mesmas repeticoes no tuplo de letras 
    
    if word == "":
        return True
    elif letterSet == ():
        return False
    else:
        letterSet_Index = 0
        while letterSet_Index < len(letterSet):
            if word[0] == letterSet[letterSet_Index]:
                return True and validWord_inLetterSet(word[1:] , letterSet[:letterSet_Index] + letterSet[letterSet_Index + 1 : ]  )
            else:
                letterSet_Index = letterSet_Index + 1
    
    return False 



# TAD palavra_potencial

def cria_palavra_potencial (word,letterSet):
    """
    cadeia de caracteres x tuplo de letras --> palavra_potencial
    """
    
    if not isinstance(word,str) or not isinstance(letterSet,tuple):
        raise ValueError ("cria_palavra_potencial:argumentos invalidos.")

    if not valid_letterSet(letterSet) or not valid_letterSet(word):
        raise ValueError ("cria_palavra_potencial:argumentos invalidos.")
    
    if len(word) > len(letterSet) or not validWord_inLetterSet(word,letterSet):
        raise ValueError ("cria_palavra_potencial:a palavra nao e valida.")
    
    return word


def palavra_tamanho(potential_word):
    """
    palavra_potencial --> inteiro
    """
    
    if not e_palavra_potencial(potential_word):
        raise ValueError ("palavra_tamanho: potential_word tem de ser uma palavra potencial.")     
    
    return len(potential_word)
    
    

def e_palavra_potencial (potential_word):
    """
    universal --> logico
    """
    
    return isinstance(potential_word,str) and (potential_word == "" or valid_letterSet(potential_word))
    
    

def palavras_potenciais_iguais (potential_word1,potential_word2):
    """
    palavra_potencial x palavra_potencial --> logico
    """
    
    if not e_palavra_potencial(potential_word1) or not e_palavra_potencial(potential_word2):
        raise ValueError ("palavras_potenciais_iguais: potential_word1 e potential_word2 tem de ser ambas palavra potencial.")
    
    return potential_word1 == potential_word2



def palavra_potencial_menor (potential_word1,potential_word2):
    """
    palavra_potencial x palavra_potencial --> logico
    """
    
    if not e_palavra_potencial(potential_word1) or not e_palavra_potencial(potential_word2):
        raise ValueError ("palavra_potencial_menor: potential_word1 e potential_word2 tem de ser ambas palavra potencial.")
    
    return potential_word1 < potential_word2



def palavra_potencial_para_cadeia (potential_word):
    """
    palavra_potencial --> cadeia de caracteres
    """
    
    if not e_palavra_potencial(potential_word):
        raise ValueError ("palavra_potencial_para_cadeia: potential_word tem de ser uma palavra potencial.") 
    
    return potential_word



# TAD conjunto_palavras

def cria_conjunto_palavras():
    """
    --> conjunto_palavras
    """
    
    return []



def numero_palavras(wordSet):
    """
    conjunto_palavras --> inteiro
    """
    
    if not e_conjunto_palavras(wordSet):
        raise ValueError ("numero_palavras: wordSet tem de ser uma lista.")  
    
    
    return len(wordSet)



def subconjunto_por_tamanho(wordSet,n):
    """
    conjunto_palavras x inteiro --> lista
    """
    
    if not e_conjunto_palavras(wordSet) or not isinstance(n,int):
        raise ValueError ("numero_palavras: wordSet tem de ser uma lista e n tem de ser inteiro positivo.")
    
    return list(filter(lambda x: palavra_tamanho(x) == n, wordSet))



def acrescenta_palavra (wordSet,potential_word):
    """
    conjunto_palavras x palavra_potencial -->
    """
    
    if not e_conjunto_palavras(wordSet) or not e_palavra_potencial(potential_word):
        raise ValueError ("acrescenta_palavra:argumentos invalidos.")
    
    if potential_word not in wordSet:
        return wordSet.append(potential_word)



def e_conjunto_palavras (wordSet):
    """
    universal --> logico
    """
    
    def testing_list_potential_words(wordSet):
        # lista --> logico
        # verifica se todos os elementos de uma lista sao palavra_potencial
        
        if len(wordSet) == 0:
            return True
        else:
            return e_palavra_potencial(wordSet[0]) and testing_list_potential_words(wordSet[1:])
        
        
    def testing_equal_potential_words(wordSet):
        # lista --> logico
        # verifica se todos os elementos de uma lista com elementos do tipo palavra_potencial sao diferentes uns dos outros
        
        if len(wordSet) <= 1:
            return True
        else:
            num = len(wordSet)-1
            flag = True
            i = 1
            while i < num:
                index = 0
                for index in range(0,i):
                    if palavras_potenciais_iguais(wordSet[i],wordSet[index]):
                        flag = False
                        break
                i = i + 1            
            return flag
        
        
    if isinstance(wordSet,list):
        if testing_list_potential_words(wordSet):
            return testing_equal_potential_words(wordSet)
            
    return False



def bubbleSort(lst):
    """
    lista --> lista
    """
    # algoritmo de ordenacao de uma lista
    
    maior_indice = len(lst) - 1
    nenhuma_troca = False
    
    while not nenhuma_troca:
        nenhuma_troca = True
        for i in range(maior_indice):
            if  not (palavra_potencial_menor(lst[i], lst[i+1])):
                lst[i], lst[i+1] = lst[i+1], lst[i]
                nenhuma_troca = False
        maior_indice = maior_indice - 1

            
            
def conjuntos_palavras_iguais(wordSet1,wordSet2):
    """
    conjunto_palavras x conjunto_palavras --> logico
    """        
        
    if not e_conjunto_palavras(wordSet1) or not e_conjunto_palavras(wordSet2):
        raise ValueError ("conjuntos_palavras_iguais: argumentos invalidos.")

              
    def testSubset(w1,w2,size,num):
        # conjunto_palavras x conjunto_palavras x inteiro x inteiro --> logico
        # verifica se todos os subconjunto_por_tamanho de dois conjunto_palavras sao iguais 
        
        if num == 0:
            return True
        else:
            subConj1 = subconjunto_por_tamanho(w1,size)
            subConj2 = subconjunto_por_tamanho(w2,size)
            bubbleSort(subConj1)
            bubbleSort(subConj2)
            return (subConj1 == subConj2) and testSubset(w1,w2,size + 1,num - len(subconjunto_por_tamanho(w1,size)))    
            
        
    if numero_palavras (wordSet1) != numero_palavras (wordSet2):
        return False
    else:
        size = 0        
        num = numero_palavras(wordSet1)        
        return testSubset(wordSet1,wordSet2,size,num)
    


def conjunto_palavras_para_cadeia (wordSet):
    """
    conjunto_palavras --> cadeia de caracteres
    """
    
    if not e_conjunto_palavras(wordSet):
        raise ValueError ("conjunto_palavras_para_cadeia: wordSet tem de ser uma lista")


    def listWrite (l):
        # lista de palavra_potencial --> cadeia de caracteres
        
        if l == []:
            return ""
        else:
            if len(l) == 1:
                return palavra_potencial_para_cadeia(l[0])
            else:
                return palavra_potencial_para_cadeia(l[0]) + ", " + listWrite(l[1:])       
        
    
    def wordSetWrite(w,size,num):
        # conjunto_palavras x inteiro x inteiro --> cadeia de caracteres        
        
        if num == 0:
            return ""
        else:
            if subconjunto_por_tamanho(w,size) == []:
                return wordSetWrite(w, size + 1, num - len(subconjunto_por_tamanho(w,size)))
            else:
                subconjunto = subconjunto_por_tamanho(w,size)
                bubbleSort(subconjunto)
                return str(size) + "->" + "[" + listWrite(subconjunto) + "];" + wordSetWrite(w, size + 1, num - len(subconjunto_por_tamanho(w,size)))

    size = 0        
    num = numero_palavras(wordSet)
    output = wordSetWrite(wordSet,size,num)
    return ("[" + output[:-1] + "]")    



# TAD jogador

def cria_jogador (name):
    """
    cadeia de caracteres --> jogador
    """
    
    if not isinstance(name,str):
        raise ValueError ("cria_jogador:argumento invalido.")
    
    return {"JOGADOR": name, "PONTOS": 0 , "VALIDAS": cria_conjunto_palavras(),"INVALIDAS": cria_conjunto_palavras()}



def jogador_nome(player):
    """
    jogador --> cadeia de caracteres
    """
    
    if not e_jogador(player):
        raise ValueError ("jogador_nome: argumento invalido.")
    
    return player["JOGADOR"]



def jogador_pontuacao(player):
    """
    jogador --> inteiro
    """
    
    if not e_jogador(player):
        raise ValueError ("jogador_pontuacao:argumento invalido.")
    
    return player["PONTOS"] 
    
    

def jogador_palavras_validas(player):
    """
    jogador --> conjunto_palavras
    """
    
    if not e_jogador(player):
        raise ValueError ("jogador_palavras_validas:argumento invalido.")
    
    return player["VALIDAS"]



def jogador_palavras_invalidas(player):
    """
    jogador --> conjunto_palavras
    """
    
    if not e_jogador(player):
        raise ValueError ("jogador_palavras_invalidas:argumento invalido.")
    
    return player["INVALIDAS"]    



def adiciona_palavra_valida (player,potential_word):
    """
    jogador x palavra_potencial -->
    
    """
    
    if not e_jogador(player) or not e_palavra_potencial(potential_word):
        raise ValueError ("adiciona_palavra_valida:argumentos invalidos.")
    
    
    if potential_word not in subconjunto_por_tamanho(jogador_palavras_validas(player),palavra_tamanho(potential_word)):
        acrescenta_palavra(jogador_palavras_validas(player),potential_word)
        player["PONTOS"] = jogador_pontuacao(player) + palavra_tamanho(potential_word)    
    
    

def adiciona_palavra_invalida (player,potential_word):
    """
    jogador x palavra_potencial -->
    
    """
    
    if not e_jogador(player) or not e_palavra_potencial(potential_word):
        raise ValueError ("adiciona_palavra_invalida:argumentos invalidos.")
    
    if potential_word not in subconjunto_por_tamanho(jogador_palavras_invalidas(player),palavra_tamanho(potential_word)):
        acrescenta_palavra(jogador_palavras_invalidas(player),potential_word)
        player["PONTOS"] = jogador_pontuacao(player) - palavra_tamanho(potential_word)
          
    
    
def e_jogador(player):
    """
    universal --> logico
    """
    
    if isinstance (player,dict):
        if len(player) == 4 and "JOGADOR" in player and "PONTOS" in player and "VALIDAS" in player and "INVALIDAS" in player:
            return isinstance(player["JOGADOR"],str) and isinstance(player["PONTOS"],int) and e_conjunto_palavras(player["VALIDAS"]) and e_conjunto_palavras(player["INVALIDAS"])
    
    return False



def jogador_para_cadeia(player):
    """
    jogador --> cadeia de caracteres
    """
    
    if not e_jogador(player):
        raise ValueError ("jogador_para_cadeia:argumento invalido.")
    
    return  "JOGADOR " + jogador_nome(player) + " PONTOS=" + str(jogador_pontuacao(player)) + " VALIDAS=" + conjunto_palavras_para_cadeia(jogador_palavras_validas(player)) + " INVALIDAS=" + conjunto_palavras_para_cadeia(jogador_palavras_invalidas(player))



# Funcoes Adicionais


def gera_todas_palavras_validas (letterSet):
    """
    tuplo de letras --> conjunto_palavras

    """
    
    if not isinstance(letterSet,tuple):
        raise ValueError ("gera_todas_palavras_validas: argumento invalido.")
    
    validWordSet = cria_conjunto_palavras()
    if len(letterSet) > 0:
        for wordSize in range(1, len(letterSet)+1):
            for permutation in itertools.permutations(letterSet, wordSize):
                word = ""
                for letter in permutation:
                    word = word + letter
                if e_palavra(word):
                    acrescenta_palavra(validWordSet,cria_palavra_potencial(word,letterSet))
                
    return validWordSet



def guru_mj (letterSet):
    """
    tuplo de letras --> 
    """
    
    if not isinstance(letterSet,tuple):
        raise ValueError ("gera_todas_palavras_validas: argumento invalido.")

    if not valid_letterSet(letterSet):
        raise ValueError ("gera_todas_palavras_validas: argumento invalido.")    
    
    print ("Descubra todas as palavras geradas a partir das letras:")
    print (str(letterSet))
    
    print ("Introduza o nome dos jogadores (-1 para terminar)...")
    playerNumber = 1
    playerSet = {}
       
    player = input ("JOGADOR " + str(playerNumber) + " -> ")
    
    while player != "-1":
        playerSet[playerNumber] = cria_jogador(player)
        playerNumber = playerNumber + 1
        player = input ("JOGADOR " + str(playerNumber) + " -> ")
        
    if len(playerSet) > 0:
        validWordSet = gera_todas_palavras_validas(letterSet)       
        wordsToDiscover = numero_palavras(validWordSet)
        playerTurn = 1
        play = 1
        
        while wordsToDiscover > 0:
            print ("JOGADA",play,"- Falta descobrir",wordsToDiscover,"palavras")
            if playerTurn == len(playerSet) + 1:
                playerTurn = 1
            
            guess = cria_palavra_potencial(input ("JOGADOR " + jogador_nome(playerSet[playerTurn]) + " -> "),letterSet)
            
            
            def guessValidRepeated(guess,playerSet):
                # palavra_potencial x dicionario de jogadores --> logico
                # verifica se a palavra_potencial proposta ja foi proposta antes
                
                flag = False
                for p in range(1,len(playerSet)+1):
                    if guess in subconjunto_por_tamanho(jogador_palavras_validas(playerSet[p]),palavra_tamanho(guess)):
                        flag = True
                        break
                return flag            
            
            
                       
            if guess in subconjunto_por_tamanho(validWordSet,len(guess)):
                if not guessValidRepeated(guess,playerSet):
                    wordsToDiscover = wordsToDiscover - 1
                    adiciona_palavra_valida(playerSet[playerTurn],guess)      
                print (guess, "- palavra VALIDA")                
            else:
                adiciona_palavra_invalida(playerSet[playerTurn],guess)
                print (guess, "- palavra INVALIDA")
                
            playerTurn = playerTurn + 1
            play = play + 1
            
        
        maxScore = jogador_pontuacao(playerSet[1])
        maxID = 1
        countMax = 1
        for p in range(2,len(playerSet)+1):
            if jogador_pontuacao(playerSet[p]) > maxScore:
                maxScore = jogador_pontuacao(playerSet[p])
                maxID = p
            else:
                if jogador_pontuacao(playerSet[p]) == maxScore:
                    countMax = 2
                    break
            
        victoryString = "FIM DE JOGO! O jogo terminou com a vitoria do jogador "
        evenString = "FIM DE JOGO! O jogo terminou em empate."

        if countMax > 1:
            print (evenString)
        else:
            print (victoryString + jogador_nome(playerSet[maxID]) + " com " + str(jogador_pontuacao(playerSet[maxID])) + " pontos.")
         
        playerSetLength = len(playerSet)
        for p in range(1,len(playerSet)+1):
            print (jogador_para_cadeia(playerSet[p]))

 

