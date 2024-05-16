from django.test import TestCase
from django.urls import reverse

from .classe.fizzBuzz import FizzBuzz

 
class test_FizzBuzz(TestCase):
    
    # test creation d'une liste de nombre de 0 a 100
    def test_creat_string_numbers_basic(self):
        obj_fizzbuzz = FizzBuzz(0, 101)
        list_numbers = obj_fizzbuzz.creat_list_numbers_basic()

        for x in range(0, 101):
            self.assertIn(x, list_numbers)
            
    # test de remplacement des numbres de la classe de 3 par fizz
    def test_add_fizz(self):
        obj_fizzbuzz = FizzBuzz(0, 101)
        list_numbers = obj_fizzbuzz.creat_list_numbers_basic()
        list_numbers = obj_fizzbuzz.add_word(list_numbers, 3, "fizz")
        a = 0
        
        for number in list_numbers:
            if a % 3 == 0:
                self.assertEqual(number, "fizz")
            a += 1
            
    # test de remplacement des numbres de la classe de 5 par buzz
    def test_add_buzz(self):
        obj_fizzbuzz = FizzBuzz(0, 101)
        list_numbers = obj_fizzbuzz.creat_list_numbers_basic()
        list_numbers = obj_fizzbuzz.add_word(list_numbers, 5, "buzz")
        a = 0
        
        for number in list_numbers:
            if a % 5 == 0:
                self.assertEqual(number, "buzz")
            a += 1
            
    # test de remplacement des numbres de la classe de 5 et 3 par fizzBuzz
    def test_add_fizzBuzz(self):
        obj_fizzbuzz = FizzBuzz(0, 101)
        list_numbers = obj_fizzbuzz.creat_list_numbers_basic()
        list_numbers = obj_fizzbuzz.add_fizzBuzz(list_numbers, 3, 5, "fizzBuzz")
        a = 0
        
        for number in list_numbers:
            if a % 3 == 0 and a % 5 == 0:
                self.assertEqual(number, "fizzBuzz")
            a += 1
         
    #test de remplacement des numbres de la classe de 5 et 3 par fizzbuzz , 3 par fzz et 5 par buzz
    def test_add_fizzbuzz_fizz_buzz(self):
        obj_fizzbuzz = FizzBuzz(0, 101)
        list_numbers = obj_fizzbuzz.add_fizzBuzz_fizz_buzz()
        a = 0
        
        for number in list_numbers:
            if a % 3 == 0 and a % 5 == 0:
                self.assertEqual(number, "fizzBuzz")
            elif a % 3 == 0:
                self.assertEqual(number, "fizz")
            elif a % 5 == 0:
                self.assertEqual(number, "buzz")    
            a += 1
            
    #test de de rajout trass au nombre avec un 3
    def test_add_fizzbuzz_fizz_buzz(self):
        obj_fizzbuzz = FizzBuzz(0, 101)
        list_numbers = obj_fizzbuzz.add_fizzBuzz_fizz_buzz()
        list_numbers = obj_fizzbuzz.add_trass(list_numbers, 3, 'trass')
        a = 0
        
        for number in list_numbers:
            if '3' in str(a):
                self.assertTrue('trass' in number)
  
            a += 1
            
    #test de de rajout bross au nombre avec un 5
    def test_add_fizzbuzz_fizz_buzz(self):
        obj_fizzbuzz = FizzBuzz(0, 101)
        list_numbers = obj_fizzbuzz.add_fizzBuzz_fizz_buzz()
        list_numbers = obj_fizzbuzz.add_trass(list_numbers, 5, 'bross')
        a = 0
        
        for number in list_numbers:
            if '5' in str(a):
                self.assertTrue('bross' in number)
  
            a += 1


