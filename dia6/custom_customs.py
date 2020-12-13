def read_file():
    with open ('input.txt', 'r') as arq:
        return arq.read().split('\n\n')

def part1(groups):
    count = 0 
    for group in groups:
        unique = set(''.join(group.split()))
        count += len(unique)

    return count

def main():
    groups = read_file()
    
    print(part1(groups))  

if __name__ == "__main__":
    main()
    