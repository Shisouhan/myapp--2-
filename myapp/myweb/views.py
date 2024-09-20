from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *

# class Art():
#     def __init__(self, _id, name, link, art):
#         self.id = _id
#         self.name = name
#         self.img = link
#         self.art = art

# landokmai = Art(1,'LANDOKMAI','https://th.bing.com/th/id/R.ac27e64bf80316a501fac1b372be3a6a?rik=MhDjzCTQmEA8lg&pid=ImgRaw&r=0',"LANDOKMAI")
# purpeech =  Art(2,'PURPEECH','https://th.bing.com/th/id/OIP.TBVLcYhxzScIoL0YqzYFigHaHa?rs=1&pid=ImgDetMain','PURPEECH')
# clocktai =  Art(3,'clocktail','https://th.bing.com/th/id/OIP.8mFg_mUI2D2-hOxnDSTKDAHaHm?rs=1&pid=ImgDetMain','clocktai')
# tdm =       Art(4,'Three man Down','https://th.bing.com/th/id/OIP.cXtNXvZ3c1vbIJf7-mCxaAAAAA?rs=1&pid=ImgDetMain','Three man Down')
# yorushika = Art(5, 'yorushika', 'https://styles.redditmedia.com/t5_ytkke/styles/communityIcon_zx8wrulvmzta1.png', 'yorushika')
# tuyu = Art(6, 'Tuyu', 'https://tuyu-official.jp/ogp.jpg', 'Tuyu')

# Arts = [landokmai ,purpeech ,clocktai , tdm, yorushika, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu, tuyu]

def index(request):
    Arts = Author.objects.all()
    if request.user.is_authenticated:
        playlists = Playlist.objects.filter(user=request.user)
    else:
        playlists = None
    return render(request, 'index.html',{"Arts":Arts,"playlists":playlists})

def signup(request):
    return render(request, "signup.html")

def addUser(request):
    username = request.POST['username']
    firstname = request.POST['f_name']
    lastname = request.POST['l_name']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword :
        if User.objects.filter(username=username).exists():
            print('Username is already used')
            messages.success(request,'Username is already used')
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            messages.success(request,'Email is already used')
            return redirect('/signup')
        else:
            user = User.objects.create_user(
            username = username,
            first_name = firstname,
            last_name = lastname,
            email = email,
            password = password
            )
            user.save()
            return redirect('/login')
    else:
        messages.success(request,'password not match repassword')
        return redirect('/signup')

def login(request):
    return render(request, 'login.html')

def loginForm(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username , password=password)
    if user is not None:
        # username pass ถูก
        auth.login(request,user)
        return redirect('/')
    else:
        print('Login bo dai')
        messages.success(request,'Invalid username or password')
        return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/')

def art(request, Art_id):
    if request.user.is_authenticated:
        playlists = Playlist.objects.filter(user=request.user)
    else:
        playlists = None
    # ดัดแปลงนิดหน่อย
    Arts = Author.objects.get(id=Art_id)
    albums = Album.objects.filter(author=Arts)
    songs = Song.objects.filter(author=Arts)[:5]
    return render(request, "art.html", {"Arts": Arts,"albums": albums,"songs": songs,"playlists":playlists})

def playlist(request, song_id):
    songs = Song.objects.get(id=song_id)
    playlists = Playlist.objects.filter(user=request.user)
    return render(request,'playlist.html',{"playlists":playlists,"songs":songs})

def createplaylistwithsong(request,song_id):
    playlists = Playlist.objects.filter(user=request.user)
    songs = Song.objects.get(id=song_id)
    return render(request,"creatplaylistwithsong.html",{"song":songs,"playlists":playlists})

def addplaylistwithsong(request,song_id):
    song = Song.objects.get(id=song_id)
    name = request.POST['name']
    desc = request.POST['desc']
    new_playlist = Playlist.objects.create(
        user=request.user,
        name=name,
        description=desc
    )
    new_playlist.save()
    ps = PlaylistSong.objects.create(
        playlist=new_playlist,
        song=song
    )
    ps.save()
    return redirect('/')

def createplaylist(request):
    playlists = Playlist.objects.filter(user=request.user)
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        new_playlist = Playlist.objects.create(
        user=request.user,
        name=name,
        description=desc
        )
        new_playlist.save()
        return redirect('/')
    else:
        return render(request,"createplaylist.html",{"playlists":playlists})
    

def detailplaylist(request,playlist_id):
    playlists = Playlist.objects.filter(user=request.user)
    playlist = Playlist.objects.get(id=playlist_id)
    playlistSong  = PlaylistSong.objects.filter(playlist=playlist) 
    return render(request,"detailplaylist.html",{"playlist":playlist,"playlists":playlists,"playlistSong":playlistSong})

def addtoplaylist(request, songs_id, playlist_id):
    playlists = Playlist.objects.filter(user=request.user)
    playlist = Playlist.objects.get(id=playlist_id)
    playlistSong = PlaylistSong.objects.filter(playlist=playlist)
    song = Song.objects.get(id=songs_id)
    if not PlaylistSong.objects.filter(playlist=playlist, song=song).exists():
        ps = PlaylistSong.objects.create(
            playlist=playlist,
            song=song
        )
        ps.save()

    return render(request, "detailplaylist.html", {"playlist": playlist, "playlists": playlists, "playlistSong": playlistSong})

def deletesong(request, song_id, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    song = Song.objects.get(id=song_id)  
    playlist_song = PlaylistSong.objects.filter(playlist=playlist, song=song)
    playlist_song.delete()  
    playlists = Playlist.objects.filter(user=request.user)
    playlistSong = PlaylistSong.objects.filter(playlist=playlist)
    return render(request, "detailplaylist.html", {"playlist": playlist, "playlists": playlists, "playlistSong": playlistSong})


def deleteplaylist(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    playlist.delete()
    return redirect('/')

def songInAlbum(request):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'songInAlbum.html', {'number': x, 'playlists': playlists})

def songDetail(request):
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'songDetail.html', {'playlists': playlists})