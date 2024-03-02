place = input("where do you wanna out your treassure?like A1 B2 C3 A2 A3 B2 B3 C2 C3\n")

line1=[" "," "," "]
line2=[" "," "," "]
line3=[" "," "," "]
map=[line1,line2,line3]
place_lower = place.lower()
abc = ["a","b","c"]
harf=place_lower[0]
kodomharf = abc.index(harf)
print(kodomharf)
adad=[1,2,3]
adadma = int(place[1])
adadkodom = adad.index(adadma)
print(adadkodom)

map[kodomharf][adadkodom] = "x"
print(f"{line1}\n{line2}\n{line3}")