import ipywidgets as widgets
from pytube import YouTube
from IPython.display import display
text=widgets.Label("Youtube Downloader")
Link=widgets.Text(placeholder="Enter the Link here",description='Link')
Button=widgets.Button(description='Download',icon='fa-youtube-square')
display(text,Link,Button)

def Download(a):
    link=str(Link.value)
    obj=YouTube(link)
    video=obj.streams.filter(progressive=True,file_extension='mp4')
    for mp4 in video:
        video.get_highest_resolution().download(output_path="/home/anthony/Downloads")
    print("Downloaded Succesfully in path")
Button.on_click(Download)
