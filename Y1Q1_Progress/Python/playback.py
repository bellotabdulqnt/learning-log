def main():
    a = playback(input("Playback: "))
    print(a)

def playback(rush):
    rush = rush.split()
    rush = "...".join(rush)
    
    return rush

main()