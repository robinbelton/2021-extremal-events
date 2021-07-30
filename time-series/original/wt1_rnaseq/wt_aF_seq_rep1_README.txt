Date of synchrony experiment: 4/21/2014
Person carrying out experiment: Tina Kelliher (notebook #2)

Strain: SBY151 15D; MATa; bar1

STARTING CONDITIONS
Starting media: YEP 2% dextrose
Starting culture: 200 ml in Large Glass Flask
Temperature of waterbath: 30 deg Celsius
Starting concentration: 1.60e7 cells/ml
Synchrony method: alpha-factor mating pheromone (30 ng/ml) in 215 ml fresh YEPD for ~1 hour 40 minutes
Pre-incubation?: No

AFTER SYNCHRONIZATION
Media used: YEP 2% dextrose
	Pre-warmed?: Yes
Concentration of cells at time 0 min: 1.0e7 cells/mL
Starting culture: 440 ml in Large Glass Flask
Temperature of waterbath: 30 deg Celsius
Waterbath used: Temperature-controlled incubator

Frequency of time points: every 5 minutes
Length of time course following synchronization: 250 minutes

BUDDING INDEX
Clock	Lifeline	Total	Budded
0	0.00	234	5
5	16.10	216	5
10	32.21	228	7
15	48.31	205	4
20	64.41	248	21
25	80.52	218	15
30	96.62	219	14
35	105.74	232	30
40	113.01	204	94
45	120.28	223	118
50	127.55	232	149
55	134.82	241	159
60	142.09	231	169
65	149.36	272	230
70	156.63	222	194
75	163.90	230	209
80	171.17	229	198
85	178.44	222	170
90	185.71	215	126
95	192.98	234	121
100	200.25	210	100
105	207.52	224	110
110	214.79	217	89
115	222.06	295	135
120	229.33	222	128
125	236.59	254	149
130	243.86	266	181
135	251.13	209	152
140	258.40	212	149
145	265.67	238	181
150	272.94	222	162
155	280.21	263	174
160	287.48	228	127
165	294.75	226	119
170	302.02	220	129
175	309.29	284	167
180	316.56	243	140
185	323.83	252	135
190	331.10	223	135
195	338.37	220	137
200	345.64	211	139
205	352.91	262	158
210	360.18	215	151
215	367.45	237	168
220	374.72	215	145
225	381.99	210	133
230	389.26	206	133
235	396.53	219	136
240	403.79	214	123
245	411.06	216	135

CLOCCS PARAMETERS
temperature setting: 32.0
recovery time: 31.05
period length: 68.78
How period length was determined: budding index in CLOCCS algorithm

RNA EXTRACTION AND SUBMISSION
Person carrying out experiment: Adam Leman
RNA was extracted using an acid phenol/chloroform protocol.
Dates of RNA extraction: 6/12-13/14
    RNA cleanup: N/A
    RNA gel on select time points: Yes

Date of RNA submission to Seq Facility: 7/1/14
50 ul (1:10 dilution of original samples) were submitted for QC (10 ul?) and library prep / analysis (40 ul?) to the Duke Sequencing Facility.

Any issues in RNA extraction or submission: RNA Seq facility QC instrument and personnel not familiar with fungal RNA samples.

Date of RNA submission to Array Facility: 7/28/14
Range of volumes (<10 ug) were submitted for QC to the Duke Microarray Core Facility.

The RNA was prepared using the TruSeq Stranded mRNA enrichment library prep kit (individual reactions are amplified in 1 cycle and barcoded).
The barcoded cDNA for each time point was applied to the Illumina HiSeq 2500 Sequencer (50 bp single-end reads).

NORMALIZATION:

The S. cerevisiae reference genome used was downloaded from Illumina iGenomes on 9/17/14 from the latest Ensembl build R-64-1-1

*.fastq files from this experiment were aligned to the S. cerevisiae reference genome using TopHat2 in 10-2014 -- 03/2015 range by CMK

*.fastq files from this experiment were aligned to the S. cerevisiae reference genome using rna-STAR in 07/2015 by CMK

The aligned reads were normalized using two approaches:

1. Use HTSeq to count the number of reads aligning to annotated genes (GTF file from Ensembl build R-64-1-1); raw counts were first normalized by library size per time point (divide by "complexity"), then log-quantile_normalized-exponentiated in R by CMK

2. Use cuffquant against the reference transcriptome (GTF file from Ensembl build R-64-1-1) to build transcripts; normalize transcript data from all time points using cuffnorm with default parameters

See the Haase lab computer README files for exact code run and output. Email tina.kelliher@gmail.com with questions.