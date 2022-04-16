#-*-coding:utf-8-*-
# nanti aku taro link filenya di komentar
import base64, zlib, marshal, sys, os, time
from getpass import getpass

# warna
a,m,h,k,b,u,c,p,bn,o = [
'\033[90m',
'\033[31m',
'\033[32m',
'\033[33m',
'\033[94m',
'\033[35m',
'\033[36m',
'\033[37m',
'\033[41m',
'\033[0m'
]


def Aldi(teks):
 for i in teks + "\n":
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(00.01)
   

def logo():
    print(p)
    os.system("toilet -f wideterm -F border '          Encrypt Python         '")
#Tampilan
def baner():
    Aldi(k+"  _______     ________ _   _  _______     _______ _______ ")
    Aldi(" |  __ \ \   / /  ____| \ | |/ ____\ \   / /  __ \__   __|")
    Aldi(" | |__) \ \_/ /| |__  |  \| | |     \ \_/ /| |__) | | |   ")
    Aldi(" |  ___/ \   / |  __| | . ` | |      \   / |  ___/  | |   ")
    Aldi(" | |      | |  | |____| |\  | |____   | |  | |      | |   ")
    Aldi(" |_|      |_|  |______|_| \_|\_____|  |_|  |_|      |_|  "+m+"- "+p+"By MR.1557 ")
    print
    Aldi(u+"["+m+"•"+u+"]"+p+" Menu "+m+": ")
    Aldi(u+"["+m+"•"+u+"]"+p+" Setop klik CTRL + Z ")
    print
    Aldi(u+"  ["+p+"01"+u+"]"+p+" endcrypt file with base64              "+m+"("+h+"on"+m+")")
    Aldi(u+"  ["+p+"02"+u+"]"+p+" endcrypt file with base16              "+m+"("+h+"on"+m+")")
    Aldi(u+"  ["+p+"03"+u+"]"+p+" endcrypt file with base32              "+m+"("+h+"on"+m+")")
    Aldi(u+"  ["+p+"04"+u+"]"+p+" endcrypt file with marshal             "+m+"("+h+"on"+m+")")
    Aldi(u+"  ["+p+"05"+u+"]"+p+" endcrypt file with zlib&base64         "+m+"("+h+"on"+m+")")
    Aldi(u+"  ["+p+"06"+u+"]"+p+" endcrypt file with zlib&base64&marshal "+m+"("+h+"on"+m+")")
    Aldi(u+"  ["+p+"07"+u+"]"+p+" endcrypt file with zlib&base16&marshal "+m+"("+h+"on"+m+")")
    Aldi(u+"  ["+p+"08"+u+"]"+p+" endcrypt file with zlib&base32&marshal "+m+"("+h+"on"+m+")")
    Aldi(u+"  ["+p+"09"+u+"]"+p+" exit                                   "+m+"("+h+"on"+m+")")
    print(u+"  ["+p+"10"+u+"]"+p+" Yt Creator                             "+m+"("+h+"on"+m+")")
    print
def main():
    os.system("clear")
    a,m,h,k,b,u,c,p,bn,o = [
    '\033[90m',
    '\033[31m',
    '\033[32m',
    '\033[33m',
    '\033[94m',
    '\033[35m',
    '\033[36m',
    '\033[37m',
    '\033[41m',
    '\033[0m'
    ]
    baner()
    choice = raw_input(u+'[•'+p+'•'+u+'] '+p+'choose'+m+' > '+h)
    
    if choice == '1' or choice == '01':
        try:
            logo()
            file = raw_input(u+'['+p+'+'+u+']'+p+' File '+m+': '+h)
            fileopen = open(file).read()
            a = base64.b64encode(fileopen)
            b = "#Encypt BY MR.1557\n#Makasih 100 subscribe\nimport base64\nexec(base64.b64decode('" + a + "'))"
            c = file.replace('.py', '_enc.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            Aldi(u+'['+h+'✓'+u+']'+p+' OUTPUT'+m+' > '+bn+p+c+o+' '+m+'< ')
            time.sleep(3)
            main()
        except:
            Aldi(u+'['+m+'X'+u+'] '+p+'File not found!')
	    time.sleep(3)
            main()

    if choice == '2' or choice == '02':
        try:
            logo()
            file = raw_input(u+'['+p+'+'+u+']'+p+' File '+m+': '+h)
            fileopen = open(file).read()
            a = base64.b16encode(fileopen)
            b = "#Encypt BY MR.1557\n#Makasih 100 subscribe\nimport base64\nexec(base64.b16decode('" + a + "'))"
            c = file.replace('.py', '_enc.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            Aldi(u+'['+h+'✓'+u+']'+p+' OUTPUT'+m+' > '+bn+p+c+o+' '+m+'< ')
            time.sleep(3)
            main()
        except:
            Aldi(u+'['+m+'X'+u+'] '+p+'File not found!')
            time.sleep(3)
            main()

    if choice == '3' or choice == '03':
        try:
            logo()
            file = raw_input(u+'['+p+'+'+u+']'+p+' File '+m+': '+h)
            fileopen = open(file).read()
            a = base64.b32encode(fileopen)
            b = "#Encypt BY MR.1557\n#Makasih 100 subscribe\nimport base64\nexec(base64.b32decode('" + a + "'))"
            c = file.replace('.py', '_enc.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            Aldi(u+'['+h+'✓'+u+']'+p+' OUTPUT'+m+' > '+bn+p+c+o+' '+m+'< ')
            time.sleep(3)
            main()
        except:
            Aldi(u+'['+m+'X'+u+'] '+p+'File not found!')
            time.sleep(3)
            main()

    if choice == '4' or choice == '04':
        try:
            logo()
            file = raw_input(u+'['+p+'+'+u+']'+p+' File '+m+': '+h)
            fileopen = open(file).read()
            a = compile(fileopen, 'dg', 'exec')
            m = marshal.dumps(a)
            s = repr(m)
            b = '#Encypt BY MR.1557\n#Makasih 100 subscribe\nimport marshal\nexec(marshal.loads(' + s + '))'
            c = file.replace('.py', '_enc.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            Aldi(u+'['+h+'✓'+u+']'+p+' OUTPUT'+m+' > '+bn+p+c+o+' '+m+'< ')
            time.sleep(3)
            main()
        except:
            Aldi(u+'['+m+'X'+u+'] '+p+'File not found!')
            time.sleep(3)
            main()

    if choice == '5' or choice == '05':
        try:
            logo()
            file = raw_input(u+'['+p+'+'+u+']'+p+' File '+m+': '+h)
            fileopen = open(file).read()
            c = zlib.compress(fileopen)
            d = base64.b64encode(c)
            e = '#Encypt BY MR.1557\n#Makasih 100 subscribe\nimport marshal,zlib,base64\nexec(zlib.decompress(base64.b64decode("' + d + '")))'
            f = file.replace('.py', '_enc.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            Aldi(u+'['+h+'✓'+u+']'+p+' OUTPUT'+m+' > '+bn+p+f+o+' '+m+'< ')
            time.sleep(3)
            main()
        except:
            Aldi(u+'['+m+'X'+u+'] '+p+'File not found!')
            time.sleep(3)
            main()

    if choice == '6' or choice == '06':
        try:
            logo()
            file = raw_input(u+'['+p+'+'+u+']'+p+' File '+m+': '+h)
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b64encode(c)
            e = '#Encypt BY MR.1557\n#Makasih 100 subscribe\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + str(d) + '"))))'
            f = file.replace('.py', '_enc.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            Aldi(u+'['+h+'✓'+u+']'+p+' OUTPUT'+m+' > '+bn+p+f+o+' '+m+'< ')
            time.sleep(3)
            main()
        except:
            Aldi(u+'['+m+'X'+u+'] '+p+'File not found!')
            time.sleep(3)
            main()

    if choice == '7' or choice == '07':
        try:
            logo()
            file = raw_input(u+'['+p+'+'+u+']'+p+' File '+m+': '+h)
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b16encode(c)
            e = '#Encypt BY MR.1557\n#Makasih 100 subscribe\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode("' + str(d) + '"))))'
            f = file.replace('.py', '_enc.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            Aldi(u+'['+h+'✓'+u+']'+p+' OUTPUT'+m+' > '+bn+p+f+o+' '+m+'< ')
            time.sleep(3)
            main()
        except:
            Aldi(u+'['+m+'X'+u+'] '+p+'File not found!')
            time.sleep(3)
            main()

    if choice == '8' or choice == '08':
        try:
            logo()
            file = raw_input(u+'['+p+'+'+u+']'+p+' File '+m+': '+h)
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b32encode(c)
            e = '#Encypt BY MR.1557\n#Makasih 100 subscribe\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode("' + str(d) + '"))))'
            f = file.replace('.py', '_enc.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            Aldi(u+'['+h+'✓'+u+']'+p+' OUTPUT'+m+' > '+bn+p+f+o+' '+m+'< ')
            time.sleep(3)
            main()
        except:
            Aldi(u+'['+m+'X'+u+'] '+p+'File not found!')
            time.sleep(3)
            main()

    if choice == '9' or choice == '09':
        Aldi(u+'['+m+'!'+u+'] '+p+'Bayy kon!!')
        sys.exit()
    else:
       if choice == '10':
           print(p)
           os.system("toilet -f wideterm -F border '      Open YT     '")
           time.sleep(2)
           os.system('xdg-open https://youtube.com/channel/UC7ygjAbDjuiN76PqOlJm40A') #link yt di ubah ajh
           time.sleep(3)
           main()
       else:
           Aldi(u+'['+m+'X'+u+']'+p+' Mata luh buta !!')
           time.sleep(2)
           main()


if __name__ == '__main__':
   def al(teks):
      for i in teks + "\n":

         sys.stdout.write(i)
         sys.stdout.flush()
         time.sleep(0.1)
   a,m,h,k,b,u,c,p,bn,o = [
  '\033[90m',
  '\033[31m',
  '\033[32m',
  '\033[33m',
  '\033[94m',
  '\033[35m',
  '\033[36m',
  '\033[37m',
  '\033[41m',
  '\033[0m'
  ]
   os.system("clear")
   print(h)
   os.system("toilet -f wideterm -F border '            Login Key           '")
   print
   e = getpass(u+'['+p+'!'+u+']'+p+' Key'+m+' : ')
   if e=="halo": #key bisa klian ubah 
      print
      al(u+'['+h+'√'+u+'] '+p+'LOGIN SUCCESS ...')
      time.sleep(1)
      main()
   else:
       print
       al(u+"["+m+"!"+u+"]"+p+" LOGIN FAILED")
       time.sleep(1)
       os.system('python2 Aldi-ganteng.py')
