def feet_to_steps(user_steps):
    return int(user_steps/2.5)

if __name__ == '__main__':
    user_feet=float(input())
    your_value=feet_to_steps(user_feet)
    print(your_value)
    
