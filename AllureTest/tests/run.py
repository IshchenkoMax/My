import unittest
from unittest import TestSuite
from tests.test_001_RunMainPage import RunMainPage
from tests.test_002_NewUserRegistration import NewUserReg
from tests.test_003_LogIn import UserLogIn
from tests.test_004_Logout import Logout
from tests.test_005_ResetPassword import ResetPassword
from tests.test_006_UpdateUserInfo import UpdateUserInfo
from tests.test_007_BrandPage import BrandPage
from tests.test_008_TakeActionVisitor import TakeActionVisitor
from tests.test_009_TakeAction_User import TakeActionUser


def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_class in (RunMainPage, NewUserReg, UserLogIn, Logout, ResetPassword, UpdateUserInfo, BrandPage,
                       TakeActionVisitor, TakeActionUser):
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


unittest.main(verbosity=2)