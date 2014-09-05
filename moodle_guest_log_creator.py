import csv, socket


def convert_ip_to_domain(filename)
	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		for row in reader:
			print ', '.join(row)
		
		
		
def main():
  if len(sys.argv) != 2:
    print 'usage: ./moodle_guest_log_creator.py file'
    print '       where file is a Moodle activity log in text format (tab delimited)'
    sys.exit(1)

  filename = sys.argv[1]
  convert_ip_to_domain(filename)

  sys.exit(1)

if __name__ == '__main__':
  main()		