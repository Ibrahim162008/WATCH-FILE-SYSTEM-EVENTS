from multiprocessing import Event
import sys
import time
import random
import os
import shutil
from typing_extensions import Self 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler;

from_dir = "C:/Users/ibrah/Desktop"

class FileEventHandler(FileSystemEventHandler):

 def on_created(self, event):
    print(f"hey, {event.src_path} has been created!")

 def on_deleted(self, event):
    print(f"Oops! Someone deleted {event.src_path}!")

 def on_modified(self, event):
    print(f"Hey there! {event.src_path} has been modified")

 def on_moved(self, event):
    print(f"Hello! {event.src_path} has been moved to a different file")

# Initialize Event Handler class
event_handler = FileEventHandler()

# Initialize observer
observer = Observer()

# Scheldule the observer
observer.schedule(event_handler, from_dir, recursive = True)

# start the observer
observer.start()


try:
   while True:
      time.sleep(2)
      print("running...")
except KeyboardInterrupt:
   print("Stopped!")
   observer.stop()
