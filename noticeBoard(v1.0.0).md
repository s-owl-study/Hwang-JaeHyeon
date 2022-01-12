# 게시판 구상 계획서

## 페이지별 존재해야 하는 기능 설계(전체적인 구조를 표현하는 예시화면 첨부함)


1. 리스트 형식으로 게시 정보가 보이며, 정보 교류가 목적인 **게시판 메인 페이지**
 
    * 화면(테이블 형식으로 보이게끔 작성되어야 함, 최신 순서로 나타나게끔 처리함)

      * 번호(INT, Primary Key)

      * 제목(VARCHAR(60))

      * 작성자(VARCHAR(20))

      * 작성일(DATETIME)
      
  ![](https://peterkimlab.github.io/assets/images/bbs_14_main.png)

2. 게시판 메인 페이지에서 글쓰기 버튼을 누르고 들어온 **글쓰기 페이지**

    * 상단 공간

      * **메인** 페이지 

      * 게시판으로 이동 가능한 **게시판**
    
    * 화면

      * 설명 : 게시판 글쓰기
      
      * 상단 input박스 : 글 제목을 입력할 수 있는 박스
      * 하단 input박스 : 글의 내용을 입력할 수 있는 박스

      * 오른쪽 맨 하단에 글 등록하기 버튼 배치함

![](https://peterkimlab.github.io/assets/images/bbs_10_write.png)

3. 게시판 메인 페이지에서 게시판 목록이 20개 이상일 경우에 다음 페이지가 추가된 페이지
 
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
      
      * 왼쪽 하단에 다음 버튼 배치함(버튼 구별을 위해 초록색으로 설정)
      * 다음 버튼을 누르면, 그 다음의 최신 순으로 20개로 화면이 변경되어 표시되며, 동시에 이전 버튼 역시 배치함.

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



