def reverseStr(text):
	strLength = len(text)
	newStr=''
	index =0
	while (strLength > 0):
		letter = text[strLength - 1]
		newStr= newStr + letter
		strLength = strLength - 1
		index = index + 1
	return newStr