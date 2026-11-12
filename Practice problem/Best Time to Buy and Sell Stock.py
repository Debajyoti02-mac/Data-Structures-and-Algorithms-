prices = [7, 6, 5, 10, 1]
min_index = 0 
max_price = float('-inf')
min_price = float('inf')
for i in range(len(prices)):
    if max_price < prices[i] :
        max_price = prices[i]
        min_index = i 
        
for i in range(len(prices)-min_index+1):
    if min_price > prices[i]:
        min_price = prices[i]
    
print(f'what is the min price : {max_price}')
print(f'what is the max price : {min_price}')
print(f'what is the count in the first : {min_index}')
        