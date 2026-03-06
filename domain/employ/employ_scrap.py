from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from domain.employ.employ_schema import EmployScrap
import time


# 특정 키워드로 채용 정보를 가져와 EmployScrap 값들을 리턴하는 함수 정의
def get_employ_by_wanted(keyword):
    # Playwright 시작
    p = sync_playwright().start()

    # Chromium 브라우저 실행
    browser = p.chromium.launch(headless=False)

    # 새로운 페이지 열기
    page = browser.new_page()

    # 키워드를 이용하여 채용 정보 검색 결과 페이지 - 포지션 탭으로 이동
    page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")

    # 채용 카드가 로드될 때까지 최대 5초만 대기
    try:
        # 최대 5초만 대기
        page.wait_for_selector("[data-cy='job-card']", timeout=5000)
    except:
        print("job card selector not found within timeout, continuing...")

    # 무한 스크롤 페이지라 여러 번 스크롤 수행
    for _ in range(5):
        page.mouse.wheel(0, 3000)
        time.sleep(2)

    # 페이지의 HTML 내용 가져오기
    content = page.content()

    # 브라우저 닫기
    browser.close()

    # Playwright 종료
    p.stop()

    # BeautifulSoup을 사용하여 HTML 내용 파싱
    soup = BeautifulSoup(content, "html.parser")

    # 채용 정보가 담긴 요소들을 찾아서 jobs 리스트에 저장
    jobs = soup.find_all("div", class_="JobCard_container__zQcZs")
    print("scraped jobs:", len(jobs))

    # 채용 정보를 저장할 리스트 초기화
    jobs_db = []
    for job in jobs:
        a_tag = job.find("a")

        if not a_tag:
            continue

        position = a_tag.get("data-position-name")
        company_name = a_tag.get("data-company-name")

        # 추출된 정보를 데이터베이스에 저장할 형식으로 변환하여 jobs_db 리스트에 추가
        jobs_db.append(EmployScrap(keyword, company_name, position))

    # 데이터베이스에 저장할 채용 정보가 담긴 리스트 반환
    return jobs_db