#Create a function format_followers 
# that takes a number and returns it in 'K' or 'M' format (e.g., 1500 → '1.5K', 1200000 → '1.2M'),
# then use map() to apply it to a list of follower counts: [950, 1500, 25000, 1200000].

def format_followers(n):
    if n>=1000000:
         return f"{n / 1000000}M"
    if n>=1000:
         return f"{n / 1000}K"
    return str(n)

counts=[950, 1500, 25000, 1200000]

map_follower=list(map(format_followers,counts))
print(map_follower)