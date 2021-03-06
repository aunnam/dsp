# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. ls : list files in current directory
> > 2. cd .. : move up one level in directory structure
> > 3. cd x : move into directory named x
> > 4. cd : go to home directory
> > 5. rm x : remove file named x within working directory
> > 6. mv x y : rename file x to y within working directory
> > 7. mkdir x : make directory x within working directory
> > 8. rmdir x : remove directory x within working directory
> > 9. pwd : print working directory
> > 10. touch x : create a file named x
> > 11. cp x y : copy file x to directory/file y
> > 12. cp -r dir1 dir2 : copy directory dir1 to directory dir2

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 1. 'ls' : list files in current directory
> > 2. 'ls -a' : list files in current directory including hidden files not see by ls
> > 3. 'ls -l' : list files in current directory in long format and showing permissions
> > 4. 'ls -lh' : lists files in current directory in long format and showing permissions, but with more readable file sizes
> > 5. 'ls -lah' : lists everything that 'ls -lh' does but includes hidden files 
> > 6. 'ls -t' : lists files in current directory sorted by time and date
> > 7. 'ls -Glp' : list files in current directory in long format and showing permissions but without appended slash directory indicators but no group names being printed

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -r : list files in current directory in reverse order
> > ls -R : list files in current directory but also includes sub directories
> > ls -u : list files in current directory sorted by access time
> > ls -x : list files in current directory as rows across the screen
> > ls -d : lists only directories within current directory

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs is a command on UNIX system that builds command lines with standard input parameters. 
> > echo 1 2 3 4 5 6 | xargs -n 2   
> > The above line runs the echo command on standard input of '1 2 3 4 5 6' with the restriction of passing 2 numbers at a time to the echo argument. So it prints the numbers from 1 to 6, 2 at a time on seperate lines.
