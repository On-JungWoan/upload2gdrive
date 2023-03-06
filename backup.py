import argparse
import shutil
import os
from tqdm import tqdm
from datetime import datetime
import sys

# dirve API
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file as f
from google_drive import initialization


def get_args_parser():
    parser = argparse.ArgumentParser('Set transformer detector', add_help=False)
    parser.add_argument('--project_dir', default='/home/unist/Desktop/OJW/')
    parser.add_argument('--backup_dir', default='/home/unist/Desktop/OJW/BackUp2GoogleDrive/backup_file/')
    parser.add_argument('--file_type', default='.zip')
    parser.add_argument('--drive_folder_id', default='1UsakSZbuK50Mrp_taK8HA4SY4Vq-cOIC') #arg this
    parser.add_argument('--file_name', default='custom_DINO') #arg this
    parser.add_argument('--ignore_dirs', nargs='+') #arg this

    return parser


def upload2drive(files, backup_path):
    store = f.Storage('storage.json')
    creds = store.get()

    if not creds:
        print("\n\n!!!! No Initialization : Run below command in terminal !!!!\nbash scripts/drive_initialization.sh")
        shutil.rmtree(backup_path)
        os.remove(f'{args.backup_dir}{files}')
        sys.exit(0)

    service = build('drive','v3',credentials=creds)

    file_metadata = {
    "name": files,
    "parents": [args.drive_folder_id]}
    # 파일 업로드
    media = MediaFileUpload(files, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()


def main(args):
    origin_path = os.path.join(args.project_dir, args.file_name)
    backup_path = os.path.join(args.project_dir, args.file_name + '_backup')

    if os.path.isdir(backup_path):
        shutil.rmtree(backup_path)
    os.mkdir(backup_path)

    files = (os.listdir(origin_path))

    print("****Progress in Copy****")
    for file in tqdm(files):
        if file not in args.ignore_dirs:
            try:
                shutil.copy(
                    os.path.join(origin_path, file),
                    os.path.join(backup_path, file)
                )
            except:
                shutil.copytree(
                    os.path.join(origin_path, file),
                    os.path.join(backup_path, file)
                )

    print("\n****Progress in Make Zip file****")
    now = datetime.now().strftime('%y%m%d_%H%M')
    file_name = f'{args.file_name}_{now}_backup'
    shutil.make_archive(file_name, 'zip', backup_path)
    print("\ndone")

    print("\n****Progress in Upload Zip file****")
    upload2drive(file_name + args.file_type, backup_path)

    shutil.move(f'{file_name}{args.file_type}', f'{args.backup_dir}{file_name}{args.file_type}' )
    shutil.rmtree(backup_path)
    print("\nsuccess!")

    

if __name__ == '__main__':
    parser = get_args_parser()
    args = parser.parse_args() 

    main(args)
    # if args.output_dir:
    #     Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    # main(args)
