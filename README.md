# EncryptPractice
Practice with encryption. Basic encryption algorithm in Python.

This program utilizes string manipulation and dictionaries in order to generate relation tables and character key values in order to
encrypt messages. Through randomization the process is further strengthend.

The current character set contains 82 characters. 26 lowercase English alphabet characters, 26 upper case English alphabet characters,
10 numerical characters, and 20 symbols. This list can be changed in the keyGenerator.py file (plan to change this list from main.py).

Encryption process:
  1) Generate relation table (a -> b -> c -> a, for example) using keyGenerator.py's functions. Keys and relations are generated of randomly chosen characters, and key lengths are determined by the person creating them. Relation tables are generated from the given character set, shuffled randomly a given amount of times
  2) Using the previously generated relations and keys, input a message to encryption.py. Each character is randomized by steping through the relation table N number of times, where N is random for each character of the key
  3) message.txt will be updated with many lines that represent your encrypted message ([iterations, starting value]), which have been
     changed into random values
  
Decryption process:
  1) Taking message.txt's iterations and starting points and the correct relations table, the message is de-randomized to now 
     show the original character keys.
  2) Using the character keys table that was used when the message was encrypted, the message can be translated from keys to
     character values. The message will be decrypted at this point.
     
Example:
  1) relation table: 
      - a -> b
      - b -> c
      - c -> a
  2) keys:
      - a -> aaa
      - b -> bbb
      - c -> ccc
  3) message: abc
  4) converted message (characters -> keys): aaabbbccc
  5) randomized message ([iterations, start value]):
      - 1 b
      - 2 c
      - 0 a
      - 1 c
      - 2 a
      - 0 b
      - 1 a
      - 2 b
      - 0 c
  6) de-randomized message ([iterations, start value]):
     - aaabbbccc
  7) de-converted message (keys -> characters): abc
  
This is an extremely basic and for explanation purposes only example. Below is what a normal relation table 
and key set (length of 25)  would look like.
     

1) Keys: {	">":"2U1aOA_1t+b&5smo2+C+e1KlZ", 	"+":"@%kytv,ZOJ)Sag+3GVHe?zbsY", 	"B":"KJDwLeSclf%/^UI0tNZCj!*UE", 	
        "Q":"WJj$Cy<*A<B8L^Rd>iMX=x8oF", 	"d":"J&cb<g9l7ObbQnx2jte!k<-yT", 	"F":"3r)5Ssd3EaP7Mqi4_zfunR=Z+", 	
        "E":"?CM9r3!/7^DjC@g01R7&!s9EY", 	"$":"dcTMJCyV#%*Abio6RNp(X&Y>j", 	"C":"o/7$gk)W4Dti*^yUsImm6waQk", 	
        "Y":"qT!vvUy6c-G=DQiSK,)YZI>SQ", 	"/":"9MxIXFMP7s/S6y%)dY8<HfZJ>", 	"M":"VA)D5.Mu7b4>bG429V3X#fQd_", 	
        "(":"K2LbP%9E)Y@H%GfD2wDrsFYhc", 	"6":"df3ju%Fe2HOov)8jQPui1CvqF", 	")":".?*4CAcrR+fQ0#GgA&u_-fm=E", 	
        "p":"s82<IlrfrYn+o,mg<eRv&p+iW", 	"X":"5T<KkVjaiY8KY5*rgcF983<jk", 	"P":"DEQ_erUAJ6q=*sZc-lJ3OiZy@", 	
        "G":"06OSM.(0RHvdYpiha(xKgpeL>", 	"x":"59?y8>-BLeERRjXYH^k7Y3?%&", 	"j":"%*gx0UlS2)7xUJhEXU&K=wUr&", 	
        "g":"+@tWtQ*(sQj%Cv?ojOIV4<VZG", 	"W":")in#hzIt*_73)IO1C6<.Qi%(N", 	"_":"s+<gEjB0=>G^Os4GOjmk7dtc!", 	
        "H":"cR=CAEI-2UW<@,E!z@DC6S%J!", 	"<":"PqT&/JzFGIi(4(8v9&C<LMOwN", 	"O":"1OX7X7FVY.D$1P@308=MU=6r!", 	
        "@":"-SJ2msmd=fd,m4J-NJ)vBW4E@", 	"U":"$BSA#o=)47ki&0QiDSE?XJ6k0", 	"5":"jtC#%/E+h42b=&P^C#w3i2ixn", 	
        "f":"!bEBo%,PQ$tf3?jF%bR?CNVYk", 	"y":"dEekv8,,>4i2/1E1o(.Q#M+@_", 	"4":"IoMe>/&a(ROKXTBV28UIl-g9b", 	
        "*":"wrC>g82v.TTfNVMeJvCKD.oX@", 	"r":"gAr^KOP7&pUmql+&a1JZHL8Fr", 	"I":"/*(V2*Xnx3GYc,wOwnM<puZ%o", 	
        "h":"^*xt?OXl?eMoWa^4h2KzLRd^-", 	"1":"OI$n#54pqQrcR^EoTw(.AGzbd", 	"!":"zx^5luqTzf3Gpes(*6Zg^p2WW", 	
        "#":"t4LZ!+eS4Iwvj)h1m5?3OF60l", 	"w":"V<wcHOhY9Z(b97XR6f#?XF*!X", 	"-":"5eOw6I1l7q$=<fzk.f#P_$mN9", 	
        "z":"?g*@x(TCJ>o8ImQvc(U7a0@G/", 	"K":"rZ-5z_cm2k+cE.P2fA.GPs(&o", 	"c":"zd7DV&NEmkR5,e#kwu+6piM$,", 	
        "3":"OqT?T9Mip4Lyn@yGU.cJ&ji-L", 	"R":"%)v3O-xLV7XX^L1$FxnICb7?B", 	"u":"eNGgg81hFDJ5ZO1O2VHB?%@ua", 	
        "A":"gU.K&2.G0l_l!kc7o!BxhDHlK", 	"J":"Zy!.ZGFI%#o(ben*iike!nv5?", 	"Z":"+NSIe?Lm<%fhvXCvidgs1d@WU", 	
        "9":"rM-wm<fpXzfmX1q+0Mkw&TIvV", 	"D":"%l1bVm?M4nGc@8_X&xE^CmR4p", 	",":"A)Bro*E(fJcU/Wmw845O6fLxO", 	
        "i":"=L&Unbe+,9dwza.Nv71AoK?,D", 	"%":"X3i+YPIh_QnEH=fGkzk717,x>", 	"l":"m-+4$Kts*1T?un7TcoQA2W3qn", 	
        "&":"gu3)2?+_FGU@+5oWcYHpV9,Q0", 	"e":"htG?81oP$<_cukpPaRUEaK=9)", 	"T":"YBp<WW/^q1yDmryyXPhEs_s4U", 	
        "^":"7+U/4(9Hv(_1%@NTy_4U@ai=P", 	"V":"uK1tn>5Iu&Z$TD(q46Y)JI-3h", 	"?":"&X3.?ZFrV3dk#yayjb,EYev@v", 	
        "m":"F^@qIM46!MM+GNq@1h<!<uo/P", 	"t":",HtyFjH_D5ppb$wJkey7iCxU!", 	"q":"30@x=cAWjwlvX-SBy0-Il/1s$", 	
        "o":"/XGCehLb$TXCl#zDv/H(REq(w", 	"L":"14A7cROzCUHqegsTp*1tP<FyN", 	"S":"To(.d>(emRAH/fDghf6Agik?N", 	
        "2":"VB.WcRS8Ms-wzng/@wZVzc<)@", 	"N":"JM1WHs*niz+uMk^zXxLCKbb/j", 	"8":"B>LttmzUOQXFxnAixuWv,oFs1", 	
        "0":"ci7JF7xT,p^nEvDn4P)Cc12l_", 	"a":"b1dx8m!t_Eil%tYxJnjFzK_G0", 	"b":"-$oZcKOp/rZ2%#pCbPhU*zOAk", 	
        "n":"v*2Bx_WB$DHHci<5v3Vibs#Y,", 	"7":"5n^#s@B5gv8PIT>Sbr)A<$%DJ", 	"v":"pQcl3e8>FYXLR$7McV.C733*l", 	
        "s":"uxk#yrtQ>z=#B7?M)Vu-2?xaT", 	".":"cZx38E5y>Elmkt@-W%2_*lZgV", 	"=":"LlTJR@n.SA2_yX.Yyc+X*WwRS", 	
        "k":"?L1@E9Em*^KbnR^1(n)a>+iLt", }
        
2) relation table: {	">":"+", 	"+":"B", 	"B":"Q", 	"Q":"d", 	"d":"F", 	"F":"E", 	"E":"$", 	"$":"C", 	"C":"Y", 	
                  "Y":"/", 	"/":"M", 	"M":"(", 	"(":"6", 	"6":")", 	")":"p", 	"p":"X", 	"X":"P", 	"P":"G", 	
                  "G":"x", 	"x":"j", 	"j":"g", 	"g":"W", 	"W":"_", 	"_":"H", 	"H":"<", 	"<":"O", 	"O":"@", 
                  "@":"U", 	"U":"5", 	"5":"f", 	"f":"y", 	"y":"4", 	"4":"*", 	"*":"r", 	"r":"I", 	"I":"h", 
                  "h":"1", 	"1":"!", 	"!":"#", 	"#":"w", 	"w":"-", 	"-":"z", 	"z":"K", 	"K":"c", 	"c":"3", 
                  "3":"R", 	"R":"u", 	"u":"A", 	"A":"J", 	"J":"Z", 	"Z":"9", 	"9":"D", 	"D":",", 	",":"i", 
                  "i":"%", 	"%":"l", 	"l":"&", 	"&":"e", 	"e":"T", 	"T":"^", 	"^":"V", 	"V":"?", 	"?":"m", 
                  "m":"t", 	"t":"q", 	"q":"o", 	"o":"L", 	"L":"S", 	"S":"2", 	"2":"N", 	"N":"8", 	"8":"0", 
                  "0":"a", 	"a":"b", 	"b":"n", 	"n":"7", 	"7":"v", 	"v":"s", 	"s":".", 	".":"=", 	"=":"k", 
                  "k":">", }
     
3) message (plaintext): these are words that will be encrpyted
4) message (encrypted): 
25 .
76 x
52 I
99 J
20 O
86 <
27 D
50 b
51 W
93 -
30 R
65 k
53 R
36 c
70 5
46 )
50 Z
97 b
20 D
11 E
13 S
52 V
11 y
51 =
21 ^
85 t
35 2
71 Y
43 O
21 B
27 i
18 I
16 a
82 m
3 ?
10 W
82 L
58 k
86 s
8 2
79 f
55 /
48 h
15 T
59 j
84 N
71 h
70 n
70 J
39 k
85 w
15 =
42 V
3 o
80 N
63 x
56 -
59 v
42 Z
21 u
57 k
60 _
77 K
76 7
87 g
84 j
81 a
88 ,
15 c
17 H
77 2
38 >
12 M
15 L
66 k
86 D
29 J
93 M
42 >
27 T
34 2
82 q
61 q
59 ^
59 j
67 o
96 i
14 P
21 X
88 2
32 c
17 4
18 =
88 i
54 )
81 2
59 w
75 6
48 w
44 W
45 >
97 =
37 l
62 K
46 h
20 e
84 2
28 R
74 >
47 a
32 l
97 ^
55 g
90 C
100 r
65 +
92 B
87 D
45 b
23 f
9 +
18 ?
12 M
11 m
79 (
78 n
59 V
23 J
13 I
89 )
19 w
11 )
10 +
37 h
37 !
65 B
15 7
92 1
20 P
67 G
51 N
64 Y
8 5
22 d
57 &
9 d
71 7
84 L
28 a
44 +
1 7
98 i
98 g
54 b
14 d
46 U
56 6
4 2
53 v
37 c
8 m
97 0
27 +
32 p
29 #
2 W
36 d
51 3
14 I
48 i
15 e
77 #
69 M
26 3
88 .
94 r
56 _
53 E
13 b
73 I
25 D
33 9
33 U
35 M
22 !
59 E
31 6
33 P
38 6
75 v
42 G
10 B
3 -
11 V
94 m
51 7
14 >
73 m
90 )
34 2
97 D
85 S
64 +
55 h
19 Y
56 (
42 @
99 I
87 6
98 z
70 (
86 J
98 t
17 P
70 d
79 p
69 V
17 t
3 4
13 j
66 e
74 h
52 9
100 N
98 y
12 Y
59 V
29 %
95 I
5 (
35 l
19 W
42 *
15 )
38 #
50 2
54 *
48 n
89 d
13 R
64 +
50 v
78 P
44 O
18 G
91 d
57 ?
42 <
84 u
92 J
32 (
22 A
73 4
25 N
42 L
62 $
65 j
18 U
49 x
94 m
47 ^
31 H
29 k
85 =
84 x
73 !
40 i
71 j
65 _
92 a
28 3
97 g
13 u
83 w
57 b
2 6
49 o
90 @
84 M
22 k
25 ?
69 %
38 y
16 H
81 T
40 &
77 d
84 T
87 3
31 b
79 Z
86 >
61 0
21 R
71 B
18 q
79 d
2 S
99 f
3 c
83 _
33 >
100 ,
94 a
68 f
82 @
97 *
38 *
5 m
7 _
81 U
65 u
15 k
84 T
87 $
27 Q
99 Y
48 d
74 z
66 I
33 e
42 U
34 H
77 +
31 o
44 (
13 8
30 n
85 s
51 v
36 e
37 $
25 >
11 E
87 4
2 v
92 Q
20 H
72 o
46 o
15 Q
56 v
69 D
37 )
19 e
97 p
69 6
88 A
17 J
33 M
86 D
34 i
89 $
15 %
91 -
3 !
62 3
88 /
48 J
83 c
7 E
56 )
83 d
98 M
10 a
82 (
23 !
95 n
50 X
2 c
3 a
73 i
72 /
64 l
27 F
4 +
78 =
21 u
23 3
49 l
55 7
73 7
64 %
5 d
77 s
64 +
41 j
68 6
26 _
33 o
80 P
30 &
99 !
33 p
10 /
31 O
94 P
98 k
77 w
3 z
64 h
19 c
60 K
45 v
10 X
21 z
45 N
81 _
60 y
40 N
48 t
16 4
100 M
88 )
82 -
55 _
23 _
2 V
33 q
90 Q
75 A
44 ,
51 8
13 z
29 S
12 a
6 w
46 o
43 O
99 =
21 A
5 W
18 n
6 2
66 K
17 5
41 O
10 *
5 .
3 t
56 $
40 v
68 l
94 l
78 #
41 @
6 ,
43 A
66 3
24 o
71 t
96 D
89 (
22 z
19 Y
66 A
21 ^
85 S
53 v
40 u
16 8
84 T
18 b
99 >
48 e
39 T
86 i
64 e
74 6
58 t
31 b
69 y
59 +
76 6
57 A
90 ?
57 >
44 @
11 K
8 )
58 .
74 P
90 4
16 2
44 b
48 t
40 l
44 1
10 G
42 +
8 e
21 g
12 8
19 9
98 M
66 #
98 <
73 M
51 =
5 c
91 E
52 i
34 ^
90 f
16 _
95 r
42 3
31 W
39 !
64 q
95 4
31 /
9 h
97 (
59 /
58 v
90 I
68 $
55 1
87 F
82 v
94 P
11 7
73 h
84 -
41 g
48 b
7 A
14 T
32 &
66 M
26 m
77 F
44 )
55 H
45 e
52 3
71 -
36 y
42 T
32 .
67 k
23 i
17 &
44 <
18 I
75 k
96 A
62 x
10 @
56 %
29 p
11 2
65 (
32 O
22 p
87 t
20 W
55 @
23 n
97 j
97 l
81 z
41 *
95 M
92 k
45 -
45 w
84 w
79 R
33 G
46 C
68 J
65 1
3 l
52 r
48 C
39 -
61 (
45 ,
29 a
70 ,
40 1
5 #
49 F
1 V
95 7
19 L
91 Q
100 6
3 m
31 7
10 v
41 3
95 ?
99 F
45 S
82 R
54 !
59 ,
5 2
90 Z
50 D
99 Z
65 a
45 $
55 !
33 f
75 @
44 >
20 =
68 J
81 u
93 F
83 s
3 m
11 l
76 V
13 P
60 @
65 ,
3 O
16 ?
8 b
53 u
24 g
39 -
32 e
91 y
99 H
97 h
47 Z
60 9
83 >
82 +
23 z
68 u
43 N
46 K
67 G
88 <
90 I
77 X
23 F
44 c
78 a
69 b
57 w
13 e
95 D
69 5
29 1
62 u
98 L
48 M
54 X
46 a
30 R
69 =
83 h
89 e
47 I
14 N
43 +
66 >
28 1
25 G
38 l
44 k
11 w
89 -
50 M
75 j
16 q
62 ?
38 n
38 g
15 r
34 p
66 l
81 1
6 a
60 s
29 1
19 3
19 K
9 i
21 2
23 _
100 r
4 W
20 (
33 =
55 B
25 4
16 C
44 E
26 <
85 %
36 9
99 )
53 %
28 i
14 h
6 6
57 s
83 d
93 B
21 j
62 m
40 T
55 r
45 0
57 i
28 V
13 4
91 h
18 #
32 )
7 $
76 8
82 F
93 7
84 u
99 l
84 #
12 v
64 +
50 y
15 F
63 x
57 z
58 7
35 K
74 G
4 U
33 s
86 D
61 V
77 M
100 h
20 (
35 >
88 I
98 _
50 z
63 <
34 *
65 I
57 0
57 ,
51 Q
83 8
75 s
94 4
94 h
43 o
32 I
18 O
29 >
28 ,
51 7
61 H
5 ^
12 !
15 3
10 E
32 s
16 s
73 R
44 1
96 M
15 %
93 g
63 I
52 6
38 K
72 L
34 F
14 7
18 7
82 8
55 ?
99 k
99 P
66 y
76 H
80 D
71 A
26 o
89 $
19 ^
23 8
85 F
43 &
73 $
31 d
96 O
33 -
5 T
43 q
50 P
20 %
77 l
46 C
87 4
48 o
99 (
60 h
17 *
35 t
50 4
12 s
92 L
67 2
83 T
85 v
97 ,
80 A
94 m
56 k
99 Q
97 F
63 2
95 A
13 G
84 Y
46 _
10 /
24 j
94 B
11 q
23 v
70 8
19 D
87 ^
15 Q
35 R
87 K
57 t
95 9
63 A
74 F
7 F
80 B
61 x
93 _
2 d
9 1
17 -
88 Q
20 /
84 0
19 3
50 d
93 S
41 7
1 4
78 y
3 6
91 Q
17 x
44 5
47 x
80 ?
4 O
48 b
84 V
6 ,
23 x
91 L
70 d
16 G
99 0
36 T
29 +
93 h
94 v
31 m
18 H
58 .
93 h
29 ,
51 W
89 1
73 $
29 3
27 j
26 r
43 B
55 _
97 p
14 a
5 1
12 $
94 L
89 X
96 r
36 q
16 %
69 H
71 i
19 !
37 G
20 /
82 !
52 1
90 O
69 v
90 r
53 v
98 V
90 l
91 Y
58 b
16 r
15 $
81 R
75 W
33 w
58 Z
81 K
30 5
88 e
17 4
47 p
39 p
10 %
93 d
85 5
30 D
96 o
7 t
57 D
4 y
32 <
85 s
87 Y
83 v
42 ?
48 h
11 4
38 g
39 X
81 !
43 K
39 q
75 I
75 <
19 .

These three keys are used to get the decrypted message after encryption.     
