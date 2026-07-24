print("관리 시스템을 시작합니다!")
prompts = []
prompt1 = {
    "제목": "오늘의 학습 정리",
    "내용": "오늘 배운 내용을 3줄로 요약하고, 복습 질문 2개를 만들어줘.",
    "카테고리": "학습 정리",
    "즐겨찾기": True,
    "날짜": "2026-07-24"
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
    "내용": "너는 기업의 홍보 담당자자야. 기업의 고객층 요구에 맞는 홍보물을 작성,등록해줘.",
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

#프로그램 메인 실행 코드
while True:
    show_menu()
    choice = input("메뉴를 선택하세요 (0-7): ")
    if choice == "1":
        print("프롬프트 추가")
    elif choice == "2":
        print("프롬프트 목록")
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