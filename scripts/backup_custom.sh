id=$(<params/DRIVE_FOLDER_ID)
ignore=$(<params/IGNORE_LIST)

python main.py \
    --file_path
    --file_type
    --backup_dir
    --drive_folder_id $id
    --ignore $ignore