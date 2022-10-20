import sys

bearer_token = "AAAAAAAAAAAAAAAAAAAAAIme1wAAAAAAWgWnQO%2B0h7g1gjFEJTnBHdozn80%3Dc4l7FjjSBq6k1eofIUHBuwGuMOrq14MnZZB2PDGr1LnzmMtsoo"

# Query (Example: '(from:twitterdev -is:retweet) OR #twitterdev')
query = ('(from:twitterdev -is:retweet) suicídio OR suicida OR se matou OR se suicidou OR matou ela mesma OR se enforcou OR acabar com a própria vida OR' +
        'tirar a própria vida OR acabar com a própria vida dela OR acabar com a própria vida dele OR acabou com a própria vida OR tirou a própria vida')

start_time = sys.argv[1:2]
end_time = sys.argv[2:3]

max_results = 500