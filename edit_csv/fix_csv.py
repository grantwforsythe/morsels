import argparseimport csvparser = argparse.ArgumentParser(add_help=False)parser.add_argument('files', type=str, nargs=2)parser.add_argument('--in-delimiter=', type=str, dest='in_del')parser.add_argument('--in-quote=', type=str, default='"', dest='quote')args = parser.parse_args()with open(args.files[0], 'r') as f:     if args.in_del:        deli = args.in_del    else:          dialect = csv.Sniffer().sniff(f.read(1024))        f.seek(0)        deli = dialect.delimiter    reader = csv.reader(f, delimiter=deli)      with open(args.files[1], 'w') as new_f:        deli = ','        writer = csv.writer(new_f, delimiter=deli)        for row in reader:            new_row = [				element.replace(deli, f'"{deli}"')				if deli in element else element				for element in row			]            print(new_row)            writer.writerow(row)