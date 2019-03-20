import time
import threading


def sing():
    """唱歌"""
    for i in range(5):
        print("-----唱歌ing-----")
        time.sleep(1)

def dance():
    """跳舞"""
    for i in range(5):
        print("-----跳舞ing-----")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()
