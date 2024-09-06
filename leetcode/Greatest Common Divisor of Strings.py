class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        #Using the Euclidean algorithm to find the GCD
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        #Calculating GCD string length
        gcd_len = get_gcd(len(str1), len(str2))
        
        #Obtain the GCD string
        gcd_str = str1[:gcd_len]

        return gcd_str
