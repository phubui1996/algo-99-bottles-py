def bottle_song():
	number = 10
	idx = number
	while(idx > 1):
		print(f"{idx} bottles of beer on the wall, {idx} bottles of beer.")
		idx -= 1
		print(f"Take one down and pass it around, {idx} bottles of beer on the wall.")

		if idx == 1:
			print(f"{idx} bottle of beer on the wall, {idx} bottle of beer.")
			print(f"Take one down and pass it around, no more bottles of beer on the wall.")
			print(f"Go to the store and buy some more, {number} bottles of beer on the wall.")

bottle_song()