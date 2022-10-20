# 게임 <마비노기> 요리 도감 사이트
게임 <마비노기>의 도감 컨텐츠 중 하나인 요리 수집 현황을 기록하는 사이트

임시 배포 http://sina0525.pythonanywhere.com/

    id:test@test.com / pw:12341234로 테스트 가능합니다.
    배포 환경인 PythonAnywhere에선 celery 이용을 지원하지 않는 관계로,
    임시 배포 사이트에선 비동기 시스템을 구축하여 개발한 비밀번호 찾기 기능은 사용할 수 없습니다.
개인 토이프로젝트 / 2개월

- 개인의 도감 기록 현황 저장을 위해 유저 시스템 개발
- 이메일 전송을 위해 celery로 비동기 시스템 개발
- ORM을 통해 데이터 조회, 생성
- 음식 혹은 재료 이름으로 검색하고 요리 방법과 수집 현황으로 필터링하는 검색 및 필터링 시스템 개발
- dotenv로 개발 환경과 배포 환경 분리
- Notion을 사용하여 이슈 보드 관리
## 개발 목적
게임 <마비노기>의 요리 수집 컨텐츠는 항목을 전부 수집하지 않으면, <ins>'수집'</ins>과 <ins>'높은 등급 수집'</ins>을 구분할 수 없는 시스템입니다.
이에 불편함을 느껴 정확한 요리 수집 현황을 기록할 수 있도록 기획하여 사이트 개발을 진행하였습니다.

## 기술 스택
Python, Flask, celery, MySQL, git

## 사이트
* 회원가입, 로그인, 로그아웃, 비밀번호 찾기, 아이디 저장 등의 유저 시스템
<img src="https://user-images.githubusercontent.com/45452033/196888919-faed5bb0-bc3b-4c13-b99e-6aa3e208c998.png">

* 게임 속 요리 항목을 미수집/수집/5성 수집 3가지의 수집 상태로 기록 가능
<img src="https://user-images.githubusercontent.com/45452033/196888561-a1bc5fad-2802-43b2-929d-5eb89e562a18.png">

* 음식 이름 혹은 재료 이름에 따라 검색하거나, 요리 방법 혹은 수집 상태에 따라 필터링 가능
<img src="https://user-images.githubusercontent.com/45452033/196889194-699cc31f-c33a-4325-88c8-38e2725757b9.png">

## 추가 구현 필요
* 새로 요리 항목을 추가하는 admin site
* 띄어쓰기 무관 검색

## 기타
* Notion 이슈 보드
https://rhyun9584.notion.site/61d869d022e6467fb73baebba871da8f?v=292df6caab7f4997a6d2b8f861e9d492
