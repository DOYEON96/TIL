# Git 초기 설정

커밋 작성자 설정

```bash
# 명령을 시키고자 하는 주체
# git아, 전역 설정 중, 유저의 email을 설정할거야.
$ git config --global user.email sbk5009@naver.com
# git아, 전역 설정 중, 유저의 name을 설정할거야.
$ git config --global user.name DOYEON96
```

- 커밋을 작성하는 사람이 누구인지 알아야 하기 때문에 



지정된 설정 확인

```bash
# git아 현재 전역에 설정된 설정 목록 보여줘
$ git config --global -l
# $ git config --global --list
```





# Git Basic

## 로컬 저장소 설정

```bash
$ git init
```

- 폴더에 git 저장소를 초기화하면,  .git이라는 숨김 폴더가 생기고 bash에는 (master)라는 표기가 생성됨

- 주의사항

  - .git 폴더를 직접적으로 수정하는 일은 없을 것이다.

  - 이미 git으로 관리하고 있는 (bash창에 master가 표기되어 있는 폴더 내에서는 절대 git init 하지 말 것)



## status

```bash
# git아 너가 관리중인 폴더의 상태 보여줘
$ git status
```



## add

```bash
# $ git add 파일명
$ git add CLI.md # 특정 파일 
$ git add . # 현재 디렉토리의 모든 파일 add
# git add directory_name/ # 특정 폴더가 가진 모든 파일
```

- working directory 상태의 파일을 staging area 상태로 변경

## touch

```bash
# $ touch 파일명
$ touch a.txt b.txt # 현재 디렉토리에 a.txt b.txt 파일을 생성
```



##  commit

```bash
# git아, commit 할 건데 -메시지는 "이걸로 해줘"
# 메시지는 보통 날짜 | 파일명 | 변경사항 작성
$ git commit -m "commit message"
# git commit -m "210624 | created CLI.md"
```

- 커밋을 통해 하나의 버전으로 기록됨
- 커밋 메시지는 현재 변경사항들을 잘 나타낼 수 있도록 작성하는 것을 권장
- 커밋 목록은 $ git log 를 통해 확인할 수 있음

```bash
$ git log # 로그 출력
```



```bash
$ git log --oneline # 로그를 한줄로 요약하여 출력
```





