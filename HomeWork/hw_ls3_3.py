playlist = [1, 2, 3, 4, 5, 6]
print("List", playlist)
p100 = playlist[: len(playlist)//2]
p200 = playlist[len(playlist)//2:]
print("Result_1:", [p100, p200])
p300 = p100[:len(p100)//2+1]
p400= p100[len(p100)//2+1:]
print("Result_2:", [p300, p400])
p500 = playlist.pop()
p500 = playlist[:3], playlist[3:5]
print("Result_3:", p500)
lst = []
p600 = [playlist[:1], lst]
print("Result_4:", p600)
p700 = [lst]*2
print("Result_5:", p700)
