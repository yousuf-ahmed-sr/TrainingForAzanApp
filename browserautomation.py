from selenium import webdriver

# Initial tabs data
tabs = {
    'scratch': 'https://scratch.mit.edu',
    'chatgpt': 'https://chat.openai.com/',
    'youtube': 'https://www.youtube.com',
    'amazon': 'https://www.amazon.com'
}

# Save the initial tabs data to 'tabs.pkl' if it doesn't exist

using = 'chrome'
driver = None

print(f'You are using {using}')

while True:
    print(f'Available tabs: {", ".join(tabs.keys())}. Choose a tab')
    action=input('or type "add"to add a new tab, "del" to delete a new tab, "rename" to rename a tab, or "switch" to switch between chrome and edge: ')

    if driver:
        driver.quit()

    if action in tabs:
        url = tabs[action]
        driver = webdriver.Chrome() if using == 'chrome' else webdriver.Edge()
        driver.get(url)
        input(f'Press Enter to close {action}...')
        driver.quit()
    elif action == 'add':
        new_tab = input('Enter tab name: ')
        new_url = input('Enter URL name: ')
        tabs[new_tab] = new_url
    elif action == 'del':
        if not len(tabs) == 1:
            tab_to_delete = input('Enter the tab name you want to delete: ')
            if tab_to_delete in tabs:
                tabs.pop(tab_to_delete)
            else:
                print(f'{tab_to_delete} does not exist.')
        else:
            print('You cannot delete the last tab.')
    elif action == 'rename':
        old_and_new_tab = input('Enter old tab name and new tab name separated by a space: ')
        old_tab, new_tab = old_and_new_tab.split()
        tabs[new_tab] = tabs.pop(old_tab)
    elif action == 'switch':
        using = 'edge' if using == 'chrome' else 'chrome'
        print(f'You switched to {using}')
    else:
        print(f'{action} is an invalid option. Please try again.')

# Save the tabs data to 'tabs.pkl'
with open('tabs.pkl', 'wb') as file:
    pickle.dump(tabs, file)