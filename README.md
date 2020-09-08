# jasan
학교 내 폐기 기자재 조사를 자동화

## 이전 로그
~~github 장애(?)로 이미지 첨부 안됨~~

## 개발목적
2~300대의 폐기 기자재를 수기로 조사하기에는 시간적, 체력적 소모가 상당하다.
기자재에 붙어있는 자산정보 스티커에 있는 QR코드를 찍으면 기자재 정보가 담긴 웹으로 연결되는 것을 확인하여
QR을 찍기만 하면 정보를 얻을 수 있도록 하였다.

## 동작
1. QR을 찍으면 URL이 DB에 저장된다.(firebase realtime DB)
2. PC에서 크롤링 프로그램을 실행시키면 csv형식으로 정보를 얻는다.(Crawing: BeautiSoup)

## IOS버전
[ios](https://github.com/DevooKim/crawing_jasan)
