from tkinter import *
from tkinter import messagebox
from pytube import *
from pytube import Playlist

ablak = Tk()
ablak.title('A legjobb YouTube-videóletöltő szoftver valaha')
ablak.geometry('700x500')
ablak.resizable(width=False, height=False)

def video():
    global urlInput
    url = urlInput.get()
    youtube = YouTube(url)
    try:
        video = youtube.streams.get_highest_resolution()
        video.download()
        messagebox.showinfo(title='Siker', message='Sikeres letöltés')
    except:
        messagebox.showerror(title='Hiba', message='Sajnos nem sikerült letölteni a videót. :( \nLehetséges problémák:\n - Nincs internet\n - A videó privát\n - A videó korhatáros')

def playlist():
    global urlInputPlaylist
    global urls
    playlist = urlInputPlaylist.get()
    urls = []
    playlist_urls = Playlist(playlist)

    for url in playlist_urls:
        urls.append(url)
    try:
        tobb_video(urls)
        messagebox.showinfo(title='Siker', message='Sikeres letöltés')
    except:
        messagebox.showerror(title='Hiba', message='Sajnos nem sikerült letölteni a videókat. :( \nLehetséges problémák:\n - Nincs internet\n - Egy vagy több videó privát\n - Egy vagy több videó korhatáros')

def tobb():
    global urlInputTobb
    videok = urlInputTobb.get(1.0, 'end-1c')
    video_lista = [y for y in (x.strip() for x in videok.splitlines()) if y] # ezt innen loptam: https://stackoverflow.com/questions/7630273/convert-multiline-into-list
    try:
        tobb_video(video_lista)
        messagebox.showinfo(title='Siker', message='Sikeres letöltés')
    except:
        messagebox.showerror(title='Hiba', message='Sajnos nem sikerült letölteni a videókat. :( \nLehetséges problémák:\n - Nincs internet\n - Egy vagy több videó privát\n - Egy vagy több videó korhatáros')

def tobb_video(videok):
    for video in videok:
        youtube = YouTube(video)
        vid = youtube.streams.get_highest_resolution()
        vid.download()

egyLabel = Label(ablak, text='Egy videó letöltése', font=('Calibri', 20))
egyLabel.place(x=0, y=0)

urlLabel = Label(ablak, text='Videó URL-je:', font=('Calibri', 15))
urlLabel.place(x=0, y=50)

urlInput = Entry(ablak, width=50)
urlInput.place(x=120, y=57)

buttonVideo = Button(ablak, text='Letöltés', command=video)
buttonVideo.place(x=450, y=54)

playlistLabel = Label(ablak, text='Lejátszási lista letöltése', font=('Calibri', 20))
playlistLabel.place(x=0, y=100)

urlLabelPlaylist = Label(ablak, text='Lejátszási lista URL-je:', font=('Calibri', 15))
urlLabelPlaylist.place(x=0, y=150)

urlInputPlaylist = Entry(ablak, width=37)
urlInputPlaylist.place(x=200, y=157)

buttonPlaylist = Button(ablak, text='Letöltés', command=playlist)
buttonPlaylist.place(x=450, y=150)

tobbLabel = Label(ablak, text='Több videó letöltése', font=('Calibri', 20))
tobbLabel.place(x=0, y=200)

tobbLabel2 = Label(ablak, text='Egy sor, egy videó. A videókat a program egymás után fogja letölteni.', font=('Calibri', 15))
tobbLabel2.place(x=0, y=230)

urlInputTobb = Text(ablak, width=70, height=10)
urlInputTobb.place(x=0, y=280)

buttonTobb = Button(ablak, text='Letöltés', command=tobb)
buttonTobb.place(x=0, y=450)

ablak.mainloop()
