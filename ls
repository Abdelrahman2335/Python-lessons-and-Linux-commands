ls: Is very very useful command in Linux and her I will show you how you 
can use it. 

 ls (To show the content in the pwd )

 ls -1(Display one file per line)

 ls -l (To show long listing information about the file or director)  

 ls -lh (You can use it to display file size in easy to read form 
 M for MB, K for KB, G for GB).

 ls -ld (When you use “ls -l” you will get the details of directories
 content. But if you want the details of the directory it self then you can
 use -d option as., For example, if you use ls -l /etc will display all the files under the etc directory. But, if you want to display the information   about the /etc/ directory, use -ld option).

 ls -lt : To sort the file names displayed in the order of last 
modification time.You will be finding it handy to use it in 
combination with -l option.

 ls -ltr : To sort the file names in the last modification time in reverse
 order. This will be showing the last edited file in the last line which 
 will be handy when the listing goes beyond a page.


 ls -a : To show all the hidden files in the directory.

 ls -A : To show the hidden files, but not the ‘.’ (current directory) 
 and ‘..’ (parent directory).

 ls -R : To display what's inside evry directory in the directory.

 ls -i :  Sometimes you may want to know the inone number of a file for
 internal maintenance. Use -i option as shown below to display inone number.
 Using inode number you can remove files that has special characters
 in it’s name.


 ls -q : To print question mark instead of the non graphics control 
 characters.


 ls -n ~/kv : Lists the output like -l, but shows the uid and gid in 
 numeric format instead of names.


 ls -F : Instead of doing the ‘ls -l’ and then the checking for the first 
 character to determine the type of file. You can use -F which classifies 
 the file with different special character for different kind of files.

    / – directory.
    nothing – normal file.
    @ – link file.
    * – Executable file


 ls –color=auto : Recognizing the file type by the color in which it gets 
 displayed is an another kind in classification of file. In the below 
 output directories get displayed in blue, soft links get displayed in 
 green, and ordinary files gets displayed in default color.


If you want to know more and see example please visit this site:

https://www.geeksforgeeks.org/practical-applications-ls-command-linux/


you don't have to write the path to ls some files you can use (which) 
which it's very good command and it can helps you to do that:
	ls -l $(which cp)
	or
	ls -l `which cp`



 Have a great day :)
