# 가상환경 설정(윈도우 cmd 기준)
## python -m venv .
## cd Scripts

# 가상환경 활성화
## activate.bat

# 패키지 설치
## pip install requests (requests 패키지 인스톨)
## pip list (패키지 리스트)
## python -m pip install --upgrade pip (pip 업그레이드)
## pip install --upgrade requests (requests 패키지 업그레이드)
## pip uninstall requests (requests 패키지 언인스톨)

# 가상환경 비활성화
## deactivate.bat

### challenge에서 설치한 패키지
### requests
### beautifulsoup4
### babel
### csv
### flask

# 경로에러 발생시
# 오류메시지 : Faltal error in launcher: Unable to create process using '' install flask
# 해결방법 : 앞에 python -m 을 붙여준다
# ex) python -m pip install falsk