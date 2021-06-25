# 원격 저장소(remote repository)

## 기본설정

1. 로컬 git 저장소 준비
2. github repository 생성
3. Repository default branch 변경



## 명령어

### 원격 저장소 주소 추가

```bash
# git아, 원격 저장소 주소 origin 이라는 이름으로 추가 할건데, 주소는 이거야.
$ git remote add origin https://github.com/DOYEON96/TIL.git
# origin은 첫 저장소 이름 관례 느낌.
```



### 원격 저장소 목록 보기

```bash
# git아, 내가 가진 저장소 목록 보여줘.
$ git remote -v
```



### 원격 저장소 삭제

```bash
# origin 이라는 이름의 저장소 삭제
$ git remote rm origin
```



###  원격 저장소에 업로드(push)

```bash
# git아 업로드 할건데 origin이라는 이름으로 저장해둔 원격 저장소에 master 브랜치의 commit 내역들을 업로드할거야.
$ git push -u origin master
```

- commit 내역이 없으면 불가능



### clone

- 원격 저장소 내용 전체 복귀

```bash
# $ git clone {원격 저장소 url}
$ git clone https://github.com/DOYEON96/TIL.git
```

- 주의사항
- 이미 git init 되어있으므로 다시 실행하지 않을 것

