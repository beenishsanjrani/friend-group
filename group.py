"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    'Jill' : {
        'Relations': {
            'Zalika' : 'friend',
            'John' : 'partner'
        },
        'Age' : '26',
        'Job' : 'Biologist'
    },
    'Zalika' : {
        'Relations': {
            'Jill' : 'friend'
        },
        'Age' : '28',
        'Job' : 'Artist'
    },
    'John' : {
        'Relations': {
            'Jill' : 'partner'
        },
        'Age' : '27',
        'Job' : 'Writer'
    },
    'Nash' : {
        'Relations': {
            'Zalika' : 'Landlord',
            'John' : 'Cousin'
        },
        'Age' : '34',
        'Job' : 'Chef'
    }
}

Jill = group.get('Jill')
Zalika = group.get('Zalika')
John = group.get('John')
Nash = group.get('Nash')
