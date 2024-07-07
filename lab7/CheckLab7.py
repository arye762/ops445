#!/usr/bin/env python3
'''
Name: CheckLab7.py
Created on: November 3, 2019 by Raymond Chan
Reasons: (1) replace old Lab 7
         (2) test for programmer-defined class object
         (3) bind functions to methods for programmer-defined objects
         (4) examples on how to set object's scope
Usage:
Check all sections for the lab 7
./CheckLab7.py -f -v
Check a specific lab section
./CheckLab6.py -f -v lab7x -- x: a, b, c, d, e, f, i

Description:
This script is used to give students more feedback and hints while working
on Lab 7. Python scripts for Lab 7 and this script should be in the same 
directory. All the Python scripts must use the correct naming scheme.
'''

import subprocess
import unittest
import sys
import os
import hashlib
import urllib.request
import socket
import time

class lab7a(unittest.TestCase):
    """All test cases for lab7a - sum_times function"""
    
    def test_0(self):
        """[Lab 7] - [Investigation 1] - [Part 1] - Test for file creation: ./lab7a.py"""
        error_output = 'file lab7a.py cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab7a.py'), msg=error_output)

    def test_1(self):
        """[Lab 7] - [Investigation 1] - [Part 1] - Test for file creation: ./lab7a1.py"""
        error_output = 'file lab7a1.py cannot be fount(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab7a1.py'), msg=error_output)

    def test_a(self):
        """[Lab 7] - [Investigation 1] - [Part 1] - Test for errors running: ./lab7a1.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab7a1.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'Your lab7a1.py script exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 7] - [Investigation 1] - [Part 1] - Test for correct shebang line: ./lab7a1.py"""
        lab_file = open('./lab7a1.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
    
    def test_a_instantiate_class_0(self):
        """[Lab 7] - [Investigation 1] - [Part 1] - Test for Creating object - should fail with 4 arguments"""
        with self.assertRaises(Exception) as context:
            import lab7a as lab7aStudent
            objtime = lab7aStudent.Time(1,2,3,4)

    def test_a_instantiate_class_1(self):
        """[Lab 7] - [Investigation 1] - [Part 1] - Test for Creating object - should fail with string arguments"""
        with self.assertRaises(Exception) as context:
            import lab7a as lab7aStudent
            objtime = lab7aStudent.Time('hour','minute','second')
            x = lab7aStudent.format_time(objtime)

    def test_b1_sum_times(self):
        """[Lab 7] - [Investigation 1] - [Part 1] - Test for sum_times() - should provide the correct output"""
        error_fail = 'sum_times() in lab7a.py contains errors(HINT: run the lab7a1.py script and fix errors)'
        error_output = 'your lab7a.py has an error(HINT: sum_times() does not have correct return values)'
        try:
            import lab7a as lab7aStudent
            time1 = lab7aStudent.Time(9, 50, 0)
            time2 = lab7aStudent.Time(1,1,1)
            timeSum = lab7aStudent.sum_times(time1, time2)
            result = lab7aStudent.format_time(timeSum)
        except:
            self.fail(error_fail)
        answer = '10:51:01'
        self.assertEqual(result, answer, msg=error_output)
    
    def test_b2_sum_times(self):
        """[Lab 7] - [Investigation 1] - [Part 1] - Test for sum_times() - should provide the correct output"""
        error_fail = 'sum_times() in lab7a.py contains errors(HINT: run the lab7a1.py script and fix errors)'
        error_output = 'your program has an error(HINT: sum_times() does not have correct return values)'
        try:
            import lab7a as lab7aStudent
            time1 = lab7aStudent.Time(8,55,0)
            time2 = lab7aStudent.Time(0,50,0)
            timeSum = lab7aStudent.sum_times(time1,time2)
            result = lab7aStudent.format_time(timeSum)
        except:
            self.fail(error_fail)
        answer = '09:45:00'
        self.assertEqual(result, answer, msg=error_output)

class lab7b(unittest.TestCase):
    """All test cases for lab7b - modifier: change_time()"""
    
    def test_0(self):
        """[Lab 7] - [Investigation 1] - [Part 2] - Test for file creation: ./lab7b.py"""
        error_output = 'file lab7b.py cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab7b.py'), msg=error_output)

    def test_a1(self):
        """[Lab 7] - [Investigation 1] - [Part 2] - Test for correct shebang line: ./lab7b.py"""
        lab_file = open('./lab7b.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
    
    def test_a_instantiate_class_0(self):
        """[Lab 7] - [Investigation 1] - [Part 2] - Test for Creating object - should fail with 4 arguments"""
        with self.assertRaises(Exception) as context:
            import lab7a as lab7aStudent
            objtime = lab7aStudent.Time(1,2,3,4)

    def test_a_instantiate_class_1(self):
        """[Lab 7] - [Investigation 1] - [Part 2] - Test for Creating object - should fail with string arguments"""
        with self.assertRaises(Exception) as context:
            import lab7b as lab7bStudent
            objtime = lab7bStudent.Time('hour','minute','second')
            x = lab7bStudent.format_time(objtime)

    def test_b1_change_time(self):
        """[Lab 7] - [Investigation 1] - [Part 2] - Test for change_time() with +1800 seconds """
        error_fail = 'change_time() in lab7b.py contains errors(HINT: check change_time() function and fix errors)'
        error_output = 'your lab7b.py has an error(HINT: change_time() does not have correct return values)'
        try:
            import lab7b as lab7bStudent
            time1 = lab7bStudent.Time(9, 50, 0)
            x = lab7bStudent.change_time(time1,1800)
            result = lab7bStudent.format_time(time1)
        except:
            self.fail(error_fail)
        answer = '10:20:00'
        self.assertEqual(result, answer, msg=error_output)
    
    def test_b2_change_time(self):
        """[Lab 7] - [Investigation 1] - [Part 2] - Test for change_time() with -1800 seconds"""
        error_fail = 'change_time() in lab7b.py contains errors(HINT: check change_time() function and fix errors)'
        error_output = 'your program has an error(HINT: sum_times() does not have correct return values)'
        try:
            import lab7b as lab7bStudent
            time1 = lab7bStudent.Time(9,50,0)
            x = lab7bStudent.change_time(time1, -1800)
            result = lab7bStudent.format_time(time1)
        except:
            self.fail(error_fail)
        answer = '09:20:00'
        self.assertEqual(result, answer, msg=error_output)

class lab7c(unittest.TestCase):
    """All test cases for lab7c - time_to_sec() and sec_to_time function"""
    
    def test_0(self):
        """[Lab 7] - [Investigation 1] - [Part 3] - Test for file creation: ./lab7c.py"""
        error_output = 'file lab7c.py cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab7c.py'), msg=error_output)

    def test_1(self):
        """[Lab 7] - [Investigation 1] - [Part 3] - Test for file creation: ./lab7c1.py"""
        error_output = 'file lab7c1.py cannot be fount(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab7c1.py'), msg=error_output)

    def test_a(self):
        """[Lab 7] - [Investigation 1] - [Part 3] - Test for errors running: ./lab7c1.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab7c1.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'Your lab7c1.py script exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a_instantiate_class_0(self):
        """[Lab 7] - [Investigation 1] - [Part 3] - Test for Creating object - should fail with 4 arguments"""
        with self.assertRaises(Exception) as context:
            import lab7c as lab7cStudent
            objtime = lab7cStudent.Time(1,2,3,4)

    def test_a_instantiate_class_1(self):
        """[Lab 7] - [Investigation 1] - [Part 3] - Test for Creating object - should fail with string arguments"""
        with self.assertRaises(Exception) as context:
            import lab7c as lab7cStudent
            objtime = lab7cStudent.Time('hour','minute','second')
            x = lab7cStudent.format_time(objtime)

    def test_b1_time_to_sec(self):
        """[Lab 7] - [Investigation 1] - [Part 3] - Test for time_to_sec() function in ./lab7c.py"""
        error_fail = 'time_to_sec() in lab7c.py contains errors(HINT: run the lab7c1.py script and fix errors)'
        error_output = 'your time_to_sec() in lab7c.py has an error(HINT: time_to_sec() does not have correct return values)'
        try:
            import lab7c as lab7cStudent
            time1 = lab7cStudent.Time(9, 50, 0)
            seconds = lab7cStudent.time_to_sec(time1)
        except:
            self.fail(error_fail)
        answer = 35400
        self.assertEqual(seconds, answer, msg=error_output)
    
    def test_b2_sec_to_time(self):
        """[Lab 7] - [Investigation 1] - [Part 3] - Test for sec_to_time() function in .lab7c.py"""
        error_fail = 'sec_to_time() in lab7c.py contains errors(HINT: run the lab7c1.py script and fix errors)'
        error_output = 'your sec_to_time() in lab7c.py has an error(HINT: sec_to_time() does not have correct return values)'
        try:
            import lab7c as lab7cStudent
            seconds = 35400
            time_from_seconds = lab7cStudent.sec_to_time(seconds)
            str_time = lab7cStudent.format_time(time_from_seconds)
        except:
            self.fail(error_fail)
        answer = '09:50:00'
        self.assertEqual(str_time, answer, msg=error_output)

class lab7d(unittest.TestCase):
    """All test cases for lab7d - bind functions to methods"""
    
    def test_0(self):
        """[Lab 7] - [Investigation 2] - [Part 1] - Test for file creation: ./lab7d.py"""
        error_output = 'file lab7d.py cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab7d.py'), msg=error_output)

    def test_a_instantiate_class_0(self):
        """[Lab 7] - [Investigation 2] - [Part 1] - Test for Creating object in ./lab7d.py - should fail with 4 arguments"""
        with self.assertRaises(Exception) as context:
            import lab7d as lab7dStudent
            objtime = lab7dStudent.Time(1,2,3,4)

    def test_a_instantiate_class_1(self):
        """[Lab 7] - [Investigation 2] - [Part 1] - Test for Creating object in ./lab7d.py - should fail with string arguments"""
        with self.assertRaises(Exception) as context:
            import lab7d as lab7dStudent
            objtime = lab7dStudent.Time('hour','minute','second')
            x = lab7dStudent.format_time(objtime)

    def test_b1_time_to_sec(self):
        """[Lab 7] - [Investigation 2] - [Part 1] - Test for time_to_sec() method in ./lab7d.py"""
        error_fail = 'time_to_sec() in lab7d.py contains errors(HINT: review the script and fix errors)'
        error_output = 'your time_to_sec() in lab7d.py has an error(HINT: time_to_sec() does not return correct values)'
        try:
            import lab7d as lab7dStudent
            time1 = lab7dStudent.Time(9, 50, 0)
            seconds = time1.time_to_sec()
        except:
            self.fail(error_fail)
        answer = 35400
        self.assertEqual(seconds, answer, msg=error_output)
    
    def test_b2_format_time(self):
        """[Lab 7] - [Investigation 2] - [Part 1] - Test for format_time() method in ./lab7d.py"""
        error_fail = 'format_time() in lab7d.py contains errors(HINT: review the script and fix errors)'
        error_output = 'your format_time() in lab7d.py has an error(HINT: format_time() does not return correct values)'
        try:
            import lab7d as lab7dStudent
            time1 = lab7dStudent.Time(9, 50, 0)
            result = time1.format_time()
        except:
            self.fail(error_fail)
        answer = '09:50:00'
        self.assertEqual(result, answer, msg=error_output)

    def test_b3_sum_times(self):
        """[Lab 7] - [Investigation 2] - [Part 1] - Test for sum_times() method in ./lab7d.py"""
        error_fail = 'sum_times() in lab7d.py contains errors(HINT: review the script and fix errors)'
        error_output = 'your sum_times() in lab7d.py has an error(HINT: sum_times() does not return correct result)'
        try:
            import lab7d as lab7dStudent
            time1 = lab7dStudent.Time(9, 50, 0)
            time2 = lab7dStudent.Time(1, 2, 3)
            sum_t1_t2 = time1.sum_times(time2)
            result = sum_t1_t2.format_time()
        except:
            self.fail(error_fail)
        answer = '10:52:03'
        self.assertEqual(result, answer, msg=error_output)

    def test_b4_change_time(self):
        """[Lab 7] - [Investigation 2] - [Part 1] - Test for change_time() method in ./lab7d.py"""
        error_fail = 'change_time() in lab7d.py contains errors(HINT: review the script and fix errors)'
        error_output = 'your change_time() in lab7d.py has an error(HINT: change_time() does not return correct result)'
        try:
            import lab7d as lab7dStudent
            time1 = lab7dStudent.Time(9, 50, 10)
            seconds = 1800
            none = time1.change_time(seconds)
            result = time1.format_time()
        except:
            self.fail(error_fail)
        answer = '10:20:10'
        self.assertEqual(result, answer, msg=error_output)

    def test_b5_valid_time(self):
        """[Lab 7] - [Investigation 2] - [Part 1] - Test for invalid time using valid_time() method in ./lab7d.py"""
        error_fail = 'valid_time() in lab7d.py contains errors(HINT: review the script and fix errors)'
        error_output = 'your valid_time() in lab7d.py has an error(HINT: valild_time() does not return correct result)'
        try:
            import lab7d as lab7dStudent
            time1 = lab7dStudent.Time(9, 50, 61)
            result = time1.valid_time()
        except:
            self.fail(error_fail)
        answer = False
        self.assertEqual(result, answer, msg=error_output)    

    def test_b6_valid_time(self):
        """[Lab 7] - [Investigation 2] - [Part 1] - Test for valid time using valid_time() method in ./lab7d.py"""
        error_fail = 'valid_time() in lab7d.py contains errors(HINT: review the script and fix errors)'
        error_output = 'your valid_time() in lab7d.py has an error(HINT: valild_time() does not return correct result)'
        try:
            import lab7d as lab7dStudent
            time1 = lab7dStudent.Time(9, 50, 59)
            result = time1.valid_time()
        except:
            self.fail(error_fail)
        answer = True
        self.assertEqual(result, answer, msg=error_output) 

    def test_b7_sec_to_time(self):
        """[Lab 7] - [Investigation 2] - [Part 1] - Test for sec_to_time() function in ./lab7d.py"""
        error_fail = 'sec_to_time() in lab7d.py contains errors(HINT: review the script and fix errors)'
        error_output = 'your sec_to_time() in lab7d.py has an error(HINT: sec_to_time() does not return correct result)'
        try:
            import lab7d as lab7dStudent
            sec_time = lab7dStudent.sec_to_time(1800)
            result = sec_time.format_time()
        except:
            self.fail(error_fail)
        answer = '00:30:00'
        self.assertEqual(result, answer, msg=error_output)    
   
class lab7e(unittest.TestCase):
    """All test cases for lab7e - add special method __str__ and __repr__"""
    
    def test_0(self):
        """[Lab 7] - [Investigation 2] - [Part 2] - Special object methods - Test for file creation: ./lab7e.py"""
        error_output = 'file lab7e.py cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab7e.py'), msg=error_output)
    
    def test_b1_import(self):
        """[Lab 7] - [Investigation 2] - [Part 2] - Test for importing ./lab7e.py"""
        error_fail = 'error trying to import lab7e.py (HINT: review the script and fix errors)'
        error_output = 'unidentify error - please informat your professor for help'
        try:
            import lab7e as lab7eStudent
        except:
            self.fail(error_fail)

    def test_b2_create_object(self):
        """[Lab 7] - [Investigation 2] - [Part 2] - Test for creating time object in ./lab7e.py"""
        error_fail = 'Error trying to create time object in lab7e.py (HINT: review the script and fix errors)'
        error_output = 'your __init__() in lab7e.py has an error(HINT: format_time() does not return correct values)'
        try:
            import lab7e as lab7eStudent
            time1 = lab7eStudent.Time(9, 50, 0)
        except:
            self.fail(error_fail)
    
    def test_b3_str(self):
        """[Lab 7] - [Investigation 2] - [Part 2] - Test for __str__ method in ./lab7e.py"""
        error_fail = '__str__() in lab7e.py contains errors(HINT: review the script and fix errors)'
        error_output = 'your __str__() in lab7e.py has an error(HINT: format_time() does not return correct values)'
        try:
            import lab7e as lab7eStudent
            time1 = lab7eStudent.Time(9, 50, 0)
            result = time1.__str__()
        except:
            self.fail(error_fail)
        answer = '09:50:00'
        self.assertEqual(result, answer, msg=error_output)

    def test_b4_repr(self):
        """[Lab 7] - [Investigation 2] - [Part 2] - Test for __repr__ method in ./lab7e.py"""
        error_fail = '_ repr__() in lab7e.py contains errors(HINT: review the script and fix errors)'
        error_output = 'your __repr__() in lab7e.py has an error(HINT: format_time() does not return correct values)'
        try:
            import lab7e as lab7eStudent
            time1 = lab7eStudent.Time(9, 50, 0)
            result = time1.__repr__()
        except:
            self.fail(error_fail)
        answer = '09.50.00'
        self.assertEqual(result, answer, msg=error_output)


class lab7f(unittest.TestCase):
    """All test cases for lab7f - implement operator overloading"""
    
    def test_0(self):
        """[Lab 7] - [Investigation 2] - [Part 3] - Operator overloading - Test for file creation: ./lab7f.py"""
        error_output = 'file lab7f.py cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab7f.py'), msg=error_output)

    def test_b1_import(self):
        """[Lab 7] - [Investigation 2] - [Part 3] - Test for importing ./lab7f.py"""
        error_fail = 'error trying to import lab7f.py (HINT: review the script and fix errors)'
        error_output = 'unidentify error - please informat your professor for help'
        try:
            import lab7f as lab7fStudent
        except:
            self.fail(error_fail)

    def test_b2_create_object(self):
        """[Lab 7] - [Investigation 2] - [Part 3] - Test for creating time object in ./lab7f.py"""
        error_fail = 'Error trying to create time object in lab7f.py (HINT: review the script and fix errors)'
        error_output = 'your __init__() in lab7f.py has an error(HINT: format_time() does not return correct values)'
        try:
            import lab7f as lab7fStudent
            time1 = lab7fStudent.Time(9, 50, 0)
        except:
            self.fail(error_fail)

    def test_b3_operator_overloading(self):
        """[Lab 7] - [Investigation 2] - [Part 3] - Test for operator overloading for + in ./lab7f.py"""
        error_fail = 'Error trying add to time object in lab7f.py (HINT: review the script and fix errors)'
        error_output = 'your __add__() in lab7f.py has an error(HINT: format_time() does not return correct values)'
        try:
            import lab7f as lab7fStudent
            time1 = lab7fStudent.Time(9, 50, 0)
            time2 = lab7fStudent.Time(1, 10, 0)
            sum_time = time1 + time2
            result = str(sum_time)
        except:
            self.fail(error_fail)
        answer = '11:00:00'
        self.assertEqual(result, answer, msg=error_output)

class lab7i(unittest.TestCase):
    """All test cases for lab7i - local and global scope"""
    
    def test_0(self):
        """[Lab 7] - [Investigation 3] - [Part 3] - Local/Global Scope - Test for file creation: ./lab7i.py"""
        error_output = 'file lab7i.py cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab7i.py'), msg=error_output)

    def test_b1_run(self):
        """[Lab 7] - [Investigation 3] - [Part 3] - Global scope - Test for successful execution: ./lab7i.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab7i.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you script produce the exact output!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_b2_run(self):
        """[Lab 7] - [Investigation 3] - [Part 3] - Global scope - Test for correct output: ./lab7i.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab7i.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if stdout from the process does not match expected output
        return_code = p.wait()
        expected_output = b'print() in main on schoolName: Seneca\nprint() in function1 on schoolName: SICT\nprint() in main on schoolName: SICT\nprint() in function2 on schoolName: SSDO\nprint() in main on schoolName: SSDO\n'
        error_output = 'output of your script does not match what is expected (HINT: make sure you script produce the exact output!)'
        self.assertEqual(stdout, expected_output, msg=error_output)


def ChecksumLatest(url=None):
    dat = ''
    with urllib.request.urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')
            dat = dat + line
    checksum = hashlib.sha256(dat.encode('utf-8')).digest()
    #print("internet", checksum)
    return checksum

def ChecksumLocal(filename=None):
    fil = open(filename, 'r', encoding='utf-8')
    dat = fil.readlines()
    textdata = ''
    for line in dat:
        textdata = textdata + line
    checksum = hashlib.sha256(textdata.encode('utf-8')).digest()
    #print("local", checksum)
    return checksum

def CheckForUpdates():
    try:
        lab_name = 'CheckLab7.py'
        lab_num = 'lab7'
        print('Checking for updates...')
        if ChecksumLatest(url='https://ict.senecacollege.ca/~eric.brauer/ops445/labs/LabCheckScripts/' + lab_name) != ChecksumLocal(filename='./' + lab_name):
            print()
            print(' There is a update available for ' + lab_name + ' please consider updating:')
            print(' cd ~/ops445/' + lab_num + '/')
            print(' pwd  #   <-- i.e. confirm that you are in the correct directory')
            print(' rm ' + lab_name)
            print(' ls ' + lab_name + ' || wget https://ict.senecacollege.ca/~eric.brauer/ops445/labs/LabCheckScripts/' + lab_name)
            print()
            return
        print('Running latest version...')
        return
    except:
        # Cleanly skip updating if any errors occur for offline or matrix issues
        print('No connection made...')
        print('Skipping updates...')
        return


def displayReportHeader():
    report_heading = 'OPS445 Lab Report - System Information for running '+sys.argv[0]
    print(report_heading)
    print(len(report_heading) * '=')
    import getpass
    print('    User login name:', getpass.getuser())
    print('    Linux system name:', socket.gethostname())
    print('    Python executable:',sys.executable)
    print('    Python version: ',sys.version_info.major,sys.version_info.minor,sys.version_info.micro,sep='')
    print('    OS Platform:',sys.platform)
    print('    Working Directory:',os.getcwd())
    print('    Start at:',time.asctime())
    print(len(report_heading) * '=')
    return

if __name__ == '__main__':
    #CheckForUpdates()
    #wait = input('Press ENTER to run the Lab Check...')
    if len(sys.argv) == 3:
       report_header = displayReportHeader()
    unittest.main()
