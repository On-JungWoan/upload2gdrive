id=$(<params/DRIVE_FOLDER_ID)
ignore=$(<params/IGNORE_LIST)

python main.py \
    --file_path $1 \
    --file_type dir --drive_folder_id $id --ignore $ignore