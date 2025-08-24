# VLSI-Expert.com Technical Content (PARTIAL)

**Extracted on:** 2025-08-25 03:13:41

**Total Articles:** 50 (PARTIAL - Scraping was interrupted)

⚠️ **Note:** This is a partial result. The scraping process was interrupted.

## 📊 Content Summary (Partial)

- **Analog**: 1 articles
- **Dft**: 1 articles
- **Low Power**: 1 articles
- **Parasitic**: 36 articles
- **Sta**: 11 articles

---

## 📚 Table of Contents (Partial)

- [Analog (1)](##analog)
- [Dft (1)](##dft)
- [Low Power (1)](##low-power)
- [Parasitic (36)](##parasitic)
- [Sta (11)](##sta)

---

## Analog

### 1. ## Tuesday, January 25, 2022

**URL:** https://www.vlsi-expert.com/2022/01/
**Date:** 2022-01
**Tags:** analog, ESD

## Tuesday, January 25, 2022

### [Unix For VLSI Industry - Part 3b - Assignment 2 - SHELL Scripting](https://www.vlsi-expert.com/2022/01/shell-debugging-assignment-2.html)

## SHELL Scripting Debugging Assignment - 2

In the [previous assignment](http://www.vlsi-expert.com/2022/01/shell-debugging-assignment-1.html), I have captured few of the practice question related to debugging part. We know very well how much this is important from Industry point of view. Like I said in last article - Understanding the Scripting syntax and using them in automation - these are 2 different things. Debugging the existing code OR say enhancing that as per the requirement is completely different. For that first you need to understand the different error messages and then you should know how to fix that part.

In this part also - there are list of questions which can help you to do practice.

1. Correct the below shell script to split the given string.

#! /bin/bash

string="abc,xyz,jkl,raw"

IFS=' '

read -r arr <<< "$string"

for val in "${arr\[@\]}";

do

printf "name = $val\\n"

done

2. Correct the below shell script to match the two input strings.

read a

read b

if \["$a"=!"$b"\] then

    echo "Matched"

elif

    echo "Not Matching"

fi

3. Correct the below shell script to create a shell function library.

function square(){

    v1=$10

    $n = $((v1\*v1))

    echo $n

}

4. Correct the below shell script to create a shell function library to calculate the factorial of a given number.

function factorial(){

    v1=$2

    n=1

    while \[\[ $v1 -gt 0 \]\];

do

v1=$(($v1 - 1))

done

    echo $n

}

5. Correct the below shell script to calculate the number of users.

read userInput

case \[$userInput\] \[in\]

    {1} lslogins -o USER ;

    {2} who --count \
![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

## Dft

### 1. ## Friday, January 28, 2022

**URL:** https://www.vlsi-expert.com/2022/
**Date:** Unknown
**Tags:** analog, ESD, dft

## Friday, January 28, 2022

### [Unix For VLSI Industry - Part 4a- TASK 1 - SHELL Scripting](https://www.vlsi-expert.com/2022/01/shell-scripting-task-1.html)

## SHELL Scripting Task - 1

In the previous articles or say [Assignment 1](http://www.vlsi-expert.com/2022/01/shell-debugging-assignment-1.html) and [Assignment 2](http://www.vlsi-expert.com/2022/01/shell-debugging-assignment-2.html), I have captured few of the practice question related to debugging of SHELL Scripting. We know very well how much this is important from Industry point of view. By now you are very much expert in the UNIX Command and specially writing any Kind of Script using the SHELL Scripting. I am now going to give you few small-small TASK which you can do yourself and these can be used directly in Industry with small modification as per the requirement.

This is the based on script or say automation, we normally use during regression-runs. If you don't know what's regressions - basically engineers run a set of code/tool on large set of small designs (known as Test cases) and analysis the result with respect to each test cases. Few test case are designed to be failed and few suppose to a pass (means should give expected result). If after running the code - result is different from the expected one - We consider regression testcase fail. :)

As you can see that it's looks like Interesting first time but it's huge in numbers and that's the reason there is a lot of automation happen around this using different type of scripting language. Today, we will discuss about the same but in SHELL scripting.

**Task 1a -:** There is a directory named “ **regression**” inside which there are more than a thousand sub-directories. Each sub-directory has two more sub-directories which are “ **golden\_dir**” and “ **current\_dir**”. Inside these sub-directories, a file with different versions is present.

- Write a script to diff files present in “ **golden\_dir**” and “ **current\_dir**”. If diff is valid then update the “ **golden\_dir**” sub-directory with the new version of the file.

**Task 1b -:**

- Step 1: Write a script named “ **parent.sh**” which run another script with “\*.sh” extension only.
- If the user has a directory including 100 script files with different extensions in it. Write a script “extension\_converter.sh” which can convert any extension of file to “\*.sh” extension and call this script inside “parent.sh” script.

**Task 1c :-**

- There is a directory containing more than 100 script files written in python, perl, and TCL syntax.
- Each python script has first line i.e., /usr/bin/python
- Each Perl script has first line i.e., /usr/bin/perl
- Each tcl script has first line i.e., /usr/bin/tclsh

Write a script to dump python scripts to “python” directory, perl scripts to “perl” directory, and TCL scripts to “TCL” directory.

**Task 1d :** A directory contains thousands of files created in 2020 and 2021.

- Write a script to create a log file which contains the list of all files created in June 2020 along with the modified time.

Try these task and I am sure if you have prepared them today - Tomorrow you can use these in Industry with slight modification.

Stay Tune and Happy Learning.

Posted by
VLSI Expert
at
[6:19 PM](https://www.vlsi-expert.com/2022/01/shell-scripting-task-1.html "")[0\\
comments](https://www.vlsi-expert.com/2022/01/shell-scripting-task-1.html#)

## Tuesday, January 25, 2022

### [Unix For VLSI Industry - Part 3b - Assignment 2 - SHELL Scripting](https://www.vlsi-expert.com/2022/01/shell-debugging-assignment-2.html)

## SHELL Scripting Debugging Assignment - 2

In the [previous assignment](http://www.vlsi-expert.com/2022/01/shell-debugging-assignment-1.html), I have captured few of the practice question related to debugging part. We know very well how much this is important from Industry point of view. Like I said in last article - Understanding the Scripting syntax and using them in automation - these are 2 different things. Debugging the existing code OR say enhancing that as per the requirement is completely different. For that first you need to understand the different error messages and then you should know how to fix that part.

In this part also - there are list of questions which can help you to do practice.

1. Correct the below shell script to split the given string.

#! /bin/bash

string="abc,xyz,jkl,raw"

IFS=' '

read -r arr <<< "$string"

for val in "${arr\[@\]}";

do

printf "name = $val\\n"

done

2. Correct the below shell script to match the two input strings.

read a

read b

if \["$a"=!"$b"\] then

    echo "Matched"

elif

    echo "Not Matching"

fi

3. Correct the below shell script to create a shell function library.

function square(){

    v1=$10

    $n = $((v1\*v1))

    echo $n

}

4. Correct the below shell script to create a shell function library to calculate the factorial of a given number.

function factorial(){

    v1=$2

    n=1

    while \[\[ $v1 -gt 0 \]\];

do

v1=$(($v1 - 1))

done

    echo $n

}

5. Correct the below shell script to calculate the number of users.

read userInput

case \[$userInput\] \[in\]

    {1} lslogins -o USER ;

    {2} who --count \
![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

## Low Power

### 1. #### 13 comments:

**URL:** https://www.vlsi-expert.com/p/low-power.html
**Date:** Unknown
**Tags:** CMOS, low-power, dft, parasitic

#### 13 comments:

01. !

 [July 4, 2017 at 12:00 PM](https://www.vlsi-expert.com/p/low-power.html)

 please update this section as soon as possible

 Reply

 Replies

 !

 [September 25, 2019 at 3:00 PM](https://www.vlsi-expert.com/p/low-power.html)

 Could you please share links/note of low power section including upf also?!

 Best regards,

 Raed

 Replies

 Reply

 Reply

02. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[January 17, 2018 at 3:33 PM](https://www.vlsi-expert.com/p/low-power.html)

 This section has already been updated. Please check your email. Thank you

 Reply

 Replies

 Reply

03. ![](https://resources.blogblog.com/img/blank.gif)

 Jeevan[March 6, 2018 at 7:54 PM](https://www.vlsi-expert.com/p/low-power.html)

 Please send me the update u did regarding this....

 Thank you

 Reply

 Replies

 Reply

04. !

 [April 5, 2018 at 3:04 PM](https://www.vlsi-expert.com/p/low-power.html)

 please send me the update(links/notes) regarding low power at nitesh.bhardwaj42@gmail.com.

 Thank You

 Reply

 Replies

 Reply

05. !

 [December 28, 2018 at 1:12 PM](https://www.vlsi-expert.com/p/low-power.html)

 Please send me the link/notes of low power vlsi design on ashishsit16@gmail.com

 Thanking you,

 Reply

 Replies

 Reply

06. !

 [December 28, 2018 at 1:13 PM](https://www.vlsi-expert.com/p/low-power.html)

 Please send me link / notes of low power vlsi design on ashishsit16@gmail.com

 Thanking You,

 Reply

 Replies

 Reply

07. !

 [April 11, 2019 at 9:14 PM](https://www.vlsi-expert.com/p/low-power.html)

 kindly forward the notes on low power to emailid sivakarthik9997@gmail.com

 Reply

 Replies

 Reply

08. !

 [May 30, 2019 at 11:46 AM](https://www.vlsi-expert.com/p/low-power.html)

 please send this content update to my mail id maddileti.swamy@gmail.com

 Reply

 Replies

 Reply

09. !

 [September 25, 2019 at 3:03 PM](https://www.vlsi-expert.com/p/low-power.html)

 could you please share links/notes of low power section include the upf blog.

 Reply

 Replies

 Reply

10. !

 [December 23, 2019 at 4:59 PM](https://www.vlsi-expert.com/p/low-power.html)

 Please send me some links or notes on low power vlsi design

 Reply

 Replies

 Reply

11. !

 [July 7, 2021 at 7:21 PM](https://www.vlsi-expert.com/p/low-power.html)

 please send some links or notes on low power cmos concepts in vlsi design

 mail id kiransai9338@gmail.com

 Reply

 Replies

 Reply

12. !

 [September 21, 2021 at 8:53 PM](https://www.vlsi-expert.com/p/low-power.html)

 Can you please share Low power all series notes on j.rashmi1696@gmail.com?

 Reply

 Replies

 Reply

Add comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

Load more...

[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

## Parasitic

### 1. #### 9 comments:

**URL:** https://www.vlsi-expert.com/p/recommended-book.html
**Date:** Unknown
**Tags:** sta, low-power, dft, parasitic

#### 9 comments:

1. !

[February 2, 2014 at 12:35 AM](https://www.vlsi-expert.com/p/recommended-book.html)

Can you pls tell me the source to buy

VLSI Interview Questions with Answers: Sam Sony (Author)

Static Timing Analysis Interview Questions : Sam Sony (Author)

in amzon i found it as specific to Kindle. i am looking for either ebook / normal book

Reply

Replies

![](https://resources.blogblog.com/img/blank.gif)

Anonymous[March 20, 2014 at 3:08 AM](https://www.vlsi-expert.com/p/recommended-book.html)

Down load the kindle app on your machine and it is an ebook

Replies

Reply

Reply

2. ![](https://resources.blogblog.com/img/blank.gif)

Anonymous[February 5, 2014 at 2:42 PM](https://www.vlsi-expert.com/p/recommended-book.html)

I think for one to build basic concepts. Reading those books is not effective. I tried to read those kind of books once and it costs me a lot of time plus very confusing. In my opinion, we should use those books to reference but not for reading, especially reading the whole thing.

Reply

Replies

Reply

3. !

[May 9, 2015 at 12:21 AM](https://www.vlsi-expert.com/p/recommended-book.html)

hi, please tell me about best vlsi training institute in chennai...please replay me...

thank you

Reply

Replies

Reply

4. ![](https://resources.blogblog.com/img/blank.gif)

aditya[June 10, 2015 at 4:26 PM](https://www.vlsi-expert.com/p/recommended-book.html)

sir please refer the material for dynamic timing analysis for single and multi cycle datapath

Reply

Replies

Reply

5. !

[July 28, 2016 at 12:11 PM](https://www.vlsi-expert.com/p/recommended-book.html)

bookzz.org

download free book daily 10

Reply

Replies

Reply

6. ![](https://resources.blogblog.com/img/blank.gif)

Anonymous[January 31, 2017 at 5:45 PM](https://www.vlsi-expert.com/p/recommended-book.html)

ladiesman217ik@gmail.com

email me for pdf of the above mentioned books

Reply

Replies

Reply

7. !

[November 6, 2017 at 12:16 PM](https://www.vlsi-expert.com/p/recommended-book.html)

Hi Sir, can share info of materials to learn Vlsi physical design.

A much helpful, if you give steps to learn Vlsi design.

Thank you

Yogananda

Reply

Replies

Reply

8. !

[November 6, 2017 at 12:17 PM](https://www.vlsi-expert.com/p/recommended-book.html)

Hi Sir, can you share info of materials to learn Vlsi physical design.

A much helpful, if you give steps to learn Vlsi design.

Thank you

Yogananda

Reply

Replies

Reply

Add comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

Load more...

[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 2. #### 43 comments:

**URL:** https://www.vlsi-expert.com/p/vlsi-basic.html
**Date:** Unknown
**Tags:** digital-design, dft, low-power, CMOS, parasitic, analog

#### 43 comments:

01. ![](https://resources.blogblog.com/img/blank.gif)

 mayur[December 14, 2013 at 11:30 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 first, u are doing awesome work....and it will help lots of people thinking to make carrier in vlsi including me....

 sir, other topics are not visible....and please add as much as examples on different complex circuits using mux and decoders...

 thanks in advance...

 Reply

 Replies

 Reply

02. !

 [December 17, 2013 at 11:19 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Hi Mayur,

 I am updating other topics .. one-by-one.. It will take some time to update on the site. I will try to include examples or references as much as possible - so that every one can clarify their concepts.

 Reply

 Replies

 !

 [February 27, 2014 at 8:21 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 sir, can u plz help me to find more information on sequential circuits and basic flip flop

 Replies

 Reply

 !

 [November 4, 2014 at 11:48 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Sure, I will try my best to do it asap

 Replies

 Reply

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[January 17, 2015 at 11:29 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Dear Administrator now,i think its time to update your blog,at-least complete those remaining topics as it have been a year now. Chapter-1,2&4 are the basic ones.Please at least fill them with your great work. Again your work is extremely good,that's why people wants you to,..pls pls pls..

 Replies

 Reply

 Reply

03. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[February 5, 2014 at 2:46 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 If you want a help. I can help you updating other topics and you can edit it if you want, that will help you save time. Email me at hainam311@gmail.com.

 Reply

 Replies

 Reply

04. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[February 5, 2014 at 4:18 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 if you want a volunteer. Email me at hainam311@gmail.com

 Reply

 Replies

 Reply

05. !

 [April 17, 2014 at 3:53 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Eagerly waiting to enhance my knowledge in remaing topics.... Hope the unseen topics will b updated soon........

 Reply

 Replies

 !

 [April 19, 2014 at 10:56 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Hi Palas,

 I am working over that.. Soon I will update few more.

 Replies

 Reply

 !

 [May 5, 2014 at 11:00 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 ok. Thanks a lot.

 Replies

 Reply

 Reply

06. !

 [May 6, 2014 at 10:39 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 thank you so much sir for giving such a wndrful explanation about basics..........but as all are said i am exiting to learn remaining topics.plz update as early as possible..thnka in advance........

 Reply

 Replies

 Reply

07. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 24, 2014 at 12:10 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 sir I really thank you from d bottom of my heart...I m pursuing mtech in vlsi and I really needed these topics...u dnt knw hw much I was in need of them...thank you very much sir

 Reply

 Replies

 Reply

08. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 24, 2014 at 12:13 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 sir I need mos device and spice models...can u please update them soon

 Reply

 Replies

 !

 [August 24, 2014 at 6:26 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Hi,

 MOS device is in process and it will be uploaded sometime in this week.

 Spice models - can take some time - but I will see if I can prepare on the priority basis.

 Replies

 Reply

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 26, 2014 at 4:21 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 sir I request u to upload them as soon as possible coz I really need it...thank you sir

 Replies

 Reply

 !

 [September 8, 2014 at 7:15 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 I am in the process.. Few I have uploaded and few are in line. Please check the "latest" section.

 Replies

 Reply

 Reply

09. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[January 17, 2015 at 11:40 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Dear Administrator now,i think its time to update your blog, at-least complete those remaining topics s it have been a year now.Chapter-1,2&4 are the basic ones.Please at least fill them with your great work.Again your work is extremely good that's why people wants you to,..pls pls pls..

 Reply

 Replies

 !

 [January 19, 2015 at 11:25 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Thanks for Showing interest. I become busy in the other topics. Topics on CMOS are almost ready. I will update soon.

 Replies

 Reply

 Reply

10. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[January 24, 2015 at 1:47 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 I am in 6 sem n now I am going to study about vlsi it helped me to know the basic thnks. ..I want to become a vlsi engineer can u guid me

 Reply

 Replies

 !

 [January 24, 2015 at 11:36 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Drop me a mail and I will try to help you or guide you.

 Replies

 Reply

 Reply

11. !

 [March 24, 2015 at 6:02 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Hi Sir,

 I am planning to move into physical design can you please provide the topics I need to be covered and tools that can be helpful.

 Reply

 Replies

 Reply

12. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[April 2, 2015 at 11:28 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Thanks a lot for all this great work! It is VERY helpful! Thanks for taking out your time to help so many people!!!!

 Could you please upload the remaining sections for digital background and the CMOS working as soon as you get some time?

 Reply

 Replies

 Reply

13. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[April 16, 2015 at 2:44 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 can you send me material regarding to chapter 6 & 7? at hm1622@gmail.com

 Reply

 Replies

 Reply

14. !

 [February 5, 2016 at 9:55 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Hai sir,

 i am planning to move vlsi layout . Can u please forward me the material and contents to my mail id: mopidevisravani.475@gmail.com and tell me the top related sites to improve my knowledge

 Reply

 Replies

 Reply

15. !

 [February 26, 2016 at 6:48 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 What is resource sharing? Please illustrate this example using a piece of Verilog and draw a picture of the hardware produced in 2 cases (with and without resource sharing)

 Reply

 Replies

 Reply

16. !

 [March 9, 2016 at 11:39 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 why are higher metal layers used for power and ground rails???

 Reply

 Replies

 !

 [March 10, 2016 at 1:39 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 There are lot of reasons but for you ...

 1) these are very close to outside Power Pins.

 2) Metal Width and Thickness are large - So less resistive in nature. So less Voltage Drop , if we will use these For Power and Ground.

 Replies

 Reply

 Reply

17. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[July 9, 2016 at 11:37 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Hey, Can you mention me which book to refer for VLSI basics ( MOS transistor theory ) ? As I see many books in the market but confused to select one.

 Reply

 Replies

 Reply

18. !

 [October 23, 2016 at 2:44 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 plz do fast sir we need more interview questions and answers

 Reply

 Replies

 Reply

19. !

 [October 26, 2016 at 7:39 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Hello sir, if possible can you please update chapter 7 ( VLSI terminology topics as you mentioned in this blog).

 Reply

 Replies

 Reply

20. !

 [December 6, 2016 at 12:17 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 some of the topics are not visible... 1.6b,1.7,chapters-2,4,6,7,8

 Reply

 Replies

 Reply

21. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[March 2, 2017 at 11:09 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Please enable the links for 4th chapter CMOS Basics

 Reply

 Replies

 Reply

22. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[March 25, 2017 at 12:19 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Sir i want to be the verification and design engineer in vlsi field

 plzz enlighten me with the topic and material the i should read for it.

 my mail id is saubhadragautam@gmail.com

 Reply

 Replies

 Reply

23. ![](https://resources.blogblog.com/img/blank.gif)

 [Dolly Harsh](http://traininginnoida.in/best-vlsi-training-in-noida.html)[May 11, 2017 at 10:41 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Well explained about basics of VLSI. Before I have studied VLSI but some of the topics was not clear to me. After reading your post it was all explained.

 Thanks a lot sir.

 Reply

 Replies

 Reply

24. !

 [April 25, 2018 at 5:26 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 sir,

 What is the meaning of 16 in 16 ffc technology? Is the following explanation correct?

 In advanced CMOS technologies, e.g. 32nm, 28 nm, these numbers usually refer to 1/2 the contacted pitch of the DRAM ,(as they are the most compact circuit which can be fabricated out) which is also 1/2 the pitch of the first level of metalization (the closest to the silicon substrate). It is close to the printed gate length of transistors, but not identical(due to overlapping of gate with source and drain region, which further leads to parasitic overlap capacitance).

 Reply

 Replies

 Reply

25. !

 [May 20, 2018 at 3:10 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Hi sir,

 Ur doing a great work please give information regarding missing topics and help the students and professionals

 Reply

 Replies

 Reply

26. !

 [September 16, 2018 at 10:49 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Dear Sir, in your book, please include a topic on the following: difference between latch and flip-flop, and metastability of flip-flops.

 Reply

 Replies

 Reply

27. !

 [March 6, 2019 at 1:14 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 I cant open 1.7 the link is nit available

 Reply

 Replies

 Reply

28. !

 [April 11, 2019 at 10:07 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 very nice explanation...plz help us by posting all missing topics..plz...

 Reply

 Replies

 Reply

29. !

 [May 5, 2019 at 12:29 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Sir .. your explanation was very good... Add missing topics also... Eagerly waiting for

 Reply

 Replies

 Reply

30. !

 [November 30, 2019 at 10:37 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Hi Sir,

 I have completed my btech. ECE in 2010 and have experience in IT industry but not satisfied. Due to family situation I couldn't wait for my dream JOB but I am not satisfied with current role. I would like to move into VLSI and I have good knowledge in C and Digital logic design and linux.. Could you please assist me what to do for getting VLSI job

 Reply

 Replies

 Reply

31. !

 [March 29, 2020 at 1:25 PM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Hi Sir, this is Srijana.

 The info provided is nice.

 Can u please tell me if op-amp plays a role in vlsi

 Reply

 Replies

 Reply

32. !

 [July 2, 2020 at 10:37 AM](https://www.vlsi-expert.com/p/vlsi-basic.html)

 Hi Sir,

 can we find any materials or book related to topics by you

 Reply

 Replies

 Reply

Add comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

Load more...

[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 3. #### 1 comment:

**URL:** https://www.vlsi-expert.com/p/vlsi-industry-fact-and-truth-abo.html
**Date:** Unknown
**Tags:** dft, parasitic

#### 1 comment:

1. !

[December 21, 2016 at 7:12 PM](https://www.vlsi-expert.com/p/vlsi-industry-fact-and-truth-abo.html)

REGARDING Help in Ph.D and my PhD topic is Design of Low Pwer VLSI design for non volatile memory application

\-\-

Best Regards

Gyan Prabhakar

Ph.D. Scholar,

Kamla Nehru Institute of Technology (K.N.I.T.),Sultanpur UP

Dept. of Electronics Engineering

Mob: - 7379314780

gyanprabhakar@gmail.com

Reply

Replies

Reply

Add comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

Load more...

[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 4. #### 8 comments:

**URL:** https://www.vlsi-expert.com/p/video-lectures.html
**Date:** Unknown
**Tags:** sta, dft, parasitic

#### 8 comments:

1. ![](https://resources.blogblog.com/img/blank.gif)

Anonymous[March 9, 2016 at 6:50 AM](https://www.vlsi-expert.com/p/video-lectures.html)

The way of explanation is so good and we want some more videos on STA

Reply

Replies

!

[March 10, 2016 at 1:15 PM](https://www.vlsi-expert.com/p/video-lectures.html)

Those are in pipeline

Replies

Reply

![](https://resources.blogblog.com/img/blank.gif)

Anonymous[March 13, 2016 at 11:01 PM](https://www.vlsi-expert.com/p/video-lectures.html)

thanks boss will be waiting for that

Replies

Reply

Reply

2. !

[April 22, 2017 at 12:11 PM](https://www.vlsi-expert.com/p/video-lectures.html)

your doing a great job. Thanks

Reply

Replies

Reply

3. !

[October 9, 2017 at 8:15 PM](https://www.vlsi-expert.com/p/video-lectures.html)

Sir,

I want some material on Clock Slew,Clock Latency,Clock Jitter,Clock Uncertainty & Clock Sense etc.

Can you please give some information about those ??

Reply

Replies

Reply

4. !

[May 24, 2018 at 12:27 PM](https://www.vlsi-expert.com/p/video-lectures.html)

you are so great, as you are doing great job by sharing your knowledge.

Reply

Replies

Reply

5. !

[May 24, 2018 at 12:29 PM](https://www.vlsi-expert.com/p/video-lectures.html)

you are doing great job by sharing the knowledge.

Reply

Replies

Reply

6. !

[September 15, 2019 at 1:18 AM](https://www.vlsi-expert.com/p/video-lectures.html)

Sir,

I want problems based on static timing analysis with concepts

Reply

Replies

Reply

Add comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

Load more...

[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 5. [Newer ](https://www.vlsi-expert.com/ "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2025-04-23T09:16:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

**URL:** https://www.vlsi-expert.com/2025/
**Date:** 2025-04-23
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/ "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2025-04-23T09:16:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 6. #### No comments:

**URL:** https://www.vlsi-expert.com/2025/04/Pranjal%20Joshi%20story.html
**Date:** 2025-04
**Tags:** dft, parasitic

#### No comments:

#### Post a Comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

[Older Post](https://www.vlsi-expert.com/2024/10/advance-sdc-techniques-part1.html "Older Post")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[Post ()](https://www.vlsi-expert.com/feeds/8263731365141826213/comments/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 7. **Electrons configuration in as per Quantum Mechanics**

**URL:** https://www.vlsi-expert.com/2024/
**Date:** 2024-03-16
**Tags:** physical-design, sta, verification, dft, ESD, parasitic, CMP

## Wednesday, March 20, 2024

### [Semiconductor Physics: Electron Spinning in an ATOM](https://www.vlsi-expert.com/2024/03/semiconductor-physics-electron-spining.html)

## Electron Spinning in an ATOM

We have discussed in our previous article ( [Semiconductor Physics:- Electron Configuration In ](https://www.vlsi-expert.com/2024/03/semiconductor-physics-electron-configuration.html), about the atoms (and analogy) and the basic idea of electron movement. If you remember, we have finished our article just introducing the spining of electrons in 3D dimensions and about the quantum numbers

- **n****\-****principal quantum number**– This is same number as we know orbital no.

- **l****\- azimuthal quantum number** – This is same as we knows,p,d,f

- **m****\-** **magnetic quantum number**.

"Among the three quantum numbers, there is another quantization condition called spin ( _s_) that electrons should fulfill. Every electron has its angular momentum or spin and can be expressed as..."

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjKzP-Y-bEeIbo4TLs_fswL6Qyprm_l-t2-xvkpB1iwSTlJu9XMXeXv3B0ZDJ0uorR7xYvxA1rxrKZOaXFqi8PtBeaOG-TcxWHnpJi5t5CWOGfjJhZxfE38636jAxmo6bbh5LSXoHz3Boe_-ehGKsmsfIkwwfCBQmYKUzu9OYHN1QVuysM1Xk2mTEVs8TY=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEjKzP-Y-bEeIbo4TLs_fswL6Qyprm_l-t2-xvkpB1iwSTlJu9XMXeXv3B0ZDJ0uorR7xYvxA1rxrKZOaXFqi8PtBeaOG-TcxWHnpJi5t5CWOGfjJhZxfE38636jAxmo6bbh5LSXoHz3Boe_-ehGKsmsfIkwwfCBQmYKUzu9OYHN1QVuysM1Xk2mTEVs8TY)

Before going through the periodic table, there is the Pauli exclusion principle which stated that no two electrons have the same quantum numbers (_n_, _l_, _m_, and_s_). In other words, two electrons may have the same quantum number n, l, and m states but the spin states must be +1/2 and -1/2.

The configuration of electrons in different energy states is summarized in Table 1.

**Table** **1** The allowed energy states and the occupation of maximum number of electrons according to quantum rules.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYgeEOiAj5OBAaeLes832fToR4wLesnDMSh2Y08M_Q2sSjeNKQQHIle7gYxmPbthwdVjTxQrw7daFuqCaln0OE2tct2RZlrYu9RGbhqctnv4OrEC2DnLlH7oDdh3NafGhSoXkFJaEme8WzluOC9-y4daKj02DhucfKlynjRqKvyDMvq7Iqi7TlUJTIdRE/s16000/table.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYgeEOiAj5OBAaeLes832fToR4wLesnDMSh2Y08M_Q2sSjeNKQQHIle7gYxmPbthwdVjTxQrw7daFuqCaln0OE2tct2RZlrYu9RGbhqctnv4OrEC2DnLlH7oDdh3NafGhSoXkFJaEme8WzluOC9-y4daKj02DhucfKlynjRqKvyDMvq7Iqi7TlUJTIdRE/s849/table.PNG)

As an example, for the 3rd electronic orbit (n=3), l should be 0, 1, and 2 followed by equation 14. Similarly, m should be -l to +l including zero for each l value. Electrons can occupy each m value with a spin +/-1/2.

The different notations for different l values are used to express the electronic configuration

**_l_ = 0,1,2,3,4,5 .......**

_**l = s, p, d, f, g, h, .....**_

The electron state can be represented as

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiALntvTIivAJFaUZwFec8FgR2EwZQYboVCiqf1PyrG5q-q4YcH9xWAELw1oel4otdl25aqNqF8vUw84rz_Cb0G4oK54g5rDBJqJ5WsmgK7d86Efn-YbrDVynJVBvJ8S_n-CJqDYv8tTNSeCOeSQu3kytILNYfTAoh_Lxi5BQqvqHmJ60qsbnyXx29sfqw=w400-h159)](https://blogger.googleusercontent.com/img/a/AVvXsEiALntvTIivAJFaUZwFec8FgR2EwZQYboVCiqf1PyrG5q-q4YcH9xWAELw1oel4otdl25aqNqF8vUw84rz_Cb0G4oK54g5rDBJqJ5WsmgK7d86Efn-YbrDVynJVBvJ8S_n-CJqDYv8tTNSeCOeSQu3kytILNYfTAoh_Lxi5BQqvqHmJ60qsbnyXx29sfqw)

I think now you are able to understand whole electron configuration which you have studied in your college days. Let’s talk about few more examples, so that you can be familiar with Semiconductor and Physics very well.

For example, Si (ic No=14) and Ge (ic No= 32), the electronic configuration is

Si         1_s_22_s_22_p_63_s_23_p_2

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhXPcsjC8aRYYQlkgSSyamtNAdVHU3RRO3mg1FsWCZKhuTnqmuRk_zEpXtfUD-j9jeRWlYUWwHe82EUJ7YA3WpFw061LKMrT3VqCzWmXGl-o9ykAy-1b7U0_ljdAL9fRYJydBGix0ABTBkDP4f_3xnD96oZhFXef4ln7j3L45WLmE1JA7jrRPqeiFENrbw=w400-h355)](https://blogger.googleusercontent.com/img/a/AVvXsEhXPcsjC8aRYYQlkgSSyamtNAdVHU3RRO3mg1FsWCZKhuTnqmuRk_zEpXtfUD-j9jeRWlYUWwHe82EUJ7YA3WpFw061LKMrT3VqCzWmXGl-o9ykAy-1b7U0_ljdAL9fRYJydBGix0ABTBkDP4f_3xnD96oZhFXef4ln7j3L45WLmE1JA7jrRPqeiFENrbw)

**Figure** **5** Electronic configuration of Silicon

Ge1_s_22_s_22_p_63_s_23_p_64_s_23_d_104_p_2

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgOnA8YpVIzsuNDNKFpB7_E1J8wStUZ2RE-NKW9ij_Qf8X0O9pOnJVuG1wZ0jS8RAIQigf5eAUO9Yq_3OGtgjDx9KU1Q4XgpcIj504tNAehkxLcN-mJ7Jv6ZzBbTkb8qfVc1saJCT29BZg0ljLCLgAzEfLys556WUrKeR_KuUTGAwlWrYfWBdLPfUKNf7Y=w400-h261)](https://blogger.googleusercontent.com/img/a/AVvXsEgOnA8YpVIzsuNDNKFpB7_E1J8wStUZ2RE-NKW9ij_Qf8X0O9pOnJVuG1wZ0jS8RAIQigf5eAUO9Yq_3OGtgjDx9KU1Q4XgpcIj504tNAehkxLcN-mJ7Jv6ZzBbTkb8qfVc1saJCT29BZg0ljLCLgAzEfLys556WUrKeR_KuUTGAwlWrYfWBdLPfUKNf7Y)

**Figure** **6** Electronic configuration of germanium

The electronic arrangements are shown in figure1

[![Electronic Configuation](https://blogger.googleusercontent.com/img/a/AVvXsEhMGSuUbY-0Ef9a836hVHDyWcBbLxQ808Almb-CQkDkqO7Ktz5Ew9RRoGm6MtFLg9fF7FqjMHzuIdKk6ilDUlpGRBWWZO6zmhScH7o-aECV1YW1xCZMeA2Uvm82I9E0RSITQ8WMfBGuqnhP7KnnjyxPFCcykwiiFXd4G9nNry-1fy2_8N_4zQWn5sC90Bo=w640-h444)](https://blogger.googleusercontent.com/img/a/AVvXsEhMGSuUbY-0Ef9a836hVHDyWcBbLxQ808Almb-CQkDkqO7Ktz5Ew9RRoGm6MtFLg9fF7FqjMHzuIdKk6ilDUlpGRBWWZO6zmhScH7o-aECV1YW1xCZMeA2Uvm82I9E0RSITQ8WMfBGuqnhP7KnnjyxPFCcykwiiFXd4G9nNry-1fy2_8N_4zQWn5sC90Bo)

**Figure** **7** Electron’s configuration rule

In the next article, we will discuss the different type of bonding between the ATOMS and the formation of energy bands which will help us to understand the Semiconductor Physics more deeply and later semiconductor Devices like PN Diode, MOSFETs and all.

**By -**

**First Author - Dr. Bhaskar Patnayak**

**Second Author (Editor) - Mr. Puneet Mittal**

Posted by
VLSI Expert
at
[5:58 PM](https://www.vlsi-expert.com/2024/03/semiconductor-physics-electron-spining.html "")[0\\
comments](https://www.vlsi-expert.com/2024/03/semiconductor-physics-electron-spining.html#)

## Saturday, March 16, 2024

### [Semiconductor Physics:- Electrons configuration in ](https://www.vlsi-expert.com/2024/03/semiconductor-physics-electron-configuration.html)

# **Electrons configuration in as per Quantum Mechanics**

To understand the movement of electrons in a semiconductor device, we need to understand the electronic configuration of an atom and how it interacts with the crystal lattice. We already know that atom consists of Neutrons (neutral charge) and Protons (positive charge) inside a nucleus &  Electrons (negative charge) revolved around the nucleus (Figure 1).

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjeN99IrqO2RyTytvabXirN6wyCt0rJZqA_dtDj2M8qP7A7v_xp6TGsG60rWRovLATmwgPyi1bjcwLwRlbizLhJQoyYozR_MJB5sCQNPBofZh3ViAeqSRSDh9gRXCruxCdUnQZMo2sHZXuV24r8D3DiKHKM55kKn6pihU3-uitAJkrC05if9CJwXxA7rzc=s320)](https://blogger.googleusercontent.com/img/a/AVvXsEjeN99IrqO2RyTytvabXirN6wyCt0rJZqA_dtDj2M8qP7A7v_xp6TGsG60rWRovLATmwgPyi1bjcwLwRlbizLhJQoyYozR_MJB5sCQNPBofZh3ViAeqSRSDh9gRXCruxCdUnQZMo2sHZXuV24r8D3DiKHKM55kKn6pihU3-uitAJkrC05if9CJwXxA7rzc)

**Figure** **1** ic structure

**Note**: (Just for your information) If you remember in the intermediate level or BTech 1st year, we have studied in quantum mechanics that these electrons are restricted to certain energy levels (quantized). In this regard, Plank’s blackbody radiation and Einstein’s photoelectric effect established the discrete nature of light (quantization). In the late 1920s, quantum mechanics had developed in which Heisenberg developed matrix mechanics and Schrödinger developed wave mechanics at the same time. Although the mathematical formulations are quite different, the basic principles are identical.

Although The Schrödinger equation describes the interaction between particles(e.g. electrons) and potential field, it’s enormously difficult to solve the Schrödinger equation in the case of complicated atoms (ic number greater than 1 or you can say the total no. of electrons in a neutral atom). Therefore, the solution of the hydrogen atom (atomic number 1) is significant to understand the permissible energy states for electron arrangements.

It is well known that a hydrogen atom consists of a single electron and a proton system. We can call this system a two-particle system. In some circumstances, the two-particle system's motion can be described as the motion of a single particle with respect to a **center of mass**. The mass of the particle is referred to as a reduced mass with respect to the center of the mass system. In this consideration, we’ll assume that the electron is relatively moved around the proton, and the proton is located at the center (in this case at the origin). **Since protons have higher mass with respect to the electron, therefore we will consider the reduced mass is equal to the electron mass, and the proton is located at the origin.**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj94tQrbr8fDKTRrN4P1rNdifc5JxcYPuD7crvYWKyLC69mutJk0tyJmDvlJ_AhZOh2kAYO5MDaTC1dlK8WgwO6TEmbQaUUVncapuFHcbVS91nh5oWCM7WtWb7hOMOAgi5KBSmK5y1P5jAG0_cyFX45EY-b3Ouk-QNXc_6IX73D2ucUVL_fdXuQfA9kxAE=s320)](https://blogger.googleusercontent.com/img/a/AVvXsEj94tQrbr8fDKTRrN4P1rNdifc5JxcYPuD7crvYWKyLC69mutJk0tyJmDvlJ_AhZOh2kAYO5MDaTC1dlK8WgwO6TEmbQaUUVncapuFHcbVS91nh5oWCM7WtWb7hOMOAgi5KBSmK5y1P5jAG0_cyFX45EY-b3Ouk-QNXc_6IX73D2ucUVL_fdXuQfA9kxAE)

**Figure** **2** (a) Center of mass concept. (b) Position of an electron with respect to proton (Origin)

Note: - I know you may be thinking what is this. Why are we assuming so many things and nothing is fixed? Basially, in an atom when we say that Proton is in center, then its important to understand which center are we talking about!

_Let me explain you in my ( **Puneet's way**) and you try to visualise it. (People or scientist may not like it but at least you can understand it. From analogy point of view you can consider it's a cloud system. When we see a cloud can we say that it's a 1 cloud of this size, this is the boundry and this is center of cloud. but still we see that whole piece of cloud moving together and merging with other piece of cloud and they have center also and outer periphery also. So this ATOM structure is like that. Now, Try to understand._

- _A Cloud system having more denser at the center (which is also moving) or say that become center of whole cloud ( **center of the mass system**)._
- _This cloud portion which is present in the center we are saying it's Proton._
- _Rest of the portion of cloud, you can say it's electron. (remember this I am trying to explain you for Hydrogen atom)_
- _Now, you can say that if these are 2 things, can we separate out but that's not going to happen or I say if it will separate out then whole system collapse, so I (scientist) said that both are related to each other (one as positive and other as negative). if you seperate out these 2, whole cloud system collapse. So, when these 2 are together then we say it's an ATOM._
- _But still outer part of Cloud can be separate out from Center part and someother part can come and replace it. So, with respect to center part, outer part (electron) is tied with center part (proton)._

_Now, Read once again the above one and then below one. You will get more clearity._

The electrons and nucleus (especially protons) are interacted with by the Coulombic potential

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi4a8goBhoxHoDTJCYNjwHez3v4qYpT6S2cYHoAZMWx4D6YNJ5OET18rLCsuYUgdIEP-axM7kP_mYJpG84AiNtjfoWjTkjbOwcf5UetCsydZYMxcMpMZlMzRhCJfqptJ7nu28siRHlBH3__GCsJm0wZNxU73uPQxOgeXjMtz5N0ET3_KaltCDLNk_f3dW0=w606-h310)](https://blogger.googleusercontent.com/img/a/AVvXsEi4a8goBhoxHoDTJCYNjwHez3v4qYpT6S2cYHoAZMWx4D6YNJ5OET18rLCsuYUgdIEP-axM7kP_mYJpG84AiNtjfoWjTkjbOwcf5UetCsydZYMxcMpMZlMzRhCJfqptJ7nu28siRHlBH3__GCsJm0wZNxU73uPQxOgeXjMtz5N0ET3_KaltCDLNk_f3dW0)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh7HZjFggDj_XtgoN09jYmBXV-wkAS2zEfPX6s3nnSp9FmODG7y4yryk2U5F3Bg-EOx5TGTcNJIniIO3RUa2mmIioXjvx7H0cZ-Dfxr6vkI7S5sYGPhid55LHiCfwmbqrMYRpiouI5DFu8pEFdMp0C2WhgtAP34fQOd7pSFwV-JnoPoww86nWrsVNDpxl8=s320)](https://blogger.googleusercontent.com/img/a/AVvXsEh7HZjFggDj_XtgoN09jYmBXV-wkAS2zEfPX6s3nnSp9FmODG7y4yryk2U5F3Bg-EOx5TGTcNJIniIO3RUa2mmIioXjvx7H0cZ-Dfxr6vkI7S5sYGPhid55LHiCfwmbqrMYRpiouI5DFu8pEFdMp0C2WhgtAP34fQOd7pSFwV-JnoPoww86nWrsVNDpxl8)

**Figure** **3** Spherical polar co-ordinate system

Let’s try to understand a few key points/equations of Quantum mechanics. If you are interested, you can go into detail by referring to the standard textbooks. Here we are just capturing for reference purposes.

**Note**:\- If you want to skip, go to equation no 11 directly but I will recommend to read it once.

Assume that the potential distribution is spherically symmetric, a time-independent three-dimensional Schrödinger equation in spherical coordinates can be written as

[![](https://blogger.googleusercontent.com/img/a/AVvXsEidZ2N7Vx6ZRP7CNkUk78JRi_bJ8LlVquHZusqzq2S_2DsfPpaBhDDHqqedRKUfs2jp18O9gGj7kiX1eXvCH_B39XOf2MeuKMd_5glSdwGds4XPYjX2rQedXCISgduI9rQXfx4moXQETKTecEGDActOI4TVW06ZvCmfwd2DmnsbIJLwLke5G4UxiaHO5BQ=w687-h460)](https://blogger.googleusercontent.com/img/a/AVvXsEidZ2N7Vx6ZRP7CNkUk78JRi_bJ8LlVquHZusqzq2S_2DsfPpaBhDDHqqedRKUfs2jp18O9gGj7kiX1eXvCH_B39XOf2MeuKMd_5glSdwGds4XPYjX2rQedXCISgduI9rQXfx4moXQETKTecEGDActOI4TVW06ZvCmfwd2DmnsbIJLwLke5G4UxiaHO5BQ)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhrPJ4ag_C4w8jd4FzjR73o8nkn8LPk4BRfkjtOOGHKWbT-N9dMdBrMO0SKf_FBGyW6vfBljJnALNMjcmiENhrEaD3qq5FxAyZSYr3SAJVaUZhGOUkQ65UY77gOUQRFT3qWCozwFCF3XWxNMkEdXUedfdRWR3AYfucz2ZqxBVh1fEK5usPwW-_jSrq9Zsk=w679-h569)](https://blogger.googleusercontent.com/img/a/AVvXsEhrPJ4ag_C4w8jd4FzjR73o8nkn8LPk4BRfkjtOOGHKWbT-N9dMdBrMO0SKf_FBGyW6vfBljJnALNMjcmiENhrEaD3qq5FxAyZSYr3SAJVaUZhGOUkQ65UY77gOUQRFT3qWCozwFCF3XWxNMkEdXUedfdRWR3AYfucz2ZqxBVh1fEK5usPwW-_jSrq9Zsk)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgzuyJcYjEDoKI4w5G27-Yu-pxkGSbY-14nU-kwW2eFHLEn80w6hlvltVvi2Ktl6REzR5DLIvTIlvB70Kgn96limUZ9JKcrzcmcUk6N6EznxGrdjAr1uUa5_dVW2GOVZV9MRwwo2o19Uu7S5FApNI-JeSKh4bFXGH5UrXKKAXQvnWuA5YpZ5iZCfhiYDX8=w694-h447)](https://blogger.googleusercontent.com/img/a/AVvXsEgzuyJcYjEDoKI4w5G27-Yu-pxkGSbY-14nU-kwW2eFHLEn80w6hlvltVvi2Ktl6REzR5DLIvTIlvB70Kgn96limUZ9JKcrzcmcUk6N6EznxGrdjAr1uUa5_dVW2GOVZV9MRwwo2o19Uu7S5FApNI-JeSKh4bFXGH5UrXKKAXQvnWuA5YpZ5iZCfhiYDX8)

Note:- Hold ON - If you are thinking about so many equations - It's okay. All these are important (may be not today but it will be one day). I will explain you. Just read it once.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi0ARFut5x8XqZPl6opUHkyKOOm4fYkqQ4d0KjuKTskTxFeK50bATKXpxFkDkezguTHuAiPTxMr_fAG1kcDeIDatzUak5TCRV359eC8K0MFOqFGgZ0As4FidaCvFN-S5I_A-uKafyibN4mAf_AHDtKQzT-4zJVX9V-dCW8PgUccqC8tu9ysx9HPYpsFA84=w670-h543)](https://blogger.googleusercontent.com/img/a/AVvXsEi0ARFut5x8XqZPl6opUHkyKOOm4fYkqQ4d0KjuKTskTxFeK50bATKXpxFkDkezguTHuAiPTxMr_fAG1kcDeIDatzUak5TCRV359eC8K0MFOqFGgZ0As4FidaCvFN-S5I_A-uKafyibN4mAf_AHDtKQzT-4zJVX9V-dCW8PgUccqC8tu9ysx9HPYpsFA84)

The negative expression specifies that the electrons are bound with the nucleus and the energy is quantized. It should be noted that the value of n should not be zero as the energy expression become invalid. Therefore, n should be an integer.

**Note:- Puneet's Way: -**

When Scientist studied it further they come to know the cloud is not in 2D and presence of outer area of cloud has some pattern in 3D (Dimensional). Also they figured out that outer surface have some motion and usually this motion is around the inner surface (neculus system - dense part) and this moment is not in X, Y, Z direction only but it's in angular form also. Remember - Whole Cloud system is moving but we are talking about the relative motion of outer cloud with respect to inner cloud (mass). and that's the reason of "Spherical polar co-ordinate system" come into the picture to correctly captured this whole system.

Among the three quantum numbers, there is another quantization condition called spin ( _s_) that electrons should fulfill. Every electron has its angular momentum or spin and can be expressed as

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjKzP-Y-bEeIbo4TLs_fswL6Qyprm_l-t2-xvkpB1iwSTlJu9XMXeXv3B0ZDJ0uorR7xYvxA1rxrKZOaXFqi8PtBeaOG-TcxWHnpJi5t5CWOGfjJhZxfE38636jAxmo6bbh5LSXoHz3Boe_-ehGKsmsfIkwwfCBQmYKUzu9OYHN1QVuysM1Xk2mTEVs8TY=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEjKzP-Y-bEeIbo4TLs_fswL6Qyprm_l-t2-xvkpB1iwSTlJu9XMXeXv3B0ZDJ0uorR7xYvxA1rxrKZOaXFqi8PtBeaOG-TcxWHnpJi5t5CWOGfjJhZxfE38636jAxmo6bbh5LSXoHz3Boe_-ehGKsmsfIkwwfCBQmYKUzu9OYHN1QVuysM1Xk2mTEVs8TY)

So, you might be thinking why all this??

I will say, have patience and we will explain all this to you in coming articles. This is an intro article. This will help you to understand the moment of electrons in the other orbits (also in outer most orbit, which is very important to understand as we always talk about Valency electron and Valence Band).

**By -**

**First Author - Dr. Bhaskar Patnayak**

**Second Author (Editor) - Mr. Puneet Mittal**

Posted by
VLSI Expert
at
[4:39 PM](https://www.vlsi-expert.com/2024/03/semiconductor-physics-electron-configuration.html "")[0\\
comments](https://www.vlsi-expert.com/2024/03/semiconductor-physics-electron-configuration.html#)

[Newer ](https://www.vlsi-expert.com/ "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2024-03-16T16:39:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 8. ## Wednesday, December 15, 2021

**URL:** https://www.vlsi-expert.com/2021/12/
**Date:** 2021-12
**Tags:** sta, digital-design, verification, dft, ESD, CMOS, parasitic, analog

## Wednesday, December 15, 2021

### [LTSPICE Based Self-Practice Questions](https://www.vlsi-expert.com/2021/12/www.vlsi-expert.com/ltspice-simulation-question.html)

We have seen a lot of students facing problems while working on several basic concepts. To understand those concepts, it's very much required to do some testing and simulation and assess yourself how much you are able to grasp the concepts.

Below are few questions which you can try over LTSPICE yourself and understand the different design concpets. It will help you in VLSI Industry, the real simulation based concepts.

Please try to solve these questions yourself.

Q1) Design the circuit which is provided with the input Vin as shown in left figure and output is obtained as Vout as shown in the right figure

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjv4pFbzaADrR6Eura7J27VYWdgE5w0OXPzsYoohKMOBEvXSz_J8_lQSDgqJqiX-KfDm-matisQ67fuMpRZxXbS8bARj6XAHn0-k_F4AAHZ0f3OlfkkwTkgir_rN2KwdPB36mx7RMIqisb2tZf9fjtXOZ2O95Lb7X6Af35Iwm642r0vQkJzeRPm5gE7=s600)](https://blogger.googleusercontent.com/img/a/AVvXsEjv4pFbzaADrR6Eura7J27VYWdgE5w0OXPzsYoohKMOBEvXSz_J8_lQSDgqJqiX-KfDm-matisQ67fuMpRZxXbS8bARj6XAHn0-k_F4AAHZ0f3OlfkkwTkgir_rN2KwdPB36mx7RMIqisb2tZf9fjtXOZ2O95Lb7X6Af35Iwm642r0vQkJzeRPm5gE7=s938)

Q2) For the circuit shown below which one is better Explain and support your answer with LTSPICE Simulation

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgumw2DBR5P9AcnYPz-OL_MgNyNG3_4mi_SMGKyMeekLnDII2hnPM-JJEGmVFvnZps5-_qyfgcP-v8aYo7k3hd64rLkSzd6Qh6AiqBVcVC5epV4cyMkihAiIs3-CJvxeZFEMCxY_RaTXVQky_d95I9kQHp-5_0zOVetv5l4BrhGOkI682RzahkKBNdF=s600)](https://blogger.googleusercontent.com/img/a/AVvXsEgumw2DBR5P9AcnYPz-OL_MgNyNG3_4mi_SMGKyMeekLnDII2hnPM-JJEGmVFvnZps5-_qyfgcP-v8aYo7k3hd64rLkSzd6Qh6AiqBVcVC5epV4cyMkihAiIs3-CJvxeZFEMCxY_RaTXVQky_d95I9kQHp-5_0zOVetv5l4BrhGOkI682RzahkKBNdF=s823)

Q3) For the given netlist generate the schematic on LTSPICE. What kind of analysis is being done here

VIN 1 7 AC 0V

IST 0 10 AC 1MA

VX   10 6 DC 0V

VDD 8 0   15V

RS    1  2    250

C1    2  3    IUF

R1    8  3    1.4MEG

R2    3  0   1MEG

RD    8  4     15K

RS1   5  9     100

RS2   9  0      15K

CS     9  0       20UF

C2    4   6       0.1UF

R3    6   7      15K

R4    7   0      5K

M1  4   3    5   5 MQ

.MODEL MQ NMOS (VTO=1 KP =6.5E-3  CBD=5PF

+RG =0 RDS =1MEG CGSO=1PF CGDO=1PF CGBO=1PF)

.AC DEC 10 10HZ 10MEGHZ

.PROBE

.END

Q4) Design a circuit for the given input and output waveform given below and after designing it draw the schematic on LTSPICE and verify that the circuit indeed generate the waveform given in here

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjY83Ivejlo_Md4LDyR3N_E23vnpwuWkNpSopjMTJvhbLg56a1tDSwMXBBCWGRWtvYESC8byVmSXn6_wZypo2AJjeBlPWqqQjy5qfpDKqAFR8vlms0bJNn1M4rzlAyJZxrxJHGUTZzH6XlraRoWYh4JxrOCnokIgWVLXmxHh2_mAHWYUrZPUYCgpI6G=s600)](https://blogger.googleusercontent.com/img/a/AVvXsEjY83Ivejlo_Md4LDyR3N_E23vnpwuWkNpSopjMTJvhbLg56a1tDSwMXBBCWGRWtvYESC8byVmSXn6_wZypo2AJjeBlPWqqQjy5qfpDKqAFR8vlms0bJNn1M4rzlAyJZxrxJHGUTZzH6XlraRoWYh4JxrOCnokIgWVLXmxHh2_mAHWYUrZPUYCgpI6G=s631)

Q5) Explain what is wrong in the Model statements given below

1)

.MODEL MQ NMOS (VTO=1 KP =6.5E-3 CBD=5PF

+RG =0 RDS =1MEG CGSO=1PF CGDO=1PF CGBO=1PF)

R1    4  3  5  5   MQ

2)

.MODEL QNP NPN (BF =50 RB=70 RC =40 TF =0.1NS TR =10NS VJC=0.85)

M1    4  3  2  QNP

3)

.MODEL DIODE D (RS =40 TT =0.1NS)

Q1    4  5  DIODE

Q6) For the Circuit shown below:

1. Shown the voltage across the Resistor R3 and R4
2. Find the Voltage VA ,VB,VC
3. Also Justify the value using LTSPICE Simulation

[![](https://blogger.googleusercontent.com/img/a/AVvXsEic9rLQ-ruqyk-buHaoreRv4rjtHQwXWiR86K5ZA3yQiZjap_U7Z61gduBdmnoALxviUpwNZgC5Rh5ZWRN-lDTyQk_Ilc3y2SluPu-f7bQbFKmB1EbR3NbxT8ndAS_nWDARYyyQ1t6BKY8mWFcpD6hon4uWQ1yYr0HTpkE2wQ3TEBMP4vHRpeAFcQTF=s600)](https://blogger.googleusercontent.com/img/a/AVvXsEic9rLQ-ruqyk-buHaoreRv4rjtHQwXWiR86K5ZA3yQiZjap_U7Z61gduBdmnoALxviUpwNZgC5Rh5ZWRN-lDTyQk_Ilc3y2SluPu-f7bQbFKmB1EbR3NbxT8ndAS_nWDARYyyQ1t6BKY8mWFcpD6hon4uWQ1yYr0HTpkE2wQ3TEBMP4vHRpeAFcQTF=s453)

Q7) For the circuit shown below write the netlist also you need to include the model used for MOSFET and Resistor

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhUM_3keWS1bOjHMhSvQ84vPyI7VDDqo_XAKjrxo1oKiIWjyZYmz9ffBgJabDZa3FG-shFt_Bi9x_LTDZWoDXuGpG7C7h4OJPJ1irV4z7N0ajWgL9VASMw6VkooPUgME9icu7Wiz2COXy8fIEj76UlG18eEX0UBtUOugO3_2QhjLYsk3i7fWk6jlH6I=s600)](https://blogger.googleusercontent.com/img/a/AVvXsEhUM_3keWS1bOjHMhSvQ84vPyI7VDDqo_XAKjrxo1oKiIWjyZYmz9ffBgJabDZa3FG-shFt_Bi9x_LTDZWoDXuGpG7C7h4OJPJ1irV4z7N0ajWgL9VASMw6VkooPUgME9icu7Wiz2COXy8fIEj76UlG18eEX0UBtUOugO3_2QhjLYsk3i7fWk6jlH6I=s439)

**-Prepared By Niti Gupta**

**(Director of eLearning and university Program)**

**(VLSI Expert Private Limited)**

**-Supervised By Puneet Mittal**

**(Founder & Director)**

**(VLSI Expert Private Limited)**

**Posted by**
**VLSI Expert**
**at**
**[6:28 PM](https://www.vlsi-expert.com/2022/01/ltspice-simulation-question.html "")[0\**\
**comments](https://www.vlsi-expert.com/2022/01/ltspice-simulation-question.html#)**

** **

**[Newer ](https://www.vlsi-expert.com/search?updated-max=2022-01-20T18:01:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2021-12-15T18:28:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)**

**Subscribe to:**
**[ ()](https://www.vlsi-expert.com/feeds/posts/default)**

**## Must Read Article**

**[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)**

**## Search This Blog**

**| | |**
**| --- | --- |**
**| | |**

**## VLSI Basics**

**- [Index](http://www.vlsi-expert.com/p/vlsi-basic.html)**
**- [Chapter 1: Digital Background](http://www.vlsi-expert.com/2013/12/digital-basic-number-system.html)**
**- [Chapter 2: Semiconductor background](http:)**
**- [Chapter 3: CMOS Processing](http://www.vlsi-expert.com/2014/09/fabrication-steps-cmos-processing-part-1.html)**
**- [Chapter 4: CMOS Basics](http:)**
**- [Chapter 5: CMOS Layout Design](http://www.vlsi-expert.com/2014/11/cmos-layout-design.html)**

**## Featured Post**

**### [10 ](https://www.vlsi-expert.com/2019/10/10-employee-awards-to-boost-morale.html)**

**Employees function as the backbone of any company and making sure that employee satisfaction is at its highest is incredibly important ...**

**Facebook**

**![Vlsi expert's photo.](https://scontent-ord5-2.xx.fbcdn.net/v/t39.30808-6/326495735_738174084319586_5864415474294797899_n.png?stp=dst-png_p130x130&_nc_cat=103&ccb=1-7&_nc_sid=4cb600&_nc_ohc=AthFkYqGYvoQ7kNvwGCYsey&_nc_oc=AdloHHus4Tp5WmnfSqNgJURY2Z_Gpqx37rQCbzsZwydZjnyAG0DrOkJFGJ6Wsg1fe4M&_nc_zt=23&_nc_ht=scontent-ord5-2.xx&edm=ADwHzz8EAAAA&_nc_gid=DNSDItjTG_rT5-T-zb81ug&oh=00_AfViVjbE8j-6B6yuJrBYaHMayxHVp84JdGkUtfBFPI6axw&oe=68B13B1D)**

**[![](https://scontent-ord5-2.xx.fbcdn.net/v/t39.30808-1/327198556_6132062116824972_7406100806473356299_n.png?stp=c8.0.163.163a_cp0_dst-png_s50x50&_nc_cat=105&ccb=1-7&_nc_sid=f907e8&_nc_ohc=80cYKW0lZfYQ7kNvwF-lcD0&_nc_oc=AdnN68WOk9wb2h4oB3KkPEL1ur7tafhh11xgHqqPFjd0w7nzHJFCFn2qKgW4es4IfSg&_nc_zt=24&_nc_ht=scontent-ord5-2.xx&edm=ADwHzz8EAAAA&_nc_gid=DNSDItjTG_rT5-T-zb81ug&oh=00_AfV71lFxzH7-_UrwlzjYx-XdV6PqoNYsKUJJYblFAseqDw&oe=68B162D2)](https://www.facebook.com/215436858491914?ref=embed_page)**

**[Vlsi expert](https://www.facebook.com/215436858491914?ref=embed_page "Vlsi expert")**

**[Follow Page](https://www.facebook.com/215436858491914?ref=embed_page "") [Followed](https://www.facebook.com/215436858491914?ref=embed_page "")**

**6.5K followers**

**## Videos**

**VLSI Expert Overview - YouTube**

**[Photo image of VLSI EXPERT (vlsi EG)](https://www.youtube.com/channel/UCT_5b65-UOeeb5tIdlH2x6A?embeds_referring_euri=https%3A%2F%2Fwww.vlsi-expert.com%2F)**

**VLSI EXPERT (vlsi EG)**

**15.6K subscribers**

**[VLSI Expert Overview](https://www.youtube.com/watch?v=oRF80Wa_97Y)**

**VLSI EXPERT (vlsi EG)**

**Search**

**Info**

**Shopping**

**Tap to unmute**

**If playback doesn't begin shortly, try restarting your device.**

**Share**

**Include playlist**

**An error occurred while retrieving sharing information. Please try again later.**

**Watch later**

**Share**

**Copy link**

**0:00**

**/**
**•Live**

**•**

**| | |**
**| --- | --- |**
**| ## Total Pageviews<br>[![Follow vlsi_expert on Twitter](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sgf59vdVRwLOu6gn1QRruYSeHKRe1pm1KMqddndcpZ8otgf8wzBfIOmN8pOE6-nTiEUxUD-e15chiipAwwgT-yNM_ndJIJVcfiEohozVNAxMgJ8DQ4mheLC39s=s0-d)](http://www.twitter.com/vlsi_expert)<br>## Popular <br>- ["Timing Paths" : Static Timing Analysis (STA) basic (Part 1)](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html)<br>- [Basic of Timing Analysis in Physical Design](https://www.vlsi-expert.com/2011/02/timing-analysis-basis-what-and-why.html)<br>- ["Examples Of Setup and Hold time" : Static Timing Analysis (STA) basic (Part 3c)](https://www.vlsi-expert.com/2011/05/example-of-setup-and-hold-time-static.html)<br>- ["Setup and Hold Time" : Static Timing Analysis (STA) basic (Part 3a)](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3a.html)<br>- ["Setup and Hold Time Violation" : Static Timing Analysis (STA) basic (Part 3b)](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html)<br>- [10 Ways to fix SETUP and HOLD violation: Static Timing Analysis (STA) Basic (Part-8)](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html)<br>- [Delay - "Wire Load Model" : Static Timing Analysis (STA) basic (Part 4c)](https://www.vlsi-expert.com/2012/03/delay-wire-load-model-static-timing.html)<br>- ["Time Borrowing" : Static Timing Analysis (STA) basic (Part 2)](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html)<br>- [Delay - "Interconnect Delay Models" : Static Timing Analysis (STA) basic (Part 4b)](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html)<br>- [Maximum Clock Frequency : Static Timing Analysis (STA) basic (Part 5b)](https://www.vlsi-expert.com/2012/09/maximum-clock-frequency-static-timing_30.html)<br>## EDN Feed<br>- [Macro models let engineers simulate circuits and systems](https://www.edn.com/design/integrated-circuit-design/4462479/Macro-models-let-engineers-simulate-circuits-and-systems) - <br>- [Reduced pin count DRAM helps IC and system designers reduce SWaP-C](https://www.edn.com/design/integrated-circuit-design/4461632/Reduced-pin-count-DRAM-helps-IC-and-system-designers-reduce-SWaP-C) - <br>- [Resistance scaling fixes miscorrelation between PNR and signoff STA](https://www.edn.com/design/integrated-circuit-design/4458222/Resistance-scaling-fixes-miscorrelation-between-PNR-and-signoff-STA) - <br>- [Hardware-assisted verification, from its dawn to SystemVerilog, UVM, and \<br>transactors](https://www.edn.com/design/integrated-circuit-design/4458133/Hardware-assisted-verification--from-its-dawn-to-SystemVerilog--UVM--and-transactors) - <br>- [Torture-testing your new SoC’s security quotient](https://www.edn.com/design/integrated-circuit-design/4457678/Torture-testing-your-new-SoC-s-security-quotient) - | ## Blog Archive<br>- ► <br> <br>[2025](https://www.vlsi-expert.com/2025/)(1) - ► <br> <br> [April](https://www.vlsi-expert.com/2025/04/)(1)<br>- ► <br> <br>[2024](https://www.vlsi-expert.com/2024/)(3)<br> <br> - ► <br> <br> [October](https://www.vlsi-expert.com/2024/10/)(1)<br> - ► <br> <br> [March](https://www.vlsi-expert.com/2024/03/)(2)<br>- ► <br> <br>[2022](https://www.vlsi-expert.com/2022/)(6)<br> <br> - ► <br> <br> [February](https://www.vlsi-expert.com/2022/02/)(1)<br> - ► <br> <br> [January](https://www.vlsi-expert.com/2022/01/)(5)<br>- ▼ <br> <br>[2021](https://www.vlsi-expert.com/2021/)(5)<br> <br> - ▼ <br> <br> [December](https://www.vlsi-expert.com/2021/12/)(2) - [TCL Practice Task S2\_1 (Scripting Language)](https://www.vlsi-expert.com/2021/12/tcl-practice-task-5.html)<br> - [LTSPICE Based Self-Practice Questions](https://www.vlsi-expert.com/2022/01/ltspice-simulation-question.html)<br> - ► <br> <br> [June](https://www.vlsi-expert.com/2021/06/)(1)<br> - ► <br> <br> [May](https://www.vlsi-expert.com/2021/05/)(1)<br> - ► <br> <br> [April](https://www.vlsi-expert.com/2021/04/)(1)<br>- ► <br> <br>[2019](https://www.vlsi-expert.com/2019/)(9)<br> <br> - ► <br> <br> [December](https://www.vlsi-expert.com/2019/12/)(3)<br> - ► <br> <br> [November](https://www.vlsi-expert.com/2019/11/)(2)<br> - ► <br> <br> [October](https://www.vlsi-expert.com/2019/10/)(1)<br> - ► <br> <br> [September](https://www.vlsi-expert.com/2019/09/)(1)<br> - ► <br> <br> [May](https://www.vlsi-expert.com/2019/05/)(2)<br>- ► <br> <br>[2018](https://www.vlsi-expert.com/2018/)(9)<br> <br> - ► <br> <br> [November](https://www.vlsi-expert.com/2018/11/)(4)<br> - ► <br> <br> [September](https://www.vlsi-expert.com/2018/09/)(1)<br> - ► <br> <br> [May](https://www.vlsi-expert.com/2018/05/)(1)<br> - ► <br> <br> [February](https://www.vlsi-expert.com/2018/02/)(1)<br> - ► <br> <br> [January](https://www.vlsi-expert.com/2018/01/)(2)<br>- ► <br> <br>[2017](https://www.vlsi-expert.com/2017/)(14)<br> <br> - ► <br> <br> [December](https://www.vlsi-expert.com/2017/12/)(3)<br> - ► <br> <br> [November](https://www.vlsi-expert.com/2017/11/)(3)<br> - ► <br> <br> [October](https://www.vlsi-expert.com/2017/10/)(6)<br> - ► <br> <br> [September](https://www.vlsi-expert.com/2017/09/)(1)<br> - ► <br> <br> [April](https://www.vlsi-expert.com/2017/04/)(1)<br>- ► <br> <br>[2016](https://www.vlsi-expert.com/2016/)(11)<br> <br> - ► <br> <br> [December](https://www.vlsi-expert.com/2016/12/)(2)<br> - ► <br> <br> [September](https://www.vlsi-expert.com/2016/09/)(1)<br> - ► <br> <br> [June](https://www.vlsi-expert.com/2016/06/)(1)<br> - ► <br> <br> [April](https://www.vlsi-expert.com/2016/04/)(1)<br> - ► <br> <br> [March](https://www.vlsi-expert.com/2016/03/)(1)<br> - ► <br> <br> [February](https://www.vlsi-expert.com/2016/02/)(4)<br> - ► <br> <br> [January](https://www.vlsi-expert.com/2016/01/)(1)<br>- ► <br> <br>[2015](https://www.vlsi-expert.com/2015/)(15)<br> <br> - ► <br> <br> [November](https://www.vlsi-expert.com/2015/11/)(2)<br> - ► <br> <br> [October](https://www.vlsi-expert.com/2015/10/)(7)<br> - ► <br> <br> [September](https://www.vlsi-expert.com/2015/09/)(2)<br> - ► <br> <br> [August](https://www.vlsi-expert.com/2015/08/)(1)<br> - ► <br> <br> [July](https://www.vlsi-expert.com/2015/07/)(3)<br>- ► <br> <br>[2014](https://www.vlsi-expert.com/2014/)(15)<br> <br> - ► <br> <br> [December](https://www.vlsi-expert.com/2014/12/)(1)<br> - ► <br> <br> [November](https://www.vlsi-expert.com/2014/11/)(4)<br> - ► <br> <br> [September](https://www.vlsi-expert.com/2014/09/)(3)<br> - ► <br> <br> [July](https://www.vlsi-expert.com/2014/07/)(1)<br> - ► <br> <br> [June](https://www.vlsi-expert.com/2014/06/)(1)<br> - ► <br> <br> [April](https://www.vlsi-expert.com/2014/04/)(1)<br> - ► <br> <br> [February](https://www.vlsi-expert.com/2014/02/)(1)<br> - ► <br> <br> [January](https://www.vlsi-expert.com/2014/01/)(3)<br>- ► <br> <br>[2013](https://www.vlsi-expert.com/2013/)(12)<br> <br> - ► <br> <br> [December](https://www.vlsi-expert.com/2013/12/)(6)<br> - ► <br> <br> [October](https://www.vlsi-expert.com/2013/10/)(2)<br> - ► <br> <br> [May](https://www.vlsi-expert.com/2013/05/)(1)<br> - ► <br> <br> [April](https://www.vlsi-expert.com/2013/04/)(1)<br> - ► <br> <br> [March](https://www.vlsi-expert.com/2013/03/)(1)<br> - ► <br> <br> [January](https://www.vlsi-expert.com/2013/01/)(1)<br>- ► <br> <br>[2012](https://www.vlsi-expert.com/2012/)(15)<br> <br> - ► <br> <br> [November](https://www.vlsi-expert.com/2012/11/)(3)<br> - ► <br> <br> [September](https://www.vlsi-expert.com/2012/09/)(2)<br> - ► <br> <br> [July](https://www.vlsi-expert.com/2012/07/)(2)<br> - ► <br> <br> [April](https://www.vlsi-expert.com/2012/04/)(2)<br> - ► <br> <br> [March](https://www.vlsi-expert.com/2012/03/)(1)<br> - ► <br> <br> [February](https://www.vlsi-expert.com/2012/02/)(5)<br>- ► <br> <br>[2011](https://www.vlsi-expert.com/2011/)(17)<br> <br> - ► <br> <br> [September](https://www.vlsi-expert.com/2011/09/)(1)<br> - ► <br> <br> [August](https://www.vlsi-expert.com/2011/08/)(1)<br> - ► <br> <br> [May](https://www.vlsi-expert.com/2011/05/)(1)<br> - ► <br> <br> [April](https://www.vlsi-expert.com/2011/04/)(2)<br> - ► <br> <br> [March](https://www.vlsi-expert.com/2011/03/)(5)<br> - ► <br> <br> [February](https://www.vlsi-expert.com/2011/02/)(7)<br>- ► <br> <br>[2010](https://www.vlsi-expert.com/2010/)(5)<br> <br> - ► <br> <br> [December](https://www.vlsi-expert.com/2010/12/)(1)<br> - ► <br> <br> [September](https://www.vlsi-expert.com/2010/09/)(1)<br> - ► <br> <br> [August](https://www.vlsi-expert.com/2010/08/)(3)<br>- ► <br> <br>[2008](https://www.vlsi-expert.com/2008/)(1) - ► <br> <br> [July](https://www.vlsi-expert.com/2008/07/)(1) |**

**## Followers**

**Followers (780) Next**

**![Shivam Sahu](https://lh3.googleusercontent.com/a/ACg8ocKDr1gGxbAYndjgnaONQoKM7b5Uup0VYw4zlftzY9J93oEZNcFp=s45-c)**

**![Naveen Arava](https://lh3.googleusercontent.com/a-/ALV-UjUz0WPfmJVOhiFrJ1jOM-B-dSEcn5O5t9y9EumeHoq8DBBDTbYJ=s45-c)**

**![Sociall Tech](https://lh3.googleusercontent.com/a/ACg8ocLUXX20lMhQ6CqTARX9pnEhF1eXYLZFLRXFqyKu6k7Pdb5DzA=s45-c)**

**![macha ganesh](https://lh3.googleusercontent.com/a-/ALV-UjXPo6wHpDr9s_pQhJpjMHMoKelJThA-rmnk9F7-xMoUWC3V5icj=s45-c)**

**![deepansh arora](https://lh3.googleusercontent.com/a-/ALV-UjUacvV2Vi5losRk2PBeQi9IPV6rZ8OxJptYMcrxppd6r_vWzJxZHw=s45-c)**

**![Sai Charan Reddy](https://lh3.googleusercontent.com/a/ACg8ocI5qMLqP1SbSUD7KBhnGfHLTiwh6itNIEob73DyzURmggubqg=s45-c)**

**![Anish](https://lh3.googleusercontent.com/a-/ALV-UjVpaadE0cY5e7AVodnQzVVoR9Ve0XjSaKCvUENdVoojxuIDim15=s45-c)**

**![Sahil Rajwar](https://lh3.googleusercontent.com/a-/ALV-UjV32J0bHjC8IDwVZeQkCXjWF1Q_sUUJsZHi_e2grr-mDjScmgE=s45-c)**

**![Pranav Singh](https://lh3.googleusercontent.com/a-/ALV-UjXzBxWYl6x60WXz2sjn9KpBae-5glA1qGqRxpmakV5bBzkf5Yb7=s45-c)**

**![homasingh byali](https://lh3.googleusercontent.com/a-/ALV-UjUispMTH4OUwkr0CzEm0FQFBSMDcst5_oClpRjqs42akxCVYzA=s45-c)**

**![sardar](https://lh3.googleusercontent.com/a-/ALV-UjV3rcR9mFd83BdQGAamZ99jujfy6bXAf9lXJGpTBWUQ_AEYt6TyVw=s45-c)**

**![Sunny Naineni](https://lh3.googleusercontent.com/a-/ALV-UjVhz0CDYrQnKs9VKcW3OXXOp2y_9vGzGGzSU4cMZzfOPe6BXYg=s45-c)**

**![Sahana M](https://lh3.googleusercontent.com/a/ACg8ocKtVdFhPe0iXYR0wR8pRa_aOR7kOc9GT1qXKtZutvlTuc2RyA=s45-c)**

**![Mohammed Irshad Ahmed](https://lh3.googleusercontent.com/a/ACg8ocIMvT5bbi1xTXsmTVB0XVxdIDJIzhWLYr_samEhYV5HdGoEmg=s45-c)**

**![Krithika Mudavath](https://lh3.googleusercontent.com/a-/ALV-UjUvIEiLUdIMp8otQmPG1KgE5TY9T-faBO-7HdOh9w32kiXJQcIP5w=s45-c)**

**![Shreeya H](https://lh3.googleusercontent.com/a/ACg8ocJQ5kU7gHvPZ9tlFPahDX7kyAqR4cKAgR81Jq_0ozk4i81Jdg=s45-c)**

**![Tú Trịnh](https://lh3.googleusercontent.com/a/ACg8ocLuIpII92jCyu_rE9abgJzpS_4Of6i_3ykK7AiEtnvhdJCthg=s45-c)**

**![Kristen Gomez](https://lh3.googleusercontent.com/a-/ALV-UjWSUOiuAnq8LTYKy_7d7ETEtZ6rQ6NTGmlsP8angedgDMVjkNQ=s45-c)**

**![李琪](https://lh3.googleusercontent.com/a/ACg8ocJQVrv0jWwQM-HuS12LutmgmrcIIigi22ctrIxUAYQbVzfQHw=s45-c)**

**![Shubham Darokar](https://lh3.googleusercontent.com/a-/ALV-UjUNb72p63Kc_UitRgS63LRaVUWVwHCGkZrPJNrMH1RtkI9_0Bk6=s45-c)**

**![Vivek molumuri](https://lh3.googleusercontent.com/a/ACg8ocK554dSngFGEzXyG0y5mf6Y42YibzD3msDyydvrITZpw2QRnbg=s45-c)**

**Follow**

**| | |**
**| --- | --- |**
**| | |**

**Vlsi expert group. .**

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 9. Untitled

**URL:** https://www.vlsi-expert.com/2021/05/
**Date:** 2021-05
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2021-12-15T18:28:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2021-05-31T00:09:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 10. Untitled

**URL:** https://www.vlsi-expert.com/2021/04/
**Date:** 2021-04
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2021-06-06T09:32:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2021-04-28T20:32:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 11. ## Monday, November 4, 2019

**URL:** https://www.vlsi-expert.com/2019/11/
**Date:** 2019-11
**Tags:** sta, dft, parasitic

## Monday, November 4, 2019

### [STA Tool Command - report\_timing -max\_paths\_count (OpenSTA -group\_count) : Part 1](https://www.vlsi-expert.com/2019/11/sta-group-count-command-1.html)

As, I have shared last time that in this series of articles, we are going to discuss about the different command of STA Tools along with the concepts. We have used OpenSTA which is an open source tool and can be downloaded from [OpenSTA](https://github.com/The-OpenROAD-Project/OpenSTA). It’s commands are similar to Primetime (Industry standard tool). By using OpenSTA you can understand the working of tool properly. Here, I have made some of the comparison between the commands of Primetime & OpenSTA (which I am going to use in another few articles). The command which I have selected is report\_timing (in Primetime) & report\_checks (in OpenSTA). The report\_checks / report\_timing command reports paths in the design

[Newer ](https://www.vlsi-expert.com/search?updated-max=2019-12-14T18:57:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2019-11-04T16:55:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 12. #### 1 comment:

**URL:** https://www.vlsi-expert.com/2019/10/10-employee-awards-to-boost-morale.html
**Date:** 2019-10
**Tags:** dft, parasitic

#### 1 comment:

1. ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYq91_QGYVu08BQJvscs0z4ub1NgH57g7b4XSne8dLN92UQD6cP-YX0YlapzeSX3bKEBgr5kIiTcFHzpubu1SXezVlit8WVwKj8fBqG1QI3Tcrrtr40n0E60yuZBuKUA/s45-c/Screenshot_3.png)

[August 1, 2021 at 11:46 PM](https://www.vlsi-expert.com/2019/10/10-employee-awards-to-boost-morale.html?showComment=1627841814908#c6586174369547184968)

Employees are our most important customers because they can provide crucial insights into the overall customer experience. But they are often overlooked or neglected, and most companies do not view them as valuable assets either in terms of providing insights into the customer experience, or as brand ambassadors. [https://perkpal.co.uk](https://perkpal.co.uk/)

Reply

Replies

Reply

Add comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

Load more...

[Newer Post](https://www.vlsi-expert.com/2019/11/sta-group-count-command-1.html "Newer Post")[Older Post](https://www.vlsi-expert.com/2019/09/sta-path-group-command.html "Older Post")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[Post ()](https://www.vlsi-expert.com/feeds/8169527459466834049/comments/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 13. Untitled

**URL:** https://www.vlsi-expert.com/2019/10/
**Date:** 2019-10
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2019-11-07T12:08:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2019-10-16T14:27:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 14. Untitled

**URL:** https://www.vlsi-expert.com/2019/09/
**Date:** 2019-09
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2019-11-04T16:55:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2019-09-24T18:45:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 15. ## Thursday, November 22, 2018

**URL:** https://www.vlsi-expert.com/2018/
**Date:** 2019-05-24
**Tags:** physical-design, sta, dft, low-power, ESD, CMOS, parasitic, analog

## Thursday, November 22, 2018

### [TCL Practice Task 3 (Scripting Language)](https://www.vlsi-expert.com/2018/11/tcl-practice-task-3.html)

TCL is very important from automation point of view in VLSI Industry but somehow students are not ready to learn this. They think it's a programing (like software programing) and they are in VLSI Industry to do some hardware related job. Reason of this - they don't know the application of TCL in VLSI Industry. In these series of articles, I am listing down few of the small projects or say programs or say exercise which can help anyone to understand the use-model of TCL inside the Industry. As a fresher, it's worth trying these task/programs/exercise, it will boost your confidence.

This is third part. If you have missed first and second part, please visit it. [TCL Practice Task 1](http://www.vlsi-expert.com/2018/11/tcl-practice-task-1.html) and [TCL Practice Task 2](http://www.vlsi-expert.com/2018/11/tcl-practice-task-2.html).

To understand this Task, you should have Task 1 and Task 2 program handy. :)

After the first 2 task, Now it's time to add some features in those programs/tasks. :)

**Task 3:- User Input and Runtime decision**

**Step 1:** Create 1 Input file ("file\_input1.txt")

Content of "file\_input1.txt" is same as in the first 2 Tasks. So, you can copy this file from previous programs. Snapshot of the file is present below.

**Input File:** “file\_input1.txt”

    Name        Delay    Trans    Load

    ---------------------------------------------

    AND1\_2X      1.50ns    0.1    1.25ff

    AND1\_3X      1.75ns    0.2    1.98ff

    AND2\_3X      2.37ns    0.3    2.27ff

    AND2\_4X      1.82ns    0.5    2.54ff

    NAND1\_2X    2.14ns    0.2    1.69ff

    NAND2\_3X    2.48ns    0.3    2.11ff

**Step 2:** Write a TCL program, where you will read input files "file\_input1.txt" and then you will display the name of these cells to the user as an info and ask them to choose cell name (or cells name) from the displayed list (which you have provided). According to the user input or inputs, you have to extract below information from input file ("file\_input1.txt") and display it in the below format (This is same output format as per Task 2 output).

Example 1:- If user Enter Cell name AND1\_2X then display data should be

    Name        Trans    Load    Delay    Total\_Delay

    ----------------------------------------------------------------------------

    AND1\_2X      0.1    1.25ff    1.50ns      1.50ns

Example 2:- If user Enter Cell name AND1\_2X, AND2\_3X, AND2\_4X & NAND2\_3X then display data should be

    Name        Trans    Load    Delay    Total\_Delay

    ----------------------------------------------------------------------------

    AND1\_2X      0.1    1.25ff    1.50ns      1.50ns

    AND2\_3X      0.3    2.27ff    2.37ns      3.87ns

    AND2\_4X      0.5    2.54ff    1.82ns      5.69ns

    NAND2\_3X    0.3    2.11ff    2.48ns      8.17ns

**Note:**

- About Total Delay, We have already discussed in previous task ( [TCL Practice Task 2](http://www.vlsi-expert.com/2018/11/tcl-practice-task-2.html))
- How are you going to ask data from user, you have freedom.
- User should be able to enter 1 (One) or multiple CELL name.
- If user enter wrong name, you should be able to provide them proper information / warning (that Cell name is incorrect).
- In case of wrong input, give user 2 more chances before exiting the program.
- After every wrong input, provide a option to user to quit (if they want).

**Step 3:** Print the above formated data as per user input onto the terminal & in output file "file\_output2.txt"

**Hint:**

- You have to reuse TCL program of Task 1 and Task 2.

 - Reading of File "file\_input1.txt" should be with the help of previous program only.
 - Get the user input and create a new file (temporary file) as per second input file (file\_input2.txt) format of Task 2.
 - Once you create a temp file, you can reuse the program of Task 2 as it is (just by converting that into procedure)

**Learning after this Program:**

- How to Open & Close Input files
- How to Read or Write from/in a file
- How to take inputs from the users.
- How to display info, warning and Error messages to user.
- Looping in a program and resetting a particular variable.
- Exit option.
- How to save user inputs in a variable or list of variables, even you don't know the number of inputs.
- How to save data in List and do different operations on that
- How to do Matching or say comparison of Data
- How to select only a specific data
- How to do mathematical calculations
- Different commands use-model

 - list, lindex, lappend
 - Foreach loop, While loop, If-else loop
 - gets and puts
 - split
 - expr
 - incr

- How to manage single space, multiple space
- Regular expression concepts
- Procedure concepts (proc in tcl)

 - How to write a Procedure
 - How to pass a value to Procedure
 - How to call a Procedure
 - How to get return from a Procedure (return command)

**Industrial Use of this Task:**

During the automation of data, many times either we work on input Template file (where user need to provide inputs by filling that) or ask inputs from user directly during runtime. These inputs can be in the form of YES/NO or may be some small inputs like Cell name or Path name.

I am sure this article will help you. In the Next article, we will discuss about a task where you have to take inputs from user as a command line option (even before running a program and not as Template file).

**-By Rajat Bansal**

**(Btech-EC:- 2019 Passout)**

**(ABES Engineering College)**

-Supervised By Puneet Mittal

(Founder & Director)

(VLSI Expert Private Limited)

Posted by
VLSI Expert
at
[4:55 PM](https://www.vlsi-expert.com/2018/11/tcl-practice-task-3.html "")[2\\
comments](https://www.vlsi-expert.com/2018/11/tcl-practice-task-3.html#)

## Thursday, November 15, 2018

### [TCL Practice Task 2 (Scripting Language)](https://www.vlsi-expert.com/2018/11/tcl-practice-task-2.html)

TCL is very important from automation point of view in VLSI Industry but students are lacking bigtime. Even if they learn, they face problem to understand the uses of TCL in VLSI Industry. In these series of articles, I am listing down few of the small projects or say programs or say exercise which can help anyone to understand the use-model of TCL in Industry. As a fresher, if you try at least once, it will boost your confidence. If you are able to automate below few task, more then 50% of work (based on TCL) can be done easily.

This is second part. If you have missed first part, please visit it ( [TCL Practice Task 1](http://www.vlsi-expert.com/2018/11/tcl-practice-task-1.html)). Because to understand this Task, you should have Task 1 program handy. :)

If you have completed previous task (task 1), I am sure now you are good in file handling.

**Task 2:- Mapping Two Files**

Step 1: Create 2 Input files ("file\_input1.txt" and "file\_input2.txt")

Content of "file\_input1.txt" is same as in the previous Task. So, you can copy file from last program. Snapshot of both the files are present below.

**Input File:** “file\_input1.txt”

    Name        Delay    Trans    Load

    ---------------------------------------------

    AND1\_2X      1.50ns    0.1    1.25ff

    AND1\_3X      1.75ns    0.2    1.98ff

    AND2\_3X      2.37ns    0.3    2.27ff

    AND2\_4X      1.82ns    0.5    2.54ff

    NAND1\_2X    2.14ns    0.2    1.69ff

    NAND2\_3X    2.48ns    0.3    2.11ff

**Input File:** “file\_input2.txt”

    CELL\_1:    AND1\_2X

    CELL\_2:    AND2\_3X

    CELL\_3:    AND2\_4X

    CELL\_4:    NAND2\_3X

Step 2: Reuse TCL Program of Task 1 and convert into procedure or procedures.

Step 3: Write a TCL program, where you will read both input files "file\_input1.txt" & "file\_input2.txt" and as per the CELL name present in second file (e.g. AND1\_2X ...), you have to extract below data and display it in the below format.

    Name        Trans    Load    Delay    Total\_Delay

    ----------------------------------------------------------------------------

    AND1\_2X      0.1    1.25ff    1.50ns      1.50ns

    AND2\_3X      0.3    2.27ff    2.37ns      3.87ns

    AND2\_4X      0.5    2.54ff    1.82ns      5.69ns

    NAND2\_3X    0.3    2.11ff    2.48ns      8.17ns

**Total Delay = Delay of Cell + Delay of Previous stage**

So, in our case,

    Delay of AND1\_2X = 1.50ns + 0ns = **1.50ns**

    Delay of AND2\_3X = 2.37ns + 1.50ns = **3.87ns**

    Delay of AND2\_4X = 1.82ns + 3.87ns = **5.69ns**

    Delay of NAND2\_3X = 2.48ns + 5.69ns = **8.17ns**

**Note:**

- All the above calculations, you have to do with in TCL Program.
- You have to reuse TCL program of Task 1.

 - Reading of File "file\_input1.txt" should be with the help of previous program only.
 - Rearranging the data should be using previous program.
 - Writing data should be as per previous program.

Step 4: Print the above formated data onto the terminal & in output file "file\_output2.txt"

**Learning after this Program:**

- How to Open & Close 2 Input files simultaneously
- How to Read or Write from/in a file
- How to save data in List and do different operation on that
- How to do Matching or say comparison of Data
- How to select only a specific data
- How to do mathematical calculations
- Different commands use-model

 - list, lindex, lappend
 - Foreach loop, While loop, If-else loop
 - gets and puts
 - split
 - expr
 - incr

- How to manage single space, multiple space
- Regular expression concepts
- Procedure concepts (proc in tcl)

 - How to write a Procedure
 - How to pass a value to Procedure
 - How to call a Procedure
 - How to get return from a Procedure (return command)

**Industrial Use of this Task:**

Most of the time, we work on automation of data in Industry.This data present in the form of report file (.rpt file) or output file or may be logfile. After reading data, we have to do a lot of operation (mathematically) and has to represent the data as per our requirement.

For example,

1. Timing Report have a lot of information about several Timing paths. You may have to create a automation to find out only slack of specific paths mentioned in other file.
2. SPEF file has C (cap) information of Nets. You want to compare 2 SPEF files of same design generated after making certain changes in design. This type of automation create a final report of Delta Cap for all Nets present in either SPEF file. Analysis of this final report (created after automation) may help you to fix design issues.

There are lot of such examples. I will try to list those sometime later. :)

I am sure this article will help you. In the Next article, we will discuss about a task where you have to take inputs from user in runtime (means during the execution of Program).

**-By Rajat Bansal**

**(Btech-EC:- 2019 Passout)**

**(ABES Engineering College)**

-Supervised By Puneet Mittal

(Founder & Director)

(VLSI Expert Private Limited)

Posted by
VLSI Expert
at
[8:59 AM](https://www.vlsi-expert.com/2018/11/tcl-practice-task-2.html "")[7\\
comments](https://www.vlsi-expert.com/2018/11/tcl-practice-task-2.html#)

## Wednesday, November 14, 2018

### [TCL Practice Task 1 (Scripting Language)](https://www.vlsi-expert.com/2018/11/tcl-practice-task-1.html)

VLSI Industry has requirement of TCL (a scripting language). Lot of Institutes helping students to learn this language. But somehow students don't know much about the use of this in real VLSI World. In this article, I am listing down few of the small projects or say programs or exercise which you should try at least once before entering into the VLSI Industry. If you are able to automate below few task, more then 50% of work (based on TCL) can be done easily.

**Task 1:- Input Output File Handling & Rearranging Data**

Step 1: Create a file and named it "file\_input1.txt" (Content of "file\_input1.txt" is given below - Remember, you have create file exactly same as given. All spaces and format should be in same manner)

**Input File:** “file\_input1.txt”

    Name        Delay    Trans    Load

    ---------------------------------------------

    AND1\_2X      1.50ns    0.1    1.25ff

    AND1\_3X      1.75ns    0.2    1.98ff

    AND2\_3X      2.37ns    0.3    2.27ff

    AND2\_4X      1.82ns    0.5    2.54ff

    NAND1\_2X    2.14ns    0.2    1.69ff

    NAND2\_3X    2.48ns    0.3    2.11ff

Step 2: Create a TCL based program which will read input file ("file\_input1.txt) and rearrange the data as per below format.

    Name        Trans    Load    Delay

    ---------------------------------------------

    AND1\_2X      0.1    1.25ff    1.50ns

    AND1\_3X      0.2    1.98ff    1.75ns

    AND2\_3X      0.3    2.27ff    2.37ns

    AND2\_4X      0.5    2.54ff    1.82ns

    NAND1\_2X    0.2    1.69ff    2.14ns

    NAND2\_3X    0.3    2.11ff    2.48ns

Step 3: Print the above formated data onto the terminal & in output file "file\_output.txt"

**Learning after completion of this task:**

- How to Open and Close file
- How to Read or Write from/in a file
- How to save data in List and do different operation on that
- Different commands usemodel

 - list, lindex, lappend
 - Foreach loop, While loop, If-else loop
 - gets and puts
 - split

- How to manage single space, multiple space
- If you are using regular expression - then things will be different but as such this program can be written without any regular expression.
- If you are new to Linus environment then few more learning after this task

 - How to write a file using any unix editor
 - How to source a file and execute a program

- If you want to use Procedure (equivalent to functions in C)

 - How to write a Procedure
 - How to pass a value to Procedure
 - How to call a Procedure

**Industrial Use of this Task:**

Most of the time, we work on automation of data in Industry.This data present in the form of report file (.rpt file) or output file or may be logfile. After reading data, we have to rearrange that data as per required format or say template (may be because of any other tool requirement or other scripting requirement or creating graphs/charts etc.)

I am sure, it will help you. In the Next article, we will discuss another Task with multiple file handling and data comparing concepts.

**-By Rajat Bansal**

**(Btech-EC:- 2019 Passout)**

**(ABES Engineering College)**

-Supervised By Puneet Mittal

(Founder & Director)

(VLSI Expert Private Limited)

Posted by
VLSI Expert
at
[3:23 PM](https://www.vlsi-expert.com/2018/11/tcl-practice-task-1.html "")[11\\
comments](https://www.vlsi-expert.com/2018/11/tcl-practice-task-1.html#)

## Tuesday, September 4, 2018

### [The Job Before the Job – How to Write a Killer Resume](https://www.vlsi-expert.com/2018/09/how-to-write-killer-resume.html)

**Author Article: (By Lucy Wyndham)**

Those looking to get into the world of
semiconductor engineering are facing one of the most competitive job markets
out there. According to the U.S. Bureau of Labor Statistics, [the projected market growth](https://www.bls.gov/ooh/architecture-and-engineering/materials-engineers.htm) for
materials engineers is only 2% between now and 2026. This stat may sound as
intimidating [as an interviewer’s questions](http://www.vlsi-expert.com/p/here-i-are-trying-to-capture-most-of.html), but
don’t worry. This just means you need to prepare for the career as thoroughly
as possible, and this starts with writing an irresistible resume.

**The**
**Basics**

Errors have always been resume-killers.
One misspelling here or glaring grammatical gaffe there is oftentimes all it
takes for a resume to get tossed in the wastebasket. When you’ve typed up a
resume, [carefully proofread it and fix](https://writing.wisc.edu/Handbook/Proofreading.html) all
the errors you spot. When you’re done, comb over it again – chances are you
missed something. Not doing so could kill your hopes before they even spring
forth.

A good-looking resume is more than just
making sure there aren’t any mistakes, though. It must be easy to read and
possess an agreeable aesthetic flow. Use a legible font that’s sized to allow
for a decent amount of white space on the page, as that will make it easier to
read. Also, stick to white or cream-colored paper, as it’s very difficult to
take a resume on colored paper seriously.

Additionally, don’t fudge. This not only
includes your qualifications or your past job info, but also your [technical skills and proficiencies](https://novoresume.com/resume-templates).
If a job is asking for, say, Excel skills, this means they are going to expect
you to work with a spreadsheet. This could be a problem if you don’t know what
you’re doing.

**Modern**
**Tips**

Because of the Internet and the power of
social media, it’s not enough to just build your resume with achievements and
proficiencies. You need to have an online presence. Studies show a whopping 93%
of recruiters will seek out your online profiles before making the call to
interview you.

Therefore, be proactive here and put your
social media links on your resume. Putting a link to your LinkedIn site, for
instance, will make your resume more appealing. After all, nobody will have to
poke around the net trying to figure you out.

Following these tips won’t necessarily
guarantee a phone call from a potential employer. However, they will increase
the likeliness of your resume getting noticed and considered. That may seem
like a small step, but considering the competitiveness of the semiconductor
engineering job market, it’s an important step to take.

-By Lucy Wyndham

(lucy.writer@lumenmail.net)

Posted by
VLSI Expert
at
[6:33 PM](https://www.vlsi-expert.com/2018/09/how-to-write-killer-resume.html "")[6\\
comments](https://www.vlsi-expert.com/2018/09/how-to-write-killer-resume.html#)

## Tuesday, May 1, 2018

### [Digital Electronics - Mux Based Interview Questions](https://www.vlsi-expert.com/2018/05/digital-electronics-mux-based-interview.html)

As a fresher or experienced candidate, digital electronics always play an important role in VLSI Interview. Whatever be the profile, it doesn't matter. Lot of candidates call me or message me and ask

- What type of questions can be asked in Digital electronics ?
- Which book/s is/are good for preparation?
- What all topics should be cover ?

and lot more such type of questions.

It's very difficult to answer such questions because Digital electronics is so vast that no one can cover it 100% with in 1 month (max time we get before any interview). So what's the best way to prepare. I am capturing few topics from Digital electronics one by one which looks to me very important. I am also trying to capture questions which can be asked by any Interviewer. If you can focus on these topics or say questions - I am sure - it will give you a good amount of confidence for any Interview.

**Note: At the end, I am trying to capture few common mistakes, more than 50% candidates do during interviews. I hope, it will help all of you to get the right answer and understand the expectation of Interviewer.**

## Multiplexer based Interview Questions:

01. Describe the operation of Multiplexer
02. How many select lines are there for 12 : 1 MUX ?
03. How many input pins are there in a 2:1 MUX ?
04. How can we convert 4:1 Mux into 2:1 Mux ?

 1. Any other method for converting 4:1MUX to 2:1, where no need to short "Select line" ?

06. How many 2:1 MUX require to make 16:1 MUX ?

 1. Draw diagram with proper labelling

08. What's the difference between MUX and Encoder?
09. Draw internal circuitry of 2:1 MUX using only NMOS, PMOS and CMOS?
10. How many Transistor (transistor count) in a 2:1 MUX?
11. Design an AND gate using MUX.
12. Design a D Flip-flop using MUX.

 1. This is very common question and lot of follow-up questions on the basis of your answer. Below are few ...
 2. Mux'ed based "Positive/Negative Triggered D-Flipflop"
 3. Mux'ed based "Positive/Negative level latch"
 4. Advantage/Disadvantage of using Mux'ed based Flipflop.

14. What's the advantage/disadvantage using MUX based AND gate over normal CMOS based AND gate?
15. Do you know anything about Clock gating?

 1. Draw a circuit for clock gating using AND gate
 2. Draw a circuit for clock gating using OR gate
 3. Draw a circuit for clock gating using MUX
 4. Out of above 3 which one you prefer and why?

17. Questions where Interviewer connect 1 input of 2:1 MUX with the ground and ask you the output function. e.g

 1. If in a 2 : 1 MUX, we connect D0 input with ground, what will be the output?

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5xzC1iHO29mEVlrzCGDqc0xMkSQBFXxfNMh-lH89UuJXPM04SwLt8J058IZvX8S0URur32nMu8N_OVJJ0-QSWCLsJuGKR7ajCN3EIgFTCjfCg5x79obpmIzIzQNpF363BdSRu1sszA-I/s320/mux-and1.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5xzC1iHO29mEVlrzCGDqc0xMkSQBFXxfNMh-lH89UuJXPM04SwLt8J058IZvX8S0URur32nMu8N_OVJJ0-QSWCLsJuGKR7ajCN3EIgFTCjfCg5x79obpmIzIzQNpF363BdSRu1sszA-I/s1600/mux-and1.PNG)

 3. If we interchange the signal applied at D0 & D1 in above figure, what will be the output?

19. In Mux'ed based AND gate, if position of Inputs are Interchanged (below fig a and fig b), is there any difference from timing perspective (Delay perspective)? Justify your answer in both case (Yes/NO).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9bezdwIspqEnXucOPvkqSxy8XVjdTe3_fpk0SIsER7muFgzqvjIMDvntauwcuJF-L_6xRa1KEzoQtE3sjDRLUpOgTFCyPXXq930CYJnSGT2uQKBWFmRZaIHsp8j4X669wAAQJGI-cd48/s400/mux-and3.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9bezdwIspqEnXucOPvkqSxy8XVjdTe3_fpk0SIsER7muFgzqvjIMDvntauwcuJF-L_6xRa1KEzoQtE3sjDRLUpOgTFCyPXXq930CYJnSGT2uQKBWFmRZaIHsp8j4X669wAAQJGI-cd48/s1600/mux-and3.PNG)

There can be more questions but unfortunately, not able to recall them. Anyone has any other questions - please help me to add here. Else, I will update this list whenever I am able to recall. :)

## Common Mistakes in Different Questions:

**Common Mistake Related to Question 1:**

While explaining the operation of Mux, candidates generally miss "select lines". If Interviewer ask to draw the diagram of MUX, candidates draw diagram without proper labelling. This is the area where anyone can confuse you. See below symbols & try to understand why I have mentioned correct or wrong.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWwtpnOmWJNKla5uBjs_Yh7AM6LuhFMJWwCdtZUNbiRdFITIk5Mktxd8oop4QpDnK5P3IJfjd2Rox3kUm9gQkg4bO9qtnjmrjoKTMRbrPJ24inJf4qLFo8ek94JD8brv5nL7XeHaqRs1w/s400/mux2-1.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWwtpnOmWJNKla5uBjs_Yh7AM6LuhFMJWwCdtZUNbiRdFITIk5Mktxd8oop4QpDnK5P3IJfjd2Rox3kUm9gQkg4bO9qtnjmrjoKTMRbrPJ24inJf4qLFo8ek94JD8brv5nL7XeHaqRs1w/s1600/mux2-1.PNG)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhraq8G7bD-dZWDDCaZvPrvaNONs3JOHI8odM-d0ydrGPq3-Ss6zPid0LAU_d7F3d4OtohiPdeq5G-2dW-meivkNzyxyMrsFelRsi_JVs3_DgMfb1blRhU44OTJAQ4bxbafW5zqE3HU1tQ/s400/mux4-1.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhraq8G7bD-dZWDDCaZvPrvaNONs3JOHI8odM-d0ydrGPq3-Ss6zPid0LAU_d7F3d4OtohiPdeq5G-2dW-meivkNzyxyMrsFelRsi_JVs3_DgMfb1blRhU44OTJAQ4bxbafW5zqE3HU1tQ/s1600/mux4-1.PNG)

**Common Mistake Related to Question 3:**

Very common Answer is 2 which is not correct. Why? Check .lib file.

**Common Mistake Related to Question 4:**

Solution is very simple - Connect both the select line or say short both the select line. But common mistake - we miss to make changes in the labelling.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHyJCzibRJ77-ZMllWL9CQ77W4F3z_NcRBo9MiwjTY_VjfIcmetX24tbcPKapsP58mwjA11aOUWhwY4u-4D_60iXqjLlDB4EQ5Yun0jWtkdxOwtO2QeBQzVJD2FGfFvkKG6dROFcXaRr0/s400/mux4to2.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHyJCzibRJ77-ZMllWL9CQ77W4F3z_NcRBo9MiwjTY_VjfIcmetX24tbcPKapsP58mwjA11aOUWhwY4u-4D_60iXqjLlDB4EQ5Yun0jWtkdxOwtO2QeBQzVJD2FGfFvkKG6dROFcXaRr0/s1600/mux4to2.PNG)

**Common Mistake Related to Question 5**

- Candidates become confuse between Decoder method and Mux method. :)
- Most of the Candidates confuse at the labelling part.

**Common Mistake Related to Question 7**

Normally, in college text books (or say basic Digital Electronics Books) - internal circuit is based on AND gate. So, we start with the AND gate based circuit of MUX and then convert respective AND gate with MOS. But actually, Interviewer need to know Pass Transistor or say Transmission gate based MUX. :)

**Common Mistake Related to Question 8**

Usually, we gave single answer but actually it depends how we have implemented MUX. Means using CMOS or Only NMOS/PMOS.

**Common Mistake Related to Question 9**

Usually we draw a single circuit, which we have learnt. But we miss to draw truth table and then implement using MUX. If you use this approach - you can implement any logic gate using MUX. Interviewer, also see your approach and need to understand whether you know the concepts or method or you have just mugged it.

Happy Learning and Best of Luck.

Posted by
VLSI Expert
at
[11:48 PM](https://www.vlsi-expert.com/2018/05/digital-electronics-mux-based-interview.html "")[7\\
comments](https://www.vlsi-expert.com/2018/05/digital-electronics-mux-based-interview.html#)

## Friday, February 9, 2018

### [Logic Level & Noise Margin](https://www.vlsi-expert.com/2018/02/logic-level-noise-margin.html)

Today, we will talk about the logic levels and what’s all this. I came across several students and realize that they are struggling big time to understand the Logic level, Input-output logic level and all.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh21qsQgzHL7C45mNieus_oZiugRCe2x-dM44Pza_GgFq5VxwYYy7zjDnAPsX3PuvlDfUWYR-tuisx7kJRdn0UiwpL6-tnx3RbIiNBCEWiGJfZQ0SnDlSCvRC09xiujGxhTZGg2gMpBp6o/s400/Logic+Level.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh21qsQgzHL7C45mNieus_oZiugRCe2x-dM44Pza_GgFq5VxwYYy7zjDnAPsX3PuvlDfUWYR-tuisx7kJRdn0UiwpL6-tnx3RbIiNBCEWiGJfZQ0SnDlSCvRC09xiujGxhTZGg2gMpBp6o/s1600/Logic+Level.PNG)

Let’s start with above known logic level diagram. Here, you can see that range of signal for Logic 0 is 0V to 1V and similarly for Logic 1 – It’s 2V to 3V, Till this point, everyone is (should be) clear. But the moment I ask what’s between Logic 1 and Logic 0 – confusion start. Few says it’s Undefined region and few smart kid says – it’s Noise Margin. :) The moment I ask them to define or provide more insight about this Noise region (as per smart kid), none of them able to define it. :)

In this article, we will discuss about this region and more related concepts.

Remember, everything above is with respect to Positive Logic Level and same we will discuss through out this article. To understand what’s Positive Logic Level and Negative Logic Level – please refer [Digital Basic (Logic Gates – Part a)](http://www.vlsi-expert.com/2013/12/digital-basic-13-logic-gates-part-a.html).

## Voltage Logic Level (Input/Output)

Let's try to understand the **Logic Level at the Input and Output of a Gate.**

Logic Level at the input of the Gate is known as **Input Logic Level** and corresponding voltage range as:

- **Logic 1: Start from VIH (Minimum Input Voltage for Logic High) and Ends at VDD**
- **Logic 0: Start from VSS and Ends at VIL (Maximum Input Voltage for Logic Low)**

Logic Level at the output of the Gate is known as **Output Logic Level** and corresponding voltage range as:

- **Logic 1: Start from VOH (Minimum Output Voltage for Logic High) and Ends at VDD**
- **Logic 0: Start from VSS and Ends at VOL (Maximum Output Voltage for Logic Low)**

Below Figure, can help you to understand what I am talking about...

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjp5qqLjYeq4ZxGUK_sS1_3CkxuOSfk9iuaroZfn4iKhyphenhyphenuL9eWU9ldOnHCEm9eh1CUW3iU9bdIT-EcpYwEm92mKOKwXyj36iZjgUBKfmONaSO2wTjadXPMuFZnPma5bwa7jshs5hQY7Py4/s640/Input-Output-Logic-Level.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjp5qqLjYeq4ZxGUK_sS1_3CkxuOSfk9iuaroZfn4iKhyphenhyphenuL9eWU9ldOnHCEm9eh1CUW3iU9bdIT-EcpYwEm92mKOKwXyj36iZjgUBKfmONaSO2wTjadXPMuFZnPma5bwa7jshs5hQY7Py4/s1600/Input-Output-Logic-Level.PNG)

Now, as a difference, you can see both (Input and Output Logic levels) have voltage range for Logic 1 & Logic 0. So **Next question is**:

- Are VOH = VIH and VOL = VIL ??
- What's the relationship between different voltage level? ??

You have to justify your answer with proper reason. Let me try from my side :) with logical explanation.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8HXW5OtICCu70OgTyAulAzEg1P6Km5G3D9e1-605fDfkrrNcUcQtMlEUyApI-qBZqdSDh8TCsxll1YF1-IJH3t6I8o-lmQWcMzBoLnli9o4Z-Y1e50TUmse3POhEuZ0C1eK87EmVISU8/s400/Logic+propagation+Output+to+Input.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8HXW5OtICCu70OgTyAulAzEg1P6Km5G3D9e1-605fDfkrrNcUcQtMlEUyApI-qBZqdSDh8TCsxll1YF1-IJH3t6I8o-lmQWcMzBoLnli9o4Z-Y1e50TUmse3POhEuZ0C1eK87EmVISU8/s1600/Logic+propagation+Output+to+Input.PNG)

In above fig, 2 NAND gates (1 & 2) are connected back to back. Let’s consider both NAND gates are 100% similar. If, NET Delay is Zero, **Our Expectation is** :: **Any signal at the output of “Gate1 with Logic 1” should be identify as “Logic 1 at the Input of Gate2”. Same goes with Logic 0 also.** Let's try to understand with example (if helps you to understand more clearly).

**Scenario 1:** **VOH < VIH ; VDD = 5V, VOH = 3V, VIL = 1V, VIH = 4V**

- **Output Logic 1**

 - Voltage range of Output Logic 1 is between 3V to 5V.
 - It means any signal with a voltage value between 3V and 5V is consider as Logic 1 at the output pin of Gate1.

- **Input Logic 1**

 - Voltage range of Input Logic 1 is between 4V to 5V.
 - It means any signal with a voltage value between 4V and 5V is considered as Logic 1.
 - **Any signal below 4V is NOT considered as part of Logic 1.**

Now, assume that a signal coming out from Gate 1 has voltage = 3V. It’s consider as part of Logic 1 for Gate 1 but when this signal propagate and reach at input of Gate 2, it will be nowhere (Means neither 1 nor 0 because voltage range of Logic 1 start from 4V and voltage range of Logic 0 ends at 1V).

So, in this Ideal scenario (Ideal means No Net Voltage Drop), to capture the Logic 1 at the input of Gate 2, Output voltage of Gate 1 for Logic 1 should have below condition.

**VOH ≥ VIH**

**Scenario 2:** **VOL ≥ VIL ; VSS = 0V, VOL = 2V, VIL = 1V, VIH = 4V**

- **Output Logic 0**

 - Voltage range of Output Logic 0 is between 0V to 2V.
 - It means any signal with a voltage value between 0V and 2V is consider as Logic 0.

- **Input Logic 0**

 - Voltage range of Input Logic 0 is between 0V to 1V.
 - It means any signal with a voltage value between 0V and 1V is considered as Logic 0.
 - **Any signal above 1V is not considered as part of Logic 0.**

Now, assume that a signal coming out from Gate 1 has voltage = 2V. It’s consider as part of Logic 0 for Gate 1 but when this signal propagate and reach at input of Gate 2, it will be nowhere (Means neither 1 nor 0 because voltage range of Logic 0 ends at 1V and voltage range of Logic 1 start from 4V).

So in this Ideal scenario (Ideal means No Net Voltage Drop), to capture the Logic 0 at the input of Gate 2, Output voltage of Gate 1 for Logic 0 should have below condition.

**VOL ≤ VIL**

On the basic of above 2 scenarios, I can easily summarize that ...

**VOH ≥ VIH**

**VOL ≤ VIL**

In above example, we have discussed all between 2 different gates (Output logic of 1st Gate and Input Logic of 2nd) and you may be thinking on the basis we summarize this relationship (because original question was Input Logic Vs Output Logic of Same Gate :)). Just in case, if that’s your confusion – then check again – I have mentioned above that both gates are identical (so it means input logic levels of 2nd Gate == Input Logic Levels of 1st Gate also. :):) ).

On the basis of this, if anyone give you below 4 options and ask you which one is the right set of Input-Output Logic combination – I am sure , it will be easy to find out. (I am not going to give answer, you can write in comment section with reason :) ).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1Xp2x7oNp1rB9COtOpMP4oiUNloH927GWtYBEBTET4dTN6g9aXCBM0rbRA0Y8pdN10RDEOJS_B6UofZulhIbstyLsFipF113XYwK-eq4r4nCyzMRC7tx0013LVdROdOvyMW2MxAD5E48/s640/Input-Output-Logic-Level-question.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1Xp2x7oNp1rB9COtOpMP4oiUNloH927GWtYBEBTET4dTN6g9aXCBM0rbRA0Y8pdN10RDEOJS_B6UofZulhIbstyLsFipF113XYwK-eq4r4nCyzMRC7tx0013LVdROdOvyMW2MxAD5E48/s1600/Input-Output-Logic-Level-question.PNG)

Till now, we considered the Ideal scenario (NO voltage drop across NET) But as you know nothing is ideal in this world, so keeping that in mind – our conditions changes and in **real world condition will be**….

### **VOH \> VIH** **VOL < VIL**

Now, If I want to represent this In a single diagram – below is the representation.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeuD3NPTvC1tmn7EgsuvHmreqokSTE7zhUaJz_W58qbwr1RDQVhxmXFPrkDUNvqRomgjMVTkSu-y5ZFkZj6zKJjRzgJvwNac44t4b233IfN9pbzPDsc38nVIX70p3QQlJGDmueql7Yrbk/s400/Logic+level+2.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeuD3NPTvC1tmn7EgsuvHmreqokSTE7zhUaJz_W58qbwr1RDQVhxmXFPrkDUNvqRomgjMVTkSu-y5ZFkZj6zKJjRzgJvwNac44t4b233IfN9pbzPDsc38nVIX70p3QQlJGDmueql7Yrbk/s1600/Logic+level+2.PNG)

Okay, so till now we are able to understand different nomenclature, Like VOH , VIH , VOL , VIL in logic level, their importance and relationship between them.

Now, if you remember, our discussion started with 2 things – Undefined Region and Noise Margin...

## Noise Region and Undefined Region

To understand the Noise Margin, you have to first understand what a "Noise" can do! In general, we can categorize Noise in 2 ways

- Noise Inside the Gate

 - Noise inside the Gate already taken care during simulation of Gate & only after that we define (or conclude) VOH, VOL

- Noise Outside the Gate

 - This Noise effects the signal which is traveling from the output pin of a gate to input pin to other gate

Let's talk about the Noise which developed or generated because of environment and effect Signal traveling between input and output pin of a Gate.

In general, Noise is Random in nature and you can’t model it exactly (at least the source of Noise :)). This Noise can be positive or negative in nature (when I am saying positive/negative it means with respect to zero reference level). It means if there is a output signal of 4V and suddenly a positive noise of 0.5V come, signal convert into 4.5V. Similarly, if Negative Noise of 0.5V come, output signal convert into 3.5V.

Let’s consider a scenario,

**For Gate 2:** VOH = 4V, VIH = 3.5V,

**Output signal from the 1st Gate is of 4V.**

Now, question is **what should be the maximum Noise value (in terms of voltage), so that even after noise 2nd Gate identify Logic 1 correctly ?**

As, we have discussed Noise can be Positive and Negative also –

If Noise is Positive then it’s going to add in output voltage .. Means output is going to increase above 4V, which is okay for 2nd gate because for 2nd Gate Voltage range start for Logic level 1 is above 3.5V.

If Noise is Negative then it’s going to reduce output voltage .. It means output is going to decrease & value will be less the 4V. If that’s the case we have to understand that Voltage range for Input logic High (1) start from 3.5V. Any signal less then 3.5V is not considered as Logic 1 signal at the input of Gate2. So, I can easily say that in this scenario, **Maximum allowable Noise in negative side is 4V – 3.5V = 0.5V** or you can say that **VOH – VIH**. This difference we are saying NOISE MARGIN for LOGIC HIGH.

**NOISE MARGIN HIGH LOGIC = VOH – VIH**

With the similar explanation, I can easily say that in case of Logic 0, any noise which increases the voltage of output logic signal beyond Max input Voltage for Logic 0, consider as not acceptable Noise. So, **any Noise between VOL and VIL is acceptable for Logic 0.** Means..

**NOISE MARGIN LOW LOGIC = VIL – VOL**

Okay, so if this is the NOISE Margin, what’s the Undefined Region ? Answer is simple – Remaining portion is considered as Undefined Region. :)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh56T8Xe8O2-gTudM5BCZRZ63J0w4pMJNyzkstpRrQ3LaMJibqDV2a2FMQV2T-qgwgLuub9JRO11NeXeVs_XUkUNu0gMi3vWv8maC1VUS60s6t0AkvMIGcC98hNY_faCMTZvNWAf4IAuj0/s400/Noise+Margin.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh56T8Xe8O2-gTudM5BCZRZ63J0w4pMJNyzkstpRrQ3LaMJibqDV2a2FMQV2T-qgwgLuub9JRO11NeXeVs_XUkUNu0gMi3vWv8maC1VUS60s6t0AkvMIGcC98hNY_faCMTZvNWAf4IAuj0/s1600/Noise+Margin.PNG)

I know, now you may be thinking that above description is good when we talk in terms of Input Vs Output Logic Level. But If we talk only about Logic level (Individual), then how can we defined the region between “Min Voltage for Logic 1” and “Max Voltage for Logic 0”.

Any signal with in this range is considered as uncertain, and no one is going to give you guarantee how other Gate (input Gate) would interpret such signal because that depends on Input level of 2nd gate :). Now, if your other gate (gate which is going to receive this signal at input port) has wider voltage range for Logic 1 or 0, most of your signals between uncertain range can be consider either Logic 0 or Logic 1.

So, This region is considered as **Uncertain Region**. It means signal in this region can be consider as Logic 0 or 1 depends on Logic level Range of Next stage Input gate. I will not say that it’s Undefined Region because undefined means – It's neither be 0 nor 1.

**Note:** "Either be 0 or 1" is completely different from "Neither be 0 nor 1".

If you are not clear with my statement – let's try to understand with one more example of say scenario.:).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2GWa3hnreV1XRRrf0kZHXbi9LbwiKu6aUtkaFwHQ85L-6TrZhpPvKi94T-ZNSv38leX-m1woTJIvB5fj3upHLu8jgJcP9ZErmz2TXen6kyCelaSqXQzd5RDdmQS4T9sOKO10RsVnW2iY/s400/Uncertain+Region+Vs+Undefined+Region.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2GWa3hnreV1XRRrf0kZHXbi9LbwiKu6aUtkaFwHQ85L-6TrZhpPvKi94T-ZNSv38leX-m1woTJIvB5fj3upHLu8jgJcP9ZErmz2TXen6kyCelaSqXQzd5RDdmQS4T9sOKO10RsVnW2iY/s1600/Uncertain+Region+Vs+Undefined+Region.PNG)

In above circuit, output of NAND Gate“1” is connected with 2 another NAND Gates. All NAND gates are different.

**Input Logic Level of NAND 2:**

Logic 0 – From 0V to 2V

Logic 1 – From 3V to 5V

**Input Logic Level of NAND 3:**

Logic 0 – From 0V to 1.5V

Logic 1 – From 3.5V to 5V.

**Output Logic Level of NAND 1:**

Logic 0 – From 0V to 1V

Logic 1 – From 4V to 5V.

Let’s assume At a particular instance, the output signal voltage at NAND Gate 1 is 3.2V. As per Output voltage levels (as per our above discussion), it’s in Uncertain Area. When this signal propagate through wire & reaches at

- **NAND Gate 3**

 - It’s below Voltage range for Logic level 1 (3.5V to 5V)
 - And above Voltage range for Logic level 0 (0V to 1.5V)
 - So this signal is considered as part of **UNDEFINED Region**.

- **NAND Gate 2**

 - It’s above Voltage range for Logic level 1 (3V to 5V)
 - So, this signal is considered as part of **Logic 1**.

So, it means **Same voltage can be part of Undefined Region and also as part of Logic Level 1.**Same case can happen for Logic 0 also.

**## In Summary:**

**- Range between VOH and VOL can be consider as uncertain range with respect to that gate.**
**- A range between VIH and VIL is considered as undefined region for that particular gate.**
**- Undefined region is with respect to Input Signal range.**
**- Uncertain Region is with respect to Output Signal Logic Range**
**- Noise Margin always with respect to Input and Output Logic range. :)**

### **VOH \> VIH** **VOL < VIL** NOISE MARGIN HIGH LOGIC = VOH – VIH NOISE MARGIN LOW LOGIC = VIL – VOL

I hope this article will help you to understand the Logic Level concepts in much more depth and help everyone (Specially Students) to understand the concepts :).

**HAPPY LEARNING**

Posted by
VLSI Expert
at
[8:56 AM](https://www.vlsi-expert.com/2018/02/logic-level-noise-margin.html "")[9\\
comments](https://www.vlsi-expert.com/2018/02/logic-level-noise-margin.html#)

## Monday, January 22, 2018

### [Unateness of Complex Circuit: Timing Arc](https://www.vlsi-expert.com/2018/01/unateness-of-complex-circuit-timing-arc.html)

## Monday, January 1, 2018

### [AOI (AND-OR-INVERTER) Cell](https://www.vlsi-expert.com/2018/01/aoi-and-or-inverter-cell.html)

AOI also known as AND-OR-Inverter.

AND-OR-Invert (AOI) logic or say gates are two-level logic functions constructed from the combination of one or more AND gates followed by a NOR gate. If we construct AND, OR and NOT gate separately, Number of transistor in AOI gates are less.

You might be thinking why need individual logic gate, why can't we implement it using just 2 AND gate and 1 NOR gate. Yes, you are right. But now think from CMOS point of view. In CMOS, we can implement AND gate using 1 CMOS NAND gate and 1 Inverter. It means above 2 AND gate changes into 2 NAND and 2 Inverter. I hope this explanation rang a bell in your mind. If not, keep patience (this is only I am going to explain in this article :) ).

Let's take an example and try to understand it.

**For example: 2-2 AOI gate: ((A.B) + (C.D))'**

Let's see how this function be implemented using logic gates (separately) Vs AOI cells.

**Using Individual NAND, NOT and NOR Gate:**

First we have to change the function as per logic gates availability. Y== ((A.B) + (C.D))' == (((A.B)')' + ((C.D)')')'

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTGtxK0Ev_q6KcIAR8ljezskmPupB-fjLm1i1gMqisEG6Ld1pbqGPz2A2ZgcacDpomfNqnwJvI8Rai_lkRBNbBI3LCA88LBw5JMCxf-fOsonzN-mAlo-QPiF8IQmaX2bmxnn9AF0vA_O4/s400/AOI+cell+using+seperate+Logic+Gates.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTGtxK0Ev_q6KcIAR8ljezskmPupB-fjLm1i1gMqisEG6Ld1pbqGPz2A2ZgcacDpomfNqnwJvI8Rai_lkRBNbBI3LCA88LBw5JMCxf-fOsonzN-mAlo-QPiF8IQmaX2bmxnn9AF0vA_O4/s1600/AOI+cell+using+seperate+Logic+Gates.PNG)

Function (((A.B)')' + ((C.D)')')' can be implemented as:

- NAND Gates:

 - 2 NAND gates: 1st for (A.B)' and 2nd for (C.D)' (Assume X=(A.B)' and Y=(C.D)')
 - 1 NAND gate uses 2 PMOS transistor and 2 NMOS transistor.
 - So, total Transistors in **2 2-input NAND gate are 8 Transistors.**

- Inverter:

 - 2 Inverter: 1st (X)' and 2nd for (Y)'
 - 1 Inverter uses 1 PMOS and 1 NMOS
 - So, total Transistors in **1 Inverter are 2 Transistors.**

- NOR Gates:

 - 1 NOR Gate: (X' + Y')'
 - 1 NOR gate uses 2 PMOS transistor and 2 NMOS transistor.
 - So, total Transistors in 1 2-input NOR gate are 4 Transistors.

**Total Transistor in case of Individually implementing ((A.B) + (C.D))' = 14 Transistor.**

CMOS Representation of above function is given below.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSOYcmFskwFGzniuUlk1dGY_Wo4B7wP4vK3afZjtFfsOh2DfZEXNVbCj2P_2XVfH6uk8IDT12Cg_TBKawW1KpZ3cz4rWY1YYjgpjvDjQYeddbRXh7CFlO6KakAsZRzGcw9K0UIU-aTLUY/s640/AOI+CMOS+Cell+using+seperate+logic.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSOYcmFskwFGzniuUlk1dGY_Wo4B7wP4vK3afZjtFfsOh2DfZEXNVbCj2P_2XVfH6uk8IDT12Cg_TBKawW1KpZ3cz4rWY1YYjgpjvDjQYeddbRXh7CFlO6KakAsZRzGcw9K0UIU-aTLUY/s1600/AOI+CMOS+Cell+using+seperate+logic.PNG)

**Using AOI logic gates.**

Implementation using AOI cells are very easy. In this case, we are not suppose to change the function. Y == ((A.B) + (C.D))'

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRQlXfLW_VjQ2xCeKJG0F-YByeOHwEEEpttys-_GGMXh02jM2AUkg7c0L7gCDzbfSPRDHGu9KWisizHCRDtNMzao12ixaNzWVoD4ReEJ3bai_5ojBNkncbrvszD_ky0f8VRF6dOE3Ug14/s400/AOI+Gate.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRQlXfLW_VjQ2xCeKJG0F-YByeOHwEEEpttys-_GGMXh02jM2AUkg7c0L7gCDzbfSPRDHGu9KWisizHCRDtNMzao12ixaNzWVoD4ReEJ3bai_5ojBNkncbrvszD_ky0f8VRF6dOE3Ug14/s1600/AOI+Gate.PNG)

Below diagram can help you to understand how cells can implement using CMOS. In this case, total Transistor require are 8 Transistor. If you are not able to understand this part (I am sure you need to refresh your concept for CMOS circuit).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguF1E7snflAE5sGtt5E6WM-tzouk4tltqSqmJfLJS5lvFajjolNCrpczyRLzyULZaTAOatSQrqh2atfrsQuAvyOh9zKY1tJGFV-Jwh2bicJu-IP-vMUOoFA2xNTD8fyJ-nQ687JXwpRkM/s640/AOI+CMOS+Cell.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguF1E7snflAE5sGtt5E6WM-tzouk4tltqSqmJfLJS5lvFajjolNCrpczyRLzyULZaTAOatSQrqh2atfrsQuAvyOh9zKY1tJGFV-Jwh2bicJu-IP-vMUOoFA2xNTD8fyJ-nQ687JXwpRkM/s1600/AOI+CMOS+Cell.PNG)

From above explanation, I am sure you are now in position to understand the importance of AOI cells. These cells are so important that in Standard cell library, you can easily find these cells (as other logic gates). So in short, I can say that these are also part of STANDARD Cells (So don't assume that only NAND, AND, OR, Buffer, Inverter, XOR, XNOR are Standard cells).

In a similar fashion, you can take any example and try to understand how many transistors are required in case of implementing that function in AOI form. This type of questions are very common during Interview or Written test.

**Less number of Transistors for implementing a particular logic function helps in multiple ways.** Like

- **Increased speed:** Less transistor means less delay, means fast response time.
- **Reduced Power:** Less number of transistor means less power consumption.
- **Smaller area:** Less number of transistor means less area consumption.
- **Potentially lower fabrication cost:** Fabrication cost is also less because of less number of manufacturing of transistor.

You can also understand OAI cells in similar way OR if you are not able to .. then wait for my Article. :)

Posted by
VLSI Expert
at
[8:23 PM](https://www.vlsi-expert.com/2018/01/aoi-and-or-inverter-cell.html "")[3\\
comments](https://www.vlsi-expert.com/2018/01/aoi-and-or-inverter-cell.html#)

[Newer ](https://www.vlsi-expert.com/search?updated-max=2019-05-24T20:00:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2018-01-01T20:23:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 16. Untitled

**URL:** https://www.vlsi-expert.com/2018/02/
**Date:** 2018-02
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2018-09-04T18:33:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2018-02-09T08:56:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 17. ## Monday, January 1, 2018

**URL:** https://www.vlsi-expert.com/2018/01/
**Date:** 2018-01
**Tags:** sta, dft, low-power, CMOS, parasitic

## Monday, January 1, 2018

### [AOI (AND-OR-INVERTER) Cell](https://www.vlsi-expert.com/2018/01/aoi-and-or-inverter-cell.html)

AOI also known as AND-OR-Inverter.

AND-OR-Invert (AOI) logic or say gates are two-level logic functions constructed from the combination of one or more AND gates followed by a NOR gate. If we construct AND, OR and NOT gate separately, Number of transistor in AOI gates are less.

You might be thinking why need individual logic gate, why can't we implement it using just 2 AND gate and 1 NOR gate. Yes, you are right. But now think from CMOS point of view. In CMOS, we can implement AND gate using 1 CMOS NAND gate and 1 Inverter. It means above 2 AND gate changes into 2 NAND and 2 Inverter. I hope this explanation rang a bell in your mind. If not, keep patience (this is only I am going to explain in this article :) ).

Let's take an example and try to understand it.

**For example: 2-2 AOI gate: ((A.B) + (C.D))'**

Let's see how this function be implemented using logic gates (separately) Vs AOI cells.

**Using Individual NAND, NOT and NOR Gate:**

First we have to change the function as per logic gates availability. Y== ((A.B) + (C.D))' == (((A.B)')' + ((C.D)')')'

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTGtxK0Ev_q6KcIAR8ljezskmPupB-fjLm1i1gMqisEG6Ld1pbqGPz2A2ZgcacDpomfNqnwJvI8Rai_lkRBNbBI3LCA88LBw5JMCxf-fOsonzN-mAlo-QPiF8IQmaX2bmxnn9AF0vA_O4/s400/AOI+cell+using+seperate+Logic+Gates.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTGtxK0Ev_q6KcIAR8ljezskmPupB-fjLm1i1gMqisEG6Ld1pbqGPz2A2ZgcacDpomfNqnwJvI8Rai_lkRBNbBI3LCA88LBw5JMCxf-fOsonzN-mAlo-QPiF8IQmaX2bmxnn9AF0vA_O4/s1600/AOI+cell+using+seperate+Logic+Gates.PNG)

Function (((A.B)')' + ((C.D)')')' can be implemented as:

- NAND Gates:

 - 2 NAND gates: 1st for (A.B)' and 2nd for (C.D)' (Assume X=(A.B)' and Y=(C.D)')
 - 1 NAND gate uses 2 PMOS transistor and 2 NMOS transistor.
 - So, total Transistors in **2 2-input NAND gate are 8 Transistors.**

- Inverter:

 - 2 Inverter: 1st (X)' and 2nd for (Y)'
 - 1 Inverter uses 1 PMOS and 1 NMOS
 - So, total Transistors in **1 Inverter are 2 Transistors.**

- NOR Gates:

 - 1 NOR Gate: (X' + Y')'
 - 1 NOR gate uses 2 PMOS transistor and 2 NMOS transistor.
 - So, total Transistors in 1 2-input NOR gate are 4 Transistors.

**Total Transistor in case of Individually implementing ((A.B) + (C.D))' = 14 Transistor.**

CMOS Representation of above function is given below.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSOYcmFskwFGzniuUlk1dGY_Wo4B7wP4vK3afZjtFfsOh2DfZEXNVbCj2P_2XVfH6uk8IDT12Cg_TBKawW1KpZ3cz4rWY1YYjgpjvDjQYeddbRXh7CFlO6KakAsZRzGcw9K0UIU-aTLUY/s640/AOI+CMOS+Cell+using+seperate+logic.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSOYcmFskwFGzniuUlk1dGY_Wo4B7wP4vK3afZjtFfsOh2DfZEXNVbCj2P_2XVfH6uk8IDT12Cg_TBKawW1KpZ3cz4rWY1YYjgpjvDjQYeddbRXh7CFlO6KakAsZRzGcw9K0UIU-aTLUY/s1600/AOI+CMOS+Cell+using+seperate+logic.PNG)

**Using AOI logic gates.**

Implementation using AOI cells are very easy. In this case, we are not suppose to change the function. Y == ((A.B) + (C.D))'

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRQlXfLW_VjQ2xCeKJG0F-YByeOHwEEEpttys-_GGMXh02jM2AUkg7c0L7gCDzbfSPRDHGu9KWisizHCRDtNMzao12ixaNzWVoD4ReEJ3bai_5ojBNkncbrvszD_ky0f8VRF6dOE3Ug14/s400/AOI+Gate.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRQlXfLW_VjQ2xCeKJG0F-YByeOHwEEEpttys-_GGMXh02jM2AUkg7c0L7gCDzbfSPRDHGu9KWisizHCRDtNMzao12ixaNzWVoD4ReEJ3bai_5ojBNkncbrvszD_ky0f8VRF6dOE3Ug14/s1600/AOI+Gate.PNG)

Below diagram can help you to understand how cells can implement using CMOS. In this case, total Transistor require are 8 Transistor. If you are not able to understand this part (I am sure you need to refresh your concept for CMOS circuit).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguF1E7snflAE5sGtt5E6WM-tzouk4tltqSqmJfLJS5lvFajjolNCrpczyRLzyULZaTAOatSQrqh2atfrsQuAvyOh9zKY1tJGFV-Jwh2bicJu-IP-vMUOoFA2xNTD8fyJ-nQ687JXwpRkM/s640/AOI+CMOS+Cell.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguF1E7snflAE5sGtt5E6WM-tzouk4tltqSqmJfLJS5lvFajjolNCrpczyRLzyULZaTAOatSQrqh2atfrsQuAvyOh9zKY1tJGFV-Jwh2bicJu-IP-vMUOoFA2xNTD8fyJ-nQ687JXwpRkM/s1600/AOI+CMOS+Cell.PNG)

From above explanation, I am sure you are now in position to understand the importance of AOI cells. These cells are so important that in Standard cell library, you can easily find these cells (as other logic gates). So in short, I can say that these are also part of STANDARD Cells (So don't assume that only NAND, AND, OR, Buffer, Inverter, XOR, XNOR are Standard cells).

In a similar fashion, you can take any example and try to understand how many transistors are required in case of implementing that function in AOI form. This type of questions are very common during Interview or Written test.

**Less number of Transistors for implementing a particular logic function helps in multiple ways.** Like

- **Increased speed:** Less transistor means less delay, means fast response time.
- **Reduced Power:** Less number of transistor means less power consumption.
- **Smaller area:** Less number of transistor means less area consumption.
- **Potentially lower fabrication cost:** Fabrication cost is also less because of less number of manufacturing of transistor.

You can also understand OAI cells in similar way OR if you are not able to .. then wait for my Article. :)

Posted by
VLSI Expert
at
[8:23 PM](https://www.vlsi-expert.com/2018/01/aoi-and-or-inverter-cell.html "")[3\\
comments](https://www.vlsi-expert.com/2018/01/aoi-and-or-inverter-cell.html#)

[Newer ](https://www.vlsi-expert.com/search?updated-max=2018-05-01T23:48:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2018-01-01T20:23:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 18. ## Friday, October 27, 2017

**URL:** https://www.vlsi-expert.com/2017/10/
**Date:** 2017-10
**Tags:** dft, parasitic

## Friday, October 27, 2017

### [Metal Layer Stack (Nomenclature) Part 2](https://www.vlsi-expert.com/2017/10/metal-layer-stack-nomenclature-part-2.html)

In the last part we have discussed about the Metal Stack. The way foundry provide data, different restrictions and available options. Now it's time to understand the very next step - how to communicate the complex Metal Stack information across the design team or groups or companies. For this Foundry also provide Nomenclature of metal stack.

If you remember in the last article we have discussed that there are different metal wires like Mx, My, Mz, Mr , Mu, etc (in XYZ Foundry). Below diagram can help you to remind this very well.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjccLBKxRsJ28WtqOBk17v4p28O0BePLfhiiP2cPmPlHRILZkvJmIryMg4zv_AP13X-yYoMF-ynKsMBlmmF1SdwLRDc9Fp0YJYSeBQCmu9Xjop16O9EdlF6DGNr7J_B2JoCTv_M3PeZgwM/s640/metalization+option+1.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjccLBKxRsJ28WtqOBk17v4p28O0BePLfhiiP2cPmPlHRILZkvJmIryMg4zv_AP13X-yYoMF-ynKsMBlmmF1SdwLRDc9Fp0YJYSeBQCmu9Xjop16O9EdlF6DGNr7J_B2JoCTv_M3PeZgwM/s1600/metalization+option+1.PNG)

Now, lets suppose you want to use Stack type 7 and same you want to communicate to other user, then there is a standard way for this. (You might be thinking that I will communicate directly that you are referring Stack type 7. But if we do this - every time user has to refer this table to understand different metal layer optons. :) ).

If you will check closely the Stack Type 7, you will find below information.

- There are Total 6 metal layers.
- Metal 1 is of M1 type.
- Metal 2, 3, 4 are of Mx type. Means next 3 Metal layers (After M1) are of Mx type.
- Metal 5 is of My type. Means next 1 metal layer (after Mx) is of is of My type.
- Metal 6 is of Mz type. Means next 1 metal layer (after My) is of is of Mz type.

Now, if I combine all this information and write something like this.

**M1\_3Mx\_My\_Mz : 1 (M1 Type) + 3 (Mx type) + 1 (My Type) + 1 (Mz Type) = 6 Metal layer.**

Between 2 metal layers (e.g M1 and M2) - we will use VIA as per upper metal layer type (e.g Vx type)

The way I have defined the sequence also help to understand the sequence of Metal layer.

Any one can now interpret that :

**Metal 1** = M1

**Metal 2** = Mx1 (Mx Type)

**Metal 3** = Mx2 (Mx Type)

**Metal 4** = Mx3 (Mx Type)

**Metal 5** = My1 (My Type)

**Metal 6** = Mz1 (Mz Type)

**VIA 1** = Vx1 (Vx type)

**VIA 2** = Vx1 (Vx type)

**VIA 3** = Vx1 (Vx type)

**VIA 4** = Vx1 (Vy type)

**VIA 5** = Vx1 (Vz type)

Remember, number of VIAs are always 1 less then the number of Metal layers. :)

Different companies uses different way to understand this. Like following are few examples.

1. **M1\_3Mx\_My\_Mz** : 1 (M1 Type) + 3 (Mx type) + 1 (My Type) + 1 (Mz Type) = 6 Metal layer.
2. **3Mx\_My\_Mz** : 1 (M1 Type) + 3 (Mx type) + 1 (My Type) + 1 (Mz Type) = 6 Metal layer.
3. **3MxMyMz** : 1 (M1 Type) + 3 (Mx type) + 1 (My Type) + 1 (Mz Type) = 6 Metal layer.
4. **6M\_3MxMyMz** : 1 (M1 Type) + 3 (Mx type) + 1 (My Type) + 1 (Mz Type) = 6 Metal layer.
5. **1P6M\_3MxMyMz** : 1 (M1 Type) + 3 (Mx type) + 1 (My Type) + 1 (Mz Type) = 6 Metal layer.

**Note:**

- In the 2nd, 3rd, 4th and 5th option, First Metal layer M1 is considered by default.
- In the 4th option, It was mentioned explicitly that stack has 6 metal layer (6M).
- In the 5th option, It was mentioned explicitly that stack has 1 Poly layer (1P) and 6 metal layer (6M).

For the above figure, I have added all the nomenclature as per 5th option. Also for your easiness, I have mentioned Stack name at the Top and Bottom (both places same information). I am sure, after this there will be no confusion. :)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfdhboS0P98-Svm6xMKOfqrWTHyhMVcJ23mOI9nSuwGrgqZRNHycIEBBY1OCo8RilLBdTLMfSvnVuVNVim-bPDvoaSXz-JRxgm29HkXD2TA5nH4kZcoUhM0C4Nh-rYChGlNiUYW4da7Aw/s640/metalization+option+3.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfdhboS0P98-Svm6xMKOfqrWTHyhMVcJ23mOI9nSuwGrgqZRNHycIEBBY1OCo8RilLBdTLMfSvnVuVNVim-bPDvoaSXz-JRxgm29HkXD2TA5nH4kZcoUhM0C4Nh-rYChGlNiUYW4da7Aw/s1600/metalization+option+3.PNG)

In the last, I just wanted to highlight that above nomenclature and metal stack options is for 1 foundry. But different Foundries may have different ways to provide and representation their information. With in the companies or group or team, they can also decide their own way to represent Metal Stack but when they communicate with outside world, either they have to use certain standard or they have to provide details of their nomenclature (which is very common).

Posted by
VLSI Expert
at
[1:10 PM](https://www.vlsi-expert.com/2017/10/metal-layer-stack-nomenclature-part-2.html "")[4\\
comments](https://www.vlsi-expert.com/2017/10/metal-layer-stack-nomenclature-part-2.html#)

## Monday, October 23, 2017

### [Metal Layer Stack (Metallization Option) Part 1](https://www.vlsi-expert.com/2017/10/metal-layer-stack-metallization-option1.html)

There are different metal layers which we uses in our design. As we move down the technology node number of standard cells increases or you can say that number of connections increases drastically. As all of us know that these connection are made of Metal wire, it means number of metal wires increases. Below figure help you to understand the scenario.

**Case1** : I didn't decrease the size of the chip (despite change in the no of standard cells per unit area) as we go down the technology node. You can see that number of metal wires increases. Silicon utilization improves with improved routability. But these numbers (standard cell) increases 4 times (per node if we are decreases the size by 1/2, overall area decreases by 1/2\*1/2=1/4). With available options of metal wire in higher node, it's difficult to route the same design in lower technology node. And that's the reason as we go down number of metal wires increases (vertically also).

**Case 2**: This is the real scenario. As Technology node decreases, no of standard cells increases and also chip size decreases. So you can imagine how difficult it is to route the design with a single metal wire or say on a single level. That's the reason we have multiple levels of metal wires. These levels are in vertical direction. As we go down the technology node, these levels increases. So you can say that down the technology node, size of the chip decreases in one dimension (in 2D) but increases in other dimension (vertically). :) :)

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 19. Untitled

**URL:** https://www.vlsi-expert.com/2017/04/
**Date:** 2017-04
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2017-10-02T01:01:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2017-04-12T07:32:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 20. Untitled

**URL:** https://www.vlsi-expert.com/2016/04/
**Date:** 2016-04
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2016-09-13T12:58:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2016-04-20T12:39:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 21. Untitled

**URL:** https://www.vlsi-expert.com/2016/03/
**Date:** 2016-03
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2016-06-01T20:43:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2016-03-13T23:53:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 22. Untitled

**URL:** https://www.vlsi-expert.com/2016/01/
**Date:** 2016-01
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2016-02-08T03:47:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2016-01-20T14:08:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 23. Untitled

**URL:** https://www.vlsi-expert.com/2015/08/
**Date:** 2015-08
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2015-09-24T01:13:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2015-08-03T05:02:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 24. ## Monday, November 17, 2014

**URL:** https://www.vlsi-expert.com/2014/
**Date:** 2015-07-19
**Tags:** dft, ESD, CMOS, parasitic, analog

## Monday, November 17, 2014

### [CMOS Layout Design: Introduction](https://www.vlsi-expert.com/2014/11/cmos-layout-design.html)

## CMOS Layout Design: Introduction

## Thursday, November 6, 2014

### [Create Contact and Metal-M1: CMOS Processing (Part 6)](https://www.vlsi-expert.com/2014/11/Metal-Contact.html)

## Create Contact and Metal-M1

## Wednesday, November 5, 2014

### [Implant P+ Impurities: CMOS Processing (Part 5)](https://www.vlsi-expert.com/2014/11/Implant-p-impurity.html)

## Implant P+ Impurities: CMOS Processing (Part 5)

## Monday, November 3, 2014

### [Implant N+ Impurities: CMOS Processing (Part 4)](https://www.vlsi-expert.com/2014/11/ImplantNImpurity.html)

## Implant N+ Impurities:

## Tuesday, September 9, 2014

### [Creating Gate Oxide and Poly Layer: CMOS Processing (Part3)](https://www.vlsi-expert.com/2014/09/creating-gate-oxide-and-poly-layer-cmos.html)

**Creating Gate Oxide and Poly Layer**

## Saturday, September 6, 2014

### [Create N-well And Field Oxide: CMOS Processing (Part 2)](https://www.vlsi-expert.com/2014/09/create-n-well-and-field-oxide-cmos.html)

**Create N-well And Field Oxide**

## Thursday, September 4, 2014

### [Fabrication Steps: CMOS Processing (Part 1)](https://www.vlsi-expert.com/2014/09/fabrication-steps-cmos-processing-part-1.html)

## Fabrication Steps: CMOS Processing

[Newer ](https://www.vlsi-expert.com/search?updated-max=2015-07-19T11:24:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2014-09-04T15:27:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 25. Untitled

**URL:** https://www.vlsi-expert.com/2014/12/
**Date:** 2014-12
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2015-07-19T11:24:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2014-12-25T10:52:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 26. ## Thursday, November 6, 2014

**URL:** https://www.vlsi-expert.com/2014/11/
**Date:** 2014-11
**Tags:** CMOS, ESD, dft, parasitic

## Thursday, November 6, 2014

### [Create Contact and Metal-M1: CMOS Processing (Part 6)](https://www.vlsi-expert.com/2014/11/Metal-Contact.html)

## Create Contact and Metal-M1

## Wednesday, November 5, 2014

### [Implant P+ Impurities: CMOS Processing (Part 5)](https://www.vlsi-expert.com/2014/11/Implant-p-impurity.html)

## Implant P+ Impurities: CMOS Processing (Part 5)

## Monday, November 3, 2014

### [Implant N+ Impurities: CMOS Processing (Part 4)](https://www.vlsi-expert.com/2014/11/ImplantNImpurity.html)

## Implant N+ Impurities:

[Newer ](https://www.vlsi-expert.com/search?updated-max=2015-07-17T13:23:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2014-11-03T23:11:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 27. ### Isotropic Etch Process:

**URL:** https://www.vlsi-expert.com/2014/07/
**Date:** 2014-07
**Tags:** physical-design, dft, parasitic

### Isotropic Etch Process:

In the Isotropic etch process etchant attacks the layer surfaces equally in all the directions.  Most of the liquid etchant are isotropic. Since etchant attacks in all the direction (horizontal and vertical both direction), the resultant layer shape is not as per the expectation. Below figure help you to understand.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6ohdOpttIXUBL-AYf-XIwo-1oXhwsuBBpjvTb0fYVdeyLBUPCCXQM5YUxCtP3tgY0KuV-G6qfqj0R-EtTsxa10mXVzfx83jdaBGhAnKFwxFHIrEGDArkl7jNpyAJjre1Nto4FD_rEIEY/s1600/Etching4.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6ohdOpttIXUBL-AYf-XIwo-1oXhwsuBBpjvTb0fYVdeyLBUPCCXQM5YUxCtP3tgY0KuV-G6qfqj0R-EtTsxa10mXVzfx83jdaBGhAnKFwxFHIrEGDArkl7jNpyAJjre1Nto4FD_rEIEY/s1600/Etching4.jpg)

You can see that the resultant layer become narrow in size. When the layer width and spacing is significantly larger than the thickness of the layer, Isotropic results a minor problem but when layer width and spacing is comparable to thickness of the layer then plasma etching technique which is capable of anisotropic etching is used (I will discuss this later in post).

As per the etchant solution, if amount of narrowing the feature in horizontal direction can be figured out, we can use compensation method to make it as ideal as possible. In the mask compensation method, the mask size is increased from the desired size of layer (which increase the width of deposited Resist) in such a way that after etching and stripping of Resist, resultant layer width becomes equal to (or approximately equal to) required size. But again this method can’t be used if thickness of layer is comparable to width/size of layer.

Below diagram helps you to understand the final result of isotropic etching in more detail.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxQ-hwznVommiw1JtwAQL1QL5HyuBH4zWfZorUzp4sr5Y1R__TJTwhlN_4jJvbe72EG-P7p6NllXVCTcFiNJGcg7pRloCkKnRk5nBIFdHLTe4ghH1nG213HfkLTRFqh-EVBg0hYBgQPPM/s1600/Etching5.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxQ-hwznVommiw1JtwAQL1QL5HyuBH4zWfZorUzp4sr5Y1R__TJTwhlN_4jJvbe72EG-P7p6NllXVCTcFiNJGcg7pRloCkKnRk5nBIFdHLTe4ghH1nG213HfkLTRFqh-EVBg0hYBgQPPM/s1600/Etching5.jpg)

Now correlate this with the actual process which we have discussed in the previous part. I have just changed the color so that you can understand this clearly.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWQbj0G-WvZr8Zg__1T6DRHATopMY6ouwfhqORIuQ3nvCNA9V_wE_OtGtAtMDPYCB0Kxv4XvWifZskfn-KlHGu7lV55x6BhkhjHm1WHo_PxU46yRgyfCYz2dioh80I_fbWoBiO0uXYhug/s1600/Etching2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWQbj0G-WvZr8Zg__1T6DRHATopMY6ouwfhqORIuQ3nvCNA9V_wE_OtGtAtMDPYCB0Kxv4XvWifZskfn-KlHGu7lV55x6BhkhjHm1WHo_PxU46yRgyfCYz2dioh80I_fbWoBiO0uXYhug/s1600/Etching2.jpg)

### Anisotropic Etching Process:

As I have mentioned above, when layer width and spacing is comparable to thickness of the layer then plasma etching technique which is capable of anisotropic etching is used.  You can understand this with the following diagram.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghwQ658nRPdZHrH1XdulZWT_SEop8VrETMQqYaG65S_LeZWfz7n29EHlwg7SRd-5vwUMG4JDecIXV8QGif9Tw_XUgf57lAGNoJbfsvJUmXgn0f4CYjcoOaNlSWfua9I22XWj_kLUX__6I/s1600/Etching3.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghwQ658nRPdZHrH1XdulZWT_SEop8VrETMQqYaG65S_LeZWfz7n29EHlwg7SRd-5vwUMG4JDecIXV8QGif9Tw_XUgf57lAGNoJbfsvJUmXgn0f4CYjcoOaNlSWfua9I22XWj_kLUX__6I/s1600/Etching3.jpg)

The degree of Anisotropy of an etch process can be expressed as:

A = 1 – Vh/Vv

Where

A = Degree of Anisotropy

Vh = horizontal Etch rate

Vv = Vertical Etch Rate

When A=0, it represent Isotropic etching and A=1 represent Anisotropic etching.

Remember, we always try to get A=1 but that’s the ideal scenario. :) In the above diagram, I have mentioned Directional Etch and that’s the thing we can get practically. :)

You might be confused but below figures can remove your confusion (I captured these figures from Internet and then just modified little bit)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6Wx60F2PDYWaUKSrHWeEUPU41iLzPEWwUdFyMH8xhQ2rr45Aw-_h_ACx_bAICU51Mgzr-S677cZHkn1osX3uHjpDWf7MufjN-HnHNjEVFAA2ZWUbX4r3hukySbfrQRFmcIWN0K72x-ss/s1600/Etching6.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6Wx60F2PDYWaUKSrHWeEUPU41iLzPEWwUdFyMH8xhQ2rr45Aw-_h_ACx_bAICU51Mgzr-S677cZHkn1osX3uHjpDWf7MufjN-HnHNjEVFAA2ZWUbX4r3hukySbfrQRFmcIWN0K72x-ss/s1600/Etching6.jpg)

From above you can see that in case of Isotropic – Etch rate is same in all the direction, Anisotropic – highly directional etching with different etch rate in different directions.

Now you may ask how this (isotropic and anisotropic) is going to affect differently our process, I will explain this again with the help of following fig (again from Internet).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgenxlRI1K0m_hyphenhyphenOJtLjzGGYTr_2Zrvn2XoAa-d2LdHQdzjHKi5ByIYQUx1Ks-0tEHAtU2jrGsJgeDntETrcCK6ZTAVF66_GWqE6JFyFH5LRFa1akqwK2eUUdV7UWQ-VF182Qp5tm6RgGE/s1600/Etching7.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgenxlRI1K0m_hyphenhyphenOJtLjzGGYTr_2Zrvn2XoAa-d2LdHQdzjHKi5ByIYQUx1Ks-0tEHAtU2jrGsJgeDntETrcCK6ZTAVF66_GWqE6JFyFH5LRFa1akqwK2eUUdV7UWQ-VF182Qp5tm6RgGE/s1600/Etching7.jpg)

Here you can see that metal “BIAS” is different in different cases.

In case of Isotropic, we don’t have control in the horizontal direction. It’s equal in both direction and that’s the reason I have mentioned previously that if width is larger than thickness – we can use Isotropic but when with is comparable to height, then if we use this process, then we will get very small (or almost zero) width of the layer (I hope you can imagine this).

In case of Anisotropic, we can control horizontal biasing/etching. And we always like those things which are in our control. J

**_From the Above discussion, It's clear that In the Width Variation of Metal or Dielectric - Etching has an Important role._**

I hope this much is sufficient to build a base of etching process effects. But before I will write my final words, I would like to touch few more things which are related to Etch process just in the form of Summary.

**What is ETCHING?**

As the name suggest it’s the process of removing something. In the semiconductor world – It’s the process of chemically removing layers from the surface of wafer during manufacturing.

**Few things we have to remember:**

- Every wafer has to undergo with several etching steps.
- You can’t skip the Etching steps and none of the etching process is ideal.
- Depends on the type of Etching process, you are using – type of defects are introduces in the chip and also depend the intensity of those defects.

**There are 2 type of etch process** (apart of Isotropic and Anisotropic – which we have discussed above):

1. **Wet Etch**

 - Liquid Etchant
 - Chemical process Only
 - Advantage:

 - Low Cost and easy to implement
 - High etching rate
 - Good selectivity for most material.

 - Disadvantage:

 - Very hard to control critical feature Dimension
 - Eliminates Toxic fumes.

3. **Dry etch**

 - Gas Phase etchants in a plasma
 - Chemical and physical (sputtering) process
 - Advantage:

 - Both isotropic and anisotropic process can be done.
 - High resolution and cleanliness
 - Better process control
 - Ease of automation.

In the next part we will discuss one more effect of Etching and then the way foundry model these variation’s effects.

Posted by
VLSI Expert
at
[8:57 AM](https://www.vlsi-expert.com/2014/07/effect-of-etching-process_28.html "")[4\\
comments](https://www.vlsi-expert.com/2014/07/effect-of-etching-process_28.html#)

[Newer ](https://www.vlsi-expert.com/search?updated-max=2014-09-06T09:47:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2014-07-28T08:57:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 28. ## Thursday, December 19, 2013

**URL:** https://www.vlsi-expert.com/2013/
**Date:** 2014-01-10
**Tags:** dft, parasitic

## Thursday, December 19, 2013

### [DIGITAL BASIC - 1.4 : Combinational Circuits](https://www.vlsi-expert.com/2013/12/digital-basic-14-combinational-circuits.html)

### **Introduction**

[Newer ](https://www.vlsi-expert.com/search?updated-max=2014-01-10T17:17:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2013-12-19T06:46:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 29. Untitled

**URL:** https://www.vlsi-expert.com/2013/04/
**Date:** 2013-04
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2013-10-05T22:58:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2013-04-26T00:33:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 30. Untitled

**URL:** https://www.vlsi-expert.com/2013/03/
**Date:** 2013-03
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2013-05-10T19:22:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2013-03-02T10:04:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 31. Untitled

**URL:** https://www.vlsi-expert.com/2013/01/
**Date:** 2013-01
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2013-04-26T00:33:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2013-01-24T11:21:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 32. ## Monday, February 20, 2012

**URL:** https://www.vlsi-expert.com/2012/02/
**Date:** 2012-02
**Tags:** dft, parasitic

## Monday, February 20, 2012

### [Design constraint : Maximum Fanout](https://www.vlsi-expert.com/2012/02/design-constraint-maximum-fanout.html)

Error 404 (Not Found)!!1

**404.** That’s an error.

The requested URL `/host/0B8GyWNXT7IOJaWZ1VUFLVVc1a2M` was not found on this server. That’s all we know.

[Newer ](https://www.vlsi-expert.com/search?updated-max=2012-04-13T19:35:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2012-02-20T18:32:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 33. Untitled

**URL:** https://www.vlsi-expert.com/2011/09/
**Date:** 2011-09
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2012-02-12T02:33:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2011-09-11T21:55:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 34. ## Friday, March 18, 2011

**URL:** https://www.vlsi-expert.com/2011/03/
**Date:** 2011-03
**Tags:** sta, ESD, dft, parasitic

## Friday, March 18, 2011

### [How To Read SDF (Standard Delay Format) - Part3](https://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format_17.html)

Error 404 (Not Found)!!1

**404.** That’s an error.

The requested URL `/host/0B8GyWNXT7IOJaWZ1VUFLVVc1a2M` was not found on this server. That’s all we know.

## Wednesday, March 16, 2011

### [How To Read SDF (Standard Delay Format) - Part2](https://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format_16.html)

Error 404 (Not Found)!!1

**404.** That’s an error.

The requested URL `/host/0B8GyWNXT7IOJaWZ1VUFLVVc1a2M` was not found on this server. That’s all we know.

[Newer ](https://www.vlsi-expert.com/search?updated-max=2011-04-08T00:45:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2011-03-16T22:34:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 35. Untitled

**URL:** https://www.vlsi-expert.com/2010/09/
**Date:** 2010-09
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2011-02-06T01:15:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2010-09-22T23:59:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 36. [Newer ](https://www.vlsi-expert.com/search?updated-max=2010-08-24T00:59:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Home](https://www.vlsi-expert.com/)

**URL:** https://www.vlsi-expert.com/2008/
**Date:** 2010-08-24
**Tags:** dft, parasitic

[Newer ](https://www.vlsi-expert.com/search?updated-max=2010-08-24T00:59:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

## Sta

### 1. #### 11 comments:

**URL:** https://www.vlsi-expert.com/p/static-timing-analysis.html
**Date:** Unknown
**Tags:** sta, dft, parasitic

#### 11 comments:

01. ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHkSgA9ATcndkIRF92c4vhyAgUDWe_0QSGedwfryVwT_HfM38iI-Oj-ZEiNYEEDutsZDy5oEDoAABf4k27Zgrlhby7BkIt-qeI5M0Z1zM83zRWbVJerFdQkUFVor9onnY/s45-c/kite1.png)

 [December 15, 2015 at 7:42 PM](https://www.vlsi-expert.com/p/static-timing-analysis.html)

 Fantastic information. Really appreciate it. You succeeded in explaining what many tool manuals don't explain.

 I am only missing one thing in this blog, though. Giving an STA example from the point of view of one interface. E.g. we are designing an SPI slave controller which needs to interface an SPI master for which we have a timing diagram.

 I find extremely annoying the way timing diagrams are explained in datasheets, and how to match the different specs given there to the concepts (Ts and Th basically) you have introduced in the blog.

 Thanks

 Reply

 Replies

 Reply

02. !

 [June 6, 2016 at 12:52 AM](https://www.vlsi-expert.com/p/static-timing-analysis.html)

 superb information about vlsi..

 now its my fav website for gain vlsi knowledge....

 Reply

 Replies

 Reply

03. !

 [June 17, 2016 at 11:10 PM](https://www.vlsi-expert.com/p/static-timing-analysis.html)

 very good explanation.... thanks a lot

 Reply

 Replies

 Reply

04. !

 [January 24, 2017 at 6:28 PM](https://www.vlsi-expert.com/p/static-timing-analysis.html)

 At [this source](https://pro-academic-writers.com/blog/argumentative-essay-topics) collected numerous writing tips and writers' secrets that would be a great help for novices.

 Reply

 Replies

 Reply

05. !

 [March 29, 2017 at 7:59 PM](https://www.vlsi-expert.com/p/static-timing-analysis.html)

 sir u r awessome ...best VLSI blog i ever seen

 Thank u sir

 Reply

 Replies

 Reply

06. !

 [September 11, 2017 at 1:15 PM](https://www.vlsi-expert.com/p/static-timing-analysis.html)

 how to download this concepts ..?

 Reply

 Replies

 Reply

07. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 30, 2017 at 10:50 PM](https://www.vlsi-expert.com/p/static-timing-analysis.html)

 Hi

 i would like to thank you for your effort of creating this amazing and comprehensive site.

 it really helped me to get the whole picture of the STA analysis and constraints.

 Well done!

 Reply

 Replies

 Reply

08. !

 [October 3, 2017 at 2:33 AM](https://www.vlsi-expert.com/p/static-timing-analysis.html)

 You indeed have described it to-the-point and covered all important points while keeping it brief, with easy to understand language.

 Thanks for the knowledge sharing.

 Reply

 Replies

 Reply

09. !

 [November 7, 2017 at 11:49 AM](https://www.vlsi-expert.com/p/static-timing-analysis.html)

 Which latency is good 5ns and 3ns?

 In both case timing is met

 Reply

 Replies

 Reply

10. !

 [April 18, 2018 at 10:30 PM](https://www.vlsi-expert.com/p/static-timing-analysis.html)

 really a awesome material.

 Reply

 Replies

 Reply

11. !

 [May 7, 2018 at 11:38 PM](https://www.vlsi-expert.com/p/static-timing-analysis.html)

 Really very good explanation, I always refer this for clarifying my doubts about timing analysis..

 Reply

 Replies

 Reply

Add comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

Load more...

[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 2. ## Saturday, December 14, 2019

**URL:** https://www.vlsi-expert.com/2019/12/
**Date:** 2019-12
**Tags:** physical-design, sta, OPC, digital-design, dft, parasitic, analog

## Saturday, December 14, 2019

### [How To Read SDF (Standard Delay Format) - Part5](https://www.vlsi-expert.com/2019/12/standard-delay-format-5.html)

In the last few articles ( [PART 1](http://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format.html), [PART 2](http://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format_16.html) and [PART 3](http://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format_17.html)), we have discussed the following things

- SDF different sections and different construct - In [PART 2](http://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format_16.html)
- Cell Section details - In [PART 3](http://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format_17.html)
- Delay Details in SDF - In [PART 4](http://www.vlsi-expert.com/2019/12/standard-delay-format-4.html)

Now. it's the time to discuss about the SDF using an example.

Lets discuss the below circuit.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-laVviWsQh8mcy7U_EPgQKg3L9qhgnZfpZ0Rcvu3rgA5ydy6MBbgou6SZ4dXs41l0HVc1BojP4Jq5nM6qU1il8hUfhgEyKZDpilFrKM28ZoClM1h2R_kOpTftCV9UEVSUkayGhrbRF7M/s400/example1.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-laVviWsQh8mcy7U_EPgQKg3L9qhgnZfpZ0Rcvu3rgA5ydy6MBbgou6SZ4dXs41l0HVc1BojP4Jq5nM6qU1il8hUfhgEyKZDpilFrKM28ZoClM1h2R_kOpTftCV9UEVSUkayGhrbRF7M/s1600/example1.PNG)

As a part of SDF, if you remember, we have discussed in [PART 2](http://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format_16.html) \- that there is a HEADER section, Then CELL Section. In our circuit, there are 5 instance of Cells - r1, r2, r3, u1 & u2. These cells are mapped with Library as (This information you can get from .lib or from .v file)

**r1, r2 and r3 -> DFF\_X1**

**u1 -> BUF\_X1**

**u2 -> AND2\_X1**

Header Section - marked as RED Color

CELL Section where we are talking about interconnect Delays - marked as GREEN color

CELL Section with respect to Flipflops - marked as BLUE color

CELL Section with respect to Buffer - marked as BLACK color

CELL Section with respect to AND gate - marked as LIGHT GREEN color.

And that's all the construct.

> (DELAYFILE
>
> (SDFVERSION "OVI 2.1")
>
> (DESIGN "vlsiexpert")
>
> (DATE "Thu Dec 12 20:33:26 2019")
>
> (VENDOR "vlsiexpert")
>
> (PROGRAM "customized")
>
> (VERSION "01")
>
> (DIVIDER /)
>
> (VOLTAGE 2.25:2.25:2.25)
>
> (PROCESS "1.000:1.000:1.000")
>
> (TEMPERATURE 125.00:125.00:125.00)
>
> (TIMESCALE 1ns)
>
> (CELL
>
> (CELLTYPE "vlsiexpert")
>
> (INSTANCE)
>
> (DELAY
>
>     (ABSOLUTE
>
> // Offset in1 vs in2, rise vs fall arrivals so results are deterministic.
>
>      (INTERCONNECT in1 r1/D (0.011:0.011:0.011) (0.01:0.01:0.01))
>
>      (INTERCONNECT in2 r2/D (0.021:0.021:0.021) (0.02:0.02:0.02))
>
>      (INTERCONNECT clk1 r1/CK (0.0:0.0:0.0) (0.0:0.0:0.0))
>
>      (INTERCONNECT clk2 r2/CK (0.0:0.0:0.0) (0.0:0.0:0.0))
>
>      (INTERCONNECT clk3 r3/CK (0.0:0.0:0.0) (0.0:0.0:0.0))
>
>      (INTERCONNECT r1/Q u2/A1 (0.0:0.0:0.0) (0.0:0.0:0.0))
>
>      (INTERCONNECT r2/Q u1/A (0.0:0.0:0.0) (0.0:0.0:0.0))
>
>      (INTERCONNECT u1/Z u2/A2 (0.0:0.0:0.0) (0.0:0.0:0.0))
>
>      (INTERCONNECT u2/ZN r3/D (0.0:0.0:0.0) (0.0:0.0:0.0))
>
>      (INTERCONNECT r3/Q out (0.0:0.0:0.0) (0.0:0.0:0.0))
>
>     )
>
> )
>
> )
>
> (CELL
>
> (CELLTYPE "DFF\_X1")
>
> ( **INSTANCE r1**)
>
> (DELAY
>
> (ABSOLUTE
>
>     (IOPATH CK Q (1:1:1) (1.1:1.1:1.1))
>
> )
>
> )
>
> (TIMINGCHECK
>
> (SETUP D (posedge CK) (.5:.5:.5))
>
> (HOLD D (posedge CK) (.1:.1:.1))
>
> (PERIOD (posedge CK) (1.0:2.0:3.0))
>
> )
>
> )
>
> (CELL
>
> (CELLTYPE "DFF\_X1")
>
> ( **INSTANCE r2**)
>
> (DELAY
>
> (ABSOLUTE
>
>     (IOPATH CK Q (1:1:1) (1.1:1.1:1.1))
>
> )
>
> )
>
> (TIMINGCHECK
>
> (SETUP D (posedge CK) (.5:.5:.5))
>
> (HOLD D (posedge CK) (.1:.1:.1))
>
> (PERIOD (posedge CK) (1.0:2.0:3.0))
>
> )
>
> )
>
> (CELL
>
> (CELLTYPE "DFF\_X1")
>
> ( **INSTANCE r3**)
>
> (DELAY
>
> (ABSOLUTE
>
>     (IOPATH CK Q (1:1:1) (1.1:1.1:1.1))
>
> )
>
> )
>
> (TIMINGCHECK
>
> (SETUP D (posedge CK) (.5:.5:.5))
>
> (HOLD D (posedge CK) (.1:.1:.1))
>
> (PERIOD (posedge CK) (1.0:2.0:3.0))
>
> )
>
> )
>
> (CELL
>
> (CELLTYPE "BUF\_X1")
>
> ( **INSTANCE u1**)
>
> (DELAY
>
> (ABSOLUTE
>
>     (IOPATH A Z (1:1:1) (1.1:1.1:1.1))
>
> )
>
> )
>
> )
>
> (CELL
>
> (CELLTYPE "AND2\_X1")
>
> ( **INSTANCE u2**)
>
> (DELAY
>
> (ABSOLUTE
>
>     (IOPATH A1 ZN (1:1:1) (1.1:1.1:1.1))
>
>     (IOPATH A2 ZN (1:1:1) (1.1:1.1:1.1))
>
> )
>
> )
>
> )
>
> )

**Note:**

- In the Interconnect Delay, SDF has delays of all 10 wires/interconnects.

 - Input port to Reg input D pin (in1 to r1/D , in2 to r2/D)
 - Clock\_source to Clock\_input pin of Register (clk1 to r1/CK, clk2 to r2/CK, clk3 to r3/CK)
 - Reg output Q pin to Output port (r3/Q to out)
 - All internal combinational nets

- For all flipflop we have all required info which we need from .Lib

 - Clock to Q delay
 - Setup and Hold constraint
 - Positive Edge or Negative Edge triggered Flipflop
 - Clock Time period information

- For all other logic cells, we have following information

 - Cell Rising and Falling delay
 - Cell - Min, Max and Typical Delay
 - Input pin - output pin specific delay (also know as ARC delay - like in case of AND - a->y and b-y)

Posted by
VLSI Expert
at
[6:57 PM](https://www.vlsi-expert.com/2019/12/standard-delay-format-5.html "")[0\\
comments](https://www.vlsi-expert.com/2019/12/standard-delay-format-5.html#)

## Thursday, December 12, 2019

### [How To Read SDF (Standard Delay Format) - Part4](https://www.vlsi-expert.com/2019/12/standard-delay-format-4.html)

In the last few articles ( [PART 1](http://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format.html), [PART 2](http://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format_16.html) and [PART 3](http://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format_17.html)), we have discussed the following things

- What is SDF and what information it contain?
- Construct of SDF (2 Section – Header and CELL)

 - Header Section contain general information about the Tool which is used to create/generate the SDF and the Design related information (like Design name, Process, Voltage, Temperature of the design for which SDF is generated).
 - Cell Section can be multiple in the SDF file. These CELL section can represent to a specific Primitive cell (standard Cell) or a region of the design (Blocks) or any instance in a hierarchy.
 - Cell section has 3 different sub-section – CELLTYPE , INSTANCE, Timing specification section.
 - Timing specification section contain actual timing data associated with that cell. There are four types of timing specifications that are identified by the DELAY, TIMINGCHECK, TIMINGENV, and LABEL keywords.

 - DELAY: Specify the delay related information for back-annotation.
 - TIMINGCHECK: Specify Timing checks limit data for back-annotation
 - TIMINGENV: Specify timing environment data and constraint data for forward-annotation.
 - LABEL: Set the values of timing model variables upon that delays and timing constraint values depend

In this Article, we will discuss more details about the DELAY construct. This is the most important part of the SDF. It’s a Standard Delay format – so it’s important to have a separate Article only for Delay.

Delay values are defined in SDF in the form of list. This list can have 1,2,3,6 or 12 pairs. These pairs are corresponds to the transition of the signal at the output port. The sequence of those transition is fixed and described in the following table.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvqkahBdYryLrJvFHBZYWGRF2o96LJjfXkKkqDdlF7f4h56cl5hVGKt-e2jbOXShCANkCT8fGtY8oq-S5dRYt-U5h5Xn90GSUiF4O2YQYJzef8dbxCmi57VYE12gWcj7MPRj9urHZeVTY/s640/sdf+delay+table.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvqkahBdYryLrJvFHBZYWGRF2o96LJjfXkKkqDdlF7f4h56cl5hVGKt-e2jbOXShCANkCT8fGtY8oq-S5dRYt-U5h5Xn90GSUiF4O2YQYJzef8dbxCmi57VYE12gWcj7MPRj9urHZeVTY/s1600/sdf+delay+table.PNG)

**Note:**

- If only 1 pair is present in the delay list then it’s same for all 12 transition.
- There are chances that in SDF, any pair has NULL value. It is consider as placeholder for that particular transition. Means the stage where SDF is created, the delay info corresponding to that transition is not available and later it can be filled.

**Example 1: (IOPATH i3 o1 () () (2:4:5) (4:5:6) (2:4:5) (4:5:6))**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNIIr3BQtCYz2WZpOADp9RbeQJpcNCqAwB8nMhAeU_yR65QBxH-gjsGZOOGHyt0mbYtirP2SA3rJEanRvMnRuMDvMLC1OlGWO1tO02HH7Z5ICVq9AKxFQKtJwu8h8ybsdvyw2Aryj7ZHw/s640/example_sdf.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNIIr3BQtCYz2WZpOADp9RbeQJpcNCqAwB8nMhAeU_yR65QBxH-gjsGZOOGHyt0mbYtirP2SA3rJEanRvMnRuMDvMLC1OlGWO1tO02HH7Z5ICVq9AKxFQKtJwu8h8ybsdvyw2Aryj7ZHw/s1600/example_sdf.png)

In the above example, there is no delay value present for 0->1 and 1->0 transition.

### Type of Delay:

There are 2 types of Delay based on how it will be annotated into the design.

**Incremental Delay:** If any delay value is defined under this category it means it will add SDF value into the Delay present in the design (at the time you are trying to annotate SDF delay).

**Absolute Delay:** If any delay value is defined under this category it means it will replace the Delay present in the design (at the time you are trying to annotate SDF delay).

### Category of Delay in SDF:

Delay in the SDF can be any of the following category.

**1) Input-output path Delay:**

- Represent the delays on a legal path from an input/bidirectional port to an output/bidirectional port of a device. Each delay value shall be associated with a unique input\_port - output\_port pair.
- Input or a bidirectional port can have an edge identifier.
- No edge Identifier can be present in case of output or a bidirectional port.
- Representation of Delay values are in the same fashion as explained in above.
- Construct used in SDF : IOPATH

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhw769yupYXGVys6Je71p3yRs_q6fGxAKy2ddz8qNt4Q-HXr-kjeJnMgwSFh-kqr7Nts5jxpNKQdNJttgulP8b-hSPxLWOZR6dqdF-MiuH0lK9HZI4pnnY-JyZPJj6mTUaWyFhnKVK4lDk/s400/Input-Output-pathdelay-sdf.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhw769yupYXGVys6Je71p3yRs_q6fGxAKy2ddz8qNt4Q-HXr-kjeJnMgwSFh-kqr7Nts5jxpNKQdNJttgulP8b-hSPxLWOZR6dqdF-MiuH0lK9HZI4pnnY-JyZPJj6mTUaWyFhnKVK4lDk/s1600/Input-Output-pathdelay-sdf.PNG)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiAP1zd3wVHi6TmBXCWUE1tY0K8_mQhdZmZd3gSefvPmEOx076y-NweQtOpcUi9QAhNgxjEGTuHzXJur76dF39P6pjOWJ82jVjnU3DReDZcyWa8GUiwJhe7PWVBzRxH77qsoLrQMP2kiXA/s640/sdf+input+output+path+delay.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiAP1zd3wVHi6TmBXCWUE1tY0K8_mQhdZmZd3gSefvPmEOx076y-NweQtOpcUi9QAhNgxjEGTuHzXJur76dF39P6pjOWJ82jVjnU3DReDZcyWa8GUiwJhe7PWVBzRxH77qsoLrQMP2kiXA/s1600/sdf+input+output+path+delay.PNG)

**Note:**

- For in1, positive edge identifier is specified.
- These Delay are absolute (ABSOLUTE) in nature. Means it’s going to replace any delay specified in Timing models for these paths under specified transitions.
- For in3, delay values are NULL for first 2 transition (0->1 and 1->0). It means for these transition, Delay values are unchanged (it will remain as-it-is as in the timing models).

**2) Conditional path delays:**

Now if you want to apply a particular condition before applying a particular path delay, we can use this method. The conditional path delay shall specify conditional (state-dependent) input-to-output path delays.

There are 2 ways to apply the conditions

- If a Particular Condition met, then apply the Delay value

 - The annotator must locate in the timing model a path delay with conditions matching those specified in the SDF file. Other path delays between the same ports but with different conditions shall not receive the data.
 - The expression shall evaluate to a logical signal, rather than a boolean. The analysis tool shall treat a logical zero as FALSE and any other logical value (1, X, or Z) as TRUE. A particular conditional path delay in the timing model shall be used only if the condition is TRUE.
 - Use the SDF Construct : COND

- If a Particular Condition doesn’t met, then apply the Delay value

 - The delay values specified in SDF shall be used if none of the conditions specified for the path in the model are TRUE but a signal must still be propagated over the path.
 - Use the SDF construct: CONDELSE

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVFWrx_IJSsJpowbwEKg7-bcGvv1Spu9nhkceU_3dg6-iCGLurEySnpVjRUZzMzcUX7UxYuUpsqzfFGaZtvuaKWQ7xsUp0g-rMj0BU_GqATo5kLbgH8z5RvzzR2YNUTbGWVoJrHVNOoMI/s640/conditional+path+delay+sdf.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVFWrx_IJSsJpowbwEKg7-bcGvv1Spu9nhkceU_3dg6-iCGLurEySnpVjRUZzMzcUX7UxYuUpsqzfFGaZtvuaKWQ7xsUp0g-rMj0BU_GqATo5kLbgH8z5RvzzR2YNUTbGWVoJrHVNOoMI/s1600/conditional+path+delay+sdf.PNG)

**3) Port Delay:**

- Port delay specify the interconnect delay (actual or estimated) that are modelled as delay at input port.
- Use the SDF Construct: PORT

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzOcQINKGeSgk-TxTlPG5YfhxqzCFQWQm0vm9UBlsAeM0tJjnJfuEwX5fa-QvTjYLzGRIQbgwcRXoAah5fQimGroJeN2Ipshg4HQHv7qOx-b5_0UnFRRQQ8M-zGliOVCUahauDgZ90kOE/s640/portdelay-sdf.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzOcQINKGeSgk-TxTlPG5YfhxqzCFQWQm0vm9UBlsAeM0tJjnJfuEwX5fa-QvTjYLzGRIQbgwcRXoAah5fQimGroJeN2Ipshg4HQHv7qOx-b5_0UnFRRQQ8M-zGliOVCUahauDgZ90kOE/s1600/portdelay-sdf.PNG)

**Note:** Above delay is applied same for net between “y” and “c.r1.a” and “c.r2.a”.

**4) Interconnect Delay**

- The interconnect delay shall specify the propagation delay across a net connecting a driving module port (the source) to a driven module port (the load).
- Either or both ports can be bidirectional. Both source and load ports for the delay path shall be specified.
- Use the SDF Construct: INTERCONNECT

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFJAs6DKAj-3LXCtwa1F0G0ntuau_dFQIX1sw4kQ0OdSACbouUJU9JUAnsxry69vXgtj7HhxtHZX3x7g8Ck-fHVtMI_IP8bw72_wwJDre58y8BIRPSFb4pCyqfQUIpS0L1qC8DnY80rng/s400/interconnect-delay-sdf.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFJAs6DKAj-3LXCtwa1F0G0ntuau_dFQIX1sw4kQ0OdSACbouUJU9JUAnsxry69vXgtj7HhxtHZX3x7g8Ck-fHVtMI_IP8bw72_wwJDre58y8BIRPSFb4pCyqfQUIpS0L1qC8DnY80rng/s1600/interconnect-delay-sdf.PNG)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxiBlBDq8PcQ0YHSQ7EoCfn0yNT7IJaaLAeSC1zv-I_YlABp6HCxU2RswgWm12rYdI9LZRNnZ9HlFqEVFdt6L-R__FkBuDXwAu59BgncNlhVShOlp-Dm4_TTpBga4o8GjG7Wfro_WODtY/s640/sdf+interconnect+delay+example.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxiBlBDq8PcQ0YHSQ7EoCfn0yNT7IJaaLAeSC1zv-I_YlABp6HCxU2RswgWm12rYdI9LZRNnZ9HlFqEVFdt6L-R__FkBuDXwAu59BgncNlhVShOlp-Dm4_TTpBga4o8GjG7Wfro_WODtY/s1600/sdf+interconnect+delay+example.PNG)

**5) Net Delay:**

- The net delays shall specify the propagation delays from all sources to all loads of a net.
- Neither start nor end points for the delay path are specified, and the delays from all the source ports to all the destination ports will have the same value.
- Use the SDF Construct: NETDELAY

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLU81cgs-1Zb_Cv5FW-aR3GQySNwp5YV-L0meerhuntqNtccEYNe6pxw-JoWKpBtgFn46t_fGGNS3wPvTuno-z159HVqfvVuV_jtYecJAUKi0urnuTOehlzmBqkFzEEeE4fBH1QenMeWU/s640/netdelay+sdf.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLU81cgs-1Zb_Cv5FW-aR3GQySNwp5YV-L0meerhuntqNtccEYNe6pxw-JoWKpBtgFn46t_fGGNS3wPvTuno-z159HVqfvVuV_jtYecJAUKi0urnuTOehlzmBqkFzEEeE4fBH1QenMeWU/s1600/netdelay+sdf.PNG)

There are other SDF construct also but I am not discussing them here. The reason being – it will increase the length of the Article & looks to me that’s not required right now.;) For the detail info, you can refer the “IEEE standard for Standard Delay format for electronic design format”. Most of my content also have same reference.

Apart of this – Most important thing is SDF constructs are originally targeted for annotation to tools using the Verilog language, so many SDF constructs are analogous to those in Verilog specify blocks. Those already familiar with the Verilog specify block will find many of the SDF constructs familiar. So it’s very easy for those who are champ in Verilog. 

In the Next Article, we will take a circuit and respective SDF, to give you an idea - how to read SDF with respect to a circuit.

Posted by
VLSI Expert
at

[Newer ](https://www.vlsi-expert.com/search?updated-max=2021-05-31T00:09:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2019-12-12T18:34:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 3. ### [Timing\_sense : Timing Arc in .LIB Files (Part1)](https://www.vlsi-expert.com/2017/12/timing-sense-in-lib-1.html)

**URL:** https://www.vlsi-expert.com/2017/
**Date:** 2018-01-22
**Tags:** physical-design, sta, dft, ESD, parasitic, analog

### [Timing\_sense : Timing Arc in .LIB Files (Part1)](https://www.vlsi-expert.com/2017/12/timing-sense-in-lib-1.html)

## Monday, December 25, 2017

### [Single VIA, VIA array, Stacked VIA](https://www.vlsi-expert.com/2017/12/vias.html)

A via forms a connection between overlapping geometries on different layers through a cut layer, and is formed by geometries on all three layers.

Three types of vias:

1. a single via,
2. an array via,
3. and a stacked via.

### 1) Single VIA

Below diagram help you to understand how single VIA are placed between 2 metal and help them to connect them.

**2D /Top view with different arrangement (also known as Layout View)**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjf6oH7RloZOkaMtyLcAzzcem2Nb-jXfjIooVKNxf-Bj2uA5Dqfptkb35sNdnPLoDnnxR3iuCUIqPubIXyjjx4Cl9aG2xvvag8V5M8lzvQ5C5Jmh0QaM_WZQq32rT4z3DLLjLaJVT1hEWk/s640/single_via_top_view.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjf6oH7RloZOkaMtyLcAzzcem2Nb-jXfjIooVKNxf-Bj2uA5Dqfptkb35sNdnPLoDnnxR3iuCUIqPubIXyjjx4Cl9aG2xvvag8V5M8lzvQ5C5Jmh0QaM_WZQq32rT4z3DLLjLaJVT1hEWk/s1600/single_via_top_view.PNG)

**3D view (Help you to understand connection more closely).**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhT4tpIVOghgcVHkVH8Jy4hDz20MpvH4HvNdv-qyGZ1dUdf3XriFymQkugJE8XC_0DHp7PdWY29uZTPxlaH0Y66mvqvzVzuOMr-EnWQndLMKnlR95Kfsd3ee6h1S2NQ3npJCYe6TZq-ucY/s640/single_via_3D_view.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhT4tpIVOghgcVHkVH8Jy4hDz20MpvH4HvNdv-qyGZ1dUdf3XriFymQkugJE8XC_0DHp7PdWY29uZTPxlaH0Y66mvqvzVzuOMr-EnWQndLMKnlR95Kfsd3ee6h1S2NQ3npJCYe6TZq-ucY/s1600/single_via_3D_view.png)

Figure 3D\_b is a transparent view of the 3D\_a. It helps you to understand how different layers are connected with each other.

**Side View of Via and Metal connection.**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi11oxwoZWfboCYNwT6BcfQVDkrN0ftWwM6fdQsDI7B1YyANpMXyMRLoaS_aklet2Da-k-OqTRhqH81jDtaHWUWH3ltFxa-tjTxHywjyOoqaG7RTsnwr79aTfyXpDBWoHR6VTbKD_d2tZU/s400/single_via_side_view.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi11oxwoZWfboCYNwT6BcfQVDkrN0ftWwM6fdQsDI7B1YyANpMXyMRLoaS_aklet2Da-k-OqTRhqH81jDtaHWUWH3ltFxa-tjTxHywjyOoqaG7RTsnwr79aTfyXpDBWoHR6VTbKD_d2tZU/s1600/single_via_side_view.PNG)

There are certain Design rules for VIAs also. I am not going to capture those in detail here but below figure give you a general idea.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFOHwmucFbjkVaNavgHns1ThaeI7NmDd_QBvpsiCRt5m9vwToIwRBzp834Mf80HZY0PoVBcwcZa_5ZrtHZG2i3JFq7tLAxty5skWErPdukOHqgrWfv9MG8z6OOCXq5pfj59Qqe8lWI7No/s400/via_design_rules.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFOHwmucFbjkVaNavgHns1ThaeI7NmDd_QBvpsiCRt5m9vwToIwRBzp834Mf80HZY0PoVBcwcZa_5ZrtHZG2i3JFq7tLAxty5skWErPdukOHqgrWfv9MG8z6OOCXq5pfj59Qqe8lWI7No/s1600/via_design_rules.PNG)

Vias can be asymmetric, meaning the overhangs in the x and y directions are different. The overhang parameters refer to those of a via connecting preferred-direction wires. If the wires are in the nonpreferred direction, the via is rotated and the overhangs are reversed, meaning that the extensions in the x direction are given by the y overhang parameters.

### 2) VIA Array

Array vias are used for connecting wide wires where the required cut size would exceed the maximum cut size of the simple via. In an array via, the region of intersection of the wires is filled by a regular array of small cuts of fixed size and separation.

**2D /Top view with and without preferred direction of Metal arrangement (also known as Layout View)**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6_09oBCJLuHwV3ioiCINO4z5ZTEXYPI3pJk3aEY-olph2ZWNtrJVVVaUlOwjHFoLROwpOgxRKX8UrZfwx2WcE9JvLornFH604QKK8MH8ZaynfFy6ITrhJBOpjQKoz1GMVcHoDI4RPL9s/s640/array_via_top_view.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6_09oBCJLuHwV3ioiCINO4z5ZTEXYPI3pJk3aEY-olph2ZWNtrJVVVaUlOwjHFoLROwpOgxRKX8UrZfwx2WcE9JvLornFH604QKK8MH8ZaynfFy6ITrhJBOpjQKoz1GMVcHoDI4RPL9s/s1600/array_via_top_view.PNG)

**3D view (Help you to understand connection more closely).**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTgWZlRqv4zUI66cqKsnjCYphP63OuYvN7LY_ozqjHsMB_lCx8fTinykOLNS4XjNeWiSYRC-Lq2M6wwr8IBGoFgOwNkQmZk1DWfwyIilDQdjCcr0eGFlrfZgNozTw9pXLjzeiurbQ2DFU/s640/array_via_3D_view.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTgWZlRqv4zUI66cqKsnjCYphP63OuYvN7LY_ozqjHsMB_lCx8fTinykOLNS4XjNeWiSYRC-Lq2M6wwr8IBGoFgOwNkQmZk1DWfwyIilDQdjCcr0eGFlrfZgNozTw9pXLjzeiurbQ2DFU/s1600/array_via_3D_view.PNG)

Figure 3D\_b is a transparent view of the 3D\_a. It helps you to understand how different layers are connected with each other. you can also see that array size is 3x1 between M1 and M2. When it comes to M2 and M3, Single VIA connects both the wire. But dnt think that it will always be the case. It depends on design that and width of Metal wire, if you want to use VIA array or Single VIA. In the below figure, you can see that M1 and M2 are using 3x3 VIA array. Between M2 and M3 - it's 1x3 VIA array.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYqL9rHdR950fGY0V_eRKP51panaxd4b9hXOil_Q77zoX3iwtF6Hs_zlBdrHkVBg-gVRXKn5f18CGs6Knev3ycnmSxI89e9jKj0IKZ5mzx0E8satMG78F0S2JKrpfH5BJibrWG99yC0NU/s400/array_via_3D_view1.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYqL9rHdR950fGY0V_eRKP51panaxd4b9hXOil_Q77zoX3iwtF6Hs_zlBdrHkVBg-gVRXKn5f18CGs6Knev3ycnmSxI89e9jKj0IKZ5mzx0E8satMG78F0S2JKrpfH5BJibrWG99yC0NU/s1600/array_via_3D_view1.PNG)

### 3) Stack VIA

**3D view (Help you to understand connection more closely).**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPKlfpg_2F9WmfzMel7-z0cPomGGD-o6TwS8RD9JJjLeYyMiPr0K85vgq8b70aogMH-rEhEuI15A4oFjO2HcewUZzw_IUSva1XauT8MqSJ0LmzLaz12xFm30nyEzvOSxM12zf-wK4whM4/s400/stacked_via_3D_view.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPKlfpg_2F9WmfzMel7-z0cPomGGD-o6TwS8RD9JJjLeYyMiPr0K85vgq8b70aogMH-rEhEuI15A4oFjO2HcewUZzw_IUSva1XauT8MqSJ0LmzLaz12xFm30nyEzvOSxM12zf-wK4whM4/s1600/stacked_via_3D_view.PNG)

2D view of Stack via is not easy to understand. But if you want to try, you can do it in any tool to understand properly.

**I can summarize this article with combined view of all 3 type of VIAs.**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQruVz3iDKGOQH183g3oavS0ammJusUAnJhLmFTx-GT0LojOCt5FG6PsYSDqz4k_J-fZFR3dQHjDGJ-kef8pzpk287sIyecwm0v8TVBiK9Cun2cMW-IPQzpwZ8_lj3T4PmIRFeCrdwaI8/s640/via_single_array_stack.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQruVz3iDKGOQH183g3oavS0ammJusUAnJhLmFTx-GT0LojOCt5FG6PsYSDqz4k_J-fZFR3dQHjDGJ-kef8pzpk287sIyecwm0v8TVBiK9Cun2cMW-IPQzpwZ8_lj3T4PmIRFeCrdwaI8/s1600/via_single_array_stack.PNG)

Posted by
VLSI Expert
at
[2:22 PM](https://www.vlsi-expert.com/2017/12/vias.html "")[5\\
comments](https://www.vlsi-expert.com/2017/12/vias.html#)

## Monday, November 27, 2017

### [Metal Wire Orientation (HVH or VHV)](https://www.vlsi-expert.com/2017/11/metal-wire-orientation.html)

In [previous articles](http://www.vlsi-expert.com/2017/10/metal-layer-stack-nomenclature-part-2.html), we have discussed a lot about type of metal wire like Mx, My and others. We have also discussed about the Metal stack like 6 Metal layer stack : M1\_3Mx\_My\_Mz. (If you have confusion, please refer Article " [Metal Layer Stack Nomenclature](http://www.vlsi-expert.com/2017/10/metal-layer-stack-nomenclature-part-2.html)").

In this article, we are going to understand another important concept: "Metal layer Orientation". Actually during routing of design, we use a terminology "Preferred Routing Direction" of Metal layer. May be you have heard HVH or VHV routing strategy. Even if not - then I am sure you have seen below fig somewhere :) .

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8Ro396XyrBZOF-SpVMODlWSRW3sI62YHipGKrOkehOTLV_g5ZzZiqDyeoLXIZAlg-c_k_wtfGdv0ZpB_0boyKft5fFMonuCmJ5r0pmg2nM86QfKbNbjMQVvtZWV6YlE1fRA1uLhTGp44/s400/metal_layer_orientation_1.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8Ro396XyrBZOF-SpVMODlWSRW3sI62YHipGKrOkehOTLV_g5ZzZiqDyeoLXIZAlg-c_k_wtfGdv0ZpB_0boyKft5fFMonuCmJ5r0pmg2nM86QfKbNbjMQVvtZWV6YlE1fRA1uLhTGp44/s1600/metal_layer_orientation_1.PNG)

In the above pic, you can see that M1, M3 & M5 are in Horizontal direction and M2 & M4 are in vertical direction. Still confused ??? :) Let me help you.

Metal wires in our design are at different levels. If, I assume that M1 is at first level then M2 is at second level, M3 at third and so on. Type of Metal (Mx, My, Mz) depends as per Metal Stack you are going to choose for your design. (For more detailing about the Metal stack - please refer Article " [Metal Layer Stack](http://www.vlsi-expert.com/2017/10/metal-layer-stack-metallization-option1.html)"). By now, you should be clear that different metals present at different height with respect to substrate.

Now, only one question is remaining, how we are going to route these metals? How in the sense - in which direction or say orientation. Is/are there any standard/s behind this or user can route these metals wires as per their requirement? Very short answer of this question - There are standards or say recommendation for routing Metal wires. Timing is very critical now a days. From metal wires point of view - capacitance between them plays a very important role. ( **Note:** Delay has relationship with RC constant - and this C is because of Capacitance between the wires). So as a designer we have to understand or say use those technique which can minimize these unwanted Capacitance (Remember - capacitance between Wires are always unwanted. It's always has side effect in negative sense :) ). To understand different type of capacitance between wires, you can refer Article " [Basic of Capacitance & Resistance (from VLSI Point of view)](http://www.vlsi-expert.com/2012/02/parasitic-interconnect-corner-rc-corner.html)"

Capacitance between 2 plates depends on area of plates parallel to each other OR I can say overlap area between 2 metal wires. During Routing - there are 2 extreme routing methodology.

1. Parallel Routing Grid
2. Cross Routing Grid

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEim7Z5ppNqD4psUfCQjBQjyHY_0CjVwfNxU8EnCDohDf_OlEBbDyRV2MUYxSRwWVg5PK43ElAhUlsU6BxoLdXYieFDyC3JXteKDWp2mkrIIqrORAf_MXl0zV0HKX5PD-SMMIEu827zQkY8/s640/Metal_layer_Routing_grid.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEim7Z5ppNqD4psUfCQjBQjyHY_0CjVwfNxU8EnCDohDf_OlEBbDyRV2MUYxSRwWVg5PK43ElAhUlsU6BxoLdXYieFDyC3JXteKDWp2mkrIIqrORAf_MXl0zV0HKX5PD-SMMIEu827zQkY8/s1600/Metal_layer_Routing_grid.PNG)

If we place metal wire on these routing grids (as an example - just picked only 2 wires of same metal layer), you can easily understand the concept of overlap area. Remember, right now we are talking about Ground cap (or Area cap) and not Coupling cap.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiysZ-Sy7EpArsS2qh404v6ICaIbG_UVofWhDWJM21ga8mRMYM7-a3yWTxPvKOAwDl3iBDc_qRVEa9LpHjRdnMyAZea4GlUY1CUHc1G1Vz1T5JpSnTTcdwKOQfJsxECNjHfi-uvkQXXttY/s640/Metal_wire_orientation.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiysZ-Sy7EpArsS2qh404v6ICaIbG_UVofWhDWJM21ga8mRMYM7-a3yWTxPvKOAwDl3iBDc_qRVEa9LpHjRdnMyAZea4GlUY1CUHc1G1Vz1T5JpSnTTcdwKOQfJsxECNjHfi-uvkQXXttY/s1600/Metal_wire_orientation.PNG)

**Parallel Metal Wire Orientation:**

In the below figure, I have tried to show arrangement of capacitance between parallel metal wire between metal layers of different levels Like capacitance between M1 and M2. Since M1 and M2 both are parallel to each other 100%, Capacitance between them has dependency on width and length of the wire. This arrangement gives maximum Ground cap (Area cap).

**Note**: We are not discussing the capacitance between same type of metal layers (Between M1 and M1) known as Coupling Capacitance.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfuyhPlZJrTJH2GR6423waCRWA9OBn-uPTD2XTOJ_Enlc39sg1nMzaY-bKCOCA8rWUWYx7rQ4iXbV4eYOYp_3G5nHdXVmWLu1GWMCCA16k4N2rYW6JzNijKO5tvuEDg5nJzvju_y3xGPE/s400/Parallel+Wire+Orientation.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfuyhPlZJrTJH2GR6423waCRWA9OBn-uPTD2XTOJ_Enlc39sg1nMzaY-bKCOCA8rWUWYx7rQ4iXbV4eYOYp_3G5nHdXVmWLu1GWMCCA16k4N2rYW6JzNijKO5tvuEDg5nJzvju_y3xGPE/s1600/Parallel+Wire+Orientation.PNG)

**Cross / Perpendicular Metal Wire Orientation:**

In the below figure, you can see that overlap area between M1 and M2 is only at their cross-section. This overlap area depends on their corresponding width parameter. You can see that their is no dependency on length of the wire. This arrangement gives minimum Ground cap (Area cap).

Front view and Side view of this arrangement helps you to understand this routing methodology more closely.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHdT0XOyoN8I9WjeiTtvmxtbXfEl9Q5dDm-NDKrakxkJiqDGRgBgc0HVnAiALt7OcmwE45V72ZXAEtKhtlUWDCWGoxvlkVPm3v0FdAeDocIgMDr05UZ6qYT8afrdtDmf3wNqIYo_u3QIU/s640/Cross+Wire+Orientation.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHdT0XOyoN8I9WjeiTtvmxtbXfEl9Q5dDm-NDKrakxkJiqDGRgBgc0HVnAiALt7OcmwE45V72ZXAEtKhtlUWDCWGoxvlkVPm3v0FdAeDocIgMDr05UZ6qYT8afrdtDmf3wNqIYo_u3QIU/s1600/Cross+Wire+Orientation.PNG)

You can see that if we want to reduce the CAP then orientation of the Metal wire is very important. Cross (perpendicular) metal wire orientation gives minimum capacitance and that's the reason it's recommended. One of the direction is considered as Horizontal and other as Vertical. That's the reason - these orientation is known as HVH or VHV orientation (and corresponding routing strategy as HVH or VHV routing methods).

Posted by
VLSI Expert
at
[8:19 PM](https://www.vlsi-expert.com/2017/11/metal-wire-orientation.html "")[3\\
comments](https://www.vlsi-expert.com/2017/11/metal-wire-orientation.html#)

## Saturday, November 25, 2017

### [Delay Interview Questions (Part 2)](https://www.vlsi-expert.com/2017/11/delay-interview-questions-part2.html)

In the last part ( [Delay Interview Questions: Part 1](http://www.vlsi-expert.com/2017/10/delay-interview-question-part1.html)), we have discusses 2 scenarios

1. Min & Max Delay Between 2 points having multi-paths when Delay are given as absolute number.
2. Min & Max Delay between 2 points having multi-paths when Delay are given as Rise and Fall delay.

We have discussed these concepts from Interview point of view.

**Note:** [Example 1](http://www.vlsi-expert.com/2017/10/delay-interview-question-part1.html#example1) and [Example 2](http://www.vlsi-expert.com/2017/10/delay-interview-question-part1.html#example2), we have already discussed in last article.

### Example 3:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVuGfKUXGZmZT0FgMHbEHnoe6oDjxfGVznDBewTBd-v6weVfkoU83cr1DQDbViW9KcyveVBqqxHd-mOOWWlLhBsX2Kd8nmvyiEWLlCYC__4iV0AP4WWsx40nxWZzQGiwLam4iJCyBvxbQ/s640/Delay+3.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVuGfKUXGZmZT0FgMHbEHnoe6oDjxfGVznDBewTBd-v6weVfkoU83cr1DQDbViW9KcyveVBqqxHd-mOOWWlLhBsX2Kd8nmvyiEWLlCYC__4iV0AP4WWsx40nxWZzQGiwLam4iJCyBvxbQ/s1600/Delay+3.PNG)

**Note:** Above figure is same as in Example 1 and Example 2 (with small addition).

All Buffer has same (min, max) delay = (0.1ns, 0.2ns)

All NOT Gate has same (min, max) delay = (0.25ns, 1ns)

AND gate (min, max) delay:

                  Arc a1 -> y1 = (1.25ns, 1.5ns)

                  Arc b1 -> y1 = (1.1ns, 1.9ns)

OR gate (min, max) delay:

                  Arc a2 -> y2 = (0.3ns, 0.4ns)

                  Arc b2 -> y2 = (0.5ns, 0.9ns)

**Question: Find out the Minimum and Maximum Delay between Q1 and D2?**

**Explanation:**

This question is almost equal to the example 1 but with slight modification. Now, we are talking about the different input and output combination of AND gate. Remember, every input and output combination has it's own delay value. When we talk about the Delay of a Gate and if it's not related to input and output combination, it means we are talking about Boundaries of overall gate delay. To understand this concept - you need to revise or say understand Timing Arc concepts. Please read article [Timing Arc](http://www.vlsi-expert.com/2016/09/timing-arc.html) and [Unate: Timing Arc](http://www.vlsi-expert.com/2016/12/unate-timing-arc.html).

Intension of this question is to get more accurate delay value based on Path base analysis.

**Note:** Delay calculation in such circuit are of 2 type - Path base Analysis and Graph Base Analysis. You can get more detail about this in Article - [Path Base Vs Graph Base Analysis: Part 1](http://www.vlsi-expert.com/2017/11/pba-vs-gba-1.html).

There is a little bit change in the picture of Path 1 and Path 2 (in compare to Example 1 and Example 2).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvTK9dviPSo7AewtaIBe2MnWYefjMSgsMcD5vaGXd_MMoRH_UADLi4zR-upeMHDy2_xvVG4uk1LjdGbyYoG0GtvxbEcEy3q6WyWgJvjBNb0tEw-SN-SU-z8L4UdE1VEm8A0jhhE-TvCKg/s640/Delay+4.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvTK9dviPSo7AewtaIBe2MnWYefjMSgsMcD5vaGXd_MMoRH_UADLi4zR-upeMHDy2_xvVG4uk1LjdGbyYoG0GtvxbEcEy3q6WyWgJvjBNb0tEw-SN-SU-z8L4UdE1VEm8A0jhhE-TvCKg/s1600/Delay+4.PNG)

In the above figure, you can see that

**Path 1: Q1 -> Inverter -> b1 -> y1 -> Buffer -> a2 -> y2 -> Buffer -> D2**

**Path 2: Q1 -> Inverter -> Inverter -> Inverter -> b2 -> y2 -> Buffer -> D2**

**In Path 1:**

b1 -> y1 is basically part of AND gate and during delay calculation we will use **delay value as per Arc b1 -> y1 = (1.1ns, 1.9ns)**.

a2 - > y2 is basically part of OR gate and **delay values are as per Arc a2 -> y2 = (0.3ns, 0.4ns)**.

**In Path 2:**

b2 - > y2 is basically part of OR gate and **delay values are as per Arc b2 -> y2 = (0.5ns, 0.9ns)**.

**Solution:**

Path 1 (Min Delay) : 0.25 (inverter) + 1.1 (b1 -> y1) + 0.1 (buffer) + 0.3 (a2 -> y2) + 0.1 (buffer) = 1.85ns

Path 1 (Max Delay) : 1.00 (inverter) + 1.9 (b1 -> y1) + 0.2 (buffer) + 0.4 (a2 -> y2) + 0.2 (buffer) = 3.70ns

Path 2 (Min Delay) : 0.25 (inverter) + 0.25 (inverter) + 0.25 (inverter) + 0.5 (b2 -> y2) + 0.1 (buffer) = 1.35ns

Path 2 (Max Delay) : 1.00 (inverter) + 1.0 (inverter) + 1.0 (inverter) + 0.9 (b2 -> y2) + 0.2 (buffer) = 4.1ns

**Overall Min Delay between Q1 and D2 = 1.35ns (From Path 2)**

**Overall Max Delay between Q1 and D2 = 4.1ns (From Path 2)**

### Example 4:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVuGfKUXGZmZT0FgMHbEHnoe6oDjxfGVznDBewTBd-v6weVfkoU83cr1DQDbViW9KcyveVBqqxHd-mOOWWlLhBsX2Kd8nmvyiEWLlCYC__4iV0AP4WWsx40nxWZzQGiwLam4iJCyBvxbQ/s640/Delay+3.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVuGfKUXGZmZT0FgMHbEHnoe6oDjxfGVznDBewTBd-v6weVfkoU83cr1DQDbViW9KcyveVBqqxHd-mOOWWlLhBsX2Kd8nmvyiEWLlCYC__4iV0AP4WWsx40nxWZzQGiwLam4iJCyBvxbQ/s1600/Delay+3.PNG)

All Buffer has same delay:

                  Tphl (min, max) = (0.1ns, 0.18ns)

                  Tplh (min, max) = (0.15ns, 0.20ns)

All NOT Gate has same delay:

                  Tphl (min, max) = (0.25ns, 0.75ns)

                  Tplh (min, max) = (0.5ns, 1.0ns)

AND gate delay:

        Arc a1 -> y1:

                    Tphl (min, max) = (1.25ns, 1.5ns)

                    Tplh (min, max) = (1.3ns, 1.75ns)

        Arc b1 -> y1

                    Tphl (min, max) = (1.0ns, 1.9ns)

                    Tplh (min, max) = (1.1ns, 2.0ns)

OR gate (min, max) delay:

        Arc a2 -> y2:

                    Tphl (min, max) = (0.3ns, 0.35ns)

                    Tplh (min, max) = (0.31ns, 0.4ns)

        Arc b2 -> y2:

                    Tphl (min, max) = (0.51ns, 0.9ns)

                    Tplh (min, max) = (0.5ns, 0.75ns)

**Note:**

Tphl = Propagation Delay High to Low

Tplh = Propagation Delay Low to High

**Question: Find out the Tplh and Tphl at point D2 with respect to Input Q1?**

**Explanation:**

For this you need to understand the concepts of Tphl and Tplh. I am assuming that you know this part. Here we have to understand how different waveform (Rising input or Falling input) is going to behave in this circuit.

There is a little bit change in the picture of Path 1 and Path 2 (in compare to Example 1 and Example 2).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvTK9dviPSo7AewtaIBe2MnWYefjMSgsMcD5vaGXd_MMoRH_UADLi4zR-upeMHDy2_xvVG4uk1LjdGbyYoG0GtvxbEcEy3q6WyWgJvjBNb0tEw-SN-SU-z8L4UdE1VEm8A0jhhE-TvCKg/s640/Delay+4.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvTK9dviPSo7AewtaIBe2MnWYefjMSgsMcD5vaGXd_MMoRH_UADLi4zR-upeMHDy2_xvVG4uk1LjdGbyYoG0GtvxbEcEy3q6WyWgJvjBNb0tEw-SN-SU-z8L4UdE1VEm8A0jhhE-TvCKg/s1600/Delay+4.PNG)

We have to do 2 type of analysis for each path - Rising & Falling signal analysis at D1 for both paths.

**Rising Signal Analysis (For Path1):**

- Inverter is Negative Unate -> Rising Signal at input means falling signal at output -> Means Tphl of NOT gate => (0.25ns, 0.75ns)
- AND gate is Positive Unate -> Falling signal at input means falling signal at output -> Means Tphl of AND gate for ARC b1 -> y1 => (1.0ns, 1.9ns)
- Buffer is Positive Unate -> Falling signal at input means falling signal at output -> Means Tphl of Buffer gate => (0.1ns, 0.18ns)
- OR is Positive Unate -> Falling signal at input means falling signal at output -> Means Tphl of OR gate for ARC a2 -> y2 => (0.3ns, 0.35ns)
- Buffer is Positive Unate -> Falling signal at input means falling signal at output -> Means Tphl of Buffer gate => (0.1ns, 0.18ns)

For Rising Signal at the Input (Q1), we are getting Falling Signal at the Output (D2) through Path1. So in this scenario, delay between Q1 and D1 through Path1 = **Tphl**.

Minimum Tphl at D1 through Path 1 = 0.25ns + 1.0ns + 0.1ns + 0.3ns + 0.1ns = 1.75ns

Maximum Tphl at D1 through Path 1 = 0.75ns + 1.9ns + 0.18ns + 0.35ns + 0.18ns = 3.36ns

**Falling Signal Analysis (For Path1):**

- Inverter is Negative Unate -> Falling Signal at input means rising signal at output -> Means Tplh of NOT gate => (0.5ns, 1.0ns)
- AND gate is Positive Unate -> Rising signal at input means rising signal at output -> Means Tplh of AND gate for ARC b1 -> y1 => (1.1ns, 2.0ns)
- Buffer is Positive Unate -> Rising signal at input means rising signal at output -> Means Tplh of Buffer gate => (0.15ns, 0.20ns)
- OR is Positive Unate -> Rising signal at input means rising signal at output -> Means Tplh of OR gate for ARC a2 -> y2 => (0.31ns, 0.4ns)
- Buffer is Positive Unate -> Rising signal at input means rising signal at output -> Means Tplh of Buffer gate => (0.15ns, 0.20ns)

For Falling Signal at the Input (Q1), we are getting Rising Signal at the Output (D2) through Path1. So in this scenario, delay between Q1 and D1 through Path1 = **Tplh**.

Minimum Tplh at D1 through Path 1 = 0.5ns + 1.1ns + 0.15ns + 0.31ns + 0.15ns = 2.21ns

Maximum Tplh at D1 through Path 1 = 1.0ns + 2.0ns + 0.20ns + 0.40ns + 0.20ns = 3.80ns

**Rising Signal Analysis (For Path2):**

- Inverter is Negative Unate -> Rising Signal at input means falling signal at output -> Means Tphl of NOT gate => (0.25ns, 0.75ns)
- Inverter is Negative Unate -> Falling signal at input means rising signal at output -> Means Tplh of NOT gate => (0.5ns, 1.0ns)
- Inverter is Negative Unate -> Rising signal at input means falling signal at output -> Means Tphl of NOT gate => (0.25ns, 0.75ns)
- OR is Positive Unate -> Falling signal at input means falling signal at output -> Means Tphl of OR gate for ARC b2 -> y2 => (0.51ns, 0.9ns)
- Buffer is Positive Unate -> Falling signal at input means falling signal at output -> Means Tphl of Buffer gate => (0.1ns, 0.18ns)

For Rising Signal at the Input (Q1), we are getting Falling Signal at the Output (D2) through Path2. So in this scenario, delay between Q1 and D1 through Path2 = **Tphl**.

Minimum Tphl at D1 through Path 2 = 0.25ns + 0.5ns + 0.25ns + 0.51ns + 0.10ns = 1.61ns

Maximum Tphl at D1 through Path 2 = 0.75ns + 1.0ns + 0.75ns + 0.90ns + 0.18ns = 3.58ns

**Falling Signal Analysis (For Path2):**

- Inverter is Negative Unate -> Falling Signal at input means rising signal at output -> Means Tplh of NOT gate => (0.5ns, 1.0ns)
- Inverter is Negative Unate -> Rising signal at input means falling signal at output -> Means Tphl of NOT gate => (0.25ns, 0.75ns)
- Inverter is Negative Unate -> Falling signal at input means rising signal at output -> Means Tplh of NOT gate => (0.5ns, 1.0ns)
- OR is Positive Unate -> Rising signal at input means rising signal at output -> Means Tplh of OR gate for ARC b2 -> y2 => (0.5ns, 0.75ns)
- Buffer is Positive Unate -> Rising signal at input means rising signal at output -> Means Tplh of Buffer gate => (0.15ns, 0.20ns)

For Falling Signal at the Input (Q1), we are getting Rising Signal at the Output (D2) through Path2. So in this scenario, delay between Q1 and D1 through Path2 = **Tplh**.

Minimum Tplh at D1 through Path 2 = 0.50ns + 0.25ns + 0.50ns + 0.50ns + 0.15ns = 1.90ns

Maximum Tplh at D1 through Path 2 = 1.00ns + 0.75ns + 1.00ns + 0.75ns + 0.20ns = 3.70ns

**Solution:**

Through Path 1 (Min Tplh) : 2.21ns

Through Path 1 (Min Tphl) : 1.75ns

Through Path 2 (Min Tplh) : 1.90ns

Through Path 2 (Min Tphl) : 1.61ns

Through Path 1 (Max Tplh) : 3.80ns

Through Path 1 (Max Tphl) : 3.36ns

Through Path 2 (Max Tplh) : 3.70ns

Through Path 2 (Max Tphl) : 3.58ns

**Overall Minimum Tplh** at D2 (when input is at Q1) = 1.90ns (Through Path 2)

**Overall Maximum Tplh** at D2 (when input is at Q1) = 3.80ns (Through Path 1)

**Overall Minimum Tphl** at D2 (when input is at Q1) = 1.61ns (Through Path 2)

**Overall Maximum Tphl** at D2 (when input is at Q1) = 3.58ns (Through Path 2)

In Summary, I can write, **At D2 with respect to Q1 Tphl = (1.61ns, 3.58ns) & Tplh = (1.90ns, 3.80ns)**

Is it done? I mean do you think Interviewer is going to stop at this point. :) :) Don't ever think. By now they will realize that you are good in below concepts.

- Min and Max Delay Calculation
- Delay calculation based on Timing Arc (I can say some part of Path base & Graph base analysis)
- Tphl and Tplh based Delay Calculation
- Multipath Delay Calculation
- Use of Rising edge and Falling Edge at Input during delay calculation

Now, it's time to check few more concepts related to CELL Delay (Like Cell Delay as a function of Input Transition Vs Output Load) and then how you can use those concepts in delay calculation of Combinational Circuit. :) Lets discuss this in Next Article.

Posted by
VLSI Expert
at

## Tuesday, November 7, 2017

### [Path Base Analysis (PBA) Vs Graph Base Analysis (GBA) - part1](https://www.vlsi-expert.com/2017/11/pba-vs-gba-1.html)

Today, we are going to discuss about the Path base analysis Vs Graph base analysis. As such difference is more complex compare to what I am going to explain, but right now it's sufficient to start with. :)

Let's you have a combinational path with Net delay (min, max) and Cell delay (As per the Timing Arc). If, you have any confusion with respect to the timing arc, please refer below articles.

- [Introduction of Timing Arc](http://www.vlsi-expert.com/2016/09/timing-arc.html)
- [Unateness](http://www.vlsi-expert.com/2016/12/unate-timing-arc.html)

In the below figure, you can see AND gate (1) has 2 input, so 2 set of input-output delay combination.

- Min Delay = 0.5ns, Max Delay = 1.5ns
- Min Delay = 0.2ns, Max Delay = 1.2ns

Similarly, for other logic gates.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjynDpRhyUsa_Jtp4nG4mvax-t8UO6z130WDbDpGDkT_FfeEaoR24SP8kARahrs_Y2tLW7OxwawgSK0uGWmCPYnDudi6uwckRzZFJIb4KVPg0yOFFVVQBz-p4546u5gRSkQWDag0_HajBI/s640/Combinational+Delay.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjynDpRhyUsa_Jtp4nG4mvax-t8UO6z130WDbDpGDkT_FfeEaoR24SP8kARahrs_Y2tLW7OxwawgSK0uGWmCPYnDudi6uwckRzZFJIb4KVPg0yOFFVVQBz-p4546u5gRSkQWDag0_HajBI/s1600/Combinational+Delay.PNG)

Now, if I will ask you to calculate the delay between point A and point B, then the concept of PBA and GBA comes into the picture. Before, I explain you this concept, please refer below few figures and then see the difference between PBA and GBA.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1QVwnnphq8o0dy7TIZqnBoFzW3TRiGVjfEaRyXOx_ysq73ww3htCLeywQBnx75T7TKUF0dYGmNtFHK0IhSnLCqeidMaG8-DVn6tcGwBYJQBz3V2kKKv5vBLtaWE4mqzEuzNUUNOIIVPQ/s640/PBA+Vs+GBA+1.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1QVwnnphq8o0dy7TIZqnBoFzW3TRiGVjfEaRyXOx_ysq73ww3htCLeywQBnx75T7TKUF0dYGmNtFHK0IhSnLCqeidMaG8-DVn6tcGwBYJQBz3V2kKKv5vBLtaWE4mqzEuzNUUNOIIVPQ/s1600/PBA+Vs+GBA+1.PNG)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj47CMYct1SnTzyL50ViMuD_JRwqXVWEy3VlNNfOS2061ogIOHOFStv1PZ0_229WhBc1Vo7ST86r7VXWBYxEH1mowmxV-yBX-twNd9iMQq3mfgFbWRBK6wDmLbT47KMzdvnclvYdM7p3UE/s640/PBA+Vs+GBA+2.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj47CMYct1SnTzyL50ViMuD_JRwqXVWEy3VlNNfOS2061ogIOHOFStv1PZ0_229WhBc1Vo7ST86r7VXWBYxEH1mowmxV-yBX-twNd9iMQq3mfgFbWRBK6wDmLbT47KMzdvnclvYdM7p3UE/s1600/PBA+Vs+GBA+2.PNG)

I am sure, if you have notice closely, then you have already realized the difference. :) But still let me highlight that.

In **GBA (Graph Base Analysis)**, in place of choosing 2 combinations of AND gate (1) delay, i.e. (Combination\_1: 0.5ns, 1.5ns ; Combination\_2: 0.2ns, 1.2ns) we choose extreme boundaries, i.e. **min delay = 0.2ns and max delay = 1.5ns.**

In case of **PBA (Path base Analysis)**, we are using actual delay between input pin and output combination (means choosing both combination of delay).

- Combination\_1: 0.5ns, 1.5ns
- Combination\_2: 0.2ns, 1.2ns

**Note:** Check the similar difference for AND gate (2) also.

You might be thinking that this is not accurate (means why in GBA we missed 2 value), we are adding unnecessary delay in our calculation. And I am glad to say that you are right. :) The reason we are doing this because from tool point of view - doing analysis or say calculation as per GBA is very fast compare to PBA. **Runtime of tool is very low.** And only difference is that we are adding pessimism in our calculation.

Now, if you want to understand the calculation of delay between different input pin (A, B, C) and Output Pin (Y), please check below figures.

**Note:** For clarity purpose (used different color combination) - I did this calculation and pasting in the form of picture. :)

**Delay Calculation in Case of GBA (Graph base Analysis).**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgGFjDMI-WrRSzuWjXv0qxym_VvJbR3Jp9AKlt-_sRgl1Aym2NvHz_oQmMBYuNUtgpRfFG1VwiGM8cjdL7Y_gCcEUOPAzfLOaCAyX6W8wAivl6seRViKNgLi4Qs9OQKTULH93EYge6T0k/s640/graph+base+analysis.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgGFjDMI-WrRSzuWjXv0qxym_VvJbR3Jp9AKlt-_sRgl1Aym2NvHz_oQmMBYuNUtgpRfFG1VwiGM8cjdL7Y_gCcEUOPAzfLOaCAyX6W8wAivl6seRViKNgLi4Qs9OQKTULH93EYge6T0k/s1600/graph+base+analysis.PNG)

**Delay Calculation in Case of PBA (Path base Analysis).**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUdq_kTPTbx22b_LAxt-B5NDIijzNEjDuudsCYAFt_TdvE3eTrjeasDdsDG8Rc8IUFUM85Jh0_QuAUixYSxpk9xj2leglTQH1sjk43CXvq6sJxzHGVYV2tdHu2ksCxU6Hku1Hs4z0rxoQ/s640/Path+base+analysis.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUdq_kTPTbx22b_LAxt-B5NDIijzNEjDuudsCYAFt_TdvE3eTrjeasDdsDG8Rc8IUFUM85Jh0_QuAUixYSxpk9xj2leglTQH1sjk43CXvq6sJxzHGVYV2tdHu2ksCxU6Hku1Hs4z0rxoQ/s1600/Path+base+analysis.PNG)

**Important observation, which you all should noticed:**

**Delay between A and Y**

Graph base analysis (Min, Max) : 7.25ns, 10.35ns

Path base analysis (Min, Max) : 7.55ns, 10.10ns

You can see that delay between A and Y - in case of GBA is superset of PBA.

Means:

**min\_delay\_in\_GBA < min\_delay\_in\_PBA**

**max\_delay\_in\_GBA > max\_delay\_in\_PBA**

**Delay between B and Y**

Graph base analysis (Min, Max) : 7.75ns, 10.85ns

Path base analysis (Min, Max) : 7.75ns, 10.30ns

You can see that delay between B and Y - in case of GBA is superset of PBA.

Means:

**min\_delay\_in\_GBA = min\_delay\_in\_PBA**

**max\_delay\_in\_GBA > max\_delay\_in\_PBA**

**Delay between C and Y**

Graph base analysis (Min, Max) : 7.05ns, 9.05ns

Path base analysis (Min, Max) : 7.25ns, 9.05ns

You can see that delay between A and Y - in case of GBA is superset of PBA.

Means:

**min\_delay\_in\_GBA < min\_delay\_in\_PBA**

**max\_delay\_in\_GBA = max\_delay\_in\_PBA**

**Let me summarize whole concept:**

> **min\_delay\_in\_GBA <= min\_delay\_in\_PBA**
>
> **max\_delay\_in\_GBA >= max\_delay\_in\_PBA**

Now, everything is good but still you may have confusion or question - why GBA? Because from above calculation, it's not clear how it's going to save Analysis Time of a Tool. How it's beneficial for Industry? If you have all these questions, no need to worry, I will explain but not in this article. I will do that next time. But I can give you hint, so that you can think about this once.

Hint:

1) Check how these minimum and maximum delays are calculated?

2) Adding Pessimism is not an problem, it's just margin in your delay calculation. How adding margin can help us?

3) What all different environment or other factors or parameters you have to consider while calculating Delay based on different timing Arc of a gate?

I think, for now, these hints are good enough. Comment here - if you know the Answer of this, else wait for next related article. :)

BEST OF LUCK.

**By - Puneet Mittal**

**(Founder of VLSI-Expert Group)** PBA)

Posted by
VLSI Expert
at
[6:31 AM](https://www.vlsi-expert.com/2017/11/pba-vs-gba-1.html "")[5\\
comments](https://www.vlsi-expert.com/2017/11/pba-vs-gba-1.html#)

## Monday, October 30, 2017

### [Technology File: Modelling of Dielectric Layer](https://www.vlsi-expert.com/2017/10/technology-file-modelling-of-dielectric.html)

### Background of Types of Dielectric layer

Dielectric layers are of 2 types.

1. Planar Dielectric
2. Conformal Dielectric

**Note:** We have already discussed about the [conformal dielectric](http://www.vlsi-expert.com/2010/09/conformal-dielectric.html) in detail. You can review once again ( [Click here](http://www.vlsi-expert.com/2010/09/conformal-dielectric.html)).

Below figures can help you to refresh your memories about Planar and Conformal dielectric.

**Planar Dielectric:**

All Dielectric in the below figure (D1 to D7) are Planar dielectric.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0VExEb1vUHLwMWpxTPF7xRck2VN13JirFOXF596ENZQhm7kstZvou-A8Le8PPfEMaSH0WRVFbkTCB45IFON81LadTaIEcId1jkt1e-s2WZ7aSFRf4uiOqgbERTXzffp8QQ5il-sWoRhc/s400/planar+dielectric.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0VExEb1vUHLwMWpxTPF7xRck2VN13JirFOXF596ENZQhm7kstZvou-A8Le8PPfEMaSH0WRVFbkTCB45IFON81LadTaIEcId1jkt1e-s2WZ7aSFRf4uiOqgbERTXzffp8QQ5il-sWoRhc/s1600/planar+dielectric.PNG)

**Conformal Dielectric:**

Different type of Conformal dielectric structures are shown in below figure. There are certain parameters which helps to identify any conformal dielectric like Side thickness, Bottom thickness or Top thickness.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjCs1lvEC1gCR-G-QOFQLDnxBVTQR_Hx7q468EBPlmwdfmpVJ5nxhoa24oDw0mNsIbhYen_IkUXaRTq_sZ4iQre16opocyZ2vND_Eml-LqX4HEGXtFIHjcn5VKFTPLiM8elGFGowCwt0M/s640/conformal_dielectric.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjCs1lvEC1gCR-G-QOFQLDnxBVTQR_Hx7q468EBPlmwdfmpVJ5nxhoa24oDw0mNsIbhYen_IkUXaRTq_sZ4iQre16opocyZ2vND_Eml-LqX4HEGXtFIHjcn5VKFTPLiM8elGFGowCwt0M/s1600/conformal_dielectric.PNG)

### Modelling of Dielectric in Technology File

Modelling of Dielectric layer in technology file vary as per extraction software or you can say that as per EDA vendor. Different EDA vendor uses different ways to represents this as per their requirement. Even if I know their syntax, I can't write here. :) But what I am going to do - explain everything in more easy language. :) Once you start working, you can check their manual and try to map my syntax with their syntax. :)

To represent a **Planar Dielectric** (Non-Conformal) we need to have following basic information.

( **Parameter Name : my\_nomenclature**)

**Dielectric constant** : di\_constant

**Thickness** : thickness

**Height from the Substrate** : height

**Name of Dielectric** : DIELECTRIC

**Type of Dielectric** : conformal=false

To represent a **Conformal Dielectric** we need to have following extra information.

( **Parameter Name : my\_nomenclature**)

**Side Thickness** : S\_thickness

**Bottom Thickness** : B\_thickness

**Top Thickness** : T\_thickness

**Type of Dielectric** : conformal=true

**Parent Layer** : p\_layer (This is the layer around which dielectric is present. It can be a conductor like Poly, Metal1 or may be any other Dielectric also. In above figure, M1 is the Parent layer).

**Planar Dielectric**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTpGfo6pJ1TyCECU8qYwpU5ERZuwtcS_y9JcI33QsBucDwQqYzKvG6cQzdRVCUZdmL9KhWXoLeOFnu-KGtoB7MpZZD6crD8vItuYhpYQK-7Xn5ta7SZRfq9cHr533nVsLjZgRVfMNu1NE/s400/Dielectric_layer.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTpGfo6pJ1TyCECU8qYwpU5ERZuwtcS_y9JcI33QsBucDwQqYzKvG6cQzdRVCUZdmL9KhWXoLeOFnu-KGtoB7MpZZD6crD8vItuYhpYQK-7Xn5ta7SZRfq9cHr533nVsLjZgRVfMNu1NE/s1600/Dielectric_layer.PNG)

Modelling in Technology file:

**DIELECTRIC DEL2**

di\_constant = 4.8

thickness = 2.7

height = 4.1

conformal = false

**DIELECTRIC DEL3**

di\_constant = 2.8

thickness = 0.3

height = 6.8

conformal = false

**Conformal Dielectric**

There are different scenarios which need to understand. These scenarios are same as we have discussed in the article of [Conformal Dielectric](http://www.vlsi-expert.com/2010/09/conformal-dielectric.html)(It will help you to map easily)

### Scenario 1:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguKZ8EL27yzqdjfSHKG6dnV269lpDXY3rjkWWn02nfv2_3n-MvI_nJQASsULAWTOJR3EyNfExcuRjAXcms97ymBCsScDKChOOKIfNyrnn6SDcwGSvGAQ3IURsgGkJOOc0dYtVe3M-jSOU/s640/Conformal+Dielectric+1.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguKZ8EL27yzqdjfSHKG6dnV269lpDXY3rjkWWn02nfv2_3n-MvI_nJQASsULAWTOJR3EyNfExcuRjAXcms97ymBCsScDKChOOKIfNyrnn6SDcwGSvGAQ3IURsgGkJOOc0dYtVe3M-jSOU/s1600/Conformal+Dielectric+1.PNG)

Modelling in Technology file:

**DIELECTRIC DEL\_M1a**

conformal = true

T\_thickness = 0.2

S\_thickness = 0.2

B\_thickness = 0

di\_constant = 3.8

thickness = 0

height = 4.1

p\_layer = M1

**DIELECTRIC DEL\_M1b**

conformal = true

T\_thickness = 0

S\_thickness = 0.2

B\_thickness = 0.2

di\_constant = 3.8

thickness = 0

height = 4.1

p\_layer = M1

### Scenario 2:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1OGc0GccvpxYwvkU5o2oVYPBp45ZcnE__4KDO3WxKmQZIJct3IcmOJR34R0pYXbzDoOY6kA287-cplKA2pY-qEfnoOVDAkZOWwhMEoW2FXwduWt-bNafx5Hot6QnmRr5wRX6pyoeBiU8/s640/Conformal+Dielectric+2.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1OGc0GccvpxYwvkU5o2oVYPBp45ZcnE__4KDO3WxKmQZIJct3IcmOJR34R0pYXbzDoOY6kA287-cplKA2pY-qEfnoOVDAkZOWwhMEoW2FXwduWt-bNafx5Hot6QnmRr5wRX6pyoeBiU8/s1600/Conformal+Dielectric+2.PNG)

Modelling in Technology file:

**DIELECTRIC DEL\_a**

conformal = true

T\_thickness = 0.2

S\_thickness = 0

B\_thickness = 0

di\_constant = 3.8

thickness = 0

height = 4.1

p\_layer = M1

**DIELECTRIC DEL\_b**

conformal = true

T\_thickness = 0

S\_thickness = 0.2

B\_thickness = 0

di\_constant = 3.8

thickness = 0

height = 4.1

p\_layer = M1

**DIELECTRIC DEL\_c**

conformal = true

T\_thickness = 0

S\_thickness = 0

B\_thickness = 0.2

di\_constant = 3.8

thickness = 0

height = 4.1

p\_layer = M1

### Scenario 3:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWXaH3BH7-nJaLzqE0ulJI3fw2QNFV15EmnWI3I1gK4NKoDSdmapaWVVLkKyrEKUqFfJlM2hYpXTnMFSjdjX989STHcnVIv8CqbKBuH1Gw2f26IXtMSIX_z9cDNACDwYFCUTrYfxcmecI/s640/Conformal+Dielectric+3.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWXaH3BH7-nJaLzqE0ulJI3fw2QNFV15EmnWI3I1gK4NKoDSdmapaWVVLkKyrEKUqFfJlM2hYpXTnMFSjdjX989STHcnVIv8CqbKBuH1Gw2f26IXtMSIX_z9cDNACDwYFCUTrYfxcmecI/s1600/Conformal+Dielectric+3.PNG)

Representation of DEL\_a1, DEL\_a2 and DEL\_a3 in Technology file:

**DIELECTRIC DEL\_a1**

conformal = true

T\_thickness = 0.2

S\_thickness = 0

B\_thickness = 0

di\_constant = 3.8

thickness = 0

height = 4.1

p\_layer = M1

**DIELECTRIC DEL\_a2**

conformal = true

T\_thickness = 0.15

S\_thickness = 0

B\_thickness = 0

di\_constant = 2.8

thickness = 0

height = 4.1

p\_layer = DEL\_a1

**DIELECTRIC DEL\_a3**

conformal = true

T\_thickness = 0.15

S\_thickness = 0

B\_thickness = 0

di\_constant = 1.8

thickness = 0

height = 4.1

p\_layer = DEL\_a2

**Remember:** In above representation, for DEL\_a2, p\_layer is previous dielectric (i.e DEL\_a1). It's because this dielectric has parent layer DEL\_a1. It's deposited on the top of DEL\_a1. Top thickness also measured with respect to DEL\_a1.

Note: you might be thinking why Height parameter is same in all 3 cases. It depends on EDA vendor, how they want to represent the height of Conformal layer. Here I am assuming that my tool is going to automatically measure actual height with the help of provided data. :)

Representation of DEL\_b1 and DEL\_b2 in Technology file:

**DIELECTRIC DEL\_b1**

conformal = true

T\_thickness = 0

S\_thickness = 0.2

B\_thickness = 0

di\_constant = 3.8

thickness = 0

height = 4.1

p\_layer = M1

**DIELECTRIC DEL\_b2**

conformal = true

T\_thickness = 0

S\_thickness = 0.15

B\_thickness = 0

di\_constant = 2.8

thickness = 0

height = 4.1

p\_layer = DEL\_b1

Similarly, Representation of DEL\_c1 and DEL\_c2 in Technology file:

**DIELECTRIC DEL\_c1**

conformal = true

T\_thickness = 0

S\_thickness = 0

B\_thickness = 0.2

di\_constant = 3.8

thickness = 0

height = 4.1

p\_layer = M1

**DIELECTRIC DEL\_c2**

conformal = true

T\_thickness = 0

S\_thickness = 0

B\_thickness = 0.15

di\_constant = 2.8

thickness = 0

height = 4.1

p\_layer = DEL\_c1

### Scenario 4:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXM1OhoeYNX5hBoUGNztx8kR4fvvKNgbWchsnDLnpOobSnMfj98ph-ir-U-D7oTt8mFV_BpEqXFiKYheUSST7W-vekMlxCwjzdNpdNb_CWjailss2QkpmpXSiojhzQvxLjpy2mAFPZSTc/s640/conformal_dielectric1.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXM1OhoeYNX5hBoUGNztx8kR4fvvKNgbWchsnDLnpOobSnMfj98ph-ir-U-D7oTt8mFV_BpEqXFiKYheUSST7W-vekMlxCwjzdNpdNb_CWjailss2QkpmpXSiojhzQvxLjpy2mAFPZSTc/s1600/conformal_dielectric1.PNG)

Modelling in Technology file:

**DIELECTRIC DEL2**

conformal = true

**T\_thickness = 0.1**

S\_thickness = 0.2

B\_thickness = 0.0

di\_constant = 2.8

**thickness = 0.4**

height = 4.1

p\_layer = M1

DEL2 is a conformal dielectric & the reason behind this is - It has a Side Thickness and Top thickness parameter. But you may be thinking that it looks like a planar at all other places, it's shape is similar to non-conformal dielectric. I can understand your confusion. Actually, you are right that at certain places it's conformal and at some places it's non-conformal.

In the representation of all conformal layer, you may have noticed that thickness parameter is 0. It's because they dnt have any thickness as such (I am not talking about top thickness. That's a different parameter). In this case, this thickness parameter is non-zero like in case of Planar dielectric.

At the end, I just wanted to highlight once again that different EDA vendors have different syntax and different way to represent dielectric layers in technology file. Above representation is just for your understanding purpose, it's not specific to any company.

Posted by
VLSI Expert
at
[4:11 PM](https://www.vlsi-expert.com/2017/10/technology-file-modelling-of-dielectric.html "")[2\\
comments](https://www.vlsi-expert.com/2017/10/technology-file-modelling-of-dielectric.html#)

[Newer ](https://www.vlsi-expert.com/search?updated-max=2018-01-22T09:30:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2017-10-30T16:11:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 4. ## Friday, January 10, 2014

**URL:** https://www.vlsi-expert.com/2014/01/
**Date:** 2014-01
**Tags:** sta, ESD, dft, parasitic

## Friday, January 10, 2014

### [10 Ways to fix SETUP and HOLD violation: Static Timing Analysis (STA) Basic (Part-8)](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html)

## Wednesday, January 8, 2014

### [Effect of Threshold voltage: Static Timing Analysis (STA) Basic (Part-7c)](https://www.vlsi-expert.com/2014/01/effect-of-threshold-voltage-static.html)

[Newer ](https://www.vlsi-expert.com/search?updated-max=2014-04-12T11:05:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2014-01-08T14:07:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 5. #### 43 comments:

**URL:** https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html
**Date:** 2014-01
**Tags:** physical-design, sta, digital-design, dft, Crosstalk, parasitic

#### 43 comments:

01. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[February 16, 2014 at 2:00 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1392539413414#c3044909821091272936)

 Awesome Learning Experience. It is a very interesting blog to refresh the concepts on STA. Thank you:)

 Reply

 Replies

 Reply

02. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[March 7, 2014 at 2:24 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1394139268300#c1957778556597394462)

 Kudos to you!! This is one great blog for learners like me! Thank you loads for all your effort! May god bless you!

 Reply

 Replies

 Reply

03. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[April 20, 2014 at 7:31 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1398002502851#c2482945654228289410)

 really nice to learn...

 Reply

 Replies

 Reply

04. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[June 5, 2014 at 2:51 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1401960117692#c3134151107892942962)

 Explanation in awesome. Efficient use of examples. Looking forward to read more topics.

 Reply

 Replies

 Reply

05. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[June 28, 2014 at 3:42 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1403907161809#c6450715174419022539)

 thank you very much.

 interesting.....

 Reply

 Replies

 Reply

06. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 20, 2014 at 3:01 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1408527118404#c3960795444562401989)

 The explanation is great. Thanks for sharing the post :)

 Reply

 Replies

 Reply

07. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 8, 2014 at 1:55 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1410121500029#c7809176290291726245)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

08. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[October 6, 2014 at 6:59 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1412602165806#c7213725253388806704)

 Thank you very informative :)

 Reply

 Replies

 Reply

09. !

 [December 22, 2014 at 9:03 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1419262423471#c6939551279148237730)

 Hi, Sir,

 when will RC delay (wire delay) > cell delay?

 Sincerely,

 Eric

 Reply

 Replies

 Reply

10. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[February 12, 2015 at 11:54 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1423765495881#c6264800395658646620)

 Thank you for a very informative blog on STA. Lot of concepts got clearer.

 Reply

 Replies

 Reply

11. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[February 16, 2015 at 9:57 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1424104061239#c518105412521436641)

 Very nice and great work sir..Kudos to you..

 Reply

 Replies

 Reply

12. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[April 20, 2015 at 12:38 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1429513683666#c137032945652341579)

 Great stuff. Check method 2, bullet 3.

 Reply

 Replies

 Reply

13. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[June 3, 2015 at 9:38 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1433304532922#c2059299935416955400)

 If a chip has hold violations it can be fixed by changing the supply voltage. For hold you might need to increase the logic delay and so decreasing the supply voltage. This might actually trigger set up violation but care needs to be taken.

 Reply

 Replies

 Reply

14. ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdXkRMbTHHN2fCuFPO3cOX3dcR7013FUCmgMROEzp2orjtNqBG93O1X56_7Q2ZE_RTOGjtlp1pCrYq92OXvGZuUpnItsIUc52RCB_2f7TOOIsTfqIy2pP_UZEj3DquiQ/s45-c/DSC00715.JPG)

 [July 28, 2015 at 12:56 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1438025174874#c3334034244642024146)

 This was really helpful. Can you please suggest any sources to practice questions on this topic?

 Reply

 Replies

 Reply

15. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 12, 2015 at 10:32 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1442077369396#c413468996566482817)

 Thank you very much

 Reply

 Replies

 Reply

16. !

 [October 30, 2015 at 10:30 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1446181204352#c5298645021570497937)

 wow super pakka very good explanation

 Reply

 Replies

 Reply

17. !

 [November 20, 2015 at 3:43 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1448014395922#c6709218075957732100)

 Thanks a lot!!! learnt a lot from this blog

 Reply

 Replies

 Reply

18. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[December 12, 2015 at 7:25 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1449928508247#c4501535639202252221)

 Hi,

 You have said, "hold violation happens when data is too fast compared to clock speed". But how can hold violation be related to clock speed? Here with clock speed do you mean delay in capture path or clock frequency?

 Reply

 Replies

 Reply

19. ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHkSgA9ATcndkIRF92c4vhyAgUDWe_0QSGedwfryVwT_HfM38iI-Oj-ZEiNYEEDutsZDy5oEDoAABf4k27Zgrlhby7BkIt-qeI5M0Z1zM83zRWbVJerFdQkUFVor9onnY/s45-c/kite1.png)

 [December 15, 2015 at 7:15 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1450187101269#c5510814527266848308)

 You got to efficiently explain what Synopsys and Cadence manuals don't do. Thanks a mill.

 Reply

 Replies

 Reply

20. !

 [January 14, 2016 at 8:45 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1452741320159#c7430758265886545156)

 Who fix these setup and hold violation?

 Whether the designer or backend team?

 Reply

 Replies

 !

 [January 18, 2016 at 4:46 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1453115812271#c9099689308515714627)

 Before I can help you with the Answer - you have to differentiate the work of Designer and backend Team? What do you mean by Backend team ?

 Replies

 Reply

 Reply

21. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[March 17, 2016 at 1:29 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1458158355445#c5781337238824247036)

 sir ur saying like first go for setup violation then after for hold ..but after CTS also preference only for setup first and then for hold ???...plz clearify

 Reply

 Replies

 Reply

22. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[April 16, 2016 at 10:02 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1460824344468#c764096319656181472)

 Thanks for the blog post . Quick query : Hold time of a flop dictates that logic delay of the combinational path be more than a given value ( Tdelay > Thold ) . So can we say that Thold puts a limit on the max frequency of operation since 1/ (max freq) > Tsetup + Tdelay ( I am ignoring c2q delays and clk skews for simplicity )

 Reply

 Replies

 !

 [April 18, 2016 at 8:54 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1460949895175#c1089683521959785362)

 I can reply you .. but best is you check these 2 Articles

 http://www.vlsi-expert.com/2016/02/setup-and-hold-check.html

 http://www.vlsi-expert.com/2016/02/setup-and-hold-violation.html

 At the end of these 2, I am sure you can yourself figure out whether it has dependency or not. If Not - Ping me again - I will explain you.

 Replies

 Reply

 !

 [April 18, 2016 at 8:59 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1460950193150#c6044964870629815736)

 links are:

 [Advance Setup and Hold Check](http://www.vlsi-expert.com/2016/02/setup-and-hold-check.html)

 [Advance Setup and Hold Violation](http://www.vlsi-expert.com/2016/02/setup-and-hold-violation.html)

 Replies

 Reply

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[May 26, 2016 at 12:18 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1464245293982#c2874955002743008230)

 Hi, thanks for the reply.. I read through the blogs; still I think there is a dependence ie If I reduce the combinational path delay to a very low value (~0) then there would be hold violation; hence "max freq period" = Tsetup + Tcombdelay.

 Replies

 Reply

 Reply

23. !

 [June 19, 2016 at 10:09 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1466311170903#c8862619219605066732)

 Thanks a lot for information...............

 Reply

 Replies

 Reply

24. !

 [June 20, 2016 at 1:00 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1466364651600#c6590599685133160378)

 If there is a long wire between cells then adding buffers will reduces the delay through decrease in transition time. So, my question is, how is optimum number of buffers are determined? I hope adding in more numbers will increase delay than reducing it!!

 Reply

 Replies

 !

 [June 20, 2016 at 11:33 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1466402592919#c1271844824591894826)

 You are right .. If you will add more buffer , it will increase the delay. There are lot of ways to find the optimum number of buffers. Basically there are algorithm for that. but this post is just to provide a insight about the methods which can help you in the field or during design.

 Other Algorithm I will try to cover in some other post.

 Replies

 Reply

 Reply

25. !

 [August 27, 2016 at 10:03 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1472315638528#c7304802483950528998)

 Is it possible to fix the hold violation of a manufactured chip by tweaking operating condition, e.g., decreasing supply voltage or increasing temperature?

 Reply

 Replies

 Reply

26. ![](https://resources.blogblog.com/img/blank.gif)

 Srinivasan[May 31, 2017 at 5:33 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1496232229076#c4889027484347750226)

 Hi,

 I am using Vivado design suite from Xilinx. After synthesis, in timing summary, I got a some setup time violations. There was an option to maximize the delay from start point to end point. After following that step, the setup time violation issue was solved.

 The above condition contradicts the fact that "decreasing the delay" fixes the setup time violation. Please explain.

 Reply

 Replies

 Reply

27. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[October 11, 2017 at 1:57 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1507710433941#c4610700145136041168)

 hi expert

 what about pipeline technique?

 if the timing is not meeting b/wn two flops by regular methods .we can insert flop to meet timing is it correct or not? please reply me

 Reply

 Replies

 Reply

28. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[November 13, 2017 at 9:07 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1510544244370#c3026814617466877422)

 So stage delay (cell delay + wire delay) in case of single buffer < stage delay in case of 2 inverter in the same path. I think here stage delay of buffer is > stage delay of 2inverters...also can you please explain why transition time of inverter is low..thank you

 Reply

 Replies

 Reply

29. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[November 16, 2017 at 11:58 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1510813729295#c7257268235518704059)

 wat is the relation between violations and crosstalk.and also how do v relate delay with crosstalk

 Reply

 Replies

 Reply

30. !

 [November 23, 2017 at 1:12 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1511422954232#c7847609568943817081)

 Can we Change the setup and hold violations after the chip is manufactured?

 Reply

 Replies

 Reply

31. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[February 9, 2018 at 7:03 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1518183181097#c2063273768378130323)

 Thanks,,. will tool(cadence encounter) take cares above steps in its algorithm else we have to specify at each stage??

 If yes help me with the commands for various steps you mentioned above .

 Thank you

 Reply

 Replies

 Reply

32. !

 [October 23, 2018 at 1:15 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1540237533042#c3001861183228687724)

 It looks like all the methods described here are for fixing setup and hold violations during the backend stage (placement and routing) of the design. Methods like buffering in a path, inserting repeaters, HVT swap, driver size adjustment, cell position adjustment all comes in backend only. What are the possible solutions to setup and hold violations in early stage of the design, say during RTL design?

 Reply

 Replies

 Reply

33. !

 [September 6, 2019 at 11:18 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1567748894559#c908467085655551705)

 Thanks expert !! For clear explanation for solving setup and hold violation.

 if the supply voltage reduces delay will increase and hold violation clear.

 so why we can dump chip after fabrication??

 Reply

 Replies

 Reply

34. !

 [September 6, 2019 at 11:20 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1567749028991#c8184088143461607858)

 Thanks expert !! For clear explanation for setup and hold fixing

 if we decrease the supply voltage, delay will increase

 why we dump chip after fabrication for hold violation??

 Reply

 Replies

 Reply

35. !

 [November 2, 2019 at 2:00 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1572683429291#c884082550046320312)

 Please explain me about hold analysis...and how exactly the uncertainty effect the timing analysis

 Reply

 Replies

 Reply

36. !

 [March 28, 2020 at 7:12 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1585402952016#c5064667960856295353)

 In Method 1 of Fixing Setup violation, How reducing the cell delay increases wire delay ? Please resolve my doubt..

 Reply

 Replies

 Reply

37. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[April 26, 2020 at 12:21 AM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1587840700464#c7010790818054055083)

 For a 4 input NAND gate is there is delay difference from A->O and D->O ?

 Reply

 Replies

 Reply

38. !

 [August 30, 2021 at 12:47 PM](https://www.vlsi-expert.com/2014/01/10-ways-to-fix-setup-and-hold-violation.html?showComment=1630307864982#c2398683194700416364)

 Wonderful explanation and understandable even to a beginner. Thanks for the information. What is the book that you had mentioned in the Method 4? can you please reply with that..!!!

 Reply

 Replies

 Reply

Add comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

Load more...

[Newer Post](https://www.vlsi-expert.com/2014/01/5-steps-to-build-career-in-vlsi.html "Newer Post")[Older Post](https://www.vlsi-expert.com/2014/01/effect-of-threshold-voltage-static.html "Older Post")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[Post ()](https://www.vlsi-expert.com/feeds/1214005786851276612/comments/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 6. ## Thursday, July 26, 2012

**URL:** https://www.vlsi-expert.com/2012/07/
**Date:** 2012-07
**Tags:** sta

## Thursday, July 26, 2012

### [Static Timing Analysis (STA) Using EDA Tool - Part1](https://www.vlsi-expert.com/2012/07/static-timing-analysissta-using-eda.html)

Error 404 (Not Found)!!1

**404.** That’s an error.

The requested URL `/host/0B8GyWNXT7IOJaWZ1VUFLVVc1a2M` was not found on this server. That’s all we know.

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 7. #### 15 comments:

**URL:** https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html
**Date:** 2011-09
**Tags:** physical-design, sta, dft, parasitic

#### 15 comments:

01. ![](https://resources.blogblog.com/img/blank.gif)

 Shubham[September 16, 2011 at 2:24 PM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1316163295130#c1943581693966690942)

 nice explanation.

 I have a question though, when we calculate the total delay of the path we addup cell delay + interconnect delay and cell delay is calculated by taking into account the interconnect loading effect.So, isn't this wrong as we are taking the interconnect effect twice in our delay calculation

 Reply

 Replies

 Reply

02. ![](https://resources.blogblog.com/img/blank.gif)

 Your VLSI[September 19, 2011 at 8:57 AM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1316402877416#c4878829763889229314)

 Hi Shubham,

 Its not like that .. we take care about the every reasons/cause of the delay with in a particular path. But we never do anything twice.If you can wait for sometime .. you will see in my few next blog, how we usually calculate the cell delay. Just give me some more time. If its urgent .. please drop me a mail.. I will try to explain you there..

 Reply

 Replies

 Reply

03. ![](https://resources.blogblog.com/img/blank.gif)

 sharankumar[March 6, 2012 at 12:19 AM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1330973374398#c4705709810519031132)

 excellent work for who are looking for detailed and well explained STA especially freshers

 Reply

 Replies

 Reply

04. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[March 6, 2012 at 5:32 PM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1331035358067#c7396094980719802153)

 Dear sir,

 please explain about wire load model also.

 Reply

 Replies

 !

 [March 7, 2012 at 2:30 PM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1331110850786#c2337322133364495665)

 Hi,

 Its Done. Please Check the next blog.

 Replies

 Reply

 Reply

05. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[February 27, 2013 at 6:21 PM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1361969507392#c1966961077446892154)

 Dear Sir,

 Please explain the need of interconnect delay model.

 Reply

 Replies

 Reply

06. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[March 6, 2015 at 5:23 PM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1425642813072#c3199987820317932153)

 Sir,

 As u told we consider characteristics of Driver and load while calculating interconnect delay....but that is already consider in our cell delay....so it counts twice in delay calculation

 Reply

 Replies

 !

 [April 20, 2015 at 10:04 AM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1429504460607#c2761201951128150694)

 Hi ... I am talking about the characteristics .. It can be considered several time. we are not using the delay values twice.

 Think that you are traveling by a bus - you bus is not in a good condition - so you will feel tired after journey. So in case you have to visit somewhere - it matters how is your Bus condition. Means characteristic of BUS IMPACT a lot.

 Since Bus is not in a good condition - it is also sure that it will also take more time to reach destination. But that in above case we are not talking about that time taken by BUS (means delay added by BUS in your visit).

 Hope it helps you.

 Replies

 Reply

 !

 [August 16, 2016 at 12:43 PM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1471331638501#c6711568857480473621)

 This comment has been removed by the author.

 Replies

 Reply

 Reply

07. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 16, 2016 at 12:46 PM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1471331767987#c8131663336743793200)

 This is still not clear. Could you please explain more on this.

 Reply

 Replies

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 16, 2016 at 12:59 PM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1471332567839#c3266008588919722936)

 While calculating the cell delays we consider the loading effect of interconnect on the cells. Then we calculate the delays through the nets as well. Arn't we adding the delays of the interconnects twice,

 Replies

 Reply

 Reply

08. ![](https://resources.blogblog.com/img/blank.gif)

 [html color](http://htmlcolorspicker.com/)[August 7, 2017 at 8:07 AM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1502073470154#c361709338399108128)

 Your article reflects the issue people are concerned about. The article provides timely information that reflects multi-dimensional views from multiple perspectives. I look forward to reading quality articles that contain timely information from you.

 Reply

 Replies

 Reply

09. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[March 18, 2018 at 8:38 AM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1521342492929#c6591903874696647165)

 Its like you read my mind! You seem to know so much about this, like you wrote the book in it or something.

 I think that you could do with a few pics to drive the message home

 a little bit, but other than that, this is wonderful blog.

 An excellent read. I will definitely be back.

 Reply

 Replies

 Reply

10. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[March 18, 2018 at 11:28 PM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1521395929116#c6258775617797334808)

 Sir,please tell me how to measure delay for a digital circuit in transient analysis using synopsys hspice netlist.

 Reply

 Replies

 Reply

11. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[May 24, 2018 at 12:38 AM](https://www.vlsi-expert.com/2011/09/delay-interconnect-delay-models-static.html?showComment=1527102498406#c1696413579959360106)

 Keep this going please, great job!

 Reply

 Replies

 Reply

Add comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

Load more...

[Newer Post](https://www.vlsi-expert.com/2012/02/signal-integrity-si-part-1.html "Newer Post")[Older Post](https://www.vlsi-expert.com/2011/08/delay-timing-path-delay-static-timing.html "Older Post")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[Post ()](https://www.vlsi-expert.com/feeds/8556215832382366827/comments/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 8. ## Thursday, April 7, 2011

**URL:** https://www.vlsi-expert.com/2011/04/
**Date:** 2011-04
**Tags:** sta, dft, parasitic

## Thursday, April 7, 2011

### ["Setup and Hold Time" : Static Timing Analysis (STA) basic (Part 3a)](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3a.html)

[Newer ](https://www.vlsi-expert.com/search?updated-max=2011-08-04T09:17:00%2B05:30&max-results=1&reverse-paginate=true "Newer ")[Older ](https://www.vlsi-expert.com/search?updated-max=2011-04-07T15:09:00%2B05:30&max-results=1 "Older ")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[ ()](https://www.vlsi-expert.com/feeds/posts/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 9. #### 57 comments:

**URL:** https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html
**Date:** 2011-04
**Tags:** sta, dft, parasitic

#### 57 comments:

01. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[February 2, 2012 at 2:57 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1328131650177#c9203398835345563544)

 should not the launch edge be the second rising edge of CLK, since hold checks are done for the same clock cycle?

 Reply

 Replies

 !

 [February 7, 2012 at 10:18 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1328590085120#c6954634259136857511)

 Hi,

 I didn't get you question very clearly. Please elaborate it.

 Replies

 Reply

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[May 19, 2012 at 9:20 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1337399447700#c8424774535965553206)

 dear clock checks ideally should be done at the rising or capturing edge of clock b only.. but sir has written and shown in the diagram that the data is arriving at the ff2 d before the clock b and it is in the transition region..which is a hold violation and we l loose data.. at the end sir has written that to avoid it.. either decrease the buffers in the clock path or increase the delay in the data so that the data arrives at or before the capturing edge of the clock b.. just to show the hold violation sir has made the same in the diagram

 Replies

 Reply

 Reply

02. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[February 15, 2012 at 4:42 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1329304364608#c1228863630920285900)

 I think there is misprint in hold time analysis

 Reply

 Replies

 !

 [February 16, 2012 at 12:10 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1329331209573#c4441889467125201507)

 can you please let me know what's that misprint?

 Replies

 Reply

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[April 29, 2012 at 12:46 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1335683772949#c455302552455846258)

 3rd Paragraph from last. It has" because of very short logic delay between FF1/Q and FF1/D" Its FF2/D

 Replies

 Reply

 !

 [May 2, 2012 at 11:44 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1335939252033#c6360559411920677770)

 thanks man ... You are right.. It should be FF2/D.

 Replies

 Reply

 !

 [June 13, 2012 at 10:38 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1339607318567#c6725847794849410479)

 Thank you so much for the excellent tutorial, sir! Can you please correct the misprint in the original post just in case readers do not see the comment? Thanks again!

 Replies

 Reply

 ![](https://resources.blogblog.com/img/blank.gif)

 follower[December 25, 2016 at 9:41 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1482682295045#c3250638555064290856)

 Could you correct the misprint? Thank you.

 Replies

 Reply

 Reply

03. ![](https://resources.blogblog.com/img/blank.gif)

 hairol[March 3, 2012 at 11:53 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1330755793194#c7358930589713285593)

 Thank you very much.

 Reply

 Replies

 Reply

04. !

 [July 13, 2012 at 12:38 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1342120113906#c2261281443755264872)

 hi , do u have nay idea about datapulse violations

 Reply

 Replies

 Reply

05. !

 [October 26, 2012 at 10:20 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1351227027976#c5586261471735237024)

 is setup and hold time for given input slew is constant?

 Reply

 Replies

 Reply

06. !

 [October 26, 2012 at 10:21 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1351227088598#c4752646790783698910)

 i:e

 Ts+Th=constant

 Reply

 Replies

 !

 [October 26, 2012 at 12:00 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1351233016472#c564721388809415697)

 Hi Jigs,

 For a particular FF, these numbers are always constant.

 Replies

 Reply

 !

 [January 15, 2013 at 7:10 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1358214054369#c7787340945140260461)

 plz can u explain me ?

 Replies

 Reply

 Reply

07. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[March 7, 2013 at 3:20 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1362649805365#c2014461621834987171)

 thank you

 Reply

 Replies

 Reply

08. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[March 14, 2013 at 5:00 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1363260655600#c5171098452566845502)

 sir i don't understand.. setup check at next clock edge and hold check at same clock edge.. while launching and capturing edge are different.. plz explain

 Reply

 Replies

 !

 [March 14, 2013 at 11:26 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1363283775692#c224222801368322012)

 Clock edge at Launching FF - considered as launching edge but when this edge reaches capturing FF, it become Capturing Edge.

 Now in setup and hold we are talking every thing on the Capturing FF, means every thing is related to Capturing edge.

 I hope you got my point. Still If some confusion, please write in detail about your confusion.

 Replies

 Reply

 Reply

09. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[March 26, 2013 at 7:56 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1364308001001#c7890793888262917842)

 Thank you sir, I got your point..

 Reply

 Replies

 Reply

10. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[May 14, 2013 at 8:30 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1368543611050#c4040204100385239175)

 Hi VLSI Expert,

 You have mentioned that we need to reduce the delay of the clock to avoid the hold time violation right. Could you please clarify me if you are talking about reducing the CLKB clock width?

 Reply

 Replies

 Reply

11. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 30, 2013 at 3:51 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1377858114914#c2370542946699616294)

 yyyy

 Reply

 Replies

 Reply

12. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[October 4, 2013 at 9:18 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1380858498774#c341083011457980468)

 In the Hold Check Timing diagram, it looks like the first transition of FF2/D (1 > 0) happens at about the same time as the first rising edge of CLKB.

 So this will result in setup violation (and maybe hold violation too), even before we get to the second rising edge of CLKB.

 Reply

 Replies

 Reply

13. !

 [January 21, 2014 at 5:21 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1390305062526#c7904519940544369022)

 Can you please elaborate why setup check at next clock edge and hold check at same clock edge ?

 from CLK1 .. We check both at next clock edge and calculate also like that but why we say diffrently?

 Please elaborate

 Reply

 Replies

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[February 23, 2014 at 11:46 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1393179393587#c3171650239258692540)

 Data can arrive at the following flip flop only at the next clock edge. At T1, FF1 generated its output to data D1, whereas FF2 was processing FF1's output to data D0. FF2 will be able to process FF1's output to D1 only at the next clock edge, T2 = T1 + T(clk).

 Hold analysis is done only after the data has already arrived, and so naturally for the same clock cycle.

 As for the figures posted above, I think the one for Hold Time is perhaps erroneous, since T(launch) and T(capture) must be at the same clock cycle. I've already posted a comment below, highlighting the same. Awaiting yourVLSI's reply!

 Replies

 Reply

 Reply

14. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[February 23, 2014 at 11:40 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1393179034661#c8297053352969090214)

 In the Hold Time diagram, the Capture edge has been shown one clock cycle after Launch edge, whereas it should be at the same clock edge (delayed by buffers).

 The Set-up Time diagram, too uses the same clock edges, which though, is correct.

 Reply

 Replies

 !

 [February 24, 2014 at 1:51 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1393230103806#c908994073020730752)

 For the same data Capture and launch edges are always one clock cycle. But for analysis purpose of Hold - you analysis the whole concept at the same edge. I would say - check the pic more closely and you will crack this figure also.

 Replies

 Reply

 Reply

15. !

 [June 7, 2014 at 11:13 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1402119831673#c214136111944016961)

 Hi,

 I am a silent follower of your blog. You are doing a phenomenal service to millions of people through your high caliber VLSI knowledge. If I may request you to write on the following topics, I would be grateful to you,

 1\. Setup/hold calculation of Multicycle path

 a. slow to fast clock path

 b. fast to slow clock path

 Thanks a lot!

 -Mainul

 Reply

 Replies

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[June 8, 2014 at 1:07 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1402169823205#c8505211071815684907)

 Indeed, this set of brilliant engineers managing this blog are the pride of India, and the whole family of electronics engineers!!!

 Your request for Multi-cycle Timing explanation is something that many, including me, have been waiting to make!

 Replies

 Reply

 Reply

16. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 7, 2014 at 11:22 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1407390756400#c3851174228746614891)

 why system goes in metastable state after setup time voilation?

 Reply

 Replies

 Reply

17. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 29, 2014 at 2:20 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409302247357#c3515097608457181334)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

18. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 29, 2014 at 4:33 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409310208379#c8519351786934626285)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

19. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 29, 2014 at 6:00 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409315458974#c1311411170665771316)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

20. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 31, 2014 at 9:51 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409458874789#c4041938326698122553)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

21. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 1, 2014 at 1:30 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409558414228#c6108827464989983321)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

22. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 1, 2014 at 1:52 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409559776048#c3429559787756532037)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

23. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 1, 2014 at 3:09 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409564363979#c824772858386235707)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

24. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 2, 2014 at 3:44 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409609681128#c2556894363770660883)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

25. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 3, 2014 at 2:19 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409690947704#c1363023009603107677)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

26. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 3, 2014 at 2:46 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409692618265#c8628381107781925162)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

27. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 4, 2014 at 1:55 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409819158221#c3781246642578469647)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

28. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 4, 2014 at 2:41 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409821861909#c8242045820794683901)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

29. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 4, 2014 at 8:04 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409841291065#c7546221684424457086)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

30. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 4, 2014 at 8:58 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409844504345#c4218772661090757445)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

31. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 5, 2014 at 3:59 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1409912965997#c5577645340095399844)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

32. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 7, 2014 at 10:34 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1410109491164#c2337296613609301471)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

33. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[March 5, 2015 at 2:53 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1425504187030#c6032221874984358483)

 At Hold Check Timing Capture Edge (Rising Edge) of CLKB should to capture the correct value of FF2.D (zero) according to the current figure. There seems to be something wrong with this part of the figure??

 Reply

 Replies

 !

 [April 20, 2015 at 10:10 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1429504840043#c3271269360376528142)

 This figure ... is trying to help you to visualize the reason of the hold Violation.

 Replies

 Reply

 Reply

34. ![](https://resources.blogblog.com/img/blank.gif)

 sri[September 10, 2015 at 1:56 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1441830403079#c576793321307477724)

 If my chip has a hold violation, can i resolve it by dropping the voltage? I sacrifice frequency potentially, but the delays usually increase with lower voltage?

 Reply

 Replies

 Reply

35. !

 [March 18, 2016 at 7:32 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1458266566617#c4974105576414824714)

 hey have a doubt as we know for flipflop we check the setup at next clock edge and for hold time at same clock edge.

 I want to know for latch where will be the setup and hold is checked ( i mean which clock edge )

 Reply

 Replies

 !

 [June 1, 2016 at 7:49 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1464790770090#c4000610080563545443)

 Latch means level-triggered (say 0 level--> 1 level ==> pos-level; 1 level-->0 level==>neg-level);

 here the setup check done before the level 1 appears

 and the setup check done before the level 1 appears

 above mentioned for pos-level

 similarly oppose to neg-level

 Replies

 Reply

 Reply

36. !

 [December 21, 2016 at 5:00 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1482319812391#c644527694879415161)

 Please clear doubt regarding latch setup and hold time claculation

 Reply

 Replies

 Reply

37. ![](https://resources.blogblog.com/img/blank.gif)

 [slither io](http://sli-therio.com/)[October 2, 2017 at 9:38 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1506917311271#c2779065827705029653)

 The knowledge you share really changes me in life, I sincerely thank you for the things you have done, sure your blog will help more people.

 Reply

 Replies

 Reply

38. ![](https://resources.blogblog.com/img/blank.gif)

 [wings io](https://sites.google.com/site/wingsio303/)[December 8, 2017 at 9:54 AM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1512707094988#c8916969597588383251)

 Yes, the article I was looking for. Your article gives me another approach on the subject. I hope to read more articles from you.

 Reply

 Replies

 Reply

39. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[January 30, 2018 at 3:30 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1517306410543#c8709725036580949282)

 In the last diagram, shouldn't the FF2Q signal be initially high?

 Reply

 Replies

 Reply

40. !

 [January 11, 2019 at 1:11 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1547192468604#c7665404658899482069)

 This comment has been removed by the author.

 Reply

 Replies

 Reply

41. !

 [January 11, 2019 at 1:12 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1547192530369#c3451607814126559416)

 why hold check on same edge?

 Reply

 Replies

 Reply

42. !

 [August 12, 2019 at 2:55 PM](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3b.html?showComment=1565601921621#c1251923632774830058)

 Set up time voilation leads in metastable state

 a. always

 b. independent

 c. never

 d. depends

 Reply

 Replies

 Reply

Add comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

Load more...

[Newer Post](https://www.vlsi-expert.com/2011/05/example-of-setup-and-hold-time-static.html "Newer Post")[Older Post](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3a.html "Older Post")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[Post ()](https://www.vlsi-expert.com/feeds/1061400870358173940/comments/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 10. #### 102 comments:

**URL:** https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html
**Date:** 2011-03
**Tags:** physical-design, sta, digital-design, dft, parasitic

#### 102 comments:

01. ![](https://3.bp.blogspot.com/-E7XICrndGFs/TcUe8m_dlvI/AAAAAAAAAY0/wYcQ3c2Z20g/s35/DSC05652.JPG)

 [March 10, 2011 at 9:48 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1299773928950#c3801176981072370856)

 Hi sir, if for a certain timing contraint u give for ex: let me say that my clock period is 5ns and if slack is met using synopsys primetime, so can i say my frequency of operation of my whole ckt is 200MHz ??? kindly reply. Thanks

 Reply

 Replies

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[February 10, 2014 at 8:01 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1392042677173#c4203588103346716833)

 Yes. Frequency = 1 / Clock Period

 Replies

 Reply

 ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgo7mztCSsb_AJX4ePCyipzX6z0F0xnSchBhJarpodT8BH4KB-OmzBJX0lclGDxkJMWsONI8qsORVIf9tuaSnQSNEac50PgJJ7sJfZZRppAJ6cltVzIqca6LEQiATWKlNU/s45-c/IMG-20171101-WA0001.jpg)

 [January 20, 2021 at 6:23 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1611147204072#c8892968353798938369)

 I apologize, but I differ with the answer. 200 MHz is the frequency which is used as clock input. The slack is met on 200 MHz, then it means the frequency of operation must be bigger than 200 MHz for sure. That number must have been mentioned in the synthesis report.

 Replies

 Reply

 !

 [December 30, 2021 at 4:36 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1640862419691#c4969527417009173542)

 Yes even i agree with bhaskar, so even if i am meeting the slack at 5ns it might be possible to meet the slack at 4.5ns although the slack would be less poisitive now but still it might be possible for my design to be running at a much higher frequency.

 Replies

 Reply

 Reply

02. !

 [April 15, 2011 at 4:03 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1302863632558#c642941349972674030)

 Hi,

 Fabulous work u r doing. Reaaly the topics covered in this blog are helping me a lot.

 Thanks & Regards,

 indu.

 Reply

 Replies

 Reply

03. !

 [April 18, 2011 at 11:19 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1303105773103#c5028503923977773576)

 Hi @Samiappa -- you are right.. if slack is meeting.. then you can say .. but still there is a "can".. :) means its not 100% true. There are other factors also. Please see my other blogs for details...

 @Indu -- Thanks a lot for such a appreciation.

 Reply

 Replies

 Reply

04. !

 [April 19, 2011 at 10:54 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1303190663785#c352428508073159841)

 Hi,

 I have some doubts in basics of CTS. How can i communicate with you to discuss about my queries? i mailed you yesterday ( mail ID i got from this blog - vlsi.expert@gamil.com ) but the mail delivery is failed. If you don't mind may i have your right mail ID.

 I will be more help-full if you can reply to my queries..Since i have more queries i'm asking you to provide any other option which i can communicate with you or do let me know if i shall post my queries here.

 Will we waiting for your reply ...

 Thanks & Regards,

 Indu.

 Reply

 Replies

 !

 [October 9, 2018 at 2:12 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1539074542086#c1681177838692744880)

 it's gmail not gamil. This may be the reason because of which your email was not sent

 Replies

 Reply

 Reply

05. !

 [April 19, 2011 at 12:51 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1303197662615#c8042786021387470134)

 Hi Indu,

 I am okay with either ways.. means by mail and by posting here...

 There is a typo in my mail id ( which you have mentioned here)-- Correct one is

 vlsi.expert@gmail.com

 Reply

 Replies

 Reply

06. !

 [April 20, 2011 at 11:06 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1303277760149#c5085604313558204226)

 Hi Expert,

 I have sent a mail with list of queries to the above given mail ID.

 Thanks a lot for your quick response.

 Regards,

 Indu.

 Reply

 Replies

 Reply

07. !

 [April 20, 2011 at 5:34 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1303301078416#c8230074440133644575)

 Hi Expert,

 These concepts helped me a lot.

 Thank you very much

 Thanks & Regards

 Anil

 Reply

 Replies

 Reply

08. !

 [April 21, 2011 at 10:25 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1303361725609#c3796474144748894003)

 Thanks Anil.

 Reply

 Replies

 Reply

09. ![](https://resources.blogblog.com/img/blank.gif)

 Karl[May 29, 2011 at 11:53 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1306693403238#c8540581771032324000)

 Easy to understand and clear...very useful!

 Reply

 Replies

 Reply

10. !

 [June 26, 2011 at 12:33 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1309028624922#c497075620865054581)

 hello sir,

 this is Harish, i just want to say few words abt it. ur blogs are so understandable way to earn knowledge about timing analysis and i recall totally what i know....

 and i got some topics from it easily to remember..

 so u did a great job..

 suggestion: i think its also good if u present this in ppts

 Reply

 Replies

 Reply

11. !

 [June 26, 2011 at 11:01 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1309066287979#c5711856430864441564)

 hi Harish,

 First of all. thanks a lot for such compliment. another thing is .. I have these in PPT and uses when ever I have to present anywhere. you can say that its for internal use. :)

 Reply

 Replies

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[July 23, 2013 at 6:54 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1374585850061#c6981757180324216424)

 hello sir,

 can u send me those ppts

 my email id is meetvatsald@gmail.com

 Replies

 Reply

 !

 [November 9, 2018 at 1:22 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1541749925398#c2939070625533288720)

 hi sir ,

 Please send STA PPTs to below mail. Thanks in advance .

 ksiva7079@gmail.com

 Thanks ,

 Siva Prasad

 Replies

 Reply

 !

 [November 9, 2018 at 1:23 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1541750008928#c712097618873106756)

 hi sir,

 Please send STA PPt to below mail.Thanks in advance.

 ksiva079@gmail.com

 thanks,

 siva Prasad

 Replies

 Reply

 !

 [February 11, 2019 at 6:34 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1549847082346#c5563467674267106035)

 Hi Sir, Could you please share the PPT to this email id, harshithajhj@gmail.com.

 Thank you in advance.

 Replies

 Reply

 !

 [March 4, 2019 at 11:13 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1551678204082#c8223834041916474511)

 Sir, could you please send me those ppts.

 my mail id is shubhamthemotivator@gmail.com

 Replies

 Reply

 !

 [November 17, 2019 at 7:40 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1573999828380#c1374969100311839101)

 Sir , please can u send me those ppts .

 My mail id is ambikahunashyal111@gmail.com

 Replies

 Reply

 Reply

12. ![](https://resources.blogblog.com/img/blank.gif)

 [vlsiinterviewquestion](http://www.vlsiinterviewquestion.com/index.html)[September 9, 2011 at 10:48 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1315545500007#c3552103701592443890)

 For multi-cycle paths remember that driving flop/latch holds/keeps output data without changing for more than one cycle, which is the key. Hence there is more time for data to setup to endpoint and more time for the hold race to not violate.

 Reply

 Replies

 Reply

13. !

 [October 28, 2011 at 10:26 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1319820971376#c7215718585944685636)

 Thanks Great work!!!

 Reply

 Replies

 Reply

14. !

 [December 10, 2011 at 9:40 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1323490230764#c4606504599118712701)

 hai sir

 this blog was very usefull for my work and easy to understand

 great job............

 thanks & regards

 vimal

 Reply

 Replies

 Reply

15. !

 [December 10, 2011 at 9:41 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1323490298300#c6928918110303325281)

 hai sir

 this blog was very usefull for my work and easy to understand

 great job............

 thanks & regards

 vimal

 Reply

 Replies

 Reply

16. ![](https://resources.blogblog.com/img/blank.gif)

 chandrakant[January 30, 2012 at 6:09 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1327927177841#c5116665000346529326)

 sir,

 your explanation is good.Thank you this blog cleared most of my doubts regarding timing paths and static timing analysis.

 regards

 chandrakant

 Reply

 Replies

 Reply

17. ![](https://resources.blogblog.com/img/blank.gif)

 chandrakant[January 30, 2012 at 6:10 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1327927209302#c2658822372631204586)

 sir,

 your explanation is good.Thank you this blog cleared most of my doubts regarding timing paths and static timing analysis.

 regards

 chandrakant

 Reply

 Replies

 Reply

18. ![](https://resources.blogblog.com/img/blank.gif)

 jabbar[March 3, 2012 at 11:22 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1330753956687#c2895549767508605493)

 thank you friend.

 Reply

 Replies

 Reply

19. ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh-4B2-ldVbMNgynR333Fcan_ZUcgEzaEFo4NGB1exeGcBbzpiX9gIuPPzt0pYaC31zLpAY0PhNDA7HDQ7KP-sZx3ziNhvm5ra57Zw8pgvtttkebJR3AarBPhm12bMDQ/s45-c/IMG_0484.JPG)

 [April 1, 2012 at 12:20 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1333219822869#c3367342572346459488)

 Very useful, must read for people like me.

 Thanks

 Swami

 Reply

 Replies

 Reply

20. ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh-4B2-ldVbMNgynR333Fcan_ZUcgEzaEFo4NGB1exeGcBbzpiX9gIuPPzt0pYaC31zLpAY0PhNDA7HDQ7KP-sZx3ziNhvm5ra57Zw8pgvtttkebJR3AarBPhm12bMDQ/s45-c/IMG_0484.JPG)

 [April 1, 2012 at 12:21 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1333219884896#c7993412215681501085)

 Very useful, must read for people like me.

 Thanks

 Swami

 Reply

 Replies

 Reply

21. !

 [April 16, 2012 at 2:09 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1334565599983#c1572047620724238551)

 The articles are nice .......I am not clear with multicycle path can u provide a figure related to that.....thanks

 Reply

 Replies

 Reply

22. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[June 8, 2012 at 11:36 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1339135617878#c1769374981000231568)

 really a nice session for sta terminology...

 Reply

 Replies

 Reply

23. ![](https://resources.blogblog.com/img/blank.gif)

 Suryansh[June 21, 2012 at 2:44 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1340270080335#c4387230601042818237)

 Great Work...

 Reply

 Replies

 Reply

24. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[July 3, 2012 at 12:52 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1341300158811#c5061073375959235103)

 Thank you very much for this illustrative explanation on timing analysis ,it is very good for beginner..

 Reply

 Replies

 Reply

25. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[July 4, 2012 at 7:42 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1341411145132#c4610388152518375237)

 Hello Sir,

 Your blog is terrific and very helpful.

 Can you please discuss required time and slack?

 Reply

 Replies

 !

 [July 10, 2012 at 2:58 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1341912507626#c4312928060380918167)

 Please read Following Blogs

 [Examples Of Setup and Hold time" : Static Timing Analysis (STA) basic (Part 3c)](http://www.vlsi-expert.com/2011/05/example-of-setup-and-hold-time-static.html)

 Replies

 Reply

 Reply

26. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 13, 2012 at 2:54 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1344849873231#c9045219445641527208)

 You should write a book for Standford and IITians. Existing articles and books on this topic shows author themselves do not know what it is. But you explained it perfectly. So you are expert.

 Reply

 Replies

 Reply

27. !

 [August 27, 2012 at 9:47 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1346084220979#c5489980229380207051)

 I usually find the timing concept bit confusing. But reading your blog is just great. It now looks simple and more easy.

 Thanks a ton. Keep up the good work.

 Reply

 Replies

 Reply

28. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 29, 2012 at 6:55 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1346246759804#c6348522186114897988)

 Hello Sir,

 Your blog has been very eloquent and information wealthy.

 Thanks for such blogs.Please keep up the spirit of writing.

 Thanks,

 Shivaji.

 Reply

 Replies

 Reply

29. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 25, 2012 at 1:15 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1348559108573#c3592329337942986972)

 very Good post

 Reply

 Replies

 Reply

30. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[October 7, 2012 at 8:17 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1349621253906#c2896112270937625282)

 superb explanation from the expert....

 Reply

 Replies

 Reply

31. !

 [November 6, 2012 at 9:24 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1352174080127#c3156293136675416948)

 what is macro stacking floorplan?.

 sir please upload physical design (floorplan,placement,routing )topics ...

 Reply

 Replies

 !

 [November 8, 2012 at 12:38 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1352358511503#c1348047558671541273)

 Jigs,

 regarding the Floorplan/Placement/Routing - you have to wait little bit. But Sure i will update those info also.

 Replies

 Reply

 Reply

32. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[November 30, 2012 at 1:05 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1354260940675#c5756353752780829879)

 thank u 4 clearing my doubts

 Reply

 Replies

 Reply

33. ![](https://resources.blogblog.com/img/blank.gif)

 vijay[December 11, 2012 at 7:42 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1355235168243#c6045142959570607440)

 Excellent mr. 'expert' - MCP and shortest and longest path were lucidly described. thanks!

 Reply

 Replies

 Reply

34. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[December 11, 2012 at 10:17 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1355244439248#c1139410401649054132)

 Hi,

 This is excellent. Please also details about test modes in STA ( scan cap dc, scan cap ac , scan shift, jtag, rambist ).

 Reply

 Replies

 Reply

35. !

 [March 28, 2013 at 4:10 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1364467227014#c6075784663421405947)

 This comment has been removed by the author.

 Reply

 Replies

 !

 [March 28, 2013 at 4:11 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1364467298139#c3773140767532485401)

 Hello sir,

 Can you please tell the difference between longest path and critical path with example. I am confused with these paths.

 Thanks,

 Deepthi

 Replies

 Reply

 !

 [November 26, 2013 at 2:04 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1385454873812#c3178386369964003271)

 You should not be confused. critical path are that path - which has high impact on the design timing. It can be short or may be long path. Point is - if there is any issue in the critical path then you have to fix that one first. you can't even compromise with that path.

 Longest path .. means more number of gates and more delay in that path.

 Replies

 Reply

 Reply

36. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[May 16, 2013 at 1:58 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1368692900771#c7014115905894296282)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

37. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[June 6, 2013 at 3:58 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1370514489932#c7337797742786799231)

 Very good explanation. :) Good work. Thanks a lot!

 Reply

 Replies

 Reply

38. !

 [July 14, 2013 at 9:02 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1373815960114#c3694073509036122818)

 This comment has been removed by the author.

 Reply

 Replies

 Reply

39. !

 [July 14, 2013 at 9:03 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1373815986610#c818398719309873869)

 Hello Sir !! here is a link ,the questions are based upon the setup ,hold times prop delays of the system as whole are to be found out .I am clear with finding the setup and hold times as per the method you have said but I have some problem with this .Pl clarify this !

 http://web.mit.edu/6.111/www/f2007/tutprobs/sequential.html

 Reply

 Replies

 Reply

40. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[July 27, 2013 at 10:52 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1374945775501#c6461171831776298840)

 Hi

 Capture clock period and its path delay together constitute required time of data at the input of capture register.

 i didn't get this point clearly ..is the capture clock period and clock period same or its the delay of the capture clock path

 Reply

 Replies

 !

 [November 26, 2013 at 2:09 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1385455159944#c1038013425170645652)

 capture clock period == clock period of capture clock. Means there may be scenerion that there are multiple clocks and different clock are driving the capture flipflop and launching FF. So that's the reason I have mentioned specifically "capture clock period "

 Replies

 Reply

 Reply

41. !

 [August 30, 2013 at 12:03 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1377844387911#c6412377202561337116)

 This comment has been removed by the author.

 Reply

 Replies

 Reply

42. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 30, 2013 at 12:16 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1377845176645#c3438346071030012704)

 Hi,

 Thanks for the blog. It's very helpful. But i couldn't understand Multi Cycle Path. Can you update it with using some diagrams so that it can be understood easily

 Reply

 Replies

 !

 [November 26, 2013 at 2:09 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1385455185561#c8692888610679538837)

 I will try...

 Replies

 Reply

 Reply

43. !

 [November 7, 2013 at 6:59 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1383830940156#c1402469599211988989)

 hello sir i need basis of static timing verification ....and concept of static timing analysis ....i need overview for about this concepts please upload as soon as possible.......

 Reply

 Replies

 !

 [November 26, 2013 at 2:10 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1385455229064#c3320200373723408121)

 Static Timing Analysis - related a lot of article already present. Please follow other parts of this series.

 Replies

 Reply

 Reply

44. !

 [November 26, 2013 at 12:55 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1385450717653#c6987203923442846799)

 Hello sir,

 A great work on STA is given as a nutshell.Thanks a lot.It would be appreciable if you could add details on Statistical Static Timing Analysis (SSTA)also.

 Reply

 Replies

 !

 [November 26, 2013 at 2:10 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1385455258923#c8223507480675382762)

 I will try but It will take some time

 Replies

 Reply

 Reply

45. !

 [November 26, 2013 at 7:01 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1385472680289#c4324238408768037782)

 I finally understood the mumbo jumbo of STA! Thank you so much! :)

 Reply

 Replies

 Reply

46. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[November 27, 2013 at 10:40 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1385529051972#c4432212068472127319)

 well explained :-)

 Reply

 Replies

 Reply

47. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[November 30, 2013 at 10:26 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1385787376694#c2637620190083130118)

 Hello Sir,

 Thank you very much for ur efforts in explaining about STA.

 I have a doubt in MCP example explanation were, you have stated

 "However, if you have a signal in the 60MHz domain that indicates the phase of the 30MHz clock, you can design a circuit that allows for the full 33ns for the clock crossing, then the path from flop30 -> to flop60 is a MCP (again with N=2)."

 why is path between flop30 to flop60 MCP as the launching flop30 operates in slower clock it gives enough time to get sync with flop60 as the next data from flop30 will be launched after two clock cycles at flop60. ( I am taking 30Mhz clock as main clock, as assumed by your statement).

 So may be data from flop60 to flop 30 may take 2 cycles as flop60 as to keep its data stable for complete 2 cycles of its clock (60Mhz clk) to sync with flop30.

 Please let me know if I have understood something wrong.

 Thanks

 vijay

 Reply

 Replies

 Reply

48. !

 [March 12, 2014 at 11:28 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1394603938381#c3635871231552711254)

 Sir, Thank you for this blog this is the first time i understood FALSE PATHS correctly

 Reply

 Replies

 Reply

49. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[April 15, 2014 at 9:11 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1397576491268#c5993268221185768116)

 why setup time is large compared to hold time????can any one give me answer???

 Reply

 Replies

 !

 [April 20, 2015 at 9:49 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1429503586269#c3476954461425465424)

 Try to figure out once by taking the concept of master Slave flipflop. I think that will help you.

 Replies

 Reply

 Reply

50. !

 [June 18, 2014 at 2:20 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1403081430494#c3600220019427389614)

 hi sir can i get the related papers or pdfs.if so i will give email id

 Reply

 Replies

 Reply

51. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[December 30, 2014 at 5:00 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1419939033813#c653374102278672730)

 I wanted some illustrations or some problems to get perfection.. Can u share d links which provide this..

 Thanks in advance

 Reply

 Replies

 Reply

52. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[April 7, 2015 at 3:15 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1428399935341#c6527424481012152043)

 sir i need detailed explanation on critical path analysis

 Reply

 Replies

 !

 [April 20, 2015 at 9:52 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1429503727105#c7929522258269264443)

 Critical path Analysis is a very big topic. Actually It depends how you called a path Critical in your design. Path is critical because it's part of clock path or there is congestion, or setup/holds are violating there.

 So please let me know what exactly you want to know.

 Replies

 Reply

 Reply

53. !

 [May 10, 2015 at 3:49 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1431209955042#c1433608701512758928)

 Hi, this is great tutorial, congrats!

 I have a question: in the "what is a setup and hold time?" section you have a TpdDIN, this delay is the same than the data path timing?? that you mentioned in previous sections, this TpdDIN delay is the cloud drawing logic that you have in your previous figures?

 Thanks

 Reply

 Replies

 Reply

54. !

 [May 30, 2015 at 11:52 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1432966923492#c8528644675297881775)

 This comment has been removed by the author.

 Reply

 Replies

 Reply

55. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 14, 2015 at 6:24 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1442192054375#c1765239893400232934)

 Sir, in your diagram, where you have flip flops UFF1 to UFF3.

 What would happen if the clock period used were shorter than the maximum signal propagation time through the circuit?

 Why do electrical signals take time to propagate through combinatorial logic?

 Reply

 Replies

 !

 [July 10, 2020 at 5:13 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1594381382747#c1107192088868232705)

 Because of RC

 Replies

 Reply

 Reply

56. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[October 12, 2015 at 12:29 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1444633149386#c9220218208957004253)

 Hello Sir ,

 Can you please explain about Timing analysis with multiple clocks?

 Reply

 Replies

 Reply

57. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[October 16, 2015 at 3:08 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1444988281450#c5986735880198320730)

 In data path start point,2nd statement should be data pin of ff/latch/memory .

 am i correct

 Reply

 Replies

 Reply

58. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[January 21, 2016 at 1:46 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1453320966374#c5255859729563284670)

 This is the most well-explained text I have found on STA yet. Very clear and consisely told. Thank you very much for your time and effort on writing this article. As a Computer Engineering student this has helped me a lot with understanding this concept.

 Reply

 Replies

 Reply

59. !

 [March 5, 2016 at 10:15 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1457153153338#c8194712300588788948)

 Awesome stuff

 Reply

 Replies

 Reply

60. !

 [October 3, 2016 at 7:28 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1475503126116#c7992681428409244694)

 in STA description its written that its advantage is that it performs timing analysis for all possible paths(whether real or false) but in false path description its written that timing analysis is not done for false path?? im confused..can anyone plz clarify my doubt..

 Reply

 Replies

 !

 [October 4, 2016 at 12:02 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1475562774818#c639346356539043694)

 See.. STA can do analysis of any path.

 But why do you want to do the analysis on false path ?? So we specify that we don't want to do analysis on false path. If you will do the analysis don't make sense and if there are any violations - then you have to unnecessary waste your time to fix it.

 So both statements are correct. :)

 Replies

 Reply

 Reply

61. !

 [October 18, 2016 at 3:50 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1476786014781#c8116334933072579164)

 sir do you have information about to solve problems on combinational circuits delays??

 i want more no 0f problems and solutions to calculate max frequency in both combinational and sequential circuits

 plz help me sir

 Reply

 Replies

 Reply

62. ![](https://resources.blogblog.com/img/blank.gif)

 Priyangi[April 5, 2017 at 10:41 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1491412268550#c667933557511027174)

 Hi Expert,

 You have done a f=great job..!! Your blog has helped a lot in my interview preparation. But the MCP topic, can you please explain it in more detail, as I am having difficulty in understanding it, esp the 30MHz and 60MHz example.

 Reply

 Replies

 Reply

63. !

 [May 16, 2017 at 1:15 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1494877517659#c8516696101922061482)

 springs vigorously with smooth looking over and quick Select the most applicable format to rapidly fulfill your assignment, regardless of whether

 Reply

 Replies

 Reply

64. !

 [May 16, 2017 at 1:19 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1494877776685#c6328876291529045274)

 Only one click needed to convert any PDF documents into searchable and editable in the following formats:

 Reply

 Replies

 Reply

65. ![](https://resources.blogblog.com/img/blank.gif)

 [slither io](http://sli-therio.com/)[June 28, 2017 at 2:49 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1498641540996#c6531909498820187124)

 Very good, I think I found the knowledge I needed. I will see and refer some information in your post. thank you.

 Reply

 Replies

 Reply

66. !

 [October 28, 2017 at 11:51 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1509171677319#c1521052536416731718)

 Hello sir,why hold time is less compare to setup time?

 Reply

 Replies

 Reply

67. ![](https://resources.blogblog.com/img/blank.gif)

 [slither io](https://sites.google.com/site/slitherioocom03/)[December 15, 2017 at 1:35 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1513325132554#c1811589859177599853)

 it's very good, i like it

 Reply

 Replies

 Reply

68. !

 [March 30, 2018 at 3:42 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1522404723592#c2994695706420745913)

 can clock network latency be negative ?? (both case ideal propagated) if yes what does it mean

 ??

 I am running one design while report\_timing , (Innovus) i am getting negative network latency .. how it is possible ? In both case , ideal clock and in propagated clock !!

 Reply

 Replies

 Reply

69. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 21, 2018 at 8:31 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1537542117365#c1268503180749619937)

 Thanks for finally talking about >""Timing Paths" : Static Timing Analysis (STA) basic (Part 1)" <Loved it!

 Reply

 Replies

 Reply

70. !

 [December 30, 2018 at 11:14 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1546148666428#c8975821452899524832)

 What is multi clock timing analysis

 Reply

 Replies

 Reply

71. !

 [February 6, 2019 at 9:38 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1549469302993#c146571064607432113)

 sir can u please elaborate why clock gating is required

 Reply

 Replies

 !

 [March 29, 2019 at 11:59 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1553840991208#c2503685654617153822)

 for to optimize timing

 Replies

 Reply

 Reply

72. !

 [March 6, 2019 at 4:10 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1551868834329#c2235169037307129812)

 firstly why do we check hold on the same clock edge?

 Reply

 Replies

 Reply

73. !

 [March 28, 2019 at 11:21 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1553795502199#c2917077174434769478)

 hello sir

 could you please mail the ppts

 my mailid is :kotlomonica@gmail.com

 Reply

 Replies

 Reply

74. !

 [March 29, 2019 at 11:59 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1553840941453#c9180462279310598983)

 u have doe a great job sir

 Reply

 Replies

 Reply

75. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[July 29, 2019 at 12:22 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1564383121643#c4024024831802635100)

 hello,

 I am bit confused about critical path. When we consider setup critical path should be max delayed path but with respect to hold it should be least delayed path.

 Please help me with this..

 waiting for your reply..

 Thanks Regards..

 Najma

 Reply

 Replies

 Reply

76. !

 [September 3, 2019 at 12:33 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1567494212545#c3537540613936741768)

 what is difference between critical path and longest path?

 Reply

 Replies

 Reply

77. !

 [May 12, 2020 at 8:59 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1589297352589#c3252093988120511903)

 great

 Reply

 Replies

 Reply

78. !

 [May 6, 2021 at 8:43 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1620270790212#c7167949838107051964)

 Hi sir,

 What if the two input of any gate as two different slew?

 I mean at pin A the slew is 10ps and at pin B the slew is 20ps to calculate the delay of that gate using slew and delay table which input slew should consider for the delay?

 Or we should get proceed by the timing path?

 Reply

 Replies

 Reply

79. !

 [October 23, 2021 at 6:16 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-timing.html?showComment=1634993208062#c4776755599241357610)

 Hi, expert

 please send the ppt of STA to ramavenkata555@gmail.com

 Many ads are flowing here.

 Thank you Expert!!

 Reply

 Replies

 Reply

Add comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

Load more...

[Newer Post](https://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format.html "Newer Post")[Older Post](https://www.vlsi-expert.com/2011/02/timing-analysis-basis-what-and-why.html "Older Post")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[Post ()](https://www.vlsi-expert.com/feeds/5684209439444070061/comments/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

### 11. #### 55 comments:

**URL:** https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html
**Date:** 2011-03
**Tags:** sta, digital-design, dft, parasitic

#### 55 comments:

01. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[January 5, 2012 at 3:41 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1325715092341#c830081876023803246)

 Hi, the example you have provided is an out of phase clock triggered latches. But in "Few Important things" you mentioned time borrowing occur for the same phase of the same clock. Could you please clarify or provide a different example with single clock.

 Reply

 Replies

 !

 [February 7, 2012 at 11:00 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1328592607175#c744027919846681846)

 Hi,

 Its true in both way. means time borrowing can be done when the clocks are out of phase, but that's usually disable by the EDA tools.

 So prefered or say recommended thing is: both the clock should be in phase relation.

 Replies

 Reply

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[November 25, 2013 at 9:06 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1385350564812#c4965245855218916026)

 it also confused me, in the example, if L1 & L2 are within the same clock phase, it can not work, right? I don't understand when triggered latch and capture latch are using the same clock, how to borrow? for example, if G1 > 5ns, and CLK1 and CLK2 are both 5ns high in same phase, when signal reaches L2, it is already not enabled.... There must be phase different here then they can borrow, right?

 Replies

 Reply

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[July 9, 2014 at 11:54 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1404887048074#c5174295142994637155)

 I think here Fig1 clock1 and clock2 keep a constant phase difference, so they are called in "in phase".

 you could think them just keep a constant clock network delay (skew).

 here out of phase means theire phase difference is a variable.

 Replies

 Reply

 ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[July 22, 2014 at 5:34 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1406030659182#c5397632714639473879)

 YES, The two clocks are out of phase .But In few Important things , they are saying about at the time of borrowing

 You can see the time of borrowing clearly in the second figure. All borrowing occurs in the positive cycle. Both phi1 and phi2

 Replies

 Reply

 Reply

02. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[May 9, 2012 at 9:21 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1336535477316#c4627579445481006865)

 Hi,

 Most EDA tools recommend not using latches, and will issue warning. The same goes to verilog coding guidelines, where latches could cause stuck state machine. Are these the same latches you are referring to??

 Reply

 Replies

 !

 [May 28, 2012 at 7:32 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1338170554332#c7274764702350574970)

 Yes. Latches are not recommended but if you can use timing Borrowing technique, then you can use latches. :)

 Replies

 Reply

 Reply

03. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[May 31, 2012 at 10:42 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1338441159787#c504020261255088135)

 Hi, this is a great website for me ( new bird) to understand the STA concept...i will use cadence P&R tool (EDI), can you please show me how to read and understand the timing report, like skew, setup vio...etc.

 Thanks again.

 Reply

 Replies

 !

 [November 26, 2013 at 2:13 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1385455381056#c448984734519389072)

 I would say that it will be good if you read manual for that. Specifying the tool specific things are out of scope of this series. I can try that later on but right now I am really sorry.

 Replies

 Reply

 Reply

04. !

 [June 13, 2012 at 9:15 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1339602349420#c5150868794406772904)

 This comment has been removed by the author.

 Reply

 Replies

 Reply

05. !

 [June 13, 2012 at 9:16 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1339602395887#c5862799361628422139)

 "In other word we can say that path1 can borrow sometime (3ns) from the path2. Since the sum of path1 and path2 is 10ns, which is the required time of L3, there will be no voilation in either of the Latches." --> If path2 were to take 3ns, can path2 borrow 1ns from path3? I am just wondering because it is not explained. Thanks in advance!

 Reply

 Replies

 !

 [November 26, 2013 at 2:13 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1385455429679#c7362033783420260525)

 This comment has been removed by the author.

 Replies

 Reply

 Reply

06. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 28, 2012 at 3:01 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1348781467245#c9152547332162025093)

 Hi

 If the latency in clock cycle increases then will the time period go down ? For your example latency is 2 clock cycle.

 suppose path1=2ns path2=8ns then How many clock cycle(latency) is required ?Does borrowing can happen from previous stage in this case ?

 Does pulse register can use time borrowing ?

 what is the difference between time borrowing and cycle stealing ?

 Reply

 Replies

 !

 [July 19, 2016 at 10:39 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1468948192961#c7617990279818264477)

 I don't think that a previous stage can borrow time. Since, the whole concept behind time borrowing is that the next latch can wait till it's clock is high. So the combinational circuit before it can produce the result when it's high and it can be transferred to next circuit.

 Replies

 Reply

 Reply

07. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[December 7, 2012 at 10:53 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1354857830826#c6714212030512908309)

 Hi

 tell me how to take timing analysis using mentor graphics tool.what is slack in that report.difference between negative and positive slacks.

 Reply

 Replies

 Reply

08. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 29, 2014 at 8:32 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409281337390#c88739614232483872)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

09. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 29, 2014 at 2:20 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409302256507#c8878673718718768108)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

10. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 29, 2014 at 3:50 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409307654390#c8311701169222873137)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

11. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 29, 2014 at 8:53 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409325783392#c8595149034991541598)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

12. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 30, 2014 at 2:51 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409347288021#c7610080777729305227)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

13. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 30, 2014 at 5:25 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409356526559#c4314396169440370086)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

14. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 31, 2014 at 7:32 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409450571225#c5002851030974953529)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

15. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 31, 2014 at 9:51 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409458888842#c4005139985669462169)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

16. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 31, 2014 at 10:53 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409462607442#c7485811199772444730)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

17. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[August 31, 2014 at 2:20 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409475053913#c2847456795418112600)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

18. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 1, 2014 at 1:44 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409516059626#c79386310475339317)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

19. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 1, 2014 at 1:53 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409516590750#c5189372728093397576)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

20. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 1, 2014 at 4:17 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409525231429#c3395589507895060273)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

21. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 1, 2014 at 11:20 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409550655392#c1589757370830934082)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

22. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 1, 2014 at 1:30 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409558430523#c9073295562671181949)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

23. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 1, 2014 at 1:54 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409559878107#c3501823705769893992)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

24. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 1, 2014 at 10:14 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409589887258#c3604364302117244196)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

25. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 3, 2014 at 2:19 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409690963837#c409079551107826071)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

26. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 3, 2014 at 2:47 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409692640116#c2894114404134581505)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

27. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 3, 2014 at 9:45 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409717709097#c3050425140297061347)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

28. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 3, 2014 at 10:02 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409718736012#c5329917442709701310)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

29. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 3, 2014 at 9:55 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409761534842#c7532552601438035725)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

30. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 4, 2014 at 9:46 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409804174122#c2840057375666492199)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

31. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 4, 2014 at 11:39 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409810987155#c6702462911758756301)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

32. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 4, 2014 at 12:24 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409813682832#c849788424541987350)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

33. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 4, 2014 at 1:56 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409819166484#c826539087956007897)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

34. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 4, 2014 at 2:40 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409821828727#c6651987720871390897)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

35. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 4, 2014 at 8:02 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409841177553#c6666207264880149770)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

36. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 4, 2014 at 8:58 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409844516632#c3908494771939247453)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

37. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 5, 2014 at 9:32 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409889768467#c5427229884700442853)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

38. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 5, 2014 at 5:23 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1409918000797#c1948682999157145499)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

39. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 7, 2014 at 10:34 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1410109495360#c5305014483333236825)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

40. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[September 8, 2014 at 12:34 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1410116694652#c5896205896490300958)

 This comment has been removed by a blog administrator.

 Reply

 Replies

 Reply

41. ![](https://resources.blogblog.com/img/blank.gif)

 Anonymous[January 9, 2015 at 7:27 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1420811842796#c6955653720805710640)

 Hi Guys,

 To understand more about time borrowing in latch based design refer to "http://ohotspot.blogspot.in/2012/09/time-borrowing-and-time-stealing.html" (Understanding “Time Borrowing” in real designs).

 Reply

 Replies

 Reply

42. !

 [June 1, 2015 at 2:58 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1433150909867#c5428502581457630681)

 This comment has been removed by the author.

 Reply

 Replies

 Reply

43. !

 [August 23, 2017 at 2:49 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1503479949024#c55796430393244756)

 The last diagram before "few important things" which is supposed to be self-explanatory is not very clear to me. Can someone explain? Thanks!

 Reply

 Replies

 Reply

44. !

 [August 23, 2017 at 2:55 PM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1503480311603#c9013915437798817904)

 Also the statement that an edge triggered design will take 32 ns?

 I read some other blogs that insert a latch between two edge triggered flops..they explain the concept more clearly.

 https://forums.xilinx.com/t5/Technical-Blog/Time-Borrowing-in-Latches/ba-p/651529

 Reply

 Replies

 ![](https://resources.blogblog.com/img/blank.gif)

 [Kalpesh Lodha](https://plus.google.com/u/0/)[September 18, 2018 at 11:28 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1537250334118#c1124883568332552207)

 Thanks Aditya for sharing this.

 This forum has explained the concept in simple words.

 Do keep sharing such findings.

 Replies

 Reply

 Reply

45. !

 [November 27, 2018 at 11:13 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1543297388884#c520756033237043363)

 Superb and Excellent,

 Everything explained here is really very helpful to understand the STA.

 Thanks a lot for explaining in such a way.

 Reply

 Replies

 Reply

46. !

 [November 27, 2018 at 11:15 AM](https://www.vlsi-expert.com/2011/03/static-timing-analysis-sta-basic-part2.html?showComment=1543297554659#c3430583729572126289)

 Sir, Negative time borrowing I did not understand properly please help.

 Thanks,

 Gopal.

 Reply

 Replies

 Reply

Add comment

Post a Comment

To leave a comment, click the button below to sign in with Google.

Sign in with Google

Comment as:

Select Profile:

Google Account



Edit

Enter Comment

Publish

reCAPTCHA

Recaptcha requires verification.

 \- 

protected by **reCAPTCHA**

 \- 

Load more...

[Newer Post](https://www.vlsi-expert.com/2011/04/static-timing-analysis-sta-basic-part3a.html "Newer Post")[Older Post](https://www.vlsi-expert.com/2011/03/how-to-read-sdf-standard-delay-format_17.html "Older Post")[Home](https://www.vlsi-expert.com/)

Subscribe to:
[Post ()](https://www.vlsi-expert.com/feeds/8545842099322909270/comments/default)

## Must Read Article

[![Related Plugin for WordPress, Blogger...](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_sdeOyIqi1C_ZnqvlSOxYxpROBYIN6_CfOezpWNSkKJCHViWqAo90M1THkPKR-gLA-JlMQmdFabI-TtH-ofFAUgilbI4Ebb=s0-d)](http://www.linkwithin.com/)

## Search This Blog

![](https://fonts.gstatic.com/s/i/productlogos/translate/v14/24px.svg)

Original text

Rate this translation

Your feedback will be used to help improve Google Translate

---

