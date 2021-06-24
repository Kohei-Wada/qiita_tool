from QiitaAPI import *
from QiitaUser import *


def main():
    my_id = "program3152019"
    test_id = "fkooo"
    q = QiitaAPI()
    res = q.get_user(my_id)
    print(res.has_github_account())


if __name__ == '__main__':
    main()
