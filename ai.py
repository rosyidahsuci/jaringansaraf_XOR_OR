import random 
 
# Persiapan Data 
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)] 
targets = [0, 1, 1, 1] 
learning_rate = 0.1 
weight = [] 
 
# Inisialisasi Weight(weight[0] merupakan bias) 
for i in range(3):  
    weight.append(round(random.uniform(-1.0,1.0), 1)) 
 
## Training 
train = True 
while(train) :  
    for test_input, target in zip(test_inputs, targets):   
        linear_combination = weight[0] + weight[1] * test_input[0] + weight[2] * test_input[1]   
        output = int(linear_combination >= 0)   
        error = target - output   
        if (error != 0):    
            weight[0] += learning_rate * error     
            weight[1] += learning_rate * test_input[0] * error     
            weight[2] += learning_rate * test_input[1] * error     
            break  
        else :   
            train = False

### Testing 
x1 = int(input('X1 : ')) 
x2 = int(input('X2 : ')) 
 
result = weight[0] + x1 * weight[1] + x2 * weight[2] 
 
print('{} OR {} : {}'.format(x1, x2, int(result >= 0))) 
 
  