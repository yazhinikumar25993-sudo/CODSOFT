import math,random
b=[" "]*9
H,A="X","O"
def print_board():
    print("\n".join([" | ".join(b[i*3:(i+1)*3]) for i in range(3)]))
    print()
def print_guide():
    print("Board guide:")
    print("\n".join([" | ".join(str(i+1) for i in range(j*3,(j+1)*3)) for j in range(3)]))
    print()
def w(ply):return any(all(b[i]==ply for i in c) for c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])
def d():return" " not in b
def minimax(mx,alpha,beta):
    if w(A):return 1
    if w(H):return-1
    if d():return 0
    if mx:
        s=-math.inf
        for i in range(9):
            if b[i]==" ":
                b[i]=A
                s=max(s,minimax(False,alpha,beta))
                b[i]=" "
                alpha=max(alpha,s)
                if beta<=alpha:break
        return s
    s=math.inf
    for i in range(9):
        if b[i]==" ":
            b[i]=H
            s=min(s,minimax(True,alpha,beta))
            b[i]=" "
            beta=min(beta,s)
            if beta<=alpha:break
    return s
def ai():
    if b.count(" ")==9:
        mv=random.choice(range(9))
    else:
        s=-math.inf;mv=0
        for i in range(9):
            if b[i]==" ":
                b[i]=A
                v=minimax(False,-math.inf,math.inf)
                b[i]=" "
                if v>s:s,mv=v,i
    b[mv]=A
    print(f"AI chose position {mv+1}")
def hu():
    while 1:
        try:
            x=int(input("Your move (1-9): "))-1
            if 0<=x<=8 and b[x]==" ":
                b[x]=H
                break
            else:
                print("Invalid move or position taken.")
        except:
            print("Enter a number 1-9.")
def g():
    print("Tic-Tac-Toe: You=X  AI=O")
    print_guide()
    while 1:
        print_board();hu()
        if w(H):print_board();print("🎉 You win!");break
        if d():print("🤝 Draw!");break
        ai()
        if w(A):print_board();print("🤖 AI wins!");break
        if d():print("🤝 Draw!");break
g()
