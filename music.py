import os
from pytube import Playlist, YouTube
from moviepy.editor import *
# Example playlist URL
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
        
        
def Download_music(playlist_link: str, download_dir:str):   
 os.makedirs(download_dir,exist_ok=True)


 # Initialize playlist object
 try:
  playlist = Playlist(playlist_link)
 except:
     print("invalid playlist link...")
     exit(1)
 # Iterate through each video in the playlist
 for video in playlist.videos:
    
    try:
        
        print(f'Downloading {video.title}...')
        
        # Download video
        video.streams.filter(only_audio=True).first().download(output_path=download_dir)
        mp4_file_path = download_dir + "/"+ video.title
        print(mp4_file_path)
        mp3_file_path = mp4_file_path + '.mp3'
        print(mp3_file_path)
       # Convert to MP3
        video_clip = AudioFileClip((mp4_file_path + ".mp4"))
        video_clip.write_audiofile(mp3_file_path)
    
    # Step 6: Optionally, delete the MP4 file after conversion
        os.remove(mp4_file_path+".mp4")
        print(f'Finished downloading and converting {video.title}.')
        clear()
    except Exception as e:
        print(f'Error downloading {video.title}: {str(e)}')
        
def main():
   yes = "y"     
   while(yes == "y"):
        inputplay = input("""insert your playlist link.
>""")
        dir =  input("""insert thje path do the download dir.
>""")
        Download_music(inputplay,
                       dir)
        print(os.name)
        clear()
        if input("""do you want to download another playlist(n/y)?
                 >""") == "n":
            yes = "n"
        
if __name__ == "__main__":
    main()