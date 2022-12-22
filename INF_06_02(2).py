


def dfs(root):

    if root < 8:
        dfs(root*2)
        dfs(root*2+1)
        print(root, end=" ")




if __name__=="__main__":
    dfs(1)