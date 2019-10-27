
def getCategories(request):

    categories_dict = {
        'basic':'Basics',
        'math':'Mathematics',
        'ds':'Data Structures',
        'greedy':'Greedy Algorithms',
        'dp': 'Dynamic Programming',
        'graph': 'Graph Theory'
    }

    return categories_dict