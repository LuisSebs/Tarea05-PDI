import multiprocessing
import time

# Tutorial: https://www.youtube.com/watch?v=vk_s-gDTqkM

class Loading:
    def __init__(self, message="", speed=0.1) -> None:
        self.message = message
        self.speed = speed
        self.process = multiprocessing.Process(
            target = self.spin,
            args=(),
            name="Loading"
        )

    def spin(self):
        spinner = [
            "🌑 ",
            "🌒 ",
            "🌓 ",
            "🌔 ",
            "🌕 ",
            "🌖 ",
            "🌗 ",
            "🌘 "
        ]
        n = 0
        while True:
            print(f"\r{self.message}{spinner[n]}", end="")
            n += 1
            if n >= len(spinner): 
                n = 0
            time.sleep(self.speed)

    def start(self):
        self.process.start()

    def stop(self):
        if not self.process.is_alive():
            print("Warning: Loading is not running.")
        else:
            self.process.terminate()
            print()

# Codigo de ejemplo
if __name__ == '__main__':
    spinner = Loading("Hello...", 0.1)
    spinner.start()
    time.sleep(5)
    spinner.stop()
