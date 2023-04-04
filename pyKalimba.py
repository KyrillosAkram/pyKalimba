def play_note(note_path:str,interspace_time:float,mute:bool)->None:
    from time import sleep
    from gtts import gTTS
    from re import search
    from os import system,path
    from colorama import Back,Fore,Style
    from colorama import init as colorama_init

    """parse note text file to be print tab by tab with time sepation

    Args:
        note_path (str): Path of note text
        interspace_time (float): the separation time amonge tunes
    """
    note:str
    with open(note_path,'r',encoding='utf-8') as f:
        note=f.read().replace('\n',' ')

    note_tabs:list[str]=note.split(' ')
    out_name="audio_note_%s.mp3"%(search(r'(\w+)(?:\.txt)$',note_path))[1]
    if(not mute):
        if (not path.exists(out_name)):
            audio=gTTS(text='\n'.join(note_tabs),lang="en",slow=True,)
            audio.save(out_name)
        system(f".\\{out_name}")
    colorama_init(autoreset=True)
    for tab,index in zip(note_tabs,range(len(note_tabs))):
        print( f"{((Back.WHITE+Fore.BLACK) if index%2==0 else '')}{tab:^10}")
        sleep(interspace_time)

if __name__=="__main__":
    import argparse

    print("""

                  888    d8P           888 d8b               888               
                  888   d8P            888 Y8P               888               
                  888  d8P             888                   888               
88888b.  888  888 888d88K      8888b.  888 888 88888b.d88b.  88888b.   8888b.  
888 "88b 888  888 8888888b        "88b 888 888 888 "888 "88b 888 "88b     "88b 
888  888 888  888 888  Y88b   .d888888 888 888 888  888  888 888  888 .d888888 
888 d88P Y88b 888 888   Y88b  888  888 888 888 888  888  888 888 d88P 888  888 
88888P"   "Y88888 888    Y88b "Y888888 888 888 888  888  888 88888P"  "Y888888 
888           888                                                              
888      Y8b d88P                                                              
888       "Y88P"                                                               

    """)

    parser = argparse.ArgumentParser(description="enter your song note for kalimba playing")

    parser.add_argument('-p','--note_path',type=str,help="Path of note text",required=True)
    parser.add_argument('-t','--interspace_time',type=float,help="the separation time amonge tunes default value is 1.25 second",default=1.25)
    parser.add_argument('-m','--mute',help='disable auto play',action="store_true",default=False)
    parser.add_argument('-i','--install_dependancies',help='passing this flag means that you want to install gtts and colorama',action="store_true",default=False)
    
    args:object=parser.parse_args()
    if(args.install_dependancies):
        import sys
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install','colorama','gtts'])
    play_note(args.note_path,args.interspace_time,args.mute)
    