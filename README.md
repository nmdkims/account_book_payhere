# 가계부 API 개발

## ✅ 소개
- 고객은 본인의 소비내역을 기록/관리하고 싶습니다.
- 기본적인 회원가입 로그인 로그아웃을 지원하고 가계부와 관련된 CRRUD 기능을 제공할 수 있는 API를 개발합니다.

<br>

## 📌 과제 분석
1. 회원가입시 커스텀 유저모델을 이용하여 이메일을 통한 회원가입으로 설정 <br>
  1-1 AbstractBaseUser 상속 받아서 커스텀
2. 로그인, 로그아웃 기능 <br>
  2-1 구현의 마지막 제약조건에 따라 토큰을 발행해서 인증 제어하는 방식으로 구현 예정 - simple jwt 사용 예정
3. 가계부와 관련된 CRRUD기능 로그인 되어있는 사용자만 접근할 수 있게 접근 권한 설정 필요 - permission classes
4. Docker를 이용한 배포 

<br>

## 📃 API 설계
![image](https://user-images.githubusercontent.com/89897944/189605994-3dfaf25e-4017-416b-87f0-d125f27d130a.png)

로그인 로그아웃의 구성을 기본적인 장고에서 제공하는 로그아웃으로 로그아웃을 구현한것에 추가적으로 백엔드 쪽에서 refresh token을 블랙리스트에 등록해서 로그아웃 시키는 방법을 구현하였습니다.

<br>

## 📦 모델링
<img width="867" alt="image" src="https://user-images.githubusercontent.com/89897944/188925423-080a3e7c-e81e-4c3b-af7e-62f1799a9fce.png">


<br>

## 🛠 사용 기술
- API<br>
![python badge](https://img.shields.io/badge/Python-3.9-%233776AB?&logo=python&logoColor=white)
![django badge](https://img.shields.io/badge/Django-4.0.6-%23092E20?&logo=Django&logoColor=white)
- DB<br>
![mysql badge](https://img.shields.io/badge/MySQL-5.7-%234479A1?&logo=MySQL&logoColor=white)

- 배포<br>
![aws badge](https://img.shields.io/badge/AWS-EC2-%23FF9900?&logo=Amazon%20EC2&logoColor=white)
![docker badge](https://img.shields.io/badge/Docker-20.10.17-%232496ED?&logo=Docker&logoColor=white)
![nginx badge](https://img.shields.io/badge/Nginx-1.23.0-%23009639?logo=NGINX&locoColor=white)
![gunicorn badge](https://img.shields.io/badge/Gunicorn-20.1.0-%23499848?logo=Gunicorn&locoColor=white)
- ETC<br>
  <img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=Git&logoColor=white"/>
  <img src="https://img.shields.io/badge/Github action-2088FF?style=flat&logo=Github%20Actions&logoColor=white"/>

<br>

## :black_nib: 이슈 관리
깃허브의 이슈기능을 이용하여 Projects 기능의 Kanban board와 연결 태스크 관리를 합니다.

<br>

## 🕵️‍ 깃 & 코드 컨벤션
[깃 & 코드 컨벤션](https://github.com/nmdkims/account_book_payhere/wiki/Git-and-Code-Convention)

<br>

## 💡 Pre-commit 린트와 포매터
![image](https://user-images.githubusercontent.com/89897944/188915566-7afc987f-a29a-440e-b936-26f0822dad52.png)

Formatter
- isort
- black

Lint
- flake8

로컬에선 pre-commit 라이브러리 사용으로 커밋 전 세가지 라이브러리를 한번에 실행하고 통과되지않을시 커밋이 불가능합니다.
레포지토리에는 github action으로 다시 한번 체크 후, 통과되지 않으면 merge가 block됩니다.

<br>

## 🌎 배포

<br>

## ✔️ Test Case 

<br>


