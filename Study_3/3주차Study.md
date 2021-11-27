# 3주차 : Java Collections Framework

## Collections의 개념

* **Collection**
  * element : 객체들이 저장되는 곳
  * element의 개수에 따라 크기 자동 조절
  * element의 삽입, 삭제가 진행된 결과에 따라 element의 위치가 자동적으로 배치
* 목적 : 고정 크기의 배열을 다루는 어려움을 자동적으로 해소
* 의의 : 다양한 객체들의 변동사항 수행 결과의 관리를 용이하게 처리 가능

## Collection과 Generic기법(=일반화 기법)

* Generic 기법 : 특정 타입만 사용하지 않고 여러 종류의 타입으로 변신할 수 있도록 클래스 혹은 메소드를 일반화 시키는 기법
* 사용법
  * `<E>`, `<K>`, `<V>` (E, K, V : 임의의 일반화를 위한 타입)

* 사용 예

  * 일반화된 스택(=제네릭 스택)

  ``` java
  class Stack<E> {
      void push(E element) {...}
      E pop() {...}
  }
  ```

  * 정수 스택

  ``` java
  ...
  void push(Integer element) {...}
  Integer pop() {...}
  ...
  ```

  * 문자열 스택

  ``` java
  ...
  void push(String element) {...}
  String pop() {...}
  ...
  ```

## Java Collections Framework의 구성 정리

* 상위 인터페이스
  * **List** (element의 중복 포함이 가능, 순서 유지 가능)
    * ArrayList : 순차적인 삽입 및 삭제에 최적화
    * Vector : 배열의 길이제한의 특성을 극복, element의 개수가 넘쳐나는 경우 자동으로 길이 조절 처리 가능
    * LinkedList : stack, queue 등을 구현하는 경우에 활용, 삽입 및 삭제가 중간에서 이루어질 때 유리
  * **Set**(element의 중복 불가, 순서 없음)
    * HashSet : 순서가 필요없는 자료를 HashTable에 저장 가능
    * TreeSet : 값에 따라 정렬 가능
    * LinkedHashSet : 연결된 목록 단위로 구현된 Hash table에 저장 가능
  * **Map**(key 와 value 의 쌍으로 구성, key 중복 불가)
    * HashMap : 기본적이고 일반적인 Map
    * TreeMap : 정렬 처리, 순서 존재
    * HashTable : 안정적인 데이터 저장 가능

![Collection Framework의 구조](https://media.vlpt.us/images/nunddu/post/60e79219-7834-4f3d-8b9e-49e7d70ed725/image.png)

출처 : https://velog.io/@nunddu/Java-Collections-Framework

## 상위 인터페이스들의 주요 메소드들

* Collection 인터페이스

  * **boolean add(E e)** : Collection에 객체 추가하기
  * **void clear()** : Collection의 모든 객체를 제거
  * **boolean remove(Object o)** : Collection에 매개변수에 해당하는 instance가 존재하면 제거
  * **int size()** : Collection에 있는 element의 개수를 반환
  
* List 인터페이스(Collection 인터페이스를 상속 받으므로, 별도로 추가된 메소드들만 설명함.)

  * **E get(int index)** : 해당 리스트의 특정한 위치에 존재하는 요소를 반환
  * **Object[] toArray()** : 해당 리스트의 모든 요소를 Object 타입의 배열로 반환
* Map 인터페이스(Collection 인터페이스를 상속 받으므로, 별도로 추가된 메소드들만 설명함.)

  * **void put(K key, V value)** : key에 해당하는 value 값을 map에 삽입
  * **void get(K key)** : key에 해당하는 value 값을 반환
  * **boolean isEmpty()** : Map이 비어있는지 여부를 반환
  * **boolean containskey(Object key)** : Map에 key에 대응하는 value의 존재 여부를 반환
  * **boolean containsValue(Object value)** : Map에 value에 대응하는 key의 존재여부를 반환
  * **Collection values()** : value 값을 Collection으로 반환
  * **void remove(key)** : key가 있는 경우 삭제
  * **boolean remove(Object key, Object value)** : key가 존재하는 경우, key에 해당하는 value가 매개변수와 일치할 때 삭제
