import QiitaAPI

def main():

    followers = QiitaAPI.get_followers("drken")
    for follower in followers:
        print(f"id: {follower.get_id()}, github: {follower.get_github_url()}")




if __name__ == '__main__':
    main()
