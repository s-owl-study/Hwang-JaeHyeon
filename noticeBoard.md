# 게시판 구상 계획서

## 페이지별 존재해야 하는 기능 설계

1. 게시판 메인 페이지
 
    * 상단 공간

      * **메인** 페이지 

      * 게시판으로 이동 가능한 **게시판** 

      * 오른쪽에 본인 확인을 위한 **로그인** 

      * 오른쪽 맨 끝에 회원가입을 위한 **회원 등록** 버튼

    * 화면

      * 게시판 설명 : 이 게시판은 프로젝트 연습을 위한 게시판 홈페이지 입니다.

    ![](https://peterkimlab.github.io/assets/images/bbs_14_main.png)

2. 본인 확인을 위한 로그인 페이지
    * 상단 공간
      * **메인** 페이지 

      * 기존에 등록이 되지 않아 로그인이 불가능한 경우를 위한 **회원등록** 버튼
    
    * 화면

      * 설명 : 로그인
      
      * 아이디 작성을 위한 input 박스
      * 비밀번호 작성을 위한 
      input 박스(단, 보안을 위해 입력시 '*'로 보이도록 처리함)
    
    ![](https://peterkimlab.github.io/assets/images/bbs_2_login.png)


3. 회원이 아닐 경우 작성을 위한 회원등록 페이지 
    * 상단 공간
      * **메인** 페이지 

      * 기존에 회원일 경우 로그인 페이지로 이동 가능한 **로그인** 버튼
    
    * 화면

      * 설명 : 회원등록
      
      * 새로운 아이디 작성을 위한 input 박스
      * 비밀번호 작성을 위한 
      input 박스(단, 보안을 위해 입력시 '*'로 보이도록 처리함)

      * 이름을 작성할 수 있는 input 박스

      * 남자와 여자 중 하나만 선택가능하게끔 작성된 **남자**와 **여자** 버튼

      * 개인 이메일을 입력할 수 있는 input 박스

      * 모두 작성 완료시 회원등록 신청을 위한 **회원등록** 버튼


4. 리스트 형식으로 게시 정보가 보이는 **게시판 메인 페이지**
 
    * 상단 공간

      * **메인** 페이지 
      
      * 현재 페이지임을 명시하는 **게시판**

      * 오른쪽 맨 끝에 접속 종료를 위해 나갈 수 있는 **나가기** 버튼
        * "나가시겠습니까?" 를 화면에 출력하고 예, 아니오 버튼을 표시함
    
    * 화면(테이블 형식으로 보이게끔 작성되어야 함, 최신 순서로 나타나게끔 처리함)

      * 번호(INT, Primary Key)

      * 제목(VARCHAR(60))

      * 작성자(VARCHAR(20))

      * 작성일(DATETIME)


    ![](https://peterkimlab.github.io/assets/images/bbs_8_bbs.png)


5. 게시판 메인 페이지에서 글쓰기 버튼을 누르고 들어온 **글쓰기 페이지**

    * 상단 공간

      * **메인** 페이지 

      * 게시판으로 이동 가능한 **게시판**
    
    * 화면

      * 설명 : 게시판 글쓰기
      
      * 상단 input박스 : 글 제목을 입력할 수 있는 박스
      * 하단 input박스 : 글의 내용을 입력할 수 있는 박스

      * 오른쪽 맨 하단에 글 등록하기 버튼 배치함

    ![](https://peterkimlab.github.io/assets/images/bbs_10_write.png)


6. 게시판 메인 페이지에서 게시판 목록이 20개 이상일 경우에 다음 페이지가 추가된 페이지

    * 상단 공간

      * **메인** 페이지 

      * 게시판으로 이동 가능한 **게시판**
    
    * 화면

      * 설명 : 게시판 글쓰기
      
      * 상단 input박스 : 글 제목을 입력할 수 있는 박스
      * 하단 input박스 : 글의 내용을 입력할 수 있는 박스

      * 오른쪽 맨 하단에 글 등록하기 버튼 배치함
      
      * 왼쪽 하단에 다음 버튼 배치함(버튼 구별을 위해 초록색으로 설정)

    ![](https://peterkimlab.github.io/assets/images/bbs_11_list.png)


## 데이터베이스
| pk 여부 | name          | type         |
|---------|---------------|--------------|
|    O    | boardId       | int          |
|         | boardTitle    | varchar(60)  |
|         | memberName    | varchar(20)  |
|         | writeTime     | DATETIME     |
|         | boardContents | varchar(220) |
|         | memberId      | varchar(40)  |
|         | memberPw      | varchar(45)  |

* 테이블명 : noticeBoardTable

* column의 갯수 : 7

* Primary key : 글 번호(boardId)



