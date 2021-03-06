import time  
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler  
from shovel import task
import os

class SourceWatcher(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def process(self, event):
        
        # the file will be processed there
        print(event.src_path, event.event_type)  # print now only for degug

        os.system("shovel test.path " + os.path.dirname(event.src_path))

        print("\nWatching for file changes to src files.  Press ^C to exit.\n")

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)



@task
def watch_src():
    os.system("shovel test.unit")

    observer = Observer()
    observer.schedule(SourceWatcher(), path="src", recursive=True)
    observer.start()

    print("\nWatching for file changes to src files.  Press ^C to exit.\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


