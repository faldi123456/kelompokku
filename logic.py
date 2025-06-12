import random

def bagi_kelompok(daftar_mahasiswa, jumlah_per_kelompok):
    random.shuffle(daftar_mahasiswa)
    kelompok = []
    for i in range(0, len(daftar_mahasiswa), jumlah_per_kelompok):
        kelompok.append(daftar_mahasiswa[i:i + jumlah_per_kelompok])
    return kelompok
