from pytube import *
def start():
  option = input("""what would u like to do
1. interact with a playlist
2. downlaod videos
3. interact with a channel
4. search for a youtube video
~:""")
  
  return option
def playlist():
     link = input("insert the playlist url:")
     try:
        p = Playlist(link)
        p.title
     except Exception:  
        exit("Not a valid link")
      
     playlsit_option = input("""what would u like to do with to do with the playlist
1. download the playlist 
2. get the url's of the videos
3. get info about the playlist 
~/playlist:""")
     if (playlsit_option == "1" or playlsit_option == "download" ):
     
     
        print(f'Downloading: {p.title}')
        for i in p.videos:
         try:
            print(f"downloading {i.title}")
            i.streams.first().download() 
         except Exception as e:
          print(e)
     elif(playlsit_option == "2" or playlsit_option == "url"):
         case = input("""what would u like to get
1. all the urls
2. specific url
~/playlist/download:""")
         p = Playlist(link)
         if case == "1" or case == "all":
           for u,t in p.video_urls,p.videos:
            try:
             print(f"Video name:{t.title}, Video link:{u}")
            except Exception as e:
               print(e)
         else:
          sp_video = int(input("""What video would like to download?
(format as 1,2...)
~/palylist/download: """)) - 1
          print(f"Video name:{p.videos[sp_video].title}, Video link:{p.video_urls[sp_video]}")
     elif(playlsit_option == "3" or playlsit_option == "info"):
         time = 0
         for t in p.video_urls:
            time += YouTube(t).length
         print(f"""Name:{p.title}.
Owner:{p.owner}
number of Videos in the playlist:{p.length}
URL:{p.playlist_url}
Last update:{p.last_updated}
Hours to watch:{time//3600} Hours and {int((((time/3600)-(time//3600))*60))}""")
  

   
def music():
   link = input("insert the video url:")
   try:
        song = YouTube(link)
        song.title
   except Exception:  
        exit("Not a valid link")
   music_option = input("""what would u like to do with to do with the playlist
1. download the video  
2. get info about the video  
~/music:""")
   if (music_option == "1" or music_option == "download" ):   
      print(f"downloading:{song.title}")
      song.streams.first().downlaod()

   elif (music_option == "2" or music_option == "info" ):
      print(f"""Name:{song.title}.
author:{song.author}
channel url:{song.channel_url}
views:{song.views}
Description:{song.description}
""")
def channel():
   pass
#def search():
def main(option:str ):

  
   if option == "1":
      playlist()
   elif option == "2":
     music()
   elif option == "3":
      channel()
   elif option == "4":
      search()
      if input("would like go to the main menu?(y/n)") == "y".lower:
         main()
      else:
         exit("GoodBye")
   else:
      exit("Invalid option")

if __name__ == "__main__":
   main(start())
