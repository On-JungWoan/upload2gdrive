# Upload to GoogleDrive
[KOR_README is here](https://github.com/On-JungWoan/upload2gdrive/blob/master/README_KOR.md)

<br>

# Introduction
Upload2gdrive automatically uploads desired files or folders to Google Drive.

1. **Folder**: Upload2gdrive will upload files to Google Drive by compressing it into a zip file. The generated zip file will be stored under 'backup_file/'.

2. **File**: Upload2gdrive will create a copy of the original file and upload it to Google Drive. The copied file will be stored under 'backup_file/'.

<br>

# Settings

> Setting up API keys: [link](https://support.google.com/googleapi/answer/6158862?hl=en)

(...not yet)

<br>

# How to use upload2gdrive

<details>

<summary> Upload folder </summary>

If you want to upload an entire folder, enter the following command in the terminal.

```
> bash scripts/upload_dirs.sh /your/file/path/
```
</details>


<details>

<summary> Upload file </summary>

If you want to upload an specific file, enter the following command in the terminal.

```
> bash scripts/upload_files.sh /your/file.txt
```

</details>

<details>

<summary> Ignore files </summary>

If you want to ignore specific files or directories when uploading a folder, simply add their names to `params/IGNORE_LIST`. Make sure to list the names on a single line without any line breaks.

```
[params/IGNORE_LIST]

cache test log secret.txt
```

The files and directories named `cache`, `test`, `log`, and `secret.txt` will be ignored and not uploaded

</details>

<details>

<summary> Custom </summary>

If you want to customize the shell script, you can modify the contents of `scripts/upload_custom.sh`.

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
