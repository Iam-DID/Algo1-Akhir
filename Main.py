import pandas as pd
import os
from tabulate import tabulate
import time
from datetime import datetime,timedelta

def Cek_Data() : 
    dir=os.getcwd() 
    isi_dir=os.listdir(dir) 
    if "Barang.csv" not in isi_dir :
        buatcsv=dir+"\\Barang.csv"
        file=open(buatcsv,"w") 
        file.write("id\n") 
        file.close()
        with open("Barang.csv","r") as file_barang :
            df_barang = pd.read_csv(file_barang)
            konten_barang= {"id"          : "1",
                          "Nama Barang" : "PupukA",
                          "Harga"       : "10000",
                          "Stock"       : "100",
                          "Milik"       : "SyadidCH"
                          }
            df_barang = pd.concat([df_barang,pd.DataFrame([konten_barang])], ignore_index=False) 
            df_barang.to_csv("Barang.csv",index=False)  
    if "Data_User.csv" not in isi_dir :
        buatcsv=dir+"\\Data_User.csv"
        file=open(buatcsv,"w")
        file.write("Nama\n")
        file.close()
        with open("Data_User.csv","r") as file_user :
            df_user = pd.read_csv(file_user, dtype={"Nomor" : "str"})
            konten_user= {"Nama"    : "SyadidCH",
                          "Nomor"   : "085606359701",
                          "Alamat"  : "Lumajang",
                          "Password": "did",
                          "status"  : "admin"
                          }
            df_user = pd.concat([df_user,pd.DataFrame([konten_user])], ignore_index=False)
            df_user.to_csv("Data_User.csv",index=False)
    if "Log_Pembelian.csv" not in isi_dir :
        buatcsv=dir+"\\Log_Pembelian.csv"
        file=open(buatcsv,"w")
        file.write("Waktu Pemesanan,id,Nama Barang,Jumlah,Harga,Pemesan,Waktu ACC")
        file.close()
    if "Keranjang.csv" not in isi_dir :
        buatcsv=dir+"\\Keranjang.csv"
        file=open(buatcsv,"w")
        file.write("id,Nama Barang,Jumlah,Harga,Milik")
        file.close()
    if "Member.csv" not in isi_dir :
        buatcsv=dir+"\\Member.csv"
        file=open(buatcsv,"w")
        file.write("Nama")
        file.close()        

def awal_login(): 
    Cek_Data()
    os.system("cls")
    print("""
          
████████╗ █████╗ ███╗   ██╗██╗███╗   ███╗ █████╗ ██████╗ ████████╗
╚══██╔══╝██╔══██╗████╗  ██║██║████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝
   ██║   ███████║██╔██╗ ██║██║██╔████╔██║███████║██████╔╝   ██║   
   ██║   ██╔══██║██║╚██╗██║██║██║╚██╔╝██║██╔══██║██╔══██╗   ██║   
   ██║   ██║  ██║██║ ╚████║██║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
            Toko Untuk Segala Kebutuhan Pertanianmu                                                  

          """)
    time.sleep(3)
    os.system('cls')
    while True :
        print('Selamat datang di TaniMart, Silahkan Login Terlebih Dahulu')
        print("1. Login")
        print("2. Belum punya akun? Register")
        pilihan=input("Masukkan Pilihan Anda : ")
        if pilihan=="1":
            os.system('cls')
            login()
            break
        if pilihan=="2":
            os.system('cls')
            register()
            break
        else :
            os.system('cls')
            print("Harap Untuk Input Pilihan Yang Tersedia!")  
            
def login(): 
    while True :
        hp=input("Masukkan Nomor HP anda : ")
        if hp=="" :
            awal_login()
        try :
            nohp=int(hp)
            break
        except ValueError :
            os.system('cls')
            print("Harap Diisi Angka")
    with open("Data_User.csv","r") as file :
        isifile=pd.read_csv(file,dtype={"Nomor": str,"Password": str})
    if hp in isifile["Nomor"].values:
        password=str(input("Masukkan Password : "))
        for i in range(len(isifile["Nomor"])):
            if hp == isifile.iloc[i,1] :
                letak=i
                global posisi 
                posisi=letak
        if password==isifile.iloc[letak,3] and isifile.iloc[letak,4]=="customer":
            menu_customer()
        elif password==isifile.iloc[letak,3] and isifile.iloc[letak,4]=="admin":
            menu_admin()
        else:
            print('Password Salah!')
            enter=input('Tekan Enter Untuk Kembali')
            os.system('cls')
            login()
    else: 
        print('Data User Tidak Ditemukan!')
        enter=input('Tekan Enter Untuk Kembali')
        os.system('cls')
        login()

def register():
    with open("Data_User.csv","r") as file :
        isifile=pd.read_csv(file)
    print("1. Registrasi Akun")
    print("2. Kembali")
    pilihan=input('Masukkan Pilihan Anda :')
    os.system('cls')
    if pilihan=="1" :
        while True :
            while True :
                 nama=str(input("Masukkan Nama Anda :"))
                 if nama=="":
                     awal_login()
                 namauser=(isifile["Nama"])
                 if nama.lower() not in namauser.str.lower().values :
                     break
                 else :
                     print("Username Sudah Terpakai !")
                     enter=input("Tekan Enter Untuk Melanjutkan")
                     os.system("cls")
            while True :
                alamat=input('Masukkan Alamat Anda :')
                if alamat =="" :
                    print('Alamat Tidak Boleh Kosong')
                    input("Tekan Enter Untuk Melanjutkan")
                    os.system("cls")
                    print(f"Masukkan Nama Anda :{nama}")
                else : 
                    break
                
            with open("Data_User.csv","r") as file :
                isifile=pd.read_csv(file,dtype={"Nomor": str})
            while True :
                hp=input('Masukkan No. HP Anda :')
                if hp=="":
                    print('Nomor HP Tidak Boleh Kosong')
                    input("Tekan Enter Untuk Melanjutkan")
                    os.system("cls")
                    print(f"Masukkan Nama Anda :{nama}")
                    print(f"Masukkan Alamat Anda :{alamat}")
                    continue
                try :
                    nohp=int(hp)
                    if hp not in isifile["Nomor"].values:
                        break
                    else :
                        print('Nomor HandPhone Sudah Terdaftar Di Akun Lain! Silahkan Menggunakan Nomor Lain')
                        enter=input("Tekan Enter Untuk Melanjutkan")
                        os.system("cls")
                        print(f"Masukkan Nama Anda :{nama}")
                        print(f"Masukkan Alamat Anda :{alamat}")
                except ValueError :
                    print('Nomor HandPhone Harus Berupa Angka, Silahkan Registrasi Ulang')
                    enter=input("Tekan Enter Untuk Melanjutkan")
                    os.system("cls")
                    print(f"Masukkan Nama Anda :{nama}")
                    print(f"Masukkan Alamat Anda :{alamat}")
            break
        while True : 
            print("Silahkan Pilih Mode Akun Yang Ingin didaftarkan : ")
            print("1. Admin")
            print("2. Customer")
            mode=input("Silahkan Masukkan Pilihan Anda :")
            if mode=="1" or mode=="2" :
                while True :
                    while True :
                        password=input("Silahkan membuat password : ")     
                        password2=input("Konfirmasi password : ")
                        if password==password2 :
                            break    
                        else :
                            print("Silahkan Cek Ulang Password anda")
                            enter=input("Tekan Enter untuk melanjutkan")
                            os.system("cls")
                            print(f"Masukkan Nama Anda :{nama}")
                            print(f"Masukkan Alamat Anda :{alamat}")
                            print(f'Masukkan No. HP Anda :{hp}')
                            print("Silahkan Pilih Mode Akun Yang Ingin didaftarkan : ")
                            print("1. Admin")
                            print("2. Customer")
                            print(f"Silahkan Masukkan Pilihan Anda :{mode} ")
                    if password==password2 and mode=="1":
                        with open("Data_User.csv","r")as file :
                            df_user = pd.read_csv(file, dtype={"Nomor" : "str"})
                            konten_user= {"Nama" : nama,
                                          "Nomor" : str(hp),
                                          "Alamat": alamat,
                                          "Password" : password,
                                          "status" : "admin"}
                            df_user = pd.concat([df_user,pd.DataFrame([konten_user])], ignore_index=False)
                            df_user.to_csv("Data_User.csv",index=False)
                        print(f"Pembuatan Akun Baru Berhasil! Selamat Datang Di Tani Mart {nama}")
                        pilihan=input("Tekan Enter untuk kembali ke Menu Awal")
                        os.system('cls')
                        awal_login()
                        break
                    elif password==password2 and mode=="2":
                        with open("Data_User.csv","r")as file :
                            df_user = pd.read_csv(file, dtype={"Nomor" : "str"})
                            konten_user= {"Nama" : nama,
                                          "Nomor" : str(hp),
                                          "Alamat": alamat,
                                          "Password" : password,
                                          "status" : "customer"}
                            df_user = pd.concat([df_user,pd.DataFrame([konten_user])], ignore_index=False)
                            df_user.to_csv("Data_User.csv",index=False)
                        print(f'Pembuatan Akun Baru Berhasil! Selamat Datang Di Tani Mart "{nama}"')
                        pilihan=input("Tekan Enter untuk kembali ke Menu Awal")
                        os.system('cls')
                        awal_login()
                        break
                break
            else : 
                print('Silahkan Memilih Pilihan Yang Tersedia!')
                enter=input("Tekan Enter Untuk Melanjutkan")
                os.system("cls")
                print(f"Masukkan Nama Anda :{nama}")
                print(f"Masukkan Alamat Anda :{alamat}")
                print(f'Masukkan No. HP Anda :{hp}')
    elif pilihan=="2" :
        os.system('cls')
        awal_login()
    else :
        os.system('cls')
        print("Harap Untuk Input Pilihan Yang Tersedia!")
        register()
        
def users():
    with open("Data_User.csv","r") as file :
        isifile=pd.read_csv(file)
    return isifile.iloc[posisi,0] 

def menu_admin():
    os.system('cls')
    print(f'Halo, Selamat datang admin "{users()}"') 
    print("1.Katalog Barang")
    print("2.Pesanan") 
    print("0.Log Out")
    pilihan=input("Masukkan Pilihan Anda :")
    if pilihan=="1":
        lanjut_CRUD()
    elif pilihan=="2":
        log_admin()
    elif pilihan=="0" :
        awal_login()
    else :
        input("Harap Masukkan Inputan Yang Valid")
        menu_admin()
        
def katalog_admin():
    namapengguna=users()
    with open("Barang.csv","r") as file :
        isifile=pd.read_csv(file)
        barang_pengguna = isifile[isifile["Milik"] == namapengguna]
    barang=isifile["Milik"].values
    panjang=0
    for i in barang :
        if namapengguna==i:
            panjang+=1
    kurang=5-(panjang%5)
    indextampilawal=[]
    indextampilakhir=[]
    if panjang>0:
        for i in range (0,panjang,5) :
            if panjang%5!=0 :
                if i==(panjang-(panjang%5)) :
                    a=i
                    b=i+(5-kurang)
                    indextampilawal.append(a)
                    indextampilakhir.append(b)
                else :
                    a=i
                    b=i+5
                    indextampilawal.append(a)
                    indextampilakhir.append(b)
            else :
                a=i
                b=i+5
                indextampilawal.append(a)
                indextampilakhir.append(b)
        inow=0 
        os.system("cls")
        print(tabulate(barang_pengguna.iloc[indextampilawal[inow]:indextampilakhir[inow]],headers="keys",showindex=False))
        while True :
            print("\n1.Next")
            print("2.Back")
            print("3.Kelola Barang")
            print("0.Exit Menu")
            pilih=input("Masukkan Pilihan Anda :") 
            if pilih == "1" :
                if inow<len(indextampilawal)-1 :
                    os.system("cls")
                    inow+=1
                    print(tabulate(barang_pengguna.iloc[indextampilawal[inow]:indextampilakhir[inow]],headers="keys",showindex=False))
                else :
                    os.system("cls")
                    print(tabulate(barang_pengguna[indextampilawal[inow]:indextampilakhir[inow]],headers="keys",showindex=False))
                    print("\nList Sudah Mencapai Page Terakhir")
            elif pilih == "2" :
                if inow>0 :
                    os.system("cls")
                    inow-=1
                    print(tabulate(barang_pengguna.iloc[indextampilawal[inow]:indextampilakhir[inow]],headers="keys",showindex=False))
                else :
                    os.system("cls")
                    print(tabulate(barang_pengguna.iloc[indextampilawal[inow]:indextampilakhir[inow]],headers="keys",showindex=False))
                    print("\nList Sudah Berada pada posisi awal")
            elif pilih == "0" :
                menu_admin()
                break
            elif pilih == "3" :
                os.system('cls')
                tabel=(tabulate(barang_pengguna.iloc[indextampilawal[inow]:indextampilakhir[inow]],headers="keys",showindex=False))
                return tabel
            else :
                    os.system("cls")
                    print(tabulate(barang_pengguna.iloc[indextampilawal[inow]:indextampilakhir[inow]],headers="keys",showindex=False))
                    print("\nHarap Masukkan Inputan Yang Valid")
                    
    else :
        print("Anda Belum Memasukkan Barang Apapun!")
        enter=input("Tekan Enter Untuk Kembali atau 1 Untuk Menambah Data :")
        if enter=="1" :
            os.system("cls")
            tambah_barang()
        else :
            os.system("cls")
            menu_admin()

def lanjut_CRUD() : 
    tabel=""
    tabel = katalog_admin() 
    if tabel: 
        CRUD(tabel)
        
def CRUD(tabel): 
    while True :
        os.system("cls")
        print(tabel)
        print("\nApa Yang Ingin Anda Lakukan?")
        print("1.Tambah Barang")
        print("2.Hapus Barang")
        print("3.Update Barang")
        print("0.Exit Menu")
        pilih=input("Masukkan Pilihan Anda :")      
        if pilih=="1" :
            tambah_barang()
        elif pilih=="2":
            hapus_barang(tabel)
        elif pilih=="3":
            update_barang(tabel)
        elif pilih=="0" :
            menu_admin()
        else :
            print("Inputan Tidak Valid")
            Enter=input("Tekan Enter Untuk Melanjutkan")
            CRUD(tabel)
            
def tambah_barang(): 
    os.system("cls")
    admin=users()
    while True :
        with open("Barang.csv","r") as file :
            isifile=pd.read_csv(file)
            idnow=isifile.loc[isifile.index[-1], "id"]+1
        barang=input("Masukkan Nama Barang (0 untuk kembali) :")
        if barang=="":
            input("Nama Barang Tidak Boleh Kosong")
            os.system("cls")
            continue
        if barang=="0":
            return
        while True :
            try : 
                harga=int(input("Masukkan Harga Barang (0 untuk kembali) :"))
                if harga<1000 :
                    input("Harga Harus Diatas 1000")
                    os.system("cls")
                    print(f"Masukkan Nama Barang (0 untuk kembali) :{barang}")
                else : 
                    break
            except ValueError :
                input("Harga Harus Berupa Angka")
                os.system("cls")
                print(f"Masukkan Nama Barang (0 untuk kembali) :{barang}")
        while True :
            try :
                stock=int(input("Masukkan Stock Barang : "))
                
                break
            except ValueError :
                print("Stock Harus Berupa Angka")
                enter=input("Tekan Enter Untuk melanjutkan")
                os.system("cls")
                print(f"Masukkan Nama Barang (0 untuk kembali) :{barang}")
                print(f"Masukkan Harga Barang (0 untuk kembali) :{harga}")
        konten={"id"          : idnow,
                "Nama Barang" : barang,
                "Harga"       : harga,
                "Stock"       : stock,
                "Milik"       : admin}
        isifile = pd.concat([isifile,pd.DataFrame([konten])], ignore_index=False)
        isifile.to_csv("Barang.csv",index=False)
        print("Barang Berhasil Ditambahkan!")
        print(f"Detail Data \nid : {idnow} \nNama Barang : {barang} \nHarga : {harga} \nStock : {stock}")
        enter=input("Tekan Enter Untuk Kembali")
        break
    os.system("cls")
    lanjut_CRUD()         
                    
def hapus_barang(tabel): 
    while True :
        os.system("cls")
        print(tabel)
        try :
            pilih=int(input("Masukkan ID Barang Yang Ingin Dihapus (0 Untuk Kembali) : "))
            if pilih==0:
                return
            else :
                with open("Barang.csv","r") as file :
                    isifile=pd.read_csv(file)
                if pilih in isifile["id"].values :
                    df=isifile[isifile["id"] != pilih]
                    df.to_csv("Barang.csv", index=False)
                    print("Data Berhasil Dihapus!")
                    enter=input("Tekan Enter Untuk Melanjutkan")
                    lanjut_CRUD()
                else :
                    print("Barang Tidak Ada")
                    enter=input("Tekan Enter Untuk Melanjutkan")
        except ValueError :
            print("Input Harus Berupa Angka")
            enter=input("Tekan Enter Untuk Melanjutkan")
 
def update_barang(tabel): 
    while True :
        os.system("cls")
        print(tabel)
        while True :
            os.system("cls")
            try :
                print(tabel)
                pilihid=int(input("Masukkan ID Barang Yang Ingin Diedit (0 Untuk Kembali) : "))
                if pilihid==0:
                    return
                else :
                    while True :
                        os.system("cls")
                        print(tabel)
                        with open("Barang.csv","r") as file :
                            isifile=pd.read_csv(file)
                        if pilihid in isifile["id"].values :
                            print("\nApa Yang Ingin Anda Ubah?")
                            print("1.Nama Barang")
                            print("2.Harga Barang")
                            print("3.Stock Barang")
                            print("0.Exit")
                            pilihan1=input("Masukkan pilihan : ")
                            if pilihan1=="1":
                                inputan=input("Masukkan Update Nama Barang (0 Untuk Kembali) :")
                                if inputan=="0" :
                                    continue
                                elif inputan=="" :
                                    input("Nama Barang Tidak Boleh Kosong")
                                    continue
                                isifile.loc[isifile["id"] == pilihid, "Nama Barang"] = inputan
                                isifile.to_csv("Barang.csv", index=False)
                                enter=input("Update Berhasil! Enter untuk Kembali")
                                lanjut_CRUD() 
                            elif pilihan1=="2":
                                try :
                                    inputan=int(input("Masukkan Update Harga Barang (0 Untuk Kembali) :"))
                                    if inputan == 0 :
                                        continue
                                    if inputan <1000 :
                                        input("Harga Harus Diatas 1000")
                                        continue   
                                    isifile.loc[isifile["id"] == pilihid, "Harga"] = inputan
                                    isifile.to_csv("Barang.csv", index=False)
                                    enter=input("Update Berhasil! Enter untuk Kembali")
                                    lanjut_CRUD() 
                                except ValueError:
                                    input("Harga Harus Berupa Angka")
                                    continue
                            elif pilihan1=="3":
                                try :
                                    inputan=int(input("Masukkan Update Stock Barang (0 Untuk Kembali) :"))
                                    if inputan== 0  :
                                        continue
                                    isifile.loc[isifile["id"] == pilihid, "Stock"] = inputan
                                    isifile.to_csv("Barang.csv", index=False)
                                    enter=input("Update Berhasil! Enter untuk Kembali")
                                    lanjut_CRUD() 
                                except ValueError:
                                    input("Stock Harus Berupa Angka")
                                    continue
                            elif pilihan1=="0":
                                menu_admin()
                            else : 
                                print("Harap Masukkan Inputan Yang Valid")
                                enter=input("Tekan Enter Untuk Melanjutkan")   
                        else :
                            print("Barang Tidak Ada")
                            enter=input("Tekan Enter Untuk Melanjutkan")    
            except ValueError :
                print("Input Harus Berupa Angka")
                enter=input("Tekan Enter Untuk Melanjutkan")

def log_admin():
    username = users() 
    df_log = pd.read_csv("Log_Pembelian.csv") 
    df_barang = pd.read_csv("Barang.csv") 
    df_barang_filtered = df_barang[df_barang["Milik"] == username]
    id_barang_milik = df_barang_filtered["id"].values
    df_log_filtered = df_log[df_log["id"].isin(id_barang_milik)]
    if df_log_filtered.empty:
        input("Tidak ada log pembelian untuk barang milik Anda.")
        menu_admin()
    else:
        os.system("cls")
        print(tabulate(df_log_filtered, headers="keys", showindex=False, tablefmt="grid"))
        df_to_acc = df_log_filtered[df_log_filtered["Waktu ACC"] == "Belum di ACC"]
        if df_to_acc.empty:
            input("\nSemua barang sudah di-ACC.")
            menu_admin()
        else:
            pilihan = input("\nMasukkan ID barang yang ingin di-ACC (pisahkan dengan koma jika lebih dari satu): ").strip()
            if pilihan:
                try:
                    id_pilihan = [int(id.strip()) for id in pilihan.split(",")]
                    valid_ids = df_to_acc[df_to_acc["id"].isin(id_pilihan)]
                    if valid_ids.empty:
                        input("\nID yang dimasukkan tidak valid atau sudah di-ACC sebelumnya.")
                        menu_admin()
                    else:
                        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        df_log.loc[valid_ids.index, "Waktu ACC"] = waktu_sekarang
                        df_log.to_csv("Log_Pembelian.csv", index=False)
                        for index, row in valid_ids.iterrows():
                            id_barang = row["id"]
                            jumlah_dibeli = row["Jumlah"]
                            df_barang.loc[df_barang["id"] == id_barang, "Stock"] -= jumlah_dibeli
                        df_barang.to_csv("Barang.csv", index=False)
                        input("\nPermintaan berhasil di-ACC untuk ID yang dipilih, stok telah diperbarui.")
                        menu_admin()
                except ValueError:
                    input("\nInput tidak valid. Harap masukkan angka ID yang valid.")
                    menu_admin()
            else:
                input("\nTidak ada ID yang dipilih. Kembali ke menu admin.")
                menu_admin()
            
def menu_customer():
    while True:
        os.system('cls')
        print(f'Halo, Selamat datang {users()}')
        print("1. Lihat Barang")
        print("2. Keranjang")
        print("3. Status Member")
        print("4. Log Pembelian")
        print("0. Log Out") 
        pilihan=input("Masukkan Pilihan Anda :") 
        if pilihan=="1":
            barang_customer()  
        elif  pilihan=="2":
            keranjang()
        elif pilihan=="3" :
            status_member()
        elif pilihan=="4":
            log_customer()
        elif pilihan=="0":
            os.system("cls")
            awal_login()
        else :
            input("Harap Masukkan Inputan Yang Valid")
            
def tabel_keranjang():
    os.system("cls")
    nama=users()
    df=pd.read_csv("Keranjang.csv")
    df=df[df["Milik"]==nama].drop(columns=["Milik"])
    print(tabulate(df,headers="keys",showindex=False))

def keranjang():
    username = users() 
    datakeranjang = pd.read_csv("Keranjang.csv")
    datakeranjang = datakeranjang[datakeranjang["Milik"] == username]

    if datakeranjang.empty:
        input("Keranjang Kosong, Enter Untuk Melanjutkan")
        return
    else:
        tabel_keranjang()
        df = pd.read_csv("Keranjang.csv")
        df = df.loc[df['Milik'] == username, 'Harga'].tolist()
        jumlah = sum(df)

        member = pd.read_csv("Member.csv")
        if username in member["Nama"].values:
            harga = f"\nTotal Harga (Setelah Potongan Untuk Member 5%) : {jumlah - (jumlah * 0.05)}"
        else:
            harga = f"Total Harga : {jumlah}"

        print(harga)
        print("\nApa Yang Ingin Anda Lakukan?")
        print("1. Checkout")
        print("2. Hapus Barang")
        print("0. Kembali")
        pilih = input("Masukkan Pilihan Anda :")

        if pilih == "0":
            menu_customer()
        elif pilih == "1":
            df = pd.read_csv("Keranjang.csv")
            os.system('cls')
            tabel_keranjang() 
            print(harga)
            print("\nPilih Metode Pembayaran (0 Untuk Kembali)")
            print("1. BCA")
            print("2. BRI")
            print("3. Gopay")
            bayar = input("Masukkan Pilihan Anda :")

            if bayar != "0":
                df_log = pd.read_csv("Log_Pembelian.csv")
                dfpindah = pd.read_csv("Keranjang.csv")
                dfpindah = dfpindah[dfpindah["Milik"] == username]
                barangid = dfpindah["id"].values
                waktu = datetime.now()
                dfpindah["Waktu Pemesanan"] = waktu
                dfpindah["Waktu ACC"] = "Belum di ACC"
                dfpindah["Harga"] = dfpindah["Harga"] * (1 - 0.05)  
                dfpindah = dfpindah.rename(columns={"Milik": "Pemesan"})

                df_log_cleaned = df_log.dropna(axis=1, how='all')
                dfpindah_cleaned = dfpindah.dropna(axis=1, how='all')
                
                df_combined = pd.concat([df_log_cleaned, dfpindah_cleaned], ignore_index=True)
                df_combined.to_csv("Log_Pembelian.csv", index=False)

                dfhapus = pd.read_csv("Keranjang.csv")
                dfhapus = dfhapus[dfhapus["Milik"] != username]
                dfhapus.to_csv("Keranjang.csv", index=False)
                
                admin = pd.read_csv("Barang.csv")
                listadmin = []
                for i in barangid:
                    admin_milik = admin.loc[admin["id"] == i, "Milik"].values[0]
                    if admin_milik not in listadmin:
                        listadmin.append(admin_milik)

                nomoradmin = pd.read_csv("Data_User.csv")
                listnomor = []
                for i in listadmin:
                    nomor = nomoradmin.loc[nomoradmin["Nama"] == i, "Nomor"].values[0]
                    listnomor.append(nomor)
                    
                for i in listnomor:
                    pesan = "Halo Admin, Saya Telah Melakukan Checkout, Silahkan Untuk di ACC"
                    pesan = pesan.replace(" ", "%20").replace(",", "%2C").replace(":", "%3A").replace("/", "%2F")
                    link = f"https://wa.me/+62{i}?text={pesan}"
                    print(link)

                input("Pembayaran Berhasil, Enter Untuk Melanjutkan")
        elif pilih=="2" :
            while True :
                tabel_keranjang()
                df=pd.read_csv("Keranjang.csv")
                try :
                    idbarang=int(input("\nMasukkan ID barang :"))
                except ValueError :
                    print("Inputan Harus Berupa Angka!")
                    input("Tekan Enter Untuk melanjutkan")
                    continue
                if idbarang in df["id"].values :
                    while True:
                        try :
                            jumlahhapus=int(input("Masukkan Jumlah yang ingin dihapus :"))
                            break
                        except ValueError :
                            print("Inputan Harus Berupa Angka!")
                            input("Tekan Enter Untuk melanjutkan")
                            continue
                    jumlahawal=(df.loc[df["id"]==idbarang, "Jumlah"].values[0])
                    df.loc[df["id"]==idbarang, "Jumlah"] -= jumlahhapus
                    if (df.loc[df["id"]==idbarang, "Jumlah"].values[0]) == 0 :
                        df=df[df["id"] != idbarang]
                        df.to_csv("Keranjang.csv", index=False)
                        input("Hapus selesai Tekan Enter Untuk Kembali")
                        keranjang()
                    else :
                        harga_awal=df.loc[df["id"]==idbarang, "Harga"].values[0]
                        hargaunit= harga_awal/jumlahawal
                        hargaupdate= (jumlahawal-jumlahhapus)*hargaunit
                        df.loc[df["id"]==idbarang, "Harga"] = hargaupdate
                        df.to_csv("Keranjang.csv", index=False)
                        input("Hapus selesai Tekan Enter Untuk Kembali")
                        keranjang()
                else :
                    input("\nBarang Tidak ada, Enter Untuk Melanjutkan")
        else :
            input("Inputan Tidak Valid Enter Untuk Melanjutkan")
            os.system("cls")
            keranjang()
                           
def status_member():
    while True :
        os.system("cls") 
        username=users()
        with open("Member.csv","r") as file :
            dfmember=pd.read_csv("Member.csv")
        if username in dfmember["Nama"].values:
            print("Anda Sudah Termasuk Member")
            user_data = dfmember[dfmember["Nama"] == username]
            print(tabulate(user_data, headers="keys", showindex=False))
            input("Tekan Enter Untuk Melanjutkan")
            return
        else :
            print("Anda Belum Terdaftar Member!")
            print("1.Beli Member")
            print("0.Kembali ")
            pilih=input("Masukkan Pilihan Anda :")
            if pilih=="1" :
                beli= datetime.now()
                kadaluarsa= beli+ timedelta(days=30)
                beli=beli.strftime("%Y-%m-%d %H:%M:%S")
                kadaluarsa=kadaluarsa.strftime("%Y-%m-%d %H:%M:%S")
                kontenmember={"Nama" : username,
                        "Tanggal Beli" : beli,
                        "Kadaluarsa" : kadaluarsa
                        }
                dfmember = pd.concat([dfmember,pd.DataFrame([kontenmember])], ignore_index=False)
                dfmember.to_csv("Member.csv",index=False)
                input("Anda Sudah Menjadi Member")
            if pilih=="0" :
                return

def log_customer() :
    os.system("cls")
    username=users()
    logmember=pd.read_csv("Log_Pembelian.csv")
    logmember=logmember[logmember["Pemesan"]==username]
    logmember=logmember.drop(columns=["Pemesan"])
    print(tabulate(logmember,headers="keys",showindex=False))
    input("Enter Untuk Kembali")
    return
       
def barang_customer():
    os.system("cls")
    with open("Barang.csv","r") as file :
        isifile=pd.read_csv(file)
        isifile=isifile.drop(columns=["Milik"])
    panjang=len(isifile["id"].values)
    kurang=5-(panjang%5)
    indextampilawal=[]
    indextampilakhir=[]
    for i in range (0,panjang,5) :
        if panjang%5!=0 :
            if i==(panjang-(panjang%5)) :
                a=i
                b=i+(5-kurang)
                indextampilawal.append(a)
                indextampilakhir.append(b)
            else :
                a=i
                b=i+5
                indextampilawal.append(a)
                indextampilakhir.append(b)
        else :
            a=i
            b=i+5
            indextampilawal.append(a)
            indextampilakhir.append(b)
    inow=0 
    while True :
        print(tabulate(isifile.iloc[indextampilawal[inow]:indextampilakhir[inow]],headers="keys",showindex=False))
        print("\n1.Next")
        print("2.Back")
        print("3.Beli")
        print("4.Cari Barang")
        print("0.Exit Menu")
        pilih=input("Masukkan Pilihan Anda :")
        if pilih == "1" :
            if inow<len(indextampilawal)-1 :
                os.system("cls")
                inow+=1
                continue
            else :
                os.system("cls")
                print("List Sudah Mencapai Page Terakhir\n")
                continue
        elif pilih == "2" :
            if inow>0 :
                os.system("cls")
                inow-=1
                continue
            else :
                os.system("cls")
                print("List Sudah Berada pada posisi awal\n")
                continue
        elif pilih == "0" :
            menu_customer()
        elif pilih =="3":
            while True :
                os.system("cls")
                print(tabulate(isifile.iloc[indextampilawal[inow]:indextampilakhir[inow]],headers="keys",showindex=False))
                try :
                    kodebarang=int(input("Masukkan Kode Barang Yang ingin dibeli (0 untuk kembali)"))
                    if kodebarang==0 :
                        os.system("cls")
                        break
                    with open("Barang.csv","r") as file :
                        df=pd.read_csv(file)
                    if kodebarang in isifile["id"].values :
                        index_baris = df.index[df["id"] == kodebarang].values[0]
                        barang = df.iloc[index_baris,1]
                        harga= df.iloc[index_baris,2]
                        milik=users()
                        stock=df.iloc[index_baris,3]
                        print(f"Anda Ingin Membeli {barang}?")
                        try :
                            jumlah=int(input("Masukkan Jumlah Barang Yang Akan Dibeli (0 untuk kembali): "))
                            if jumlah==0:
                                continue
                            elif jumlah>stock :
                                print("Stock Tidak Memenuhi!")
                                enter=input("Tekan Enter Untuk Melanjutkan")
                            else :
                                with open("Keranjang.csv","r") as file :
                                    df_barang=pd.read_csv(file)
                                    konten={"id" : kodebarang,
                                            "Nama Barang" : barang,
                                            "Jumlah" : jumlah,
                                            "Harga" : harga*jumlah,
                                            "Milik" : milik
                                            }
                                    df_barang = pd.concat([df_barang,pd.DataFrame([konten])], ignore_index=False)
                                    df_barang.to_csv("Keranjang.csv",index=False)
                                    enter=input("Barang Telah dimasukkan Ke keranjang, Enter Untuk Melanjutkan")
                                    barang_customer()
                        except ValueError :
                            print("Input Harus Berupa Angka")
                            enter=input("Tekan Enter Untuk Melanjutkan")
                except ValueError:
                    print("Inputan Tidak Valid")
                    enter=input("Tekan Enter Untuk Melanjutkan")
        elif pilih=="4":
            while True:
                os.system("cls")
                print("\n=== PENCARIAN BARANG ===")
                caribarang=pd.read_csv("Barang.csv")
                kunci =input("Masukkan kata kunci pencarian (0 untuk keluar): ").strip()
                if kunci == "0":
                    os.system("cls")
                    break
                elif kunci != "0" :
                    hasil = caribarang[caribarang["Nama Barang"].str.contains(kunci, case=False)]
                    hasil=hasil.drop(columns=["Milik"])
                    if hasil.empty :
                        input("Barang yang anda cari tidak ada, Enter untuk melanjutkan")
                        continue
                    print("\nHasil Pencarian:")
                    print(tabulate(hasil,headers="keys",showindex=False))
                    try :
                        kodebarang=int(input("Masukkan Kode Barang Yang ingin dibeli (0 untuk kembali)"))
                        with open("Barang.csv","r") as file :
                            df=pd.read_csv(file)
                        if kodebarang in isifile["id"].values :
                            index_baris = df.index[df["id"] == kodebarang].values[0]
                            barang = df.iloc[index_baris,1]
                            harga= df.iloc[index_baris,2]
                            milik=users()
                            stock=df.iloc[index_baris,3]
                            print(f"Anda Ingin Membeli {barang}?")
                            try :
                                jumlah=int(input("Masukkan Jumlah Barang Yang Akan Dibeli (0 untuk kembali): "))
                                if jumlah==0:
                                    break
                                elif jumlah>stock :
                                    print("Stock Tidak Memenuhi!")
                                    enter=input("Tekan Enter Untuk Melanjutkan")
                                else :
                                    with open("Keranjang.csv","r") as file :
                                        df_barang=pd.read_csv(file)
                                        konten={"id" : kodebarang,
                                                "Nama Barang" : barang,
                                                "Jumlah" : jumlah,
                                                "Harga" : harga*jumlah,
                                                "Milik" : milik
                                                }
                                        df_barang = pd.concat([df_barang,pd.DataFrame([konten])], ignore_index=False)
                                        df_barang.to_csv("Keranjang.csv",index=False)
                                        enter=input("Barang Telah dimasukkan Ke keranjang, Enter Untuk Melanjutkan")
                                        barang_customer()
                            except ValueError :
                                print("Input Harus Berupa Angka")
                                enter=input("Tekan Enter Untuk Melanjutkan")
                    except ValueError:
                        print("Inputan Tidak Valid")
                        enter=input("Tekan Enter Untuk Melanjutkan")
                    
                    
        else :
            os.system("cls")
            print("Harap Masukkan Inputan Yang Valid\n")
 
awal_login()
