from CommonTests import CommonTests1
import sys

class AdminPortalTest1(CommonTests1):
    
    def scenario1(self):
        try:
            method_name = sys._getframe().f_code.co_name
            class_name = self.__class__.__name__
            print("start of method:", class_name)
            self.login_as_admin()
            self.test_case_1()
            self.test_case_3()
        except Exception as e:
            e.printStackTrace()
            assert False, "Error in " + method_name + ": " + str(e)

# Usage
if __name__ == "__main__":
    admin_test = AdminPortalTest1()
    admin_test.scenario1()
