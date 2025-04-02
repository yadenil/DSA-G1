class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return celsius + 273.15, 1.80 * celsius + 32.00
        
