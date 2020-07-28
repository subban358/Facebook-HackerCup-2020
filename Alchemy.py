from collections import Counter

def isValid(count):
	a, b = 0, 0
	if 'A' in count: a = count['A']
	if 'B' in count: b = count['B']
	
	return abs(a-b) == 1
	
def solve(n, Str):
	StringList = list(Str)
	count = {'A' : 0, 'B' : 0}
	for i in StringList[:3]:
		count[i] += 1
	remaining = []
	left, right = 0, 2
	while right < n:
		if not isValid(count):
			right += 1
			remaining.append(StringList[left])
			left = right-2
			if right < n:
				count[StringList[right]] += 1
			if left < n:
				count[StringList[left]] -= 1
			
		else:
			if count['A'] > count['B']: StringList[left] = 'A'
			else: StringList[left] = 'B'
			count['A'] -= 1
			count['B'] -= 1
			if right+1 < n:
				count[StringList[right+1]] += 1
			if right+2 < n:	
				count[StringList[right+2]] += 1
			right += 2
	str1, str2 = "", "".join(remaining)
	for i, j in count.items():
		str1 += i*j
	newStr = list(str2+str1)
	a, b = newStr.count('A') , newStr.count('B')
	
	return abs(a-b) == 1
			
ans = []
for tc in range(int(input())):
	n = int(input())
	StringList = input()
	if solve(n , StringList):
		ans.append('Y')
	else:
		ans.append('N')
for i in range(len(ans)):
	print("Case #%d: %c" % (i+1, ans[i]) )

