#기본세팅
import datetime  #파이썬 기본 내장 날짜 도구


print("관리 시스템을 시작합니다!")
#프롬프트 데이터 관련
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

#DEF
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
        print_prompt_line(i, p) # ← 도장 찍기만 부탁!
#출력 도장 함수 (한 줄 찍기 전담)
def print_prompt_line(i, p):
    if p["즐겨찾기"]:
        star = "⭐"
    else:
        star = ""
    print(f"{i}. {star} {p['제목']} [{p['카테고리']}] ({p['날짜']})")
        
#3.카테고리별 조회_딕셔너리(키:내용) 그룹핑+필터링 조립
def prompt_category():
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return
    #그룹핑 : 카테고리별 몇 개인지 파악 + 동일한 내용이 생기면 같은 서랍장을 안만들고, 기존 서랍장에 append만
    category_dict = {}
    for p in prompts:
        category = p["카테고리"]
        if category not in category_dict:
            category_dict[category] = []
        category_dict[category].append(p)
    #카테고리 목록을 '번호 + 개수' 형태로 출력
    category_list = list(category_dict.keys())  # 딕셔너리 key들을 리스트로 변환
    print("--- 카테고리 목록 ---")
    for i, category in enumerate(category_list, start=1):
        print(f"{i}. {category} ({len(category_dict[category])}개)")
    # 번호 입력받기 (잘못된 입력 방어)
    choice = input("조회할 카테고리 번호: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(category_list)):
        print("올바른 번호를 입력해주세요.")
        return
    selected = category_list[int(choice) - 1]  # 번호 → 카테고리 이름

    # ③ 전체 리스트 기준 번호로 필터링 출력 (번호 일관성 유지!)
    print(f"=== {selected} ===")
    for i, p in enumerate(prompts, start=1):
        if p["카테고리"] == selected:
            print_prompt_line(i, p)   # 파둔 도장 재사용!

#4. 프롬프트 검색
def prompt_search():
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return
    keyword = input_not_empty("검색어를 입력하세요: ")
    count = 0
    for i, p in enumerate(prompts, start=1):
        if keyword in p["제목"] or keyword in p["내용"]:
            print_prompt_line(i, p)
            count += 1
    if count == 0:
        print("검색 결과가 없습니다.")

#번호 프롬프트 하나 고르기
def select_prompt():
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return None
    prompt_show()  # 전체 목록 출력
    choice = input("선택할 프롬프트 번호: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("올바른 번호를 입력해주세요.")
        return None
    return prompts[int(choice) - 1]  # 선택된 프롬프트 반환

#5. 프롬프트 상세 보기
def prompt_detail():
    selected_prompt = select_prompt()
    if selected_prompt is None:   
        return # 실패면 먼저 탈출 _얼리리턴
    print("=== 프롬프트 상세 정보 ===")
    print(f"제목: {selected_prompt['제목']}")
    print(f"내용: {selected_prompt['내용']}")
    print(f"카테고리: {selected_prompt['카테고리']}")
    print(f"즐겨찾기: {'예' if selected_prompt['즐겨찾기'] else '아니오'}")
    print(f"날짜: {selected_prompt['날짜']}")

#6. 즐겨찾기 관리
def manage_favorites():
    selected_prompt = select_prompt()
    if selected_prompt is None:
        return
    # 즐겨찾기 상태 토글
    selected_prompt["즐겨찾기"] = not selected_prompt["즐겨찾기"]
    status = "즐겨찾기에 추가되었습니다." if selected_prompt["즐겨찾기"] else "즐겨찾기에서 제거되었습니다."
    print(f"'{selected_prompt['제목']}' {status}")




#프로그램 메인 실행 코드
while True:
    show_menu()
    choice = input("메뉴를 선택하세요 (0-7): ")
    if choice == "1":
        prompt_add()
    elif choice == "2":
        prompt_show()
    elif choice == "3":
        prompt_category()
    elif choice == "4":
        prompt_search()
    elif choice == "5":
        prompt_detail()
    elif choice == "6":
        manage_favorites()
    elif choice == "7":
        print("즐겨찾기 목록")
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 입력해주세요.")


