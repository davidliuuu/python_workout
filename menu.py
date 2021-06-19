def menu(**options):
    def menu_selector(): #閉包函式
        option_string = '/'.join(options)
        while True:
            choice = input(f'選擇項目 ({option_string}): ')
            if choice in options:
                return options[choice]
                break
            print('選項不存在!')
    return menu_selector
