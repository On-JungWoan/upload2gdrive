import argparse
import shutil
import os
from tqdm import tqdm
from datetime import datetime
import sys

# dirve API
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client import file as f


def get_args_parser():
    parser = argparse.ArgumentParser('Set args', add_help=False)
    parser.add_argument('--file_path', type=str, required=True)
    parser.add_argument('--file_type', default='dir')
    parser.add_argument('--backup_dir', default='backup_file/')
    parser.add_argument('--drive_folder_id', default='1UsakSZbuK50Mrp_taK8HA4SY4Vq-cOIC') #arg this
    parser.add_argument('--ignore', nargs='+') #arg this

    return parser


def upload2drive(files):
    print("\n\n****Progress in Upload file****")
    store = f.Storage('storage.json')
    creds = store.get()

    if not creds:
        print("\n\n!!!! No Initialization : Run below command in terminal !!!!\nbash scripts/drive_initialization.sh")
        if args.file_type == 'dir':
            shutil.rmtree(os.path.join(args.file_path + '_backup'))
            os.remove(files)
        sys.exit(0)

    service = build('drive','v3',credentials=creds)

    file_metadata = {
        "name": files,
        "parents": [args.drive_folder_id]
    }
    # 파일 업로드
    media = MediaFileUpload(files, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print("done")


def makezip(file_name):
    backup_path = os.path.join(args.file_path + '_backup')

    # 주의! 디렉토리 존재 시, 삭제 후 재생성
    if os.path.isdir(backup_path):
        shutil.rmtree(backup_path)
    os.mkdir(backup_path)

    files = (os.listdir(args.file_path))


    # copy origin file
    print("\n\n****Progress in Copy****")

    # debug only
    # print(files)
    # print(args.ignore)
    # import time
    # time.sleep(10000)

    for file in tqdm(files):
        if file not in args.ignore:
            try:
                shutil.copy(
                    os.path.join(args.file_path, file),
                    os.path.join(backup_path, file)
                )
            except:
                shutil.copytree(
                    os.path.join(args.file_path, file),
                    os.path.join(backup_path, file)
                )

    # make zip file
    print("****Progress in Make Zip file****")
    now = datetime.now().strftime('%y%m%d_%H%M')
    zip_file_name = f'{file_name}_{now}_backup'
    shutil.make_archive(zip_file_name, 'zip', backup_path)
    print("done")

    return zip_file_name

def main(args):
    # settings
    prj_path, file_name = os.path.split(args.file_path)

    if args.file_type == 'dir':
        zip_file_name = makezip(file_name)
        upload2drive(zip_file_name + '.zip')
        shutil.rmtree(os.path.join(args.file_path + '_backup'))
        shutil.move(f'{zip_file_name}.zip', f'{args.backup_dir}{zip_file_name}.zip' )
    elif args.file_type == 'file':
        now = datetime.now().strftime('%y%m%d_%H%M')
        f, ext = os.path.splitext(file_name)
        backup_file_path = f'{args.backup_dir}{f}_{now}_backup{ext}'

        shutil.copy(args.file_path, backup_file_path)
        upload2drive(backup_file_path)
    else:
        print(f'Unavailable file_type : {args.file_type}\nPlease use "dir" or "file"')
        sys.exit(0)
    
    print("\nsuccess!")

    

if __name__ == '__main__':
    parser = get_args_parser()    
    args = parser.parse_args()     

    main(args)
    # if args.output_dir:
    #     Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    # main(args)
