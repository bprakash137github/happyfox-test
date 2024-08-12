from CommonTests import CommonTests1

class AdminPortalTest2(CommonTests1):

    def scenario2(self):
        try:
            method_name = self.__class__.__name__
            class_name = sys._getframe().f_code.co_name
            print("start of method:", class_name)
            self.login_as_admin()
            self.test_case_1()
            self.test_case_2()
            self.test_case_3()
        except Exception as e:
            e.printStackTrace()
            assert False, "Error in " + method_name + ": " + str(e)

# Usage
if __name__ == "__main__":
    admin_test = AdminPortalTest2()
    admin_test.scenario2()
