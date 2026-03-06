# FastAPI Study
FastAPI를 학습하기 위한 개인 프로젝트입니다.
Python 기반의 FastAPI Framework를 사용하여 REST API를 구현하고,
wanted 채용공고 사이트를 크롤링하고 SQLITE DB에 저장하는 간단한 서비스입니다.

# Tech Stack
- Python
- FastAPI
- Uvicorn

# 사용법(Terminal)
1. source .venv/bin/activate (비활성화를 원할경우 deactivate)
2. uvicorn main:app --reload
3. 로그에 나오는 url을 복사후 웹 사이트에 붙여넣기 (URL + /docs)
4. PUT에서 Try it now -> keyword에 원하는 채용 정보 입력 후 execute 클릭
5. 결과를 확인하고 싶으면 sqlite3 fastapi-scrap.db -> select * from employ;
