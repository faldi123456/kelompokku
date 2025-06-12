import tkinter as tk
from tkinter import filedialog, messagebox
from logic import bagi_kelompok

def muat_mahasiswa(filepath):
    try:
        with open(filepath, 'r') as f:
            return [nama.strip() for nama in f if nama.strip()]
    except FileNotFoundError:
        return []

def simpan_hasil(kelompok, filepath):
    with open(filepath, 'w') as f:
        for i, grup in enumerate(kelompok, 1):
            f.write(f"Kelompok {i}:\n")
            for nama in grup:
                f.write(f"- {nama}\n")
            f.write("\n")

def tampilkan_kelompok(teks_box, kelompok):
    teks_box.delete('1.0', tk.END)
    for i, grup in enumerate(kelompok, 1):
        teks_box.insert(tk.END, f"Kelompok {i}:\n")
        for nama in grup:
            teks_box.insert(tk.END, f"- {nama}\n")
        teks_box.insert(tk.END, "\n")

def buat_gui():
    root = tk.Tk()
    root.title("Aplikasi Pembagi Kelompok")

    tk.Label(root, text="Jumlah anggota per kelompok:").pack()
    entry_jumlah = tk.Entry(root)
    entry_jumlah.pack()

    teks_hasil = tk.Text(root, height=20, width=50)
    teks_hasil.pack()

    def proses():
        jumlah = entry_jumlah.get()
        if not jumlah.isdigit():
            messagebox.showerror("Error", "Masukkan angka yang valid!")
            return
        daftar = muat_mahasiswa("data/daftar_mahasiswa.txt")
        if not daftar:
            messagebox.showerror("Error", "File daftar mahasiswa kosong atau tidak ditemukan.")
            return
        kelompok = bagi_kelompok(daftar, int(jumlah))
        tampilkan_kelompok(teks_hasil, kelompok)
        simpan_hasil(kelompok, "data/hasil_kelompok.txt")
        messagebox.showinfo("Sukses", "Hasil kelompok disimpan.")

    tk.Button(root, text="Bagi Kelompok", command=proses).pack()

    root.mainloop()
