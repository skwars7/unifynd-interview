class Utils:
    @staticmethod
    def get_list_input(ns:int) -> list:
        """
            use to get multiple input based on given int value
        """
        results = []
        for n in range(ns):
            results.append(str(input('Name - ')))
        return results

    @staticmethod
    def get_input(message:str,which_type:str) -> int or str:
        """
            use to get input supports int and str values only
        """
        while True:
            try:
                return eval(f'{which_type}(input(f"Enter the {message} - "))')
            except ValueError as expectederror:
                print(f'Please enter only {which_type} value \n')
            except Exception as unexpectederror:
                print('Please try again something went wrong \n') 
    
    @staticmethod
    def get_preference_dict(l1:list,l2:list,message:list) -> dict:
        """
            l1 for first loop
            l2 for second loop can swap function input to change preference for any list
            message is for displaying Preference message ex 0th value will be the which 
                    we are getting preference for and second will be to select from [Student,company]
        """
        print(f'\n Preference for {message[0]} : \n')
        results = {message[0]:[],message[1]:[]}
        for ind,i in enumerate(l1):
            for ind2, j in enumerate(l2):
                print(f'{ind2}) {j}')
            while True:
                try:
                    selected_value = Utils.get_input(f'Pfefferd {message[1]} number for {i}','int')
                    l2[selected_value]
                    break
                except IndexError as expectederror:
                    print('\n please enter number written before list \n')

            results[message[0]].append(i)
            results[message[1]].append(l2[selected_value])
            print(f'{i} preffered {l2[selected_value]} \n') 
        return results