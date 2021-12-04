# 4주차 : 람다(Lambda), 스트림(Stream), 익명 클래스(Anonymous class)

## 람다(Lambda)

* 람다(=람다식, Lambda Expression) : 임의의 메소드를 하나의 간단한 식으로 표현하는 방법

* 람다식은 메소드명과 반환값이 존재하지 않음(=익명함수, Anonymous function)

* 람다식은 두 개 이상의 입력이 있는 함수를 1개의 입력만 받도록 단순화 될 수 있음(=커링, Curring)

* 람다식의 장단점
  * 장점
    1. 코드의 간결성 - 람다식을 사용하면 불필요한 반복문 삭제가 가능
    2. 함수 바디의 단순화 - 복잡한 식을 단순하게 표현 가능
    3. 지연연산 수행 - 불필요한 연산을 최소화 가능
  * 단점
    1. 호출이 까다로움
    2. 단순 for문 및 while문 사용 시 성능저하 발생
    3. 지나치게 사용할 경우 가독성 떨어짐

* 람다식을 표현하는 방법
  * 기존 메소드 선언

  ``` java
  //메소드 선언
  ReturnType methodName(ParameterType p) {
      // body
      System.out.println(2 * p);
  }
  ```

  * 메소드명과 반환타입 을 제거하고, 매개변수 선언부와 메소드 바디 사이에 '->' 추가

  ```java
  //람다식으로 변환
  (ParameterType p) -> {
      // body
      System.out.println(2 * p);
  }
  ```

  * body의 식이 하나인 경우, '{}' 생략 가능
  
  ```java
  // {} 생략
  (ParameterType p) -> System.out.println(2 * p);
  ```

  * 매개변수 타입이 추론 가능한 경우 타입 생략 가능, 매개변수가 하나인 경우 '()' 생략 가능

  ```java
  // {} 생략
  p -> System.out.println(2 * p);
  ```

* 람다식 작성 문법 정리

  ``` markdown
  1. 기본적인 작성 규칙
    - 이름과 반환타입은 작성하지 않는다.

  2. 매개변수
    - 추론 가능한 매개변수의 타입은 생략 가능하다.
    - 선언된 매개변수가 하나인 경우 '()' 생략 가능하다.
    - 단, 매개변수 타입을 작성한 경우는 '()'를 작성한다.

  3. body {}
    - return문 대신 식으로만 작성 가능하다.
    - 식의 끝에 ';'을 붙일 수 없다.
    - '{}' 안의 문장이 하나인 경우는 생략 가능하다.
    - 단, return 문은 괄호를 생략할 수 없다.
  ```

## 스트림(Stream)

* 스트림(입출력 스트림) : 여러 데이터들의 흐름을 의미하며, 버퍼를 통하여 순차적으로 이루어짐.

* 자바의 입출력 Stream : 응용프로그램과 입출력 장치를 연결하는 시스템
  * 입력 Stream : 입력 장치로부터 자바 프로그램 내부로 데이터를 전달
  * 출력 Stream : 출력 장치로 데이터 출력
  
  ![](http://tcpschool.com/lectures/img_c_stream.png)

출처 : <http://tcpschool.com/java/java_io_stream>

* Stream 의 사용 목적 : 배열 또는 컬렉션 인스턴스 요소들에 여러 함수, 메소드들을 조합하여 원하는 결과를 필터링함

* Stream의 특징

  * data를 변경하지 않는다.
  * 1회용의 성질은 지닌다.
  * 병렬 실행이 가능하다.
  * 입력과 출력을 동시에 진행할 수 없다.
  * 각 데이터들은 선입선출 구조로 되어있다.

* 입출력 스트림의 기본 단위
  * byte Stream : 바이트
  * 문자 Stream : 문자(Java에서는 문자 1개 = 2바이트)

* Stream의 종류

  * Stream`<T>` : 범용(일반적인) Stream
  * IntStream : 값의 type이 Int인 Stream
  * LongStream : 값의 type이 Long인 Stream
  * DoubleStream : 값의 type이 Double인 Stream

* 바이트 스트림의 계층 구조

  * InputStream/OutputStream : 바이트 스트림을 다루는 모든 클래스의 슈퍼 클래스
  * FileInputStream/FileOutputStream : 파일로부터 바이트 단위로 읽거나 저장하는 클래스
  * DataInputStream/DataOutputStream : 자바의 기본 데이터 타입의 값을 바이너리 값 그대로 입출력, 문자열도 가능
  
![](https://t1.daumcdn.net/cfile/tistory/99DEDB385AA5299E0F)

출처 : <https://mainpower4309.tistory.com/18>

* 문자 스트림의 계층 구조

  * Reader/Writer : 문자 스트림을 다루는 모든 클래스의 슈퍼 클래스
  * InputStreamReader/OutputStreamWriter
  * FileReader/FileWriter : 텍스트 파일에서 문자 데이터 입출력

![](https://t1.daumcdn.net/cfile/tistory/9941F93B5AA529FD2A)

출처 : <https://mainpower4309.tistory.com/18>
  
## 익명 클래스(Anonymous class)

* 익명 클래스(=내부 클래스, Inner class) : 클래스명을 붙이지 않은 클래스

* 익명 클래스를 사용하는 이유 : 프로그램 내에서 한 번만 객체를 만드는 데 사용되는 클래스를 굳이 정의할 필요가 없는 경우에 유용하기 때문이다.

* 익명 클래스가 사용되는 예시 코드

```java

//부모 클래스
public abstract class MyInterface {
    public abstract void doSomething();
}

// 클래스 정의와 동시에 객체 생성 가능
MyInterface myclass = new MyInterface() {
    @override // 익명클래스는 이름이 없기 때문에, overide가 필요함
    public void doSomething() {
        System.out.println("doSomething");
    }
};

myclass.doSomething();
```

* 익명 클래스는 클래스 정의와 동시에 객체를 생성할 수 있다.

* 익명 클래스 내에서 상수 및 변수를 참조하는 것이 가능하다.

```java
//부모 클래스
public abstract class MyAbstractClass {
    public abstract void doSomething();
}
// 클래스 정의와 동시에 객체 생성
MyInterface myClass = new MyInterface() {
    static final int a = 0;

    @Override
    public void doSomething() {
        System.out.println("doSomething: " + a);
    }
};
