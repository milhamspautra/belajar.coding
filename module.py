def luasSegitiga(a,t):
    tinggi = t 
    alas = a
    luas = 0.5*alas*tinggi
    print(luas)

def voltaseTeganganListrik(I,R):
    kuat_arus = I
    hambatan = R
    TeganganListrik = I*R
    print(TeganganListrik)

def voltaseKuatArusListrik(V,R):
    tegangan = V
    hambatan = R
    KuatArusListrik = V/R
    print(KuatArusListrik)

def voltaseHambatanListrik(V,I):
    tegangan = V
    kuat_arus = I
    HambatanListrik = V/I
    print(HambatanListrik)

def MassaJenis(m,v):
    massa_benda = m
    volume_benda = v
    MassaJenis = m/v
    print(MassaJenis)

def energiPotensialGravitasi(m,g,h):
    massa_benda = m
    gravitasi_bumi = g
    ketinggian_benda = h
    PotensialGravitasi = m*g*h
    print(PotensialGravitasi)

def energiKinetik(m,v):
    massa = m
    kecepatan = v 
    energiKinetik = 0,5*m*v**2
    print(energiKinetik)
