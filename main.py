import subprocess

print("이 프로그램은 파이썬 학습을 돕기 위해 제작되었습니다")
print("원하시는 메뉴를 입력해주세요!")
print("1. 출력 2. 입력 3. 조건문 4. 반복문 5. 중첩반복문")

user_input = int(input())

code = []
def value(user_input):
    if user_input == 2:
        return "A"
    elif user_input == 3:
        a = 20
        return str(a)
    elif user_input == 4:
        return str(5)
    elif user_input == 5:
        return str(3)

def analyze(user_input):
    if user_input == 1:
        if check(code) == "Hello":
            print("출력결과 :", check(code))
            print("정확한 풀이")
        else:
            print("출력결과 :", check(code))
            print("잘못된 풀이")
    elif user_input == 2:
        if check(code) == value(user_input):
            print("정답 :", value(user_input))
            print("출력결과 :", check(code))
            print("정확한 풀이")
        else:
            print("정답 :", value(user_input))
            print("출력결과 :", check(code))
            print("잘못된 풀이")
    elif user_input == 3:
        if check(code) == value(user_input):
            print("정답 :", "False")
            print("출력결과 :", check(code))
            print("정확한 풀이")
        else:
            print("정답 :", "False")
            print("출력결과 :", check(code))
            print("잘못된 풀이")
    elif user_input == 4:
        if check(code) == "15":
            print("정답 : 15")
            print("출력결과 :", check(code))
            print("정확한 풀이")
        else:
            print("정답 : 15")
            print("출력결과 :", check(code))
            print("잘못된 풀이")

    elif user_input == 5:
        OK = "***\n***\n***"
        output_str = check(code).strip()  # Convert output to string

        if output_str == OK:
            print("정답 :\n***\n***\n***")
            print("출력결과 :\n" + output_str)
            print("정확한 풀이")
        else:
            print("정답 :\n***\n***\n***")
            print("출력결과 :\n" + output_str)
            print("잘못된 풀이")

def code_input():
    while True:
        line = input().rstrip() #오른쪽 코드 공백은 삭제하고 왼쪽의 공백은 삭제하여 들여쓰기 유지
        if line == "":
            print("코드 입력 완료!\n")
            break
        code.append(line)

def check(code):
    with open('test.py', 'w') as f:
        for line in code:
            f.write(line + "\n")
    if value(user_input) is not None:
        output = subprocess.run(["python", "test2.py"], input = value(user_input).encode('utf-8'), stdout = subprocess.PIPE).stdout.decode('utf-8')
        output = output.strip()
    else:
        output = subprocess.run(["python", "test2.py"],stdout=subprocess.PIPE).stdout.decode('utf-8')
        output = output.strip()

    return output

def out_question1():
    print("print()를 이용해 다음 단어를 출력하시오.")
    print("Hello\n")
    print("참고")
    print("아래와 같은 소스 코드를 작성하고 실행시키면,")
    print("지정한 '문장'이 출력(print)된다.\n")


def input_question1():
    print("변수에 문자 1개를 저장한 후 저장된 문자를 출력하시오.\n")
    print("참고")
    print("input()을 사용하면 키보드로 입력한 값을 가져옵니다.")
    print("변수 = input()")
    print("를 실행시키면 키보드로 입력한 값을 왼쪽의 변수에 저장합니다.\n")
    print("변수(variable)는 어떤 값(정수, 실수, 문자, 문자열 등)을 저장할 수 있는 공간이라고 볼 수 있다.")
    print("어떤 값을 저장했다가 다시 사용하기 위해서 변수를 사용한다. 저장할 내용들이 많으면 필요한 만큼")
    print("변수를 만들어 사용해도 된다.\n")


def if_else_question1():
    print("정수 int(n)을 입력받아")
    print("n이 10보다 작으면 True를, n이 10보다 크거나 같다면 False을 출력하시오.\n")
    print("참고")
    print("어떤 값을 비교하기 위해 비교/관계 연산자를 사용할 수 있다.")
    print("비교/관계연산자 < (less than sign) 는")
    print("왼쪽의 값이 오른쪽 값 보다 작은 경우 True(참)로 계산하고,")
    print("그 외의 경우에는 False(거짓)로 계산한다.\n")
    print("비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다.\n")
    print("예시")
    print("if a < b:")
    print("    print(\"True\")\n")


def repeat1():
    print("정수 n을 입력받아")
    print("1부터 n까지 정수합을 출력하시오.\n")
    print("참고")
    print("for 카운터변수 in range(카운터 변수의 시작값, 반복횟수, 반복횟수 증가값):")
    print("    반복해서 실행할 명령\n")
    print("예시")
    print("for i in range(1, n + 1, 1):")
    print("    print(n)\n")


def nested_repetition1():
    print("길이 n이 입력되면 길이가 n인 사각형을 출력하시오.")
    print("단, 사각형은 * 모양으로 채운다.\n")
    print("참고")
    print("아래의 코드는 n번 동안에")
    print("안쪽의 j값이 ㅜehd 출력되는 코드이다.\n")
    print("조건 선택 실행구조 안에 다른 조건 실행구조를 넣어 처리할 수 있는 것과")
    print("마찬가지로 반복 실행구조 안에 다른 반복 실행구조를 넣어 처리할 수 있다.\n")
    print("for i in range(n):")
    print("    for j in range(n):")
    print("        print(\"*\")\n")


if user_input == 1:
    print("출력을 선택했습니다.\n")
    out_question1()
    print("코드를 입력하십시오. 입력을 완료하면 엔터키를 한번 더 눌러주세요")
    code_input()
    analyze(user_input)

elif user_input == 2:
    print("입력을 선택하셨습니다.\n")
    input_question1()
    print("코드를 입력하십시오. 입력을 완료하면 엔터키를 한번 더 눌러주세요")
    code_input()
    analyze(user_input)

elif user_input == 3:
    print("조건문을 선택하셨습니다.\n")
    if_else_question1()
    print("코드를 입력하십시오. 입력을 완료하면 엔터키를 한번 더 눌러주세요")
    code_input()
    analyze(user_input)

elif user_input == 4:
    print("반복문을 선택하셨습니다.\n")
    repeat1()
    print("코드를 입력하십시오. 입력을 완료하면 엔터키를 한번 더 눌러주세요")
    code_input()
    analyze(user_input)

elif user_input == 5:
    print("중첩 반복문을 선택하셨습니다.\n")
    nested_repetition1()
    print("코드를 입력하십시오. 입력을 완료하면 엔터키를 한번 더 눌러주세요")
    code_input()
    analyze(user_input)

else:
    print("잘못된 선택입니다.")
