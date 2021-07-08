import googlemaps


user_Key= #코드
gmaps = googlemaps.Client(key=user_Key)

sch = input("조회 기관명 입력 : ")
ggmap = gmaps.geocode(sch, language='ko')

# print(ggmap)

print(ggmap[-1]['formatted_address'])
print(ggmap[-1]['geometry']['location']['lat'])
print(ggmap[-1]['geometry']['location']['lng'])
