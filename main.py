#기본세팅
import datetime  #파이썬 기본 내장 날짜 도구

#프롬프트 데이터 관련
print("관리 시스템을 시작합니다!")
prompts = []
prompt1 = {
    "제목": "오늘의 학습 정리",
    "내용": "오늘 배운 내용을 3줄로 요약하고, 복습 질문 2개를 만들어줘.",
    "카테고리": "학습 정리",
    "즐겨찾기": True,
    "날짜": "2025-01-14"
}
prompt2 = {
    "제목": "프롬프트 관리 프로그램",
    "내용": "너는 개인의 프롬프트 관리자야. 개인 사용자의 프롬프트 활용에 대한 조언을 해줘.",
    "카테고리": "프롬프트 관리",
    "즐겨찾기": False,
    "날짜": "2025-01-15"
}
prompt3 = {
    "제목": "sns 홍보 관리자",
    "내용": "너는 기업의 홍보 담당자야. 기업의 고객층 요구에 맞는 홍보물을 작성,등록해줘.",
    "카테고리": "홍보물 생성",
    "즐겨찾기": False,
    "날짜": "2025-01-16"
}
prompts.append(prompt1)
prompts.append(prompt2)
prompts.append(prompt3)


print("저장된 프롬프트 개수:", len(prompts))  #len() 함수를 사용하여 리스트의 길이를 출력_개수 확인

#메뉴 함수 세팅
def show_menu():
    print("==== 프롬프트 관리 프로그램 ====")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


#프롬프트 추가 세팅 관련 _B방법(+공란일 때 요구사항 반영)
#prompts = [] #제일 위쪽에 이미 리스트가 있으니 생략.
def input_not_empty(안내문구):
    while True:
        user_input = input(안내문구)
        if user_input.strip() == "":
            print("입력값이 비어있습니다. 다시 입력해주세요.")
        else:
            return user_input
def prompt_add():
    title = input_not_empty("제목: ")
    content = input_not_empty("내용: ")
    category = input_not_empty("카테고리: ")
    new_prompt = {
        "제목": title,
        "내용": content,
        "카테고리": category,
        "즐겨찾기": False,
        "날짜": datetime.date.today().isoformat()  #오늘 날짜를 자동으로 입력   
    }
    prompts.append(new_prompt)
    print(f"'{title}' 프롬프트가 추가되었습니다.")

#2.프롬프트 목록 -> prompt_show() 만들기 
def prompt_show():
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, start=1):
        if p["즐겨찾기"]:
            star = "⭐"
        else:
            star = ""
        print(f"{i}. {star} {p['제목']} [{p['카테고리']}] ({p['날짜']})")

        



#프로그램 메인 실행 코드
while True:
    show_menu()
    choice = input("메뉴를 선택하세요 (0-7): ")
    if choice == "1":
        prompt_add()
    elif choice == "2":
        prompt_show()
    elif choice == "3":
        print("카테고리별 조회")
    elif choice == "4":
        print("프롬프트 검색")
    elif choice == "5":
        print("프롬프트 상세 보기")
    elif choice == "6":
        print("즐겨찾기 관리")
    elif choice == "7":
        print("즐겨찾기 목록")
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 입력해주세요.")


