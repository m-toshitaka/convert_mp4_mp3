import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import sys

def convert_to_mp3(input_file_path, output_file_path):
    """
    mp4ファイルをmp3ファイルに変換する
    """
    subprocess.call(['ffmpeg', '-i', input_file_path, '-vn', '-ar', '44100', '-ac', '2', '-ab', '192k', '-f', 'mp3', output_file_path])

if __name__ == '__main__':
    # ファイルダイアログを表示して、mp4ファイルのパスを取得
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title='Select MP4 files',
        filetypes=[('MP4 files', '*.mp4')]
    )
    if not file_paths:
        print('ファイルが選択されていません。')
        sys.exit(1)

    # 出力フォルダの選択
    output_folder = filedialog.askdirectory(
        title='Select output folder'
    )
    if not output_folder:
        print('出力フォルダが選択されていません。')
        sys.exit(1)

    # 変換処理の実行
    for input_file in file_paths:
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + '.mp3')
        print('変換中:', input_file)
        convert_to_mp3(input_file, output_file)

    print('変換が完了しました。')
