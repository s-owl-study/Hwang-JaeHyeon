# 5주차 : MVC(Model-View-Controller), DAO(Data Access Object), DTO(Data Transfer Object)

## **MVC(Model-View-Controller)**

* MVC(Model-View-Controller) : 어플리케이션, 프로젝트 등의 결과물을 구성할 때, 구성 요소들을 Model, View, Controller의 세 가지 역할로 구분하여 처리하는 개발 방법론이다.
![그림1](https://mblogthumb-phinf.pstatic.net/MjAxNzAzMjVfMjUw/MDAxNDkwNDM4NzI4MTIy.4ZtITJJKJW_Nj1gKST0BhKMAzqmMaYIj9PobYJMFD4Ig.xTHT-0qyRKXsA4nZ2xKPNeCxeU2-tLIc-4oyrWq5WBgg.PNG.jhc9639/mvc_role_diagram.png?type=w800)

출처 : <https://mblogthumb-phinf.pstatic.net>

* 모델(Model) : 프로젝트의 정보 및 데이터들을 모두 포함한 구조
  * 데이터베이스, 처음 정의하는 상수, 초기화 값, 변수 등을 포함

  * Model이 가지고 있는 규칙
    1. 사용자가 편집하길 원하는 모든 데이터들을 가지고 있어야 함.

    2. Model 이외의 구조(View, Controller)에 대해서 독립적으로 존재해야 함. 즉, 어떠한 정보들도 알지 말아야 함.

    3. 변경이 발생된다면, 변경하였다는 보고에 대한 처리방법을 구현해야만 함.
  
* 뷰(View) : Input 텍스트, 체크박스 등의 모든 사용자 인터페이스 요소들을 모두 포함한 구조

  * View가 가지고 있는 규칙
    1. Model이 가지고 있는 정보를 따로 저장하지 않아야 함. 즉, 단순히 인터페이스 요소들만 표시하고, 데이터들을 저장하지 않아야 함.

    2. 데이터들을 받으면 화면에 표시해주는 역할만 담당해야 함.

    3. 변경이 일어나면 변경된 내용을 보고하는 방법을 구현해야 함.

    4. 인터페이스의 재사용 가능성이 높도록 설계를 해야 함.

* 컨트롤러(Controller) : 데이터와 사용자 인터페이스들의 요소들을 연결시키는 역할을 포함한 구조

  * Controller가 가지고 있는 규칙

    1. Model 과 View에 대해서 모두 알고 있어야 함. 즉, Controller가 서로 모르고 있는 Model 과 View 를 중재하는 역할도 담당함.

    2. Model이나 View의 변경을 실시간으로 모니터링해야 함. 즉, 변경 통지를 받으면 각각의 구성 요소들에게 보고 하는 역할임.

    3. 프로젝트의 메인 로직을 담당함.

* MVC를 사용하는 이유 : 사용자가 보는 페이지, 데이터 처리 및 이들을 제어하는 controll을 구성할 때에 각각의 구조들이 맡은 역할에만 집중할 수 있게 하기 위함.(공장에서 각자 하나의 업무만 담당하여 결과물 생산의 효율을 높이는 것과 유사)

* MVC의 의의 : 특정한 프로젝트의 구조를 **어떻게 나눌 것인가**에 대한 방법론 중 하나이다. **역할 분담의 가이드라인을 제시하는 방법 중 하나**라고 할 수 있다.

## **DAO(Data Acess Object)**

* DAO(Data Acess Object) : Database에 실질적으로 접근하는 객체

* DB에 접속하는 객체를 전용으로 하나를 생성하고, 프로젝트의 모든 페이지에서 그 객체를 호출하여 사용한다. 즉, DataBase를 사용하여 데이터를 조회하거나 조작하는 기능을 전담하도록 만든 객체라 할 수 있다.

* DAO의 기본 동작 원리 : 사용자가 자신이 필요한 Interface를 DAO에게 던지고 DAO는 이 인터페이스들을 구현한 객체를 사용자에게 편리하게 사용하도록 반환해줌.

![DAO](https://gmlwjd9405.github.io/images/setting-for-dbprogramming/dao-structure.png)
출처 : <https://gmlwjd9405.github.io>

## **DTO(Data Transfer Object)**

* DTO(Data Transfer Object) : 데이터 교환을 위한 객체

  * DB에서 데이터를 얻어서 Controller 등으로 보낼 때에 사용하는 객체이다.

  * getter/setter 메서드만을 가진다.(toString(), equals() 등의 Object 클래스 메소드를 작성하는 것은 가능)

![DTO](https://i.ytimg.com/vi/GIZ8HFjsIlE/maxresdefault.jpg)
<출처 : <https://i.ytimg.com>>
  
## DAO 클래스와 DTO 클래스 예제(참고 사항, 원리만 이해함)

### DAO 클래스 예제

``` java
public class DTOBean {
    private String name;
    private int value;
    private String data;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
}
```

출처 : <https://genesis8.tistory.com/214>

### DTO 클래스 예제

``` java
public class TestDao {
    public void add(DTOBean dto) throws ClassNotFoundException, SQLException {
        Class.forName("com.mysql.jdbc.Driver");
        Connection c = DriverManager.getConnection("jdbc:mysql://localhost/springbook", "spring", "book");

        PreparedStatement ps = c.prepareStatement("insert into users(id, name, password) value(?, ?, ?)");

        ps.setString(1, dto.getName());
        ps.setInt(2, dto.getValue());
        ps.setString(3, dto.getData());

        ps.executeUpdate();

        ps.close();
        c.close();
    }
}
```

출처 : <https://genesis8.tistory.com/214>
