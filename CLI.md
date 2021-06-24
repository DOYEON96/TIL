# CLI

## ls (list)

- `-` 은 앞에 목록 형태를 나타낼 수 있다.

- ls 명령어는 현재 작업중인 위치에 존재하는 파일 혹은 폴더 목록을 보여준다.
- ` 백틱 3개는 코드 블락을 생성할 수 있다.

```bash
김도연@DESKTOP-82V6CR4 MINGW64 ~/Desktop/github_study
$ ls
test_folder/  text.txt
```

<hr/>

##  cd(change directory)

- 현재 작업중인 디렉토리(a.k.a 폴더)를 변경하겠다.

```bash
김도연@DESKTOP-82V6CR4 MINGW64 ~
$ cd {directory name}
김도연@DESKTOP-82V6CR4 MINGW64 ~/Desktop/github_study
$ cd .. # 내 상위 폴더로 이동
```

<hr/>

## mkdir (make directory)

- 디렉토리/폴더를 생성한다

```bash
김도연@DESKTOP-82V6CR4 MINGW64 ~/Desktop/github_study
$ mkdir {directory name}
```

<hr/>

## touch

- 파일을 생성한다.

```bash
김도연@DESKTOP-82V6CR4 MINGW64 ~/Desktop/github_study
$ touch {file name}.{확장자}
```

