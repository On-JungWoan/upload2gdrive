# BackUP 2 GoogleDrive

[ENG_README is here](https://github.com/On-JungWoan/upload2gdrive/blob/master/README.md)

<br>

# Introduction
bu2gd는 원하는 파일 또는 폴더를 구글 드라이브에 자동으로 업로드 해줍니다.

1. **폴더**: zip파일로 압축하여 구글 드라이브에 업로드 합니다. 생성된 zip파일은 `backup_file/` 하위에 저장됩니다.

2. **파일**: 원본 파일의 복사본을 생성하고, 복사본을 구글 드라이브에 업로드 합니다. 복사된 파일은 `backup_file/` 하위에 저장됩니다.

<br>

# 사전준비

> Setting up API keys: [link](https://psychoria.tistory.com/674)

(생략)

<br>

# 사용법

<details>

<summary> 폴더 업로드 </summary>

폴더 전체를 업로드하고 싶다면, 터미널에 다음 명령어를 입력합니다.

```
> bash scripts/upload_dirs.sh /your/file/path/
```
</details>


<details>

<summary> 파일 업로드 </summary>

특정 파일을 업로드하고 싶다면, 터미널에 다음 명령어를 입력합니다.

```
> bash scripts/upload_files.sh /your/file.txt
```

</details>

<details>

<summary> 특정파일 무시 </summary>

만약 폴더를 업로드할 때, 특정 파일을 무시하고 업로드 하고 싶다면, `params/IGNORE_LIST`에 무시하고자 하는 디렉토리 또는 파일의 이름을 적으면 됩니다. 이 때, 줄바꿈하지 않고 한 줄로 적어야합니다.

```
[params/IGNORE_LIST]

cache test log secret.txt
```

cache, test, log, secret.txt는 무시하고 업로드하게 됩니다.

</details>

<details>

<summary> 커스텀 </summary>

만약, shell파일을 커스텀하고 싶다면, `scripts/upload_custom.sh`의 내용을 수정해주면 됩니다.

```
[scripts/upload_custom.sh]

id=$(<params/DRIVE_FOLDER_ID)
ignore=$(<params/IGNORE_LIST)

python main.py \
    --file_path ##your file path##
    --file_type ##your file type : dir or file##
    --backup_dir ##The path where backup files will be saved##
    --drive_folder_id $id
    --ignore $ignore
```

</details>

<br>

# License

MIT License

Copyright (c) 2023 온정완

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
