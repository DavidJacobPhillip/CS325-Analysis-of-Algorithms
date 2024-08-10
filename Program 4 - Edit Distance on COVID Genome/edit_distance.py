import sys

def file_contents_letters(file_name):
    """
    Takes a file name as input and returns a string consisting of the file's contents
    with all non-letter characters removed.
    
    Parameters:
        file_name: The name of the file.
    
    Returns:
        A string with the contents of <file_name> but with all non-letter characters removed.
    """

    f = open(file_name, "r")
    file_contents = f.read()
    f.close()
    return "".join([c for c in file_contents if c.isalpha()])
    
def edit_distance(s1, s2):
    """
    Computes the edit distance between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
    
    Returns:
        The edit distance between s1 and s2.
    """

    global arr
    arr = [[0 for x in range(len(s2)+1)] for y in range(len(s1)+1)]
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if(i == 0):
                arr[i][j] = j
            elif(j == 0):
                arr[i][j] = i
            else:
                subCost = arr[i-1][j-1]
                if(s1[i-1] != s2[j-1]):
                    subCost += 1
                arr[i][j] = min(arr[i][j-1]+1, arr[i-1][j] + 1, subCost)

    return arr[len(s1)][len(s2)]
    
def longest_common_subsequence(s1, s2):
    """
    Computes the length of the longest common subsequence between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
    
    Returns:
        The length of the longest common subsequence between s1 and s2.
    """

    global arr
    arr = [[0 for x in range(len(s2)+1)] for y in range(len(s1)+1)]
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if(i == 0 or j == 0):
                arr[i][j] = 0
            elif(s1[i-1] == s2[j-1]):
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
        
    return arr[len(s1)][len(s2)]

def longest_common_subsequence_string(s1, s2):
    """
    Finds the largest common subsequence
    
    Parameters:
        s1: The first string.
        s2: The second string.
    
    Returns:
        The subsequence
    """

    global arr

    length = longest_common_subsequence(s1, s2)
    lcs_string = ""
    i = len(s1)
    j = len(s2)

    while(i > 0 and j > 0):
        if(s1[i-1] == s2[j-1]):
            lcs_string = lcs_string + s1[i-1]
            i = i - 1
            j = j - 1
        elif(arr[i-1][j] > arr[i][j-1]):
            i = i - 1
        else:
            j = j - 1
    lcs_string = lcs_string[::-1]
    
    return (lcs_string)

arr = []                     # initializing a matrix array to hold the values mutations

s1 = file_contents_letters(sys.argv[1])
s2 = file_contents_letters(sys.argv[2])
print(edit_distance(s1, s2), longest_common_subsequence(s1, s2), longest_common_subsequence_string(s1, s2))
