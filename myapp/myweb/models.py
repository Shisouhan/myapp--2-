from django.db import models
from django.contrib.auth.models import User

# โมเดล ผู้แต่ง
class Author(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    bg = models.CharField(max_length=200, default='default_background_image')  # กำหนดค่าเริ่มต้น
    nationality = models.CharField(max_length=100)
    bio = models.TextField()
    website = models.CharField(max_length=100)
   

    def __str__(self):
        return self.name

# โมเดล อัลบั้ม
class Album(models.Model):
    title = models.CharField(max_length=200)  # ชื่ออัลบั้ม
    release_date = models.DateField()  # วันที่ปล่อยอัลบั้ม
    cover_image = models.CharField(max_length=200) # ปกอัลบั้ม
    genre = models.CharField(max_length=100)  # ประเภทของอัลบั้ม
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ผู้แต่ง (foreign key)
    
    def __str__(self):
        return self.title

# โมเดล เพลง
class Song(models.Model):
    title = models.CharField(max_length=200)  # ชื่อเพลง
    duration = models.DurationField()  # ความยาวของเพลง
    release_date = models.DateField()  # วันที่ปล่อยเพลง
    img = models.CharField(max_length=200)  # 
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ผู้แต่ง (foreign key)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', blank=True, null=True)  # อัลบั้ม (foreign key)
    link = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.title

# โมเดล เพลย์ลิสต์
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ผู้ใช้ (foreign key)
    name = models.CharField(max_length=100)  # ชื่อเพลย์ลิสต์
    description = models.TextField(blank=True)  # คำอธิบายเพลย์ลิสต์
    created_at = models.DateTimeField(auto_now_add=True)  # วันที่สร้าง
    updated_at = models.DateTimeField(auto_now=True)  # วันที่แก้ไขล่าสุด
    

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='playlist_songs')
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
