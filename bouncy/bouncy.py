
class Bouncy(object):
    """ set of methods to work with bouncy numbers """

    @classmethod
    def is_bouncy(self,number):
        """ determine if a number is bouncy.

        Keyword arguments:
            :param number: -- int positive number 
        """
        try:
            number=int(number)
        except:
            return 0

        increasing = False
        decreasing = False
        last = number % 10
        number =int(number / 10)
        while number > 0:
            next = number % 10
            number =int(number / 10)
            if next < last:
                increasing = True
            elif next > last:
                decreasing = True
            last = next
            if decreasing and increasing:
                return True
        return decreasing and increasing

    @classmethod
    def least_number_bouncy_by_percentage(self, percentage=90):
        """ Find the least number for which the proportion of bouncy numbers by percentage
        
        Keyword arguments:
            :param percentage: -- int positive  number is between 1 and 100, default 90
        """
        try:
            percentage=int(percentage)
        except:
            raise TypeError("Percentage number must be type (int)")

        if 0 <= percentage < 100:
            number = 99
            bouncies = 0
            while 100 * bouncies < percentage * number:
                number += 1
                if self.is_bouncy(number):
                    bouncies += 1
            return number
        else:
            raise ValueError("Percentage number is between 1 and 99")
