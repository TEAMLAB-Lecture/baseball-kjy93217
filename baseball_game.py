# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number가 정수로 변환 가능할 경우는 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_digit("551")
    #   True
    #   >>> bg.is_digit("103943")
    #   True
    #   >>> bg.is_digit("472")
    #   True
    #   >>> bg.is_digit("1032.203")
    #   False
    #   >>> bg.is_digit("abc")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    
    # 정수가 아닌 문자열 존재하면 False 출력 
    number_set = ['0','1','2','3','4','5','6','7','8','9']

    for i in user_input_number:
        if i not in number_set:
            return False

    # ==================================
    return True


def is_between_100_and_999(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    #                         입력된 값은 숫자형태의 문자열 값임이 보장된다.
    # Output:
    #   - user_input_number가 정수로 변환하여 100이상 1000미만일 경우 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_between_100_and_999("551")
    #   True
    #   >>> bg.is_between_100_and_999("103943")
    #   False
    #   >>> bg.is_between_100_and_999("472")
    #   True
    #   >>> bg.is_between_100_and_999("0")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    
    # 문자열 정수로 변환 후 대소 비교 
    integer_input_number = int(user_input_number)

    if integer_input_number >= 100 and integer_input_number < 1000:
        return True

    # ==================================
    return False


def is_duplicated_number(three_digit):
    # '''
    # Input:
    #   - three_digit : 문자열로 된 세자리 양의 정수 값
    #                   문자열로 된 세자리 양의 정수값의 입력이 보장된다.
    # Output:
    #   - three_digit 정수로 변환하였을 경우 중복되는 수가 있으면 True,
    #     그렇지 않을 경우는 False
    #   ex) 117 - True, 123 - False, 103 - False, 113 - True
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_duplicated_number("551")
    #   True
    #   >>> bg.is_duplicated_number("402")
    #   False
    #   >>> bg.is_duplicated_number("472")
    #   False
    #   >>> bg.is_duplicated_number("100")
    #   True
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    # 중복되는 숫자 존재 확인 위해 set 이용하여 중복 제거 후 길이 비교 
    remove_duplicate_element = set(three_digit)

    if len(remove_duplicate_element) == 3:
        return False

    # ==================================
    return True


def is_validated_number(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number 값이 아래 조건이면 True, 그렇지 않으면 False를 반환
    #        1) 숫자형 문자열이며, 2) 100이상 1000미만이며, 3) 중복되는 숫자가 없을 경우
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_validated_number("amvd")
    #   False
    #   >>> bg.is_validated_number("402")
    #   True
    #   >>> bg.is_validated_number("472")
    #   True
    #   >>> bg.is_validated_number("100")
    #   False
    #   >>> bg.is_validated_number("1000")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    # 세 가지 조건이 순차적으로 모두 만족하는지 
    if is_digit(user_input_number):
        if is_between_100_and_999(user_input_number):
            if not is_duplicated_number(user_input_number):
                return True
    # ==================================
    return False


def get_not_duplicated_three_digit_number():
    # '''
    # Input:
    #   - None : 입력값이 없음
    # Output:
    #   - 중복되는 숫자가 없는 3자리 정수값을 램덤하게 생성하여 반환함
    #     정수값으로 문자열이 아님
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   125
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   634
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   583
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   381
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    # get_random_number() 함수를 사용하여 random number 생성


    # 생성된 숫자에 중복된 값 있는지 체크 후 없을 때 까지 반복하여 만족하면 반환
    while True:
        candidate_random_number = get_random_number()
        candidate_string = str(candidate_random_number)

        if is_duplicated_number(candidate_string) == False:
            return candidate_random_number
    # ==================================


def get_strikes_or_ball(user_input_number, random_number):
    # '''
    # Input:
    #   - user_input_number : 문자열값으로 사용자가 입력하는 세자리 정수
    #   - random_number : 문자열값으로 컴퓨터가 자동으로 생성된 숫자
    # Output:
    #   - [strikes, ball] : 규칙에 따라 정수형 값인 strikes와 ball이 반환됨
    #   변환 규칙은 아래와 같음
    #   - 사용자가 입력한 숫자와 컴퓨터가 생성한 숫자의
    #     한 숫자와 자릿수가 모두 일치하면 1 Strike
    #   - 자릿수는 다르나 입력한 한 숫자가 존재하면 1 Ball
    #   - 세자리 숫자를 정확히 입력하면 3 Strike
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_strikes_or_ball("123", "472")
    #   [0, 1]
    #   >>> bg.get_strikes_or_ball("547", "472")
    #   [0, 2]
    #   >>> bg.get_strikes_or_ball("247", "472")
    #   [0, 3]
    #   >>> bg.get_strikes_or_ball("742", "472")
    #   [1, 2]
    #   >>> bg.get_strikes_or_ball("472", "472")
    #   [3, 0]
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    # 숫자와 위치가 같은 값 체크 후 strike 수 계산
    strike_count = 0
    for i in range(3):
        if user_input_number[i] == random_number[i]:
            strike_count += 1
    
    # 같은 숫자 존재 체크 후 ball 수 계산 
    ball_count = 0
    for i in user_input_number:
        if i in random_number:
            ball_count += 1
    # ball에 대해 strike 수 중복 카운팅 제거 
    ball_count -= strike_count

    result = [strike_count, ball_count]
    # ==================================
    return result


def is_yes(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_yes("Y")
    # True
    # >>> bg.is_yes("y")
    # True
    # >>> bg.is_yes("Yes")
    # True
    # >>> bg.is_yes("YES")
    # True
    # >>> bg.is_yes("abc")
    # False
    # >>> bg.is_yes("213")
    # False
    # >>> bg.is_yes("4562")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    lower_input = one_more_input.lower()

    if lower_input == 'yes' or lower_input == 'y':
        return True
    # ==================================
    return False


def is_no(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "N" 또는 "NO"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_no("Y")
    # False
    # >>> bg.is_no("b")
    # False
    # >>> bg.is_no("n")
    # True
    # >>> bg.is_no("NO")
    # True
    # >>> bg.is_no("nO")
    # True
    # >>> bg.is_no("1234")
    # False
    # >>> bg.is_no("yes")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    lower_input = one_more_input.lower()

    if lower_input == 'no' or lower_input == 'n':
        return True
    # ==================================
    return False


def main():
    
    print("Play Baseball")
    #user_input = 999
    # ===Modify codes below=============
    # 위의 코드를 포함하여 자유로운 수정이 가능함
    
    # 게임 시작되거나 3strike 후 'yes'통해서 재시작 할 때 반복 
    while True:
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)
        one_more = 0
        
        # 게임 시작되거나 / 잘못된 사용자 input 들어오거나 / 3strike이 나오지 않을 때 반복 
        while True:
            user_input = input('Input guess number : ')

            if user_input == '0':
                one_more = -1
                break

            if is_validated_number(user_input) == False:
                print("Wrong Input, Input again")
                continue
        
            # 정상적인 input 들어왔을 때 strike, ball 판정 
            strike, ball = get_strikes_or_ball(user_input, random_number)
            print(f"Strikes : {strike} , Balls : {ball}")

            # 3strike 나올 시 
            if strike == 3:
                # 올바른 재시작 응답 나올 시 까지 반복 
                while True:
                    yes_or_no = input('You win, one more (Y/N) ?')
                    #if yes_or_no == '0':
                    #    one_more = -1
                    #    break
                    if is_yes(yes_or_no):
                        one_more = 1
                        break
                    if is_no(yes_or_no):
                        one_more = -1
                        break
                    print("Wrong Input, Input again")
                if one_more == -1 or one_more == 1:
                    break

        # 재시작 의사 N 또는 입력값 0 인경우 종료 
        if one_more == -1:
            break
        # 재시작 의사 Y인 경우 
        elif one_more == 1:
            continue
       
    # ==================================
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
