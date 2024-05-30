def printbord(xstate, zstate):
     zero = {'x'if xstate[0] else{'0' if zstate[0] else 0}}
     one = {'x'if xstate[1] else{'0' if zstate[1] else 1}}
     two = {'x'if xstate[2] else{'0' if zstate[2] else 2}}
     three = {'x'if xstate[3] else{'0' if zstate[3] else 3}}
     four = {'x'if xstate[4] else{'0' if zstate[4] else 4}}
     five = {'x'if xstate[5] else{'0' if zstate[5] else 5}}
     six = {'x'if xstate[6] else{'0' if zstate[6] else 6}}
     siven = {'x'if xstate[7] else{'0' if zstate[7] else 7}}
     eight = {'x'if xstate[8] else{'0' if zstate[8] else 8}}
     
     print(f"{zero} | {one}  | {two}")
     print(f"--|----|--")
     print(f"{three} | {four}  | {five}")
     print(f"--|----|--")
     print(f"{six} | {seven}  | {eight}")
     pass
 
if ___name__ == "main__":
        xstate = [0,0,0,0,0,0,0,0]
        zstate = [0,0,0,0,0,0,0,0]
        tuurn = 1 #1 for x and 0 for o
        print("well come to tic toc toe")
        while(true):
            printbord():
            if(turn == 1):
               print("x's chance")
               value = int(input("plese enter a value"))
               xstate[value] = 1

            else:
               print("z's chance")
               value = int(input("plese enter a value"))
               zstate[value] = 1
           
            break
        