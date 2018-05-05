# output.py

def main():
    lines = open('outfile.txt', 'r').readlines()

    scores = []

    for line in lines:
        line = line.rstrip()
        line_parts = line.split('\t')
        scores.append(line_parts)
        
    sorted_list = sorted(scores, key = lambda x: int(x[1]),reverse=True)
    
    print('Filename\t\t\t\tScore')
    print()
    for item in sorted_list:
        print(item[0], '\t\t\t', item[1])
        
        
if __name__ == "__main__":
  #Run as main program
  main()