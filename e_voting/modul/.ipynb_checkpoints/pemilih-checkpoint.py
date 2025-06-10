listPemilih = []

def tambah_pemilih():
    idPemilih = input("Masukkan ID Pemilih :")
    if any(p['id'] == idPemilih for p in listPemilih):
        print("ID sudah terdaftar.")
        return
    namaPemilih = input("Masukkan nama pemilih :")
    jurusanPemilih = input("Masukkan jurusan pemilih :")

    listPemilih.append({"id": idPemilih,"nama": namaPemilih, "jurusan": jurusanPemilih, "sudah_memilih": False})
    print("Pemilih berhasil didaftarkan:")

def get_data():
    return listPemilih

def cari_pemilih(id):
    for p in listPemilih:
        if p['ID Pemilih'] == id:
            return p
    return None    