import time

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
    sing()
    dance()

if __name__ == "__main__":
    main()
