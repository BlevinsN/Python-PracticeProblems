n = int(raw_input())
English = map(int, raw_input().split())
b = int(raw_input())
French = map(int, raw_input().split())
Output = 0
for a in English:
     for b in French:
          if a == b: Output += 1
print(Output)
