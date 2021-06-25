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



### pull

- 원격 저장소의 변경사항을 받아옴 (업데이트)

- ```bash
  $ git pull origin master
  ```



## branch command

-  브랜치 생성

 ```bash
$ git branch 브랜치명
$ git branch main
 ```



-  브랜치 목록

```bash
$ git branch
```



-  브랜치 이동

```bash
# $ git checkout 브랜치명
$ git checkout main
(main) $
```

```bash
$ git log --oneline
b2b76df (HEAD -> master, origin/master, origin/HEAD) Delete Readme.md
```

- HEAD : 현재 우리가 속한 위치



-  브랜치 생성 + 이동

```bash
#$ git checkout -b 브랜치명
$ git checkout -b main
```



- 브랜치 병합

```bash
(master) $ git merge 브랜치명
```

반드시 master 브랜치에 `브랜치`를 병합



- 브랜치 삭제

```bash
$ git branch -d 브랜치명
```



- 브랜치 강제 삭제

```bash
$ git branch -D 브랜치명
```



## 3가지 병합 상황

### 1. fast-foward

"다른 브랜치를 생성 한 후, master 브랜치에 변경사항이 없을 때"



### 2. 3-way merge

"현재 브랜치(master)가 가리키는 커밋이 merge할 브랜치의 조상(서로 다른 커밋이 각각 존재할 경우)이 아니면, 깃은 현재 브랜치와 머지할 브랜치의 커밋 2개와 두 브랜치의 공통조상 하나를 사용한다."

1. 새로운 브랜치 signup 생성
2. signup 브랜치에서 signup.py 생성
   - git add, commit 잊지 말기
3. master 브랜치에서 new folder와 new.py 생성
   - git add, commit 잊지 말기
4. master 브랜치와 signup 브랜치 병합

5. signup 브랜치 삭제



### 3. Merge Conflict

"두 개의 브랜치가 동일한 파일의 동일한 위치를 수정하고 merge 하려고 할 때 발생하는 현상

단, 동일 파일이라고 하더라도 서로 다른 영역을 수정한다면 merge conflict는 발생하지 않는다."

- git이 자동으로 병합하지 못하는 상황

##### 1. 새로운 브랜치 hotfix 생성

```bash
$ git branch hotfix
$ git checkout hotfix
# $ git checkout -b hotfix
```

#####  2. hotfix 브랜치에서 b.txt에 새로운 내용 입력

-  git add, commit

```bash
#$ git add . or b.txt
$ git add b.txt
#$ git commit -m "message"
$ git commit -m "hotfix | b.txt modified"
```



##### 3. master 브랜치에서 b.txt에 새로운 내용 입력

- git add, commit

```bash
#$ git add . or b.txt
$ git add b.txt
#$ git commit -m "message"
$ git commit -m "master | b.txt modified"
```



##### 4. master 브랜치와 hotfix 브랜치 병합

```bash
김도연@DESKTOP-82V6CR4 MINGW64 ~/desktop/TIL (master)
$ git merge hotfix
Auto-merging b.txt
CONFLICT (content): Merge conflict in b.txt
Automatic merge failed; fix conflicts and then commit the result.

김도연@DESKTOP-82V6CR4 MINGW64 ~/desktop/TIL (master|MERGING)
$
```

