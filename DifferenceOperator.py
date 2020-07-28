# Enter your code here. Read input from STDIN. Print output to STDOUT
EnglishNum = int(raw_input())
English = map(int, raw_input().split())
FrenchNum = int(raw_input())
French = map(int, raw_input().split())
Output = 0
for x in English:
    try:
        if French.index(x):
            Output = Output
    except:
        Output+=1
print(Output)
