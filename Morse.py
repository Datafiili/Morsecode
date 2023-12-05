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
    #This is not the best way to setup, but for now it is good enough.
    #Different countries and languages have different morse symbols,
    #so the way of adding data should be easy.
    
    #Root
    Root = Node(None)

    #1. layer
    Root.left = Node("e")
    Root.right = Node("t")
    
    #2. layer
    Root.left.left = Node("i")
    Root.left.right = Node("a")

    Root.right.left = Node("n")
    Root.right.right = Node("m")
    #3. layer
    Root.left.left.left = Node("s")
    Root.left.left.right = Node("u")
    Root.left.right.left = Node("r")

    Root.left.right.right = Node("w")
    Root.right.left.left = Node("d")
    Root.right.left.right = Node("k")
    Root.right.right.left = Node("g")
    Root.right.right.right = Node("o")
    #4. layer
    Root.left.left.left.left = Node("h")
    Root.left.left.left.right = Node("v")
    Root.left.left.right.Root = Node(None)

    Root.left.left.right.left = Node("f")
    Root.left.left.right.right = Node("ö")
    Root.left.right.left.left = Node("l")
    Root.left.right.left.right = Node("ä")
    Root.left.right.right.left = Node("p")
    Root.left.right.right.right = Node("j")

    Root.right.left.left.left = Node("b")
    Root.right.left.left.right = Node("x")
    Root.right.left.right.left = Node("c")
    Root.right.left.right.right = Node("y")

    Root.right.right.left.left = Node("z")
    Root.right.right.left.right = Node("q")
    Root.right.right.right.left = Node(None)
    Root.right.right.right.right = Node(None)
    #5. layer
    Root.left.left.left.left.left = Node("5")
    Root.left.left.left.left.right = Node("4")
    Root.left.left.left.right.right = Node("3")
    Root.left.left.right.right.right = Node("2")
    Root.left.left.right.right.left = Node("!")
    
    Root.left.right.left.right.left = Node("+")
    Root.left.right.right.right.right = Node("1")
    Root.left.right.right.left.right = Node("å")

    Root.right.left.left.left.left = Node("6")
    Root.right.left.left.left.right = Node("=")
    Root.right.left.right.right.left = Node("(")
    Root.right.left.left.right.left = Node("/")

    Root.right.right.left.left.left = Node("7")
    Root.right.right.left.left.right = Node(None)
    Root.right.right.right.left.left = Node("8")
    Root.right.right.right.right.left = Node("9")
    Root.right.right.right.right.right = Node("0")
    
    #6. Layer
    Root.left.left.right.right.left.left = Node("?")
    Root.right.right.right.left.left.left = Node(":")
    Root.right.right.left.left.right.right = Node(",")
    Root.left.right.left.right.left.right = Node(".")
    Root.right.left.left.left.left.right = Node("-")
    Root.right.left.right.right.left.right = Node(")")
    
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