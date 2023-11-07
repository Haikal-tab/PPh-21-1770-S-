print("---PERHITUNGAN PPH 21 (1770-S)---", "\n","\n")

print("---PENGHASILAN BRUTO---","\n")

income_1_tahun = float(input(f"Masukkan Gaji per Tahun Anda: Rp"))
print(f"(1). Penghasilan Anda 1 tahun: Rp{income_1_tahun:,}", "\n", "\n")

print("---TUNJANGAN iSTRI---")  #(tarif 10%)
tunjangan_istri = income_1_tahun*(10/100)
print(f"(2). Tunjangan Istri 1 Tahun: Rp{tunjangan_istri:,.0f}", "\n", "\n" )

print("---TUNJANGAN ANAK---")  #(tarif 4%)
tunjangan_anak = income_1_tahun*(4/100)
print(f"(3). Tunjangan Anak 1 Tahun: Rp{tunjangan_anak:,.0f}","\n","\n")

print("---JUMLAH GAJI & TUNJANGAN KELUARGA (1+2+3)---")
jumlah_gaji = income_1_tahun+tunjangan_istri+tunjangan_anak
print(f"(4). Jumlah Gaji 1 Tahun: Rp{jumlah_gaji:,.0f}", "\n", "\n")

print("---TUNJANGAN PERBAIKAN PENGHASILAN---")
tunjangan_perbaikan = income_1_tahun*(0/100)
print(f"(5). Tunjangan Perbaikan Penghasilan 1 Tahun: Rp{tunjangan_perbaikan:,.0f}","\n","\n")

print("---TUNJANGAN STRUKTURAL/FUNGSIONAL---")  #(tarif 19%)
tunjangan_struktural = income_1_tahun*(0.189852941)
print(f"(6). Tunjangan Struktural/Fungsional 1 Tahun: Rp{tunjangan_struktural:,.0f}","\n","\n")

print("---TUNJANGAN BERAS---")  #(tarif 8%)
tunjangan_beras = income_1_tahun*(0.0785665715)
print(f"(7). Tunjangan Beras 1 Tahun: Rp{tunjangan_beras:,.0f}","\n","\n")

print("---TUNJANGAN KHUSUS---")
tunjangan_khusus = income_1_tahun*(1.47814*10**-5)
print(f"(8). Tunjangan Khusus 1 Tahun: Rp{tunjangan_khusus:,.0f}","\n","\n")

print("---TUNJANGAN LAIN-LAIN---")
tunjangan_lainnya = income_1_tahun*(0/100)
print(f"(9). Tunjangan Lain-lain 1 Tahun: Rp{tunjangan_lainnya:,.0f}","\n","\n")

print("---JUMLAH (4 S.D. 9)---")
jumlah_4sd9 = jumlah_gaji + tunjangan_perbaikan + tunjangan_struktural + tunjangan_beras + tunjangan_khusus + tunjangan_lainnya
print(f"(10). Jumlah Gaji Bruto 1 Tahun: Rp{jumlah_4sd9:,.0f}","\n","\n")



print("---PENGURANG---","\n")

print("---BIAYA JABATAN---")  #(tarif 7%)
biaya_jabatan = income_1_tahun*(0.0704217)
print(f"(11). Biaya Jabatan: Rp{biaya_jabatan:,.0f}","\n","\n")

print("---IURAN PENSIUN---")  #(tarif 5%)
iuran_pensiun = income_1_tahun*(0.05415)
print(f"(12). Iuran Pensiun: Rp{iuran_pensiun:,.0f}","\n","\n")

print("---JUMLAH PENGURANGAN (11 + 12)---")
jumlah_pengurangan = biaya_jabatan + iuran_pensiun
print(f"(13). Biaya Jabatan: Rp{jumlah_pengurangan:,.0f}","\n","\n")



print("---PENGHITUNGAN PPh PASAL 21---","\n")

print("---PENGHASILAN NETO (10 - 13)---")
gaji_neto = jumlah_4sd9 - jumlah_pengurangan
print(f"(14). Jumlah Gaji Neto 1 Tahun: Rp{gaji_neto:,.0f}","\n","\n")

print("---PENGHASILAN TIDAK KENA PAJAK (PTKP)---", "\n")
z = float(input("Masukkan Tanggungan Anda (isi '4' jika Anda bukan Tidak Kawin): " ))

print("-----Pria/Wanita Tidak Kawin-----")
if z == 0:
    print(f"PTKP Anda: Rp",int(54*1000000), "\n")
elif z == 1:
    print(f"PTKP Anda: Rp",float(58.5*1000000), "\n")
elif z == 2:
    print(f"PTKP Anda: Rp",int(63*1000000), "\n")
elif z == 3:
    print(f"PTKP Anda: Rp",float(67.5*1000000), "\n")
else: 
    print("Status Anda bukan Pria/Wanita Tidak Kawin", "\n")



a = float(input("Masukkan Tanggungan Anda (Isi '4' jika Anda bukan Pria Kawin):"))

print("-----Pria Kawin-----")
if a==0:
    print(f"PTKP Anda: Rp",float(58.5*1000000), "\n")
elif a==1:
    print(f"PTKP Anda: Rp",int(63*1000000), "\n")
elif a==2:
    print(f"PTKP Anda: Rp",float(67.5*1000000), "\n")
elif a==3:
    print(f"PTKP Anda: Rp",int(72*1000000), "\n")
else: 
    print("Status Anda Bukan Pria Kawin", "\n")



b = float(input("Masukan Tanggungan Anda (Isi '4' jika Anda bukan Suami & Istri Digabung):"))

print("-----Suami & Istri Digabung-----")
if b==0:
    print(f"PTKP Anda: Rp",float(112.5*1000000), "\n")
elif b==1:
    print(f"PTKP Anda: Rp",int(117*1000000), "\n")
elif b==2:
    print(f"PTKP Anda: Rp",float(121.5*1000000), "\n")
elif b==3:
    print(f"PTKP Anda: Rp",int(126*1000000), "\n")
else:
    print("Status Anda Bukan Suami & Istri Digabung", "\n", "\n")



print("---Penghitungan Penghasilan Kena Pajak (PKP)---\n")

p = float(input("Masukkan PTKP Anda: Rp"))
print(f"PTKP: Rp{p:,.0f}")
pkp = gaji_neto-p
print(f"PKP: Rp{pkp:,.0f}")

print(f"Nilai Maks. Lapisan ke-1: 60,000,000")
print(f"Nilai Maks. Lapisan ke-2: 250,000,000")
print(f"Nilai Maks. Lapisan ke-3: 500,000,000")
print(f"Nilai Maks. Lapisan ke-4: 5,000,000,000\n")

print("---ALOKASI TARIF PROGRESIF---\n")
number_1 = float(input("Masukkan PKP: Rp"))
number_2 = int(60000000)
number_3 = int(250000000)
number_4 = int(500000000)
number_5 = int(5000000000)
# number_2 = float(input("Nilai Maks. Lapisan ke-1: Rp"))
# number_3 = float(input("Nilai Maks. Lapisan ke-2: Rp"))
# number_4 = float(input("Nilai Maks. Lapisan ke-3: Rp"))
# number_5 = float(input("Nilai Maks. Lapisan ke-4: Rp"))
print(" ")


# Perhitungan PKP untuk Lapisan ke-1
if pkp >= number_1 :
    print(f"Nilai lapisan ke-1: Rp{number_2:,.0f}")
elif pkp < number_2:
    print(f"Nilai untuk lapisan ke-1: Rp{pkp:,.0f}")

hasil_alokasi_1 = number_1 - number_2
if hasil_alokasi_1 >= number_3:
    print(f"Nilai untuk lapisan ke-2: Rp{number_3:,.0f}")
elif hasil_alokasi_1 < number_3:
    print(f"Nilai untuk lapisan ke-2: Rp{hasil_alokasi_1:,.0f}")

hasil_alokasi_2 = hasil_alokasi_1 - number_3
if hasil_alokasi_2 >= number_4:
    print(f"Nilai untuk lapisan ke-3: Rp{number_4:,.0f}")
elif hasil_alokasi_2 < number_4:
    print(f"Nilai untuk lapisan ke-3: Rp{hasil_alokasi_2:,.0f}")

hasil_alokasi_3 = hasil_alokasi_2 - number_4
if hasil_alokasi_3 >= number_5:
    print(f"Nilai untuk lapisan ke-4: Rp{number_5:,.0f}")
elif hasil_alokasi_2 < number_5:
    print(f"Nilai untuk lapisan ke-4: Rp{hasil_alokasi_3:,.0f}")

hasil_alokasi_4 = hasil_alokasi_3 - number_5
print(f"Nilai untuk lapisan ke-5: Rp{hasil_alokasi_4:,.0f}")


# hasil_alokasi_1 = number_1 - number_2
# print(f"Nilai untuk lapisan ke-2: Rp{hasil_alokasi_1:,.0f}")

# hasil_alokasi_2 = number_2 - number_3
# print(f"Nilai untuk lapisan ke-3: Rp{hasil_alokasi_2:,.0f}")

# hasil_alokasi_3 = number_3 - number_4
# print(f"Nilai untuk lapisan ke-4: Rp{hasil_alokasi_2:,.0f}")

# hasil_alokasi_4 = number_5 - 0
# print(f"Nilai untuk lapisan ke-5: Rp{hasil_alokasi_2:,.0f}", "\n")

print(f"*Note = Jika nilainya negatif(minus) tidak masuk ke tarif progresif\n\n")


print("---TARIF PROGRESIF--- \n")


print("Lapisan Penghasilan Kena Pajak:")

print("1 : Rp0-Rp60 jt        = 5%")
print("2 : >60 jt-Rp250 jt    = 15%")
print("3 : >Rp250 jt-Rp500 jt = 25%")
print("4 : >Rp500 jt-Rp5 M    = 30%")
print("5 : >Rp5 M             = 35% \n")

hitung_pkp_1= float(input("Masukkan PKP (Lapisan 1), (ketik '0' jika lapisan Anda tdk sampai di sini): "))
hasil_1 = hitung_pkp_1*(0.04999765718744333958762424546156)
if hitung_pkp_1 == 0:
    print("Selesai")
elif hitung_pkp_1 > 1:
    print(f"Pajak per Tahun Anda: Rp{hasil_1:,.0f}")

print(" ")


hitung_pkp_2= float(input("Masukkan PKP (Lapisan 2), (ketik '0' jika lapisan Anda tdk sampai di sini): "))
hasil_2 = hitung_pkp_2*(15/100)
if hitung_pkp_2 == 0:
    print("Selesai")
elif hitung_pkp_2 > 1:
    print(f"Pajak per Tahun Anda: Rp{hasil_2:,.0f}")

print(" ")


hitung_pkp_3= float(input("Masukkan PKP (Lapisan 3), (ketik '0' jika lapisan Anda tdk sampai di sini): "))
hasil_3 = hitung_pkp_3*(25/100)
if hitung_pkp_3 == 0:
    print("Selesai")
elif hitung_pkp_3 > 1:
    print(f"Pajak per Tahun Anda: Rp{hasil_3:,.0f}")

print(" ")


hitung_pkp_4= float(input("Masukkan PKP (Lapisan 4), (ketik '0' jika lapisan Anda tdk sampai di sini): "))
hasil_4 = hitung_pkp_4*(30/100)
if hitung_pkp_4 == 0:
    print("Selesai")
elif hitung_pkp_3 > 1:
    print(f"Pajak per Tahun Anda: Rp{hasil_4:,.0f}")

print(" ")


hitung_pkp_5= float(input("Masukkan PKP (Lapisan 5), (ketik '0' jika lapisan Anda tdk sampai di sini): "))
hasil_5 = hitung_pkp_5*(35/100)
if hitung_pkp_5 == 0:
    print("Selesai")
elif hitung_pkp_3 > 1:
    print(f"Pajak per Tahun Anda: Rp{hasil_5:,.0f}")

print(" ")


print(f"===Pajak Terutang per Tahun===")

angka_1 = float(input("Masukkan lapisan 1: "))
angka_2 = float(input("Masukkan lapisan 2: "))
angka_3 = float(input("Masukkan lapisan 3: "))
angka_4 = float(input("Masukkan lapisan 4: "))
angka_5 = float(input("Masukkan lapisan 5: "))
print(" ")


hasil_pajak = angka_1 + angka_2 + angka_3 + angka_4 + angka_5
print(f"Pajak Terutang per Tahun: Rp{hasil_pajak:,.0f}", "\n")


print("#ayobayarpajak!")

print("CREATED BY: MUHAMMAD HAIKAL MUTHAHHARI")

v = input("Selesai")
