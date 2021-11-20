## 인터페이스(Interface)를 정의하는 방법

* 인터페이스 : 클래스들이 구현해야 하는 메소드들이 선언되어 있는 추상형 구조

* 인터페이스 선언 
    + **interface** 키워드로 선언
    + `public interface driver {...}`

    + 인터페이스에는 멤버 변수 선언이 불가함.

## 인터페이스를 구현하는 방법

* 구현 : 실제 기능을 가지도록 상속하는 것

* 인터페이스 구현
    + **implements** 키워드를 이용

    + `class Galaxy implements GalaxyInterface {...}`

    + 여려 가지의 인터페이스들을 한꺼번에 구현 가능

## 인터페이스 레퍼런스를 통해 구현체를 사용하는 방법

* 구현된 인터페이스들을 참조하여 객체를 생성 가능

* 인터페이스를 객체화 시키는 것이 가능

* 객체에 구현 클래스를 포함 함으로써 멤버로 설정 가능

## 인터페이스 상속

1. 인터페이스가 다른 인터페이스를 상속하는 경우
    + **extends** 키워드 이용

    + ` interface MobilePhoneInterface extends PhoneInterface {...}
    `
2. 인터페이스가 여러 개의 인터페이스를 상속하는 경우
    + ","를 활용하여 여러 인터페이스를 나열
    + ` interface MusicPhoneInterface extends MobilePhoneInterface, MP3Interface, {...}
    `
## 인터페이스의 Default Method
* default 메소드의 선언
    + **default** 키워드로 선언

    + ` default void description() {
        System.out.println("정수 계산기를 구현합니다.");
    }
    `

* default 메소드의 장점
    + 상위 인터페이스에 미리 구현함으로써, 인터페이스를 구현한 클래스에서 코드를 구현할 필요가 없음.
    + 구현하는 클래스에서 재정의(overloading)할 수 있다.

* 여러 인터페이스들에서 디폴트 메소드간의 모호성
    → 인터페이스를 구현한 클래스에서 디폴트 메소드를 재정의(overriding)해야 함.
* 디폴트 메소드와 상위 클래스의 메소드간의 충돌
    → 상위 클래스의 메소드가 상속됨과 동시에 디폴트 메소드는 무시됨.
## 인터페이스의 static 메소드

* static 메소드 : 인스턴스 생성과 무관하게 인터페이스 타입으로 호출되는 메소드

* static 메소드의 선언
    + **static** 키워드를 사용
    + 접근 제어자는 생략 가능(public으로 자동설정)
## 인터페이스의 private 메소드

* private 메소드의 장점 : 코드의 재사용성(re-usability)가 개선될 수 있다.

* 인터페이스 내의 private 메소드의 성질
    1. private intetface 메소드는 추상적이지 않음.

    2. private 메소드는 인터페이스의 내부에서만 사용 가능함.
    
    3. private static 메소드는 또다른 static 및 non-static 메소드 내에서 사용 가능함.

    4. private non-static 메소드는 private static 메소드 안에서 사용 불가함.

## new 키워드

* 클래스 타입의 객체를 생성하는 역할 담당

* 사용방법
    + `클래스 객체변수 = new 클래스();`
* 작동원리
    1. 메모리에 데이터를 저장할 공간을 할당받음.
    
    2. 그 공간의 참조값을 객체에게 반환

    3. 생성자 호출

### 출처 : 명품 자바 프로그래밍(황기태 저)