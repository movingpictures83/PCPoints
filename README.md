# PCPoints
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: TSV (coordinates)
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that outputs the first two principal component values
of all samples in a target group, as tab-delimited x-y coordinates
in an output TSV file.

The plugin accepts as input a parameter file of keyword-value pairs:
infile: File of each sample and principal component values
mapping: File of samples and corresponding groups
group: Target group

