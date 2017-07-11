def commit(n,lib):
	with open(lib, "a") as myfile:
    if myfile.write(n):
    	print "Successfully added code to library."