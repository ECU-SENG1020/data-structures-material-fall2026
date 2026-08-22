
# many problems can be solved by using divide and conquer techniques



def my_recursive_function(num_levels):

    if num_levels == 0:
        print(f'Base Case')
        return
    
    print(f'Start Level {num_levels}')
    
    my_recursive_function(num_levels - 1)
    
    print(f'Level {num_levels} completed')



def main():
    my_recursive_function(3)


if __name__ == "__main__":
    main()