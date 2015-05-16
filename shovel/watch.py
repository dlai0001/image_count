import time  
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler  
from shovel import task
import os

class SrcWatcher(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def process(self, event):
        
        # the file will be processed there
        print(event.src_path, event.event_type)  # print now only for degug
        os.system("shovel test.unit")

        print("\nWatching for file changes to src files.  Press ^C to exit.\n")

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)    


@task
def watch_src():
    observer = Observer()
    observer.schedule(SrcWatcher(), path="src", recursive=True)
    observer.start()

    print("\nWatching for file changes to src files.  Press ^C to exit.\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


