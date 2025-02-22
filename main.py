import random

def updateFile(text:str):
    with open("pass.txt", "+a") as file:
        file.write(text+"\n")


def passGenerator(n:int):
    words = [
    "SolarFlare", 
    "BlueWhale", 
    "EchoMountain", 
    "CrystalBreeze", 
    "Skyline32", 
    "ShadowFire", 
    "LunarPine", 
    "GoldenMaple", 
    "ThunderBolt", 
    "MysticRain", 
    "CleverLion", 
    "FrozenPeak", 
    "DreamCatcher", 
    "OceanWave82", 
    "SecretSunrise"
    ]
    num = [
    837264, 
    192384, 
    459701, 
    384920, 
    102938, 
    675849, 
    283746, 
    948572, 
    563018, 
    283910, 
    746281, 
    520638, 
    915724, 
    483920, 
    378601
    ]
    sym = ['@', '#', '$', '%', '&', '*', '_', '+', '=', '|', ':', ';', ',', '.', '?']

    # for i in range(1, n + 1):
    rWords = random.choice(words)
    rSymbols = random.choice(sym)
    rNum = random.choice(num)
    password = f"{rWords}{rSymbols}{rNum}"
    return password

if __name__ == "__main__":
    # w = "hello i am ready to write"
    # updateFile(w)
    a = passGenerator(8)
    print(a)