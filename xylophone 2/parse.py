import argparse
import read_txt_files_x
import cliente

parser = argparse.ArgumentParser(description="Execute the metallophone")
parser.add_argument("-p", "--score",type=str, action="store",
help="File with the notes and the duration of each one")
parser.add_argument("-d", "--ip", action="store", type=str,
help="The ip of the metallophone")

args = parser.parse_args()
score = args.score
ip = args.ip

list_score = read_txt_files_x.music_sheet_x(score)
print(list_score)
read_txt_files_x.sorting_notes(list_score)

notes = cliente.create_xilophone(list_score)
cliente.main(notes)




