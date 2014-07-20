import argparse

def parse_cl(in_args):
	sub_cmds = {"prepare": add_subparser_prepare,
	            "cluster": add_subparser_cluster}
	parser = argparse.ArgumentParser(description="small RNA analysis")
	sub_cmd = None
	if len(in_args) > 0 and in_args[0] in sub_cmds:
		subparsers = parser.add_subparsers(help="seqcluster supplemental commands")
		sub_cmds[in_args[0]](subparsers)
		sub_cmd = in_args[0]
	args = parser.parse_args()

	assert sub_cmd is not None
	kwargs = {"args": args,
	              sub_cmd: True}
	return kwargs

def add_subparser_prepare(subparsers):
	parser = subparsers.add_parser("prepare", help="prepare data")
	parser.add_argument("-c", "--conf", dest="dir",required=1,
                  help="file with fasta format paths:1st column:path 2nd column:name")
	parser.add_argument("-o", "--output", dest="out",required=1,
                  help="dir of output files")
	return parser

def add_subparser_cluster(subparsers):
	parser = subparsers.add_parser("cluster", help="cluster data")
	parser.add_argument("-a", "--afile", dest="afile",required=1,
	                  help="aligned file in bed/sam format")
	parser.add_argument("-m", "--ma", dest="ffile",required=1,
	                  help="matrix file with sequences and counts for each sample")
	parser.add_argument("-g", "--gtf",
	                   dest="gtf", help="annotate with gtf_file. It will use the 3rd column as the tag to annotate" +
	                   "\nchr1    source  intergenic      1       11503   .       +       .       ")
	parser.add_argument("-b", "--bed",
	                   dest="bed", help="annotate with bed_file. It will use the 4rd column as the tag to annotate" +
	                   "\nchr1    157783  157886  snRNA   0       -")
	parser.add_argument("-o", "--out",
	                   dest="out", help="output dir")
	parser.add_argument("-i", "--index",required=1,
	                   dest="index", help="reference fasta")
	parser.add_argument("-d", "--debug", action="store_true",
	                   dest="debug", help="max verbosity mode",default=False)
	parser.add_argument("-s", "--show", action="store_false",
	                   dest="show", help="no show sequences",default=True)
	return parser
