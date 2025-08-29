#!/usr/bin/env python3
import os, random; random.seed(47)
def w(name, n, m, A, B):
    os.makedirs("tests", exist_ok=True)
    open(f"tests/input_{name}.txt","w").write(f"{n} {m}\\n"+" ".join(map(str,A))+"\\n"+" ".join(map(str,B))+"\\n")
    C=[a+b for a,b in zip(A,B)]
    with open(f"tests/output_{name}.txt","w") as f:
        for i in range(n):
            f.write(" ".join(map(str,C[i*m:(i+1)*m]))+"\\n")
def main():
    w("min",1,1,[1],[2])
    n,m=2000,2000; A=list(range(n*m)); B=[(i*i)%97 for i in range(n*m)]; w("max",n,m,A,B)
    n,m=10,13; import random
    A=[random.randint(-100,100) for _ in range(n*m)]
    B=[random.randint(-100,100) for _ in range(n*m)]
    w("rnd", n, m, A, B)
if __name__=="__main__": main()
