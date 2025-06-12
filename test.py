import pytest
from unittest.mock import patch
import sys
from Library_SysMgmt import onStart, login, manage_user, manage_book, bookaccount

def test_onStart_exit():
    with patch('builtins.input', return_value='0'), patch('sys.exit') as mock_exit:
        onStart()
        mock_exit.assert_called_once_with('Program terminated Successfully')

def test_onStart_login():
    with patch('builtins.input', side_effect=['1', 'testuser', 'testpass']), \
         patch('Library_SysMgmt.library.Library_Management_System.Login', return_value=True), \
         patch('Library_SysMgmt.cf.cls'), \
         patch('builtins.print') as mock_print:
        onStart()
        mock_print.assert_any_call('    ** Login successful **     ')

def test_onStart_register():
    with patch('builtins.input', side_effect=['2', 'newuser', 'newpass']), \
         patch('Library_SysMgmt.cf.cls'), \
         patch('Library_SysMgmt.manage_user.register_lib') as mock_register:
        onStart()
        mock_register.assert_called_once()

def test_login_incorrect_credentials():
    with patch('builtins.input', side_effect=['wronguser', 'wrongpass', 'N']), \
         patch('Library_SysMgmt.library.Library_Management_System.Login', return_value=False), \
         patch('Library_SysMgmt.cf.cls'), \
         patch('builtins.print') as mock_print:
        login()
        mock_print.assert_any_call('Incorrect username or password.\nWould you like to register ? [Y/N]\n')

def test_manage_user_add():
    with patch('builtins.input', return_value='1'), \
         patch('Library_SysMgmt.manage_user.add', return_value=True), \
         patch('Library_SysMgmt.cf.cls'), \
         patch('builtins.print') as mock_print:
        manage_user()
        mock_print.assert_any_call('  * User added successfully *  ')

def test_manage_book_add():
    with patch('builtins.input', return_value='1'), \
         patch('Library_SysMgmt.manage_book.add', return_value=True), \
         patch('Library_SysMgmt.cf.cls'), \
         patch('builtins.print') as mock_print:
        manage_book()
        mock_print.assert_any_call('  * Book added successfully *  ')

def test_bookaccount_reserved_book():
    with patch('builtins.input', return_value='1'), \
         patch('Library_SysMgmt.manage_account.display_res') as mock_display_res:
        bookaccount()
        mock_display_res.assert_called_once()

def test_bookaccount_exit():
    with patch('builtins.input', return_value='0'), patch('sys.exit') as mock_exit:
        bookaccount()
        mock_exit.assert_called_once_with('Program terminated Successfully')
