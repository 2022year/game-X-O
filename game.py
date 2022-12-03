sout="Вы вышли из игрового поля!"
serror="Вы указали неверные координаты!"
sbusy="Эта клетка занята!"
print("===Игра Крестики-нолики===")
def board():
       board = []       
       for i in range(3):
              board.append([])
              for j in range(3):
                     board[i].append("-")
       return board

def DrawBoard(a):
       s=["a","b","c"]
       print(" ","1","2","3")
       for i in range(3):
              print(s[i],*a[i],end = " ")
              print()

def Winner(p, player):
       def OkPoint(a1,a2,a3,player):
              if a1==player and a2==player and a3==player:
                     return True
       for n in range(3):
              if OkPoint(p[n][0],p[n][1],p[n][2],player) or \
                 OkPoint(p[0][n],p[1][n],p[2][n],player) or \
                 OkPoint(p[0][0],p[1][1],p[2][2],player) or \
                 OkPoint(p[2][0],p[1][1],p[2][0],player):
                     return True

def InputCoords(a):
       def inputXY():
              s=str(input("Координаты ?  "))
              X = ord(s[0])-ord('a')+1
              s=s.replace(s[0],'')
              Y= int(s)
              return [X,Y]
       
       while True:
              while True:

                     try:
                            print("Ход Крестика")
                            [X,Y]=inputXY()
                            if a[X-1][Y-1] != "-":
                                   print(sbusy)
                            else:       
                                   a[X-1][Y-1] = "X"
                                   DrawBoard(a)
                                   break
                     except ValueError:
                            print(serror)
                     except IndexError:
                            print(sout)

              if Winner(a,"X") == True:
                     print("Победил Крестик")
                     DrawBoard(a)
                     break
              
                     
              while True:

                     try:
                            print("Ход Нолика")
                            [X,Y]=inputXY()
                            if a[X-1][Y-1] != "-":
                                   print(sbusy)
                            else:
                                   a[X-1][Y-1] = "O"
                                   DrawBoard(a)
                                   break

                     except ValueError:
                            print(serror)
                     except IndexError:
                            print(sout)
                           

              if Winner(a,"O") == True:
                     print("Победил Нолик")
                     DrawBoard(a)
                     break
              
a = board()
DrawBoard(a)
InputCoords(a)
