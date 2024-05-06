## 파일 구조
src: 각자 구현할 기능을 수행하는 .py 파일과 소스 코드<br>
data: 출판사 별 원본 데이터, 데이터 변환 및 정제 코드, 사용할 json파일

showdata.py 파일은 데이터 저장 구조 확인용이며 추후 삭제 예정

## 레포지토리 클론 직후 해야할 것
1. powershell에서 python -m venv venv 명령어 입력하여 가상 환경 생성 (최상위 폴더 바로 밑으로 생성되야 합니다)

2. powershell에서 venv/Scripts/activate 명령어 입력하여 가상 환경 실행 (Mac의 경우 venv/bin/activate)

3. Ctrl + Shift + P로 검색창 열고 interpreter 입력 -> Python: 인터프리터 설정 클릭 -> 인터프리터 경로 입력 클릭 -> 찾기 클릭 후 프로젝트 폴더의 venv/Scripts/python.exe으로 인터프리터 설정

4. powershell에서 pip install -r requirements.txt 명령어로 필요 패키지 다운

## Hackers Test Data Set 생성 방법
1. 해당 블로그의 xlsx 파일 다운로드 https://m.blog.naver.com/iireh/222511526229

2. Software-Engineering-Team5/data/hackers_test 폴더에 hackers_test_raw로 이름 수정 후 csv 파일 형태로 저장 (utf-8가 아닌 그냥으로, 경고창 모두 무시, 계속)

3. hackers_test_processing.py 실행하면 hackers_test_processed.json 파일이 생성됩니다
