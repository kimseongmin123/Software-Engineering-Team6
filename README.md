## Test Data Set 생성 방법

https://m.blog.naver.com/iireh/222511526229

1. 해당 블로그의 xlsx 파일 다운로드

2. Software-Engineering-Team5/data/hackers_test 폴더에 hackers_test_raw 의 이름과 csv 파일 형태로 저장(utf-8가 아닌 그냥으로, 경고창 모두 무시, 계속)

3. powershell에서 python -m venv venv 명령어 입력하여 가상 환경 생성 (최상위 폴더 바로 밑으로 생성되야 합니다)

4. Ctrl + Shift + P로 검색창 열고 interpreter 입력 -> Python: 인터프리터 설정 클릭 -> 인터프리터 경로 입력 클릭 -> 찾기 클릭 후 프로젝트 폴더의 venv/Scripts/python.exe으로 인터프리터 설정

5. pip install -r requirements.txt 명령어로 필요 패키지 다운

6. hackers_test_processing.py 실행하면 hackers_test_processed.json 파일이 생성됩니다
