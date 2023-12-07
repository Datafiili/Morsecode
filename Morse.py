## -------------------- Morsecobte -------------------- ##
#Written By: Aarni Junkkala

#This is mostly practice to understand binarytrees.
#Build on Finnish morse code.

class Node:
    def __init__(self,value):
        self.value = value
    left = None
    right = None

## ----- Setup ----- ##
#Puts all data on correct braches.

def Setup():
    #Currently the list should be in order by the number
    kirjaimet = ["e1","t2","i3","a4","n5","m6","s7","u8","r9","w10","d11","k12","g13","o14","h15","v16","f17","ö18","l19","ä20","p21","j22","b23","x24","c25","y26","z27","q28","531","432","334","!37","238","+41","å44","146","647","=48","/49","(53","755","859","961","062","?75",".84","-96",")108",",114",":119"]
    Root = Node(None)
    for i in kirjaimet:
        v = i[0]
        pos = int(i[1:])
        route = []
        while pos > 0:
            if pos % 2 == 0: #Oikealle
                pos = (pos - 2) / 2
                route.insert(0,1)
            else: #Vasemalle
                pos = (pos - 1) / 2
                route.insert(0,0)
        curPos = Root
        for k in range(len(route) - 1):
            if route[k] == 0:
                if curPos.left == None: #Adds an empty node, if there is not one
                    curPos.left = Node(None)
                curPos = curPos.left
            if route[k] == 1:
                if curPos.right == None: #Adds an empty node, if there is not one
                    curPos.right = Node(None)
                curPos = curPos.right
        if route[-1] == 0:
            curPos.left = Node(i[0])
        if route[-1] == 1:
            curPos.right = Node(i[0])
    return Root

Root = Setup()

## ----- Print Tree ----- ##
#Prints the hole tree, but in order from most left bottom one up to the root
#TODO: Make it print pretty tree
def PrintTree(bt): #bt = binary tree
    text = ""
    if bt.left != None:
        text += PrintTree(bt.left)
    if bt.right != None:
        text += PrintTree(bt.right)
    if bt.value != None:
        return text + bt.value
    if bt.value == None:
        return text
print("Full tree:", PrintTree(Root))

## ----- Convertion ----- ##
#Note: Uses | symbol to show spaces.

def ConvertMorse(t,bt): #t = text, bt = binary tree
    #Splits all text
    t = t.split()
    text = ""
    for i in range(len(t)): #Checks each word
        curLeaf = bt
        for k in range(len(t[i])): #Checks each letter of the word
            if t[i][k] == "|": #Space symbol
                text += " "
                break
            if t[i][k] == ".": #Left branch
                curLeaf = curLeaf.left
            if t[i][k] == "-": #Right branch
                curLeaf = curLeaf.right
            if k == len(t[i]) - 1: #Last symbol, so add it to text
                text += curLeaf.value
    return text

if __name__ == "__main__": #Testing in the main file
    #My name
    print(ConvertMorse("-- -.-- | -. .- -- . ---... | .- .- .-. -. .. | .--- ..- -. -.- -.- .- .-.. .-",Root))
    #My alphabet
    print(ConvertMorse("..-. .. -. -. .. ... .... | .- .-.. .--. .... .- -... . - ---... | .- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .--.- .-.- ..--",Root))
    #Numbers and specialcharacters
    print(ConvertMorse("-. ..- -- -... . .-. ... | .- -. -.. | ... .--. . -.-. .. .- .-.. | -.-. .... .- .-. .- -.-. - . .-. ... ---... | .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- .-.-. -....- -...- -..-. ..--. ..--.. ---... --..-- .-.-.- -....- -.--. -.--.-",Root))
    #Type yourself
    writing = input("Type morse and see what you wrote. Use dots and dashes. Space to divide letters and | to create spaces between words: ")
    print(ConvertMorse(writing,Root))