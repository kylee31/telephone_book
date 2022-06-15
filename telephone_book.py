#while 무한루프
start=True
#딕셔너리 함수 초기값
info=dict()

#시작화면
print("***전화번호부***")
print()
print('======================================')
print("1. 번호 입력\n2. 번호 삭제\n3. 정보 검색\n4. 정보 수정\n5. 전체정보 보기\n6. 초기화\n7. 종료")

#while문
while (start==True):    #start의 값이 True일 때 실행

    print()
    choice=input(">>> 원하는 메뉴 번호를 입력해주세요: ") #메뉴 선택 (choice의 type은 str)
    print('--------------------------------------')

    #1. 전화번호 입력하기
    if choice=='1': #choice가 1일 때 실행 (choice type이 str이므로 '1'이라고 해주어야 한다)
        print("# 번호 입력 선택")
        count=int(input("@ 몇 명의 번호를 입력하시겠습니까?: "))
        for i in range(0,count,1):  #명 수 만큼 반복해준다
            print("["+str(i+1)+"번"+']')
            name=input("이름: ")
            number=input("번호: ")
            info[name]=number       #이름과 번호를 각각 키와 값으로 설정하여 딕셔너리에 추가

    #2. 전화번호 삭제
    elif choice=='2': #choice가 2일 때 실행
        print("# 번호 삭제 선택")
        count=int(input("@ 몇 명을 삭제하시겠습니까?: "))
        print()
        for i in range(0,count,1):  #명 수 만큼 반복해준다
            print("["+str(i+1)+"번"+']')
            who=input("삭제하고싶은 사람의 이름 입력: ")
            if(info.get(who)==None): #값이 비어있으면 정보가 없는 것이므로 경고 메세지 출력
                print("! 없는 정보입니다 !")
            else:
                del info[who]   #딕셔너리 삭제

    #3. 전화번호 찾기
    elif choice=='3': #choice가 3일 때 실행
         print("# 정보 검색 선택")
         count=int(input("@ 몇 명을 검색하시겠습니까?: "))
         print()
         for i in range(0,count,1):  #명 수 만큼 반복해준다
             print("["+str(i+1)+"번"+']')
             search=int(input("이름으로 검색은 1번, 번호로 검색은 2번: "))
             if(search==1):
                who=input("찾고싶은 사람의 이름 검색: ")
                if(info.get(who)==None):
                    print("! 없는 정보입니다 !")
                else:
                     print('*')
                     print('%s의 번호는 %s번 입니다' %(who,info[who]))
                     print()
             elif (search==2):
                who=input("찾고싶은 사람의 번호 검색: ")
                person=[a for a,b in info.items() if b==who] #내포함수
                print('*')
                print('%s번의 주인은 %s 입니다'%(who,person))
                print()
             else:
                 print('번호 선택 오류')
    
    #4. 전화번호 수정
    elif choice=='4': #choice가 4일 때 실행
        print("# 정보 수정 선택")
        count=int(input("@ 몇 명을 수정하시겠습니까?: "))
        print()
        for i in range(0,count,1):  #명 수 만큼 반복해준다
            print("["+str(i+1)+"번"+']')
            search=int(input("이름 수정은 1번, 번호 수정은 2번: "))
            if(search==1): 
                who=input("수정하고싶은 사람의 이름 입력: ")
                if(info.get(who)==None):
                    print("! 없는 정보입니다 !")
                else:
                    number=info[who]
                    del info[who]
                    change_name=input("수정 이름: ")
                    info[change_name]=number
                    print()

            elif(search==2):
                who=input("수정하고싶은 사람의 이름 입력: ")
                if(info.get(who)==None):
                    print("! 없는 정보입니다 !")
                else:
                    change_num=input("수정 번호: ")
                    info[who]=change_num
                    print()
            else:
                print('번호 선택 오류')

    #5. 전화번호 리스트 보기
    elif choice=='5': #choice가 5일 때 실행
        print("# 전체정보 보기 선택")
        first=list(info.keys()) 
        second=tuple(info.values())
        lst=list(zip(info.keys(),info.values()))
        lst.sort() #리스트 오름차순 정렬
        for i in range(0,len(lst),1):
            print(str(i+1),'. ',str(lst[i]))
        
    #6. 전화번호부 초기화
    elif choice=='6': #choice가 6일 때 실행
        print("# 초기화 선택")
        q=input("@ 전화번호부를 초기화하시겠습니까? (yes/no) ")
        if(q=='yes'):
            info.clear() #딕셔너리 전체삭제
            print("초기화 되었습니다")
        elif(q=='no'):
            print('취소 되었습니다')
        else:
            print('입력 단어 오류')
        
    #7. 프로그램 종료
    elif choice=='7': #choice가 7일 때 실행
        print("# 종료 선택")
        q=input("@ 종료 하시겠습니까? (yes/no) ")
        if(q=='yes'):
            print("\n******종료******")
            #break 대신 start=False도 가능하다!
            break #while문 탈출
        elif(q=='no'):
            continue
        else:
            print('입력 단어 오류')

    #예외처리
    else:
        print("번호를 다시 확인해주세요")
