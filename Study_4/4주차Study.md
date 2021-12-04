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
  
  ![](data:image/png;base64,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)

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
