from __future__ import unicode_literals
import pandas as pd
import glob
import os
import sys
import yt_dlp


folder_path = '/content/drive/MyDrive/PHD/TIE_Dataset/Final_Dataset_Audios/'     #Folder Path where the audios to be stored
formats = folder_path + '%(id)s.%(ext)s'


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': formats,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


def download_videos(video_ids):
    for video_id in video_ids:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.cache.remove()
                link = f"https://www.youtube.com/watch?v={video_id}"
                ydl.download([link])
                print(f"Downloaded video with ID: {video_id}")
        except:
            print(f"Error downloading video with ID: {video_id}")


# Download multiple YouTube videos by their IDs

#Provide the ID List of YouTube Videos to be downloaded

meta_file_path "{source_folder}/Final_Dataset.csv"
df = pd.read_csv(meta_file_path)
id_list_1 = df["ID"].tolist()   #Filter the IDs based on your criteria
download_videos(id_list_1)
