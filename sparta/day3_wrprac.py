# 쓰기
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("각 줄마다 번호를 적은 파일입니다.\n")
    for i in [1, 2, 3, 4, 5]:
        f.write(f"이것은 {i}번째 줄입니다.\n")

# 읽기
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
