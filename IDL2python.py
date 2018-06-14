import os,sys

def find_file(arg,dirname,files):
	    for file in files:
			targetFile = os.path.join(dirname, file)
			if os.path.isfile(targetFile):
				cmd = "thrift-0.9.1 -r --gen py " + targetFile
				os.system(cmd)

def main():
	os.path.walk(sys.path[0] + "\\idl_output",find_file,())

if __name__ == "__main__":
	main()

