
import os
import re

# assumes student submissions are unzipped, in a dir called submissions
#
# matches a file to a student and their section
# places that file into a dir by section
# reformats filename

def main():

    for sect in sections:
        if not os.path.isdir("submissions/"+sect):
            os.mkdir("submissions/"+sect)

    submissions = os.listdir('submissions')

    #iterate through all students
    for line in students:
        reverse_name = line[1].lower() + line[0].lower()
        section = line[2]

        #search for this students file
        for filename in submissions:
            #print(filename + " | " + reverse_name)
            if reverse_name in filename:
                try:
                    os.rename("submissions/"+filename, "submissions/"+section+"/"+format_filename(filename))
                except OSError as e:
                    print(str(line[0:-1])+": could not find this student's submission")


def format_filename(filename):
    filename = filename.replace(" ", "") # whitespace
    filename = re.sub("_[0-9]*_[0-9]*_", "_", filename) #numbers between student-name and filename
    #filename = filename.replace("___", "_")
    return filename



sections = [
    "20953",
    "20830",
    "20831",
    "20832"
]

students = [
    ["Sarah","Allen","20830"],
    ["Mark","Arends","20832"],
    ["Erich","Atwell","20953"],
    ["Wyatt","Ayers","20953"],
    ["Morgan","Barnes","20953"],
    ["Maggie","Barry","20831"],
    ["Cameron","Bayer","20831"],
    ["Sophia","Bird","20832"],
    ["Devin","Bishop","20832"],
    ["Ruslan","Bulan","20831"],
    ["Chris","Bullis","20831"],
    ["Ivan","Bullock","20831"],
    ["Eugene","Cabamalan","20831"],
    ["Eddie","Carpiobran","20953"],
    ["Anthony","Chaires","20831"],
    ["Cedric","Couder","20831"],
    ["Sophia","Cressler","20953"],
    ["Nathan","Critchfield","20830"],
    ["Acamaro","Cutcher","20832"],
    ["Dylan","Desy","20830"],
    ["Rohan","Dosanjh","20831"],
    ["Alex","Easter","20953"],
    ["Justin","Enis","20830"],
    ["Cosette","Ensminger","20953"],
    ["Tatum","Epperson","20832"],
    ["Wenjing","Fan","20831"],
    ["Satya","Fawcett","20830"],
    ["Charles","Fritz","20832"],
    ["Emma","Geary","20832"],
    ["Brody","Gill","20831"],
    ["Makayla","Haverluk","20831"],
    ["Grayson","Hayden","20953"],
    ["Alex","Hessler","20830"],
    ["Hank","Hilts","20830"],
    ["Spencer","Hunt","20831"],
    ["Sam","Jeffries","20831"],
    ["Andrew","Johnson","20831"],
    ["Elena","Kargopoltsev","20953"],
    ["Sabine","Kempfe","20832"],
    ["Chandler","Patterson","20832"],
    ["Stuart","Kuehne","20953"],
    ["Jerome","Lajoie","20831"],
    ["Brian","Leach","20831"],
    ["Nick","Leca","20831"],
    ["Cole","Levy","20953"],
    ["Xuanlin","Liu","20953"],
    ["Jonathan","Lopez","20830"],
    ["Wyatt","Lutkus","20832"],
    ["Adeline","Kordich","20953"],
    ["Inti","MacDonald","20953"],
    ["Jacob","McCabe","20831"],
    ["Matthew","McElrath","20953"],
    ["Tynan","McGee","20832"],
    ["Erick","Olmedo","20830"],
    ["Skyler","Morford","20953"],
    ["Connor","Morgan","20831"],
    ["Skylar","Munds","20831"],
    ["Joe","Munizza","20830"],
    ["Sam","Tuesta","20832"],
    ["Quynh","Nguyen","20830"],
    ["Sarah","Nguyen","20830"],
    ["Joseph","Nicholls","20953"],
    ["Cece","Nielsen","20832"],
    ["Kristina","Norris","20953"],
    ["JoAnna","ONeill","20831"],
    ["Di","Pham","20830"],
    ["Amy","Poehner","20953"],
    ["Isaiah","Pouch","20953"],
    ["Wyatt","Prutch","20832"],
    ["Jake","Ramsdell","20953"],
    ["Grant","Rienstra","20832"],
    ["Anish","Rijal","20832"],
    ["Evan","Rodgers","20830"],
    ["Alexander","Rolon","20830"],
    ["Adin","Romano","20830"],
    ["Tyron","Rucker","20832"],
    ["Lucas","Salazar","20830"],
    ["Erik","Sarchi","20831"],
    ["Ezra","Sargent","20832"],
    ["Derrick","Sato","20830"],
    ["Mikey","Scafe","20831"],
    ["Christopher","Schmitt","20830"],
    ["Oliver","Schuman","20832"],
    ["Nicholas","Scott","20832"],
    ["Jack","Sell","20832"],
    ["Joey","Skaran","20953"],
    ["Adrian","Smith","20953"],
    ["John","Sobeck","20832"],
    ["Simon","Solomon","20830"],
    ["Nikita","Sotnikov","20953"],
    ["Hayley","Stephens","20830"],
    ["Eric","Tootill","20953"],
    ["Katie","Tran","20831"],
    ["Aryaa","Trivedi","20831"],
    ["Tomas","Tsega","20830"],
    ["Eben","VanEpps","20830"],
    ["Kyle","Webster","20953"],
    ["Katie","Werner","20832"],
    ["Alec","Whitaker","20832"],
    ["Ana","Wichman","20830"],
    ["Colin","Wilcox","20832"],
    ["Lauren","Wittkopf","20830"],
    ["Nathan","Wong","20832"],
    ["Drew","Ybarra","20830"]
]

main()
