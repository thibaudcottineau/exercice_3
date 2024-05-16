class FizzBuzz:
    
    def __init__(self, nbr_min, nbr_max):
        self.nbr_min = nbr_min
        self.nbr_max = nbr_max
        
    # fonction pour creer une list de nombre
    def creat_list_numbers_basic(self):
        return list(range(self.nbr_min, self.nbr_max))
      
    # fonction pour remplacer les chiffres d'une classe x  par un mot x
    def add_word(self, list_numbers, number_x, word_x):
        new_list = list_numbers
        a = self.nbr_min
        b = 0
        
        for number in list_numbers:
            if a %  number_x == 0:
                new_list[b] = word_x
            a += 1
            b += 1
                
        return new_list
    
    # fonction pour remplacer les chiffres d'une classe x et y par fizzBuzz
    def add_fizzBuzz(self, list_numbers, number_x, number_y, word_x):
        new_list = list_numbers
        a = self.nbr_min
        b = 0
        
        for number in list_numbers:
            if a %  number_x == 0 and a %  number_y == 0:
                new_list[b] = word_x
            a += 1
            b += 1
        return new_list
    
    # fonction pour remplacer les chiffres d'une classe x et y par fizzBuzz
    def add_fizzBuzz_fizz_buzz(self):
        new_list = self.creat_list_numbers_basic()
        new_list = self.add_word(new_list, 3, "fizz")
        new_list = self.add_word(new_list, 5, "buzz")
        new_list = self.add_fizzBuzz(new_list, 3, 5, "fizzBuzz")
                
        return new_list

    # fonction rajout un mot au chiffre avec un nombre_x
    def add_trass(self, list_numbers, number_x, word_x):
        new_list = list_numbers
        a = self.nbr_min
        b = 0
        
        for number in list_numbers:
            if str(number_x) in str(a):
                if isinstance(list_numbers[b], int):
                    list_numbers[b] = word_x 
                else:
                    list_numbers[b] = str(list_numbers[b]) + word_x 
  
            a += 1
            b += 1
                
        return new_list
    
    # fonction total
    def add_total(self):
        new_list = self.creat_list_numbers_basic()
        new_list = self.add_word(new_list, 3, "fizz")
        new_list = self.add_word(new_list, 5, "buzz")
        new_list = self.add_fizzBuzz(new_list, 3, 5, "fizzBuzz")
        new_list = self.add_trass(new_list, 3, 'trass')
        new_list = self.add_trass(new_list, 5, "bross")
        
                
        return new_list