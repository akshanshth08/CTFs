# [DownUnderCTF(2020/09/18)](https://play.duc.tf/)

## Team Name : ASYN

## Rank : 311/1081 , Points : 1120

Contains the writepus of the challanges I was able to solve.


### Table of Contents
* [forensics](#forensics)
  * [On the Spectrum](#On-the-Spectrum)
* [Misc](#Misc)
  * [16 Home Runs](#16-Home-Runs)
* Crypto
  * [rot-i](https://github.com/akshanshth08/CTFs/blob/master/DownUnderCTF/Crypto/rot-i.md)
* Reversing
  * formatting
* Pwn
  * [shell this!](https://github.com/akshanshth08/CTFs/blob/master/DownUnderCTF/Pwn/Shell%20This!/Writeup.md)
  
  
### forensics
========================================================================================
#### On the Spectrum
-----------------------------------------------------------------------------------------
 points 100
 
#### Description

*My friend has been sending me lots of WAV files, I think he is trying to communicate with me, what is the message he sent?*

*Author: scsc*
 
*Attached files: message_1.wav (sha256: 069dacbd6d6d5ed9c0228a6f94bbbec4086bcf70a4eb7a150f3be0e09862b5ed)*

 For this challenge we are given a .wav file and we have to find the hidden message.I loaded the file in audacity and as the name of the challenge suggests I checked the spectogram of the file to find the flag.

![image](https://user-images.githubusercontent.com/45536407/94331976-ef202b80-ff9e-11ea-9e9e-0aa45afac6ae.png)

### Misc
========================================================================================
#### 16 Home Runs
-----------------------------------------------------------------------------------------
 points 100
 
#### Description
*How does this string relate to baseball in anyway? What even is baseball? And how does this relate to Cyber Security? ¯(ツ)/¯*
*RFVDVEZ7MTZfaDBtM19ydW41X20zNG41X3J1bm4xbjZfcDQ1N182NF9iNDUzNX0=*

From the string given can deduce that it is a base64 encoded string. We can decode it online to find the flag.

![image](https://user-images.githubusercontent.com/45536407/94332186-cf8a0280-ffa0-11ea-804f-05eddd1a729d.png)



