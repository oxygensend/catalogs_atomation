import time
import json
import os
import sys
import re
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class Handler(FileSystemEventHandler):
    """ Making my own file handler couse I want to override
        FileSystemEventHandler on_modified method"""

    def on_modified(self, event):
        
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/' + filename
            isFile =  True #os.path.isfile(src)
            if  isFile and re.match('.*\.png|.*\.jpeg',filename.lower()):
                dst_folder = '/home/szymon/Pictures'
                print('xd')

            elif  isFile and re.match('.*\.pdf|.*\.doc|.*\.docx',filename.lower()):
                dst_folder = '/home/szymon/pdf'

            else:
                continue    

            dst = dst_folder + '/' + filename
            os.rename(src,dst)

folder_to_track = '/home/szymon/Downloads'

event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)

finally:
    observer.stop()
    observer.join()








            