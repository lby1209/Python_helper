print("이 프로그램은 파이썬 학습을 돕기 위해 제작되었습니다")
print("원하시는 메뉴를 입력해주세요!")
print("1. 출력 2. 입력 3. 조건문 4. 반복문 5. 중첩반복문")

user_input = int(input())


def out_question1():
    print("print()를 이용해 다음 단어를 출력하시오.")
    print("Hello\n")
    print("참고")
    print("아래와 같은 소스 코드를 작성하고 실행시키면,")
    print("지정한 '문장'이 출력(print)된다.")
    print("답을 입력하십시오")


def input_question1():
    print("변수에 문자 1개를 저장한 후 저장된 문자를 출력하시오.\n")
    print("참고")
    print("input()을 사용하면 키보드로 입력한 값을 가져옵니다.")
    print("변수 = input()")
    print("를 실행시키면 키보드로 입력한 값을 왼쪽의 변수에 저장합니다.\n")
    print("변수(variable)는 어떤 값(정수, 실수, 문자, 문자열 등)을 저장할 수 있는 공간이라고 볼 수 있다.")
    print("어떤 값을 저장했다가 다시 사용하기 위해서 변수를 사용한다. 저장할 내용들이 많으면 필요한 만큼")
    print("변수를 만들어 사용해도 된다.")


def if_else_question1():
    print("두 정수(a, b)를 입력받아")
    print("a가 b보다 작으면 True를, a가 b보다 크거나 같다면 False을 출력하시오.\n")
    print("참고")
    print("어떤 값을 비교하기 위해 비교/관계 연산자를 사용할 수 있다.")
    print("비교/관계연산자 < (less than sign) 는")
    print("왼쪽의 값이 오른쪽 값 보다 작은 경우 True(참)로 계산하고,")
    print("그 외의 경우에는 False(거짓)로 계산한다.\n")
    print("비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다.")


def repeat1():
    print("정수 n을 입력받아")
    print("0부터 n까지 정수 출력하시오.\n")
    print("참고")
    print("for 카운터변수 in range(반복횟수):")
    print("    반복해서 실행할 명령\n")
    print("예시")
    print("for i in range(n):")
    print("    print(n)")


def nested_repetition1():
    print("1부터 n까지, 1부터 m까지 서로 다른 주사위 2개를 던졌을 때,")
    print("나올 수 있는 모든 경우를 출력해보자\n")
    print("참고")
    print("아래의 코드는 i값이 1부터 n까지 순서대로 바뀌는 동안에")
    print("안쪽의 j값이 다시 1부터 m까지 변하며 출력되는 코드이다.\n")
    print("조건 선택 실행구조 안에 다른 조건 실행구조를 넣어 처리할 수 있는 것과")
    print("마찬가지로 반복 실행구조 안에 다른 반복 실행구조를 넣어 처리할 수 있다.\n")
    print("for i in range(1, n + 1):")
    print("    for j in range(1, m + 1):")
    print("        print(i, j)")


if user_input == 1:
    print("출력을 선택했습니다.\n")
    out_question1()

elif user_input == 2:
    print("입력을 선택하셨습니다.\n")
    input_question1()

elif user_input == 3:
    print("조건문을 선택하셨습니다.\n")
    if_else_question1()

elif user_input == 4:
    print("반복문을 선택하셨습니다.\n")
    repeat1()

elif user_input == 5:
    print("중첩 반복문을 선택하셨습니다.\n")
    nested_repetition1()

else:
    print("잘못된 선택입니다.")
