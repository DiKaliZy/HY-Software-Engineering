import Client
import InitializeManager


def main():
    initial = InitializeManager.InitializeManager("Professor List.txt")
    client = Client.Client(initial)

if __name__ == '__main__':
    main()