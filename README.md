# Example of using 16personalities-API
2021 디랩 코드 페어 우승작 🏆
디스코드 봇을 통한 [16personalities api wrapper](https://github.com/DevGarlic/16personalities-API) 예시 사용작
### How to build 💻
#### 모듈 다운
```python
pip install requests bs4 lxml pandas discord enum
```
#### 토큰 수정
```python
client.run(Insert your token here)
```
#### 빌드하기
```bash
python main.py
```
### Functions 🔨
#### /검사 
명령어를 사용한 채널에 비공개를 쓰레드를 연 후 검사를 진행한다.
#### /궁합 (유형1) (유형2)
두 유형간의 궁합을 확인한다. *[인터넷에서 아무거나](https://blog.kakaocdn.net/dn/BPUqI/btrz2pZ0Akp/UqNKwHU2elkerrIrhJdhf0/img.png) 가져온거라 정확도 보장 못함
#### /정보 (유형)
특정 유형의 별명,설명,캐릭터등을 불러온다 
