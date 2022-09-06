# 가계부 API 개발


## ✅ 소개
- 고객은 본인의 소비내역을 기록/관리하고 싶습니다.
- 기본적인 회원가입 로그인 로그아웃을 지원하고 가계부와 관련된 CRRUD 기능을 제공할 수 있는 API를 개발합니다.

<br>

## 📌 과제 분석
<div>
<details>
<summary>과제소개</summary> 
<div markdown="1">
🗣고객은 본인의 소비내역을 기록/관리하고 싶습니다.<br>
아래의 요구사항을 만족하는 DB 테이블과 REST API를 만들어주세요.
</div>
</details>

<details>
<summary>요구사항</summary> 
<div markdown="1">
<ul>
  <li>고객은 이메일과 비밀번호 입력을 통해서 회원 가입을 할 수 있습니다.</li>
  <li>고객은 회원 가입이후, 로그인과 로그아웃을 할 수 있습니다.</li>
  <li>고객은 로그인 이후 가계부 관련 아래의 행동을 할 수 있습니다.</li>
    <ul>
      <li>가계부에 오늘 사용한 돈의 금액과 관련된 메모를 남길 수 있습니다.</li>
      <li>가계부에서 수정을 원하는 내역은 금액과 메모를 수정 할 수 있습니다.</li>
      <li>가계부에서 삭제를 원하는 내역은 삭제 할 수 있습니다.</li>
      <li>삭제한 내역은 언제든지 다시 복구 할 수 있어야 한다.</li>
      <li>가계부에서 이제까지 기록한 가계부 리스트를 볼 수 있습니다.</li>
      <li>가계부에서 상세한 세부 내역을 볼 수 있습니다.</li>
    </ul>
  <li>로그인하지 않은 고객은 가계부 내역에 대한 접근 제한 처리가 되어야 합니다.</li>
</ul>
</div>
</details>
</div>

#### ➡️ 분석결과
1. 회원가입시 커스텀 유저모델을 이용하여 이메일을 통한 회원가입으로 설정
  1-1 AbstractBaseUser 상속 받아서 커스텀
2. 로그인, 로그아웃 기능 
  2-1 구현의 마지막 제약조건에 따라 토큰을 발행해서 인증 제어하는 방식으로 구현 예정 - simple jwt 사용 예정

<br>

## 🛠 사용 기술
- API<br>
![python badge](https://img.shields.io/badge/Python-3.9-%233776AB?&logo=python&logoColor=white)
![django badge](https://img.shields.io/badge/Django-4.0.6-%23092E20?&logo=Django&logoColor=white)
- DB<br>
![mysql badge](https://img.shields.io/badge/MySQL-8.0.29-%234479A1?&logo=MySQL&logoColor=white)

- 배포<br>
![aws badge](https://img.shields.io/badge/AWS-EC2-%23FF9900?&logo=Amazon%20EC2&logoColor=white)
![docker badge](https://img.shields.io/badge/Docker-20.10.17-%232496ED?&logo=Docker&logoColor=white)
![nginx badge](https://img.shields.io/badge/Nginx-1.23.0-%23009639?logo=NGINX&locoColor=white)
![gunicorn badge](https://img.shields.io/badge/Gunicorn-20.1.0-%23499848?logo=Gunicorn&locoColor=white)
- ETC<br>
  <img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=Git&logoColor=white"/>
  <img src="https://img.shields.io/badge/Github action-2088FF?style=flat&logo=Github%20Actions&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jira-0052CC?style=flat&logo=Jira&logoColor=white"/>

<br>

## :black_nib: 이슈 관리
깃허브의 이슈기능을 이용하여 Projects 기능의 Kanban board와 연결 태스크 관리를 합니다.

<br>

## ✨🍰✨ 코드 컨벤션
Commit message
commit message template을 설정하고 따릅니다.
 --- 제목(title) - 50자 이내로 ---
 <타입(type)> <제목(title)>
 예시(ex) : Docs : #1 README.md 수정
 --- 본문(content) - 72자마다 줄바꾸기  ---
 예시(ex) :
 - Workflow
 1. 커밋 메시지에 대한 문서 제작 추가.
 2. commit message docs add.
 --- 꼬리말(footer) ---
 <타입(type)> <이슈 번호(issue number)>
 예시(ex) : Fix #122
 --- COMMIT END ---
 <타입> 리스트
   Init    : 초기화
   Feat    : 기능추가
   Add     : 내용추가
   Update  : 기능 보완 (업그레이드)
   Fix     : 버그 수정
   Hotfix  : 긴급한 내용의 수정
   Refactor: 리팩토링
   Style   : 스타일 (코드 형식, 세미콜론 추가: 비즈니스 로직에 변경 없음)
   Docs    : 문서 (README.md, ignore파일 추가(Add), 수정, 삭제)
   Test    : 테스트 (테스트 코드 추가, 수정, 삭제: 비즈니스 로직에 변경 없음)
   Chore   : 기타 변경사항 (빌드 스크립트 수정 등)
   Rename  : 이름(파일명, 폴더명, 변수명 등)을 수정하거나 옮기는 작업만인 경우
   Remove  : 파일을 삭제하는 작업만 수행한 경우  
 ------------------
     제목 첫 글자를 대문자로
     제목은 명령문으로
     제목 끝에 마침표(.) 금지
     제목과 본문을 한 줄 띄워 분리하기
     본문은 "어떻게" 보다 "무엇을", "왜"를 설명한다.
     본문에 여러 줄의 메시지를 작성할 땐 "-" 혹은 "번호"로 구분
 ------------------ 
Branch Strategy
main-develop-feature 의 구성을 따릅니다.
기능에 맞는 feature 브랜치를 만들어서 작업을 진행합니다.
작업이 끝나면 develop 브랜치에 내용을 올리도록 하며 이는 배포 브랜치로 사용할 예정입니다.
배포를 포함한 모든 내용에 문제가 없다면 이는 main 브랜치로 병합시키도록 합니다.

feature/이슈번호
각자 맡은 기능을 개발하는 브랜치 입니다.
브랜치 이름은 feature/이슈번호로 하고, 완성이 되었을 때 develop 브랜치에 병합합니다 

main
모든 내용이 문제가 없을 경우에는 main 브랜치로 코드를 병합시켜서 보관합니다.


✅ Code Convention
Class
Pascal case
Model
snake case
Function
snake case
Variables
snake case

주석처리
Class, Function의 주석은 class, function 하단에 작성
주석으로 Assignee 작성 : 개인 프로젝트이지만 작성합니다.
API의 경우, 상단에 주석으로 url 주소 작성
<example>

- api/v1/jobs/<int:id>/run
class JobTaskView(APIView):
"""
Assignee : 김아무개
"""

"""
여러 줄인 경우
이와같이 주석을
답니다.
너무 길지 않게 작성합니다.
"""

"""한줄로 작성시에는 이와같이 작성"""

## Pre-commit 린트와 

Formatter
- isort
- black

Lint
- flake8

로컬에선 pre-commit 라이브러리 사용으로 커밋 전 세가지 라이브러리를 한번에 실행하고 통과되지않을시 커밋이 불가능합니다.
레포지토리에는 github action으로 다시 한번 체크 후, 통과되지 않으면 merge가 block됩니다.

<br>

## 🌟 API 명세서

<img width="1008" alt="image" src="https://user-images.githubusercontent.com/95380638/178380770-64ffcf20-a0da-484c-b05a-49ece67a68d2.png">

❗️ '/api/v1/accountbooks' api 호출시, 가계부 목록과, 각 가계부에 기록된 내역들을 함께 보여줍니다. <br>
❗️ '/api/v1/accountbooks' api에 <b>status=delete</b>파라미터를 추가하면 삭제된 가계부 목록을 보여줍니다.<br>
❗️ '/api/v1/accountbooks' api를 `POST`로 요청 시, 가계부를 생성합니다.<br>
❗️ 가계부 목록, 가계부 단건 조회할 때, 가계부에 기록된 금액은 <b>balance</b>, 해당 일자까지의 금액을 합산한 값은 <b>total_balance</b>필드를 생성하여 보여줍니다. <br>
❗️ 가계부, 가계부 기록 삭제 api의 http 메소드가 `PATCH`인 이유는 <b>soft delete</b>하기 위함입니다. <br>
&nbsp; &nbsp; &nbsp; 삭제된 내역은 언제든지 복구할 수 있어야 하기 때문에 DB에서 실제로 데이터를 삭제하는것이 아닌, 각 모델의 <b>is_deleted</b>필드를 False 에서 True로 수정하게 됩니다. <br>
❗️ 가계부 단건 및 가계부 기록 단건 복구 시, <b>recovery</b>를 붙여 구분합니다.<br>
❗️ 가계부, 가계부 기록 수정 api의 메소드는 `PUT`이지만 코드상 <b>partial</b> 옵션을 주어 부분적 수정도 가능합니다.<br>
❗️ 가계부, 가계부 기록은 is_deleted 필드가 False인 것만(삭제되지 않은 것만)유저에게 보여줍니다. <br>


<br>
<br>
<details>
<summary>🚀 API 호출 테스트 결과</summary>
<div markdown="1">
<ul>
  <li>
    <p>회원가입</p>
    <img width="798" alt="스크린샷 2022-07-09 오후 11 51 42" src="https://user-images.githubusercontent.com/83942213/178110954-157208b0-f350-4915-a029-c37c54099d9e.png">
  </li>
  <li>
    <p>로그인</p>
    <img width="790" alt="스크린샷 2022-07-09 오후 11 53 38" src="https://user-images.githubusercontent.com/83942213/178110998-47e3db4b-3826-4185-9e46-f0a11e64e34d.png">
  </li>
  <li>
    <p>회원정보 수정</p>
    <img width="792" alt="스크린샷 2022-07-09 오후 11 57 20" src="https://user-images.githubusercontent.com/83942213/178111116-b048464f-7d5d-43f3-8cde-27c0b58b3f8c.png">
  </li>
  <li>
    <p>회원 탈퇴(soft delete)</p>
    <img width="793" alt="스크린샷 2022-07-09 오후 11 59 06" src="https://user-images.githubusercontent.com/83942213/178111164-131cdbd2-cdef-41b9-8d58-e435cfd098ad.png">
  </li>
  <li>
    <p>가계부 목록 조회</p>
    <img width="888" alt="image" src="https://user-images.githubusercontent.com/95380638/177975927-e4fe4030-36ae-4676-bda5-331b92d05b0f.png">
  </li>
  <li>
    <p>삭제된 가계부 목록 조회</p>
    <img width="897" alt="image" src="https://user-images.githubusercontent.com/95380638/177976069-3324a7f8-a56b-4390-af1c-345fea52ab1d.png">
  </li>
  <li>
    <p>가계부 생성</p>
    <img width="828" alt="image" src="https://user-images.githubusercontent.com/95380638/177974294-501d9934-c5f0-4fe7-8b70-3f32283fa011.png">
  </li>
  <li>
    <p>가계부 조회</p>
    <img width="876" alt="image" src="https://user-images.githubusercontent.com/95380638/177974570-beb1771c-2c75-4c2f-b176-6cf5a12a91e8.png">
  </li>
  <li>
    <p>가계부 수정</p>
    <img width="871" alt="image" src="https://user-images.githubusercontent.com/95380638/177974449-38854e04-8890-4d0d-9b67-dbbed903901b.png">
  </li>
  <li>
    <p>가계부 삭제</p>
    <img width="871" alt="image" src="https://user-images.githubusercontent.com/95380638/177974627-2cb6b140-80a6-42c8-a38d-a1f1ba1524c8.png">
  </li>
  <li>
    <p>가계부 복구</p>
    <img width="877" alt="image" src="https://user-images.githubusercontent.com/95380638/177974744-f4525881-9a90-49cb-811c-617cbf5621a5.png">
    </li>
  <li>
    <p>가계부 기록 생성</p>
    <img width="877" alt="image" src="https://user-images.githubusercontent.com/95380638/177974825-4f15f3de-c781-45aa-a79f-c3532de8efb1.png">
  </li>
  <li>
    <p>가계부 기록 조회</p>
    <img width="881" alt="image" src="https://user-images.githubusercontent.com/95380638/177974942-6ba78e84-ac37-4e5d-b18a-2f33f9c132d5.png">
  </li>
  <li>
    <p>가계부 기록 수정</p>
    <img width="868" alt="image" src="https://user-images.githubusercontent.com/95380638/177975005-5eed224a-63d0-46b8-adbf-fbe226e242d7.png">
  </li>
  <li>
    <p>가계부 기록 삭제</p>
    <img width="874" alt="image" src="https://user-images.githubusercontent.com/95380638/177975062-35706646-c89a-4081-8d4b-580de38a1702.png">
  </li>
  <li>
    <p>가계부 기록 복구</p>
    <img width="875" alt="image" src="https://user-images.githubusercontent.com/95380638/177975102-a0e5433d-3759-4ac8-9a15-6197b35d287b.png">
  </li>
</ul>
</div>
</details>

<br>

## 📋 ERD
<img width="802" alt="erd" src="https://user-images.githubusercontent.com/76423946/177966917-96fa08b7-8849-4443-ae4f-d67421e19dc1.png">

- User : 유저 정보를 저장합니다.
- AccountBook : 가계부 정보를 저장합니다.
- AccountBookRecord : 각 가계부에 수입, 지출 내역을 저장합니다.

❗️ User 모델은 장고의 기본 User 모델을 그대로 사용하지 않고 커스텀하였습니다. <br>
❗️ 한 명의 유저는 여러개의 가계부를 관리할 수 있도록 User 모델과 AccountBook(가계부)모델은 1:N 관계입니다. <br>
❗️ AccountBook 모델과 AccountBookRecord 모델은 1:N 관계로, 한 개의 가계부에 여러 내역을 기록할 수 있습니다. <br>

<br>

## 🌎 배포
Docker, NginX, Gunicorn을 사용하여 EC2 서버에 배포하였습니다. <br>
#### ➡️ [기본 URL](http://54.180.109.16/) <br>
기본 URL은 404 페이지 입니다. <br>
❗️ 현재 비용의 문제로 서버 접속은 불가능합니다.

<br>

## ✔️ Test Case 
서비스하는 모든 API에 대한 TESTCASE 작성 및 수행
![image](https://user-images.githubusercontent.com/89897944/177983110-f846cef3-589e-49ca-b3cf-5a314d4b8cf2.png)

<br>

## 👋 TeamH Members
|Name|Task|Github|
|-----|----|-------|
|고희석|모델링, 가계부 관련 API 개발|https://github.com/GoHeeSeok00| 
|김민지|배포|https://github.com/my970524|
|김상백|가계부 관련 API 개발|https://github.com/tkdqor|
|김훈희|테스트 케이스 작성|https://github.com/nmdkims| 
|이정석|개발환경 셋팅, 유저 관련 API 개발|https://github.com/sxxk2|

➡️ [Payhere 과제 노션 페이지](https://www.notion.so/fa0128e74291482fb103695f735f1d0a)

