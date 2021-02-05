import ipywidgets as widgets
from pytube import YouTube
from IPython.display import display
text=widgets.Label("Youtube Downloader")
Link=widgets.Text(placeholder="Enter the Link here",description='Link')
Button=widgets.Button(description='HQ VIDEO',icon='fa-youtube-square') #font_awesome is used for the icon
Button1=widgets.Button(description='AUDIO',icon='fa-music')
display(text,Link,Button,Button1)

def Download_Video(a):
    link=str(Link.value)
    obj=YouTube(link)
    video=obj.streams.filter(progressive=True,file_extension='mp4')
    for mp4 in video:
        video.get_highest_resolution().download(output_path="#path need to be saved") #getting highest resolution
    print("Downloaded Succesfully in path")
def Download_Audio(a):
    link=str(Link.value)
    obj=YouTube(link)
    obj.streams.get_audio_only().download(output_path="#path need to be saved") #getting only auido
    print("Downloaded Succesfully in path")
Button.on_click(Download_Video)
Button1.on_click(Download_Video)
