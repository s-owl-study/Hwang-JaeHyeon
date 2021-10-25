# 9080 문제 : PC방 요금

T = int(input()) # 테스트 케이스의 갯수 입력
if(1 <= T <= 10): # 테스트 케이스 조건 검사

    for i in range(T):
        time, D = map(str, input().split()) #시간(시, 분 포함)과 게임시간 입력
        tmp_list = time.split(":")
        int_time = int(D)
        int_list_0 = ((int(tmp_list[0])+2)%24) # 편의상 22시를 0, 8시를 10으로 간주
        int_list_1 = int(tmp_list[1])
        ans = 0
        if(1 <= int_time <= 4320): #이용 시간 조건 검사
            while(int_time > 0):
                
                # 5보다 작은 수이고, 동시에 300분 이상 이용하고 싶다면 야간 정액권 이용
                if(int_list_0 <= 4 and 300 < int_time):
                    int_time -= (600-(int_list_0 * 60 + int_list_1)) #야간 정액권 이용 시간 소진
                    int_list_0 = 10    # 야간 정액권 사용 처리
                    int_list_1 = 0     # 사용 후 0 대입
                    ans += 5000        # 정액권 이용 요금 합산

                # (조건이 거짓이라면 야간 정액권 사용 X) + (시간이 남을 때까지 계속 요금을 합함)
                else:
                    int_list_0 = ((int_list_0 + 1) % 24) #시간이 남은 경우 나머지 구하기
                    int_time -= 60 # 나머지 분 값을 1시간(60분) 사용으로 처리 
                    ans += 1000 # while loop의 조건을 검사하며 분 값이 남은 경우 요금 합산
                
            print(ans) # 최종 PC방 요금 출력

            