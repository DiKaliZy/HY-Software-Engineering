import Client
import InitializeManager


def main():
    initial = InitializeManager("Professor List.txt")
    client = Client(initial)

if __name__ == '__main__':
    main()