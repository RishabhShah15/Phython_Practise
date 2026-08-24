
IPLTeam=["Gujarat Titan","Rajasthan Royal","CSK","MI","DD","KKR"]



def  GetTeam(tm):
    for i in IPLTeam:
        if(len(i)<6):
            continue
        print(i)
GetTeam(IPLTeam)

