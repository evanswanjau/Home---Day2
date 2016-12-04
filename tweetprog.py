# Program that uses a public API to send tweets through my twitter account
# Author Evans Wanjau
# Import the necesary modules
import tweepy
# Use the private key to access the API
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['2wQZPeCMgE6bWkz2ICtkCbkED'], cfg['4iaIXFBRBzYq0SPSzw2ZeoTdqSPostgTeWBHMuhQAOdZWeXTlz'])
  auth.set_access_token(cfg['	1500683036-C1nquPDytNrwgmPsi3jarnhaGKSvZDpJrEQhF5M'], cfg['DLBphtABAiYAQr1wmWzOjipK4G7cNsBO6QlUUbSG2AJ9N'])
  return tweepy.API(auth)

def main():
    cfg = {
        "consumer_key"        : "2wQZPeCMgE6bWkz2ICtkCbkED",
        "consumer_secret"     : "4iaIXFBRBzYq0SPSzw2ZeoTdqSPostgTeWBHMuhQAOdZWeXTlz",
        "access_token"        : "1500683036-C1nquPDytNrwgmPsi3jarnhaGKSvZDpJrEQhF5M",
        "access_token_secret" : "DLBphtABAiYAQr1wmWzOjipK4G7cNsBO6QlUUbSG2AJ9N"
    }

  api = get_api(cfg)
  tweet = input("Tweet:\n")
  status = api.update_status(status=tweet)

if __name__ == "__main__":
  main()
