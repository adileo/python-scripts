#Find the longest 00001111 substring with #0 left = #1 right or #1 left = #0 right
#Complexity O(n)
string = "01000111100001111110111111000000"
expansions = []
for i in range(0, len(string)):
    if i + 1 < len(string) and string[i] is not string[i+1]:
        expansions.append([i,i+1,1])
print expansions

expanded = []
for expansion in expansions:
    if expansion[0]-1 > 0 and expansion[1]+1 < len(string):
        while string[expansion[0]-1] is string[expansion[0]] and string[expansion[1]+1] is string[expansion[1]]:
            expansion[0] = expansion[0] - 1
            expansion[1] = expansion[1] + 1
            expansion[2] = expansion[2] + 1
    expanded.append(expansion)
print expanded

start = None
end = None
k = None
for subs in expanded:
    if subs[2] > k:
        k = subs[2]
        start = subs[0]
        end = subs[1]
print "Longest substring ("+str(start)+","+str(end)+","+str(k)+"): " + string[start:end+1]
